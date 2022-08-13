import PySimpleGUI as sg

from my_pdf_tools.pdf_core.pdf_save_each_page_to_picture import pdf_save_each_page_to_picture


def main():

    # sg.theme('DarkAmber')  # 设置当前主题

    # 界面布局，将会按照列表顺序从上往下依次排列，二级列表中，从左往右依此排列
    layout = [
        [sg.Text('pdf 保存每一页为图片', justification='center')],

        [sg.Text('-----------------')], 

        [sg.Text('步骤1. 选择 pdf 文件：')],  # T = Text
        [sg.InputText(key='pdf_file', visible=True)],  # InputText = Input = In = I
        [sg.FileBrowse(key='_BUTTON_KEY_', target='pdf_file', file_types=[('pdf files', '*.pdf')])],

        [sg.Text('-----------------')], 

        [sg.Text('步骤2. 选择图片保存目录（建议空目录）：')], 
        [sg.InputText(key='pic_folder', visible=True)],  # InputText = Input = In = I
        [sg.FolderBrowse(key='_BUTTON_KEY2_', target='pic_folder')],


        [sg.Text('-----------------')], 

        # [sg.Text('你选择的文件夹是:',font=("宋体", 10)),sg.Text('',key='pic_folder',size=(50,1),font=("宋体", 10))],

        [sg.Text('步骤3. 点击“开始”按钮')], 
        [sg.Button('开始', tooltip='执行pdf转图片'), sg.Button('取消', tooltip='关闭'), sg.Button('清空', tooltip='清空文件选择')],

        [sg.Output(size=(60, 15))]

        # [sg.Text('Some text on Row 1')],
        # [sg.Text('Enter something on Row 2'), sg.InputText()],

        # [sg.FolderBrowse(key='_BUTTON_KEY_', target='input_folder'), sg.OK()],
    ]

    # 创造窗口
    window = sg.Window('pdf 保存为每一页图片', layout)
    # 事件循环并获取输入值

    while True:
        event, values = window.read()
        if event in (None, '取消'):  # 如果用户关闭窗口或点击`Cancel`
            break

        # print(event)
        # print(values)

        if event == '开始':
            if values['pdf_file'] and values['pic_folder']:
                pdf_save_each_page_to_picture(values['pdf_file'], values['pic_folder'])

        if event == '清空':
            window['pdf_file'].Update('')
            window['pic_folder'].Update('')

        # if event == '重命名':
        #     if values['folder']:
        #         print('{0}正在重命名原文件为hash值{0}'.format('*'*10))
        #         mult_rename(values['folder'])
        #         print('{0}重命名完毕{0}'.format('*'*10))
        #     else:
        #         print('请先选择文件夹')

        # print('You entered ', values[0])

    window.close()


if __name__ == '__main__':
    main()

