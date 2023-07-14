from time import sleep, strftime, time
from json import load, loads, dumps
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem,QMessageBox
from PyQt5.QtCore import QThread, pyqtSignal

from ui.ui import Ui_MainWindow
from nodes import get_parameters_dict
from db import DB
from nbiot import send_data



class RequestThread(QThread):
    """
    请求得到各节点参数字典的线程
    """

    submit_signal = pyqtSignal(str, dict)

    def __init__(self, delay_time: float = 2.0):
        super(RequestThread, self).__init__()
        self.delay_time = delay_time
        self.nodes_list = list()  # 请求的节点列表

    def request(self):
        for node in self.nodes_list:
            # 请求得到一个节点的参数字典 提交一次
            self.submit_signal.emit(node, get_parameters_dict(node))

    def run(self):
        while True:
            self.request()
            sleep(self.delay_time)


class LogUpdateThread(QThread):
    log_update_signal = pyqtSignal()

    def __init__(self, parent=None):
        super(LogUpdateThread, self).__init__()

    def run(self):
        while True:
            sleep(5)
            self.log_update_signal.emit()



class UsingWindow(QMainWindow, Ui_MainWindow):
    """
    继承window.window的布局类 在此处编写逻辑代码
    """

    def __init__(self):
        super(UsingWindow, self).__init__()
        self.setupUi(self)
        self.message = QMessageBox(self)
        # 节点参数字典的字典
        self.parameters_dict_dict = dict()

        # 初始化持续请求各节点参数字典的线程
        self.request_thread = RequestThread()

        # 初始化持续更新日志的线程
        self.log_update_thread = LogUpdateThread()

        with open("settings.json", "r", encoding="utf-8") as f:
            settings = load(f)

        self.node_ip_dict = settings["node_ip_dict"]
        sensors_standard_dict = settings["sensors_standard_dict"]

        # 向节点列表中添加节点
        for node in self.node_ip_dict:
            self._nodes_list.addItem(node)  # 节点列表控件添加项
            self.request_thread.nodes_list.append(node)  # 持续请求各节点参数字典的线程节点列表
            self.parameters_dict_dict[node] = dict(status=False)

        # 请求得到参数字典 交由相应函数处理
        self.request_thread.submit_signal.connect(self.process_request_signal)

        # 更新日志信息 交由响应函数处理
        self.log_update_thread.log_update_signal.connect(self.process_log_update_signal)

        # 向传感器标准字典中添加传感器标准
        self.sensors_standard_dict = dict()
        for sensor, standard in sensors_standard_dict.items():
            min = standard[0]
            max = standard[1]
            self.sensors_standard_dict[sensor] = lambda x: min < x < max

        # 节点列表控件默认选中第一个节点
        self._nodes_list.setCurrentRow(0)

        # 节点列表控件选择发生改变调用方法
        self._nodes_list.itemSelectionChanged.connect(self.handle_selection_click)

        # 初始化数据库
        self.db = DB("./db/data.sqlite3")

        self._save_log_file.clicked.connect(self.save_txt_log)

        self.request_thread.start()  # 启动持续请求各节点参数字典的线程
        self.log_update_thread.start()

    def process_request_signal(self, node, parameters_dict):
        """
        处理请求得到的参数字典
        """
        # 在线状态改变 更新窗口日志
        self.check_if_status_changed(node, parameters_dict)
        # 更新参数字典
        self.parameters_dict_dict[node] = parameters_dict
        if self.parameters_dict_dict[node][
            "status"
        ]:  # 节点在线 检查各个传感器参数是否满足要求
            # 不满足要求 更新窗口日志
            self.check_if_data_meet_standard(node, parameters_dict)
        # 节点列表控件选择改变的事件
        self.handle_selection_click()

    def handle_selection_click(self):
        """
        每次选择改变更新状态框 得到数据更新数据字典控件
        """
        self._node_status.setText("")  # 清空节点状态框
        self._sensor_data_dict.clearContents()  # 清空数据字典控件
        self._sensor_data_dict.setRowCount(0)  # 重新设置数据字典控件的列数
        # 获取当前节点
        node = self._nodes_list.currentItem().text()
        # 获取当前节点参数字典
        parameters_dict = self.parameters_dict_dict[node]
        # 节点离线
        if not parameters_dict["status"]:
            self.echo_node_status(f"节点{node}离线", "red")
            return
        # 节点在线
        self.echo_node_status(f"节点{node}在线", "green")
        sensor_data_dict = parameters_dict["sensor_data_dict"]
        self._sensor_data_dict.setRowCount(len(sensor_data_dict))  # 设置参数表格的列
        # 将数据更新到数据字典控件中
        for i, (sensor, data) in enumerate(sensor_data_dict.items()):
            self._sensor_data_dict.setItem(i, 0, QTableWidgetItem(sensor))
            self._sensor_data_dict.setItem(i, 1, QTableWidgetItem(str(data)))

    def check_if_status_changed(self, node, parameters_dict):
        """
        在线状态改变 更新窗口日志
        """
        status_before = self.parameters_dict_dict[node]["status"]
        status_now = parameters_dict["status"]

        if status_now != status_before:
            # 状态改变
            self.echo_window_log(
                f"节点{node}{'上线' if status_now else '下线'}",
                "green" if status_now else "red",
            )

    def check_if_data_meet_standard(self, node, parameters_dict):
        """
        传感器参数不满足要求 更新窗口日志
        """
        wrong_data_list = list()  # 错误数据列表
        sensor_data_dict = parameters_dict["sensor_data_dict"]
        for sensor, standard in sensor_data_dict.items():
            if not self.sensors_standard_dict[sensor](standard):
                wrong_data_list.append(sensor)
        if len(wrong_data_list) != 0:  # 错误参数列表不为空 打印错误日志
            self.echo_window_log(
                f"节点{node}的{'、'.join(wrong_data_list)}数据存在问题", "black"
            )

    def echo_window_log(self, log: str, color: str):
        """
        更新窗口日志
        """
        current_time = strftime("%Y_%m_%d %H:%M:%S")
        self._window_logs.append(f'<b>{current_time}</b><a style="color: {color};">\t{log}</a>')

    def echo_node_status(self, status: str, color: str):
        """
        更新节点状态框
        """
        self._node_status.setText(f'<h1 style="color: {color};">{status}</h1>')
    
    def process_log_update_signal(self):
        """
        处理日志更新信号 既需要更新数据库日志 也需要更新在线日志
        日志内容均为当前时间的parameters_dict_dict内容
        """
        current_time = strftime("%H:%M:%S")
        parameters_dict_dict_str = dumps(self.parameters_dict_dict)
        self.db.insert_data(current_time, parameters_dict_dict_str)
        send_data(parameters_dict_dict_str)
    
    def save_txt_log(self):
        data = self.db.fetch_all_data()
        txt_lines = map("\t".join,data)
        with open(f"./output/{strftime('%Y_%m_%d')}.txt","w",encoding="utf-8") as f:
            f.writelines(line + "\n" for line in txt_lines)
        
        self.message.setWindowTitle("提示")
        self.message.setText("输出日志文件成功")
        self.message.setIcon(QMessageBox.Information)

        # 显示提示框
        self.message.show()


if __name__ == "__main__":
    app = QApplication([])
    win = UsingWindow()
    win.show()
    app.exec_()
