import PySide6.QtCore as Qc
import PySide6.QtWidgets as Qw
import os
import webbrowser
import subprocess

mode_list=["web","app"]

# レイアウト設定用変数
sp_exp = Qw.QSizePolicy.Policy.Expanding

class MainWindow(Qw.QMainWindow):

  def __init__(self):

    super().__init__() 
    self.setWindowTitle('MainWindow') 
    self.setGeometry(100, 80, 640, 130) 

    # メインレイアウトの設定
    central_widget = Qw.QWidget(self)
    self.setCentralWidget(central_widget)
    main_layout = Qw.QVBoxLayout(central_widget) # 垂直レイアウト

    # ボタン配置の垂直レイアウトを作成します。
    button_layout = Qw.QVBoxLayout()
    button_layout.setAlignment(Qc.Qt.AlignmentFlag.AlignLeft) # 左寄せ
    main_layout.addLayout(button_layout) # メインレイアウトにボタンレイアウトを追加

    # モードコンボボックスの見出し
    self.lb_mode = Qw.QLabel(self)
    self.lb_mode.setMinimumSize(50,20)
    self.lb_mode.setText('モード')
    self.lb_mode.setSizePolicy(sp_exp,sp_exp)
    button_layout.addWidget(self.lb_mode)

    # モードコンボボックスの本体
    self.cmb_mode = Qw.QComboBox(self)
    self.cmb_mode.setMinimumSize(50,20)
    self.cmb_mode.setMaximumSize(200,20)
    self.cmb_mode.setSizePolicy(sp_exp,sp_exp)
    button_layout.addWidget(self.cmb_mode)
    self.cmb_mode.setEditable(False)
    for p in mode_list:
      self.cmb_mode.addItem(p)
    self.cmb_mode.currentIndexChanged.connect(self.mode_changed)
    dir_path = "setweb"

    # ファイルコンボボックスの見出し
    self.lb_file = Qw.QLabel(self)
    self.lb_file.setMinimumSize(50,20)
    self.lb_file.setText('開きたいウェブが載った.txt')
    self.lb_file.setSizePolicy(sp_exp,sp_exp)
    button_layout.addWidget(self.lb_file)

    # ファイルコンボボックスの本体
    self.cmb_file = Qw.QComboBox(self)
    self.cmb_file.setMinimumSize(50,20)
    self.cmb_file.setMaximumSize(200,20)
    self.cmb_file.setSizePolicy(sp_exp,sp_exp)
    button_layout.addWidget(self.cmb_file)
    self.cmb_file.setEditable(False)
    files = os.listdir(dir_path)
    file_list=files
    file_list.insert(0,'')
    for p in file_list:
      self.cmb_file.addItem(p)
    flag=self.cmb_file.currentIndexChanged.connect(self.file_changed)

    # 実行の作成
    self.btn_run = Qw.QPushButton('実行',self)
    self.btn_run.setMinimumSize(50,20)
    self.btn_run.setMaximumSize(100,20)
    self.btn_run.setSizePolicy(sp_exp,sp_exp)
    button_layout.addWidget(self.btn_run)

    # ファイルエラーコンボボックスの見出し
    self.lb_error = Qw.QLabel(self)
    self.lb_error.setMinimumSize(50,20)
    self.lb_file.setSizePolicy(sp_exp,sp_exp)
    button_layout.addWidget(self.lb_error)

    self.btn_run.clicked.connect(self.btn_run_clicked)

  def mode_changed(self):
    idx = self.cmb_mode.currentIndex()
    print(f'「{mode_list[idx]}」が選択されました。')
    if idx==False:
        self.lb_file.setText('開きたいウェブが載った.txt')
        if not os.path.isdir("setweb"):
          os.makedirs('setweb')
        files = os.listdir("setweb")
        file_list=files
        file_list.insert(0,'')
        for i in range(self.cmb_file.count()):
          self.cmb_file.removeItem(0)
        for p in file_list:
          self.cmb_file.addItem(p)
    elif idx==True:
        self.lb_file.setText('開きたいアプリのフルパスが載った.txt')
        if not os.path.isdir("setapp"):
          os.makedirs('setapp')
        files = os.listdir("setapp")
        file_list=files
        file_list.insert(0,'')
        for i in range(self.cmb_file.count()):
          self.cmb_file.removeItem(0)
        for p in file_list:
          self.cmb_file.addItem(p)
    
  def file_changed(self):
    idx = self.cmb_file.currentIndex()
    if idx == 0 :
      print(f'テキストファイルが未選択になりました。')
      return 404
    else :
      print(f'テキストファイルが選択されました。')
      return 1

  def btn_run_clicked(self):
    Idx_mode= self.cmb_mode.currentIndex()
    idx = self.cmb_file.currentIndex()
    if self.cmb_mode.currentText()=="web":
      path="setweb"
    else:
      path = "setapp"
    files = os.listdir(path)
    file_list=files
    file_list.insert(0,'')
    self.lb_error.setText('')
    if idx != 0 and Idx_mode == 1:
      F=file_list[idx]
      with open(f"{path}/{F}") as f:
        l_strip = [s.rstrip() for s in f.readlines()]
        print(l_strip)
      for i in range(len(l_strip)):
        subprocess.Popen(l_strip[i])
    elif idx != 0 and Idx_mode == 0:
      F=file_list[idx]
      with open(f"{path}/{F}") as f:
        l_strip = [s.rstrip() for s in f.readlines()]
        print(l_strip)
      for i in range(len(l_strip)):
        webbrowser.open(l_strip[i])
    else :
      self.lb_error.setText('実行できる.txtファイルがありません')