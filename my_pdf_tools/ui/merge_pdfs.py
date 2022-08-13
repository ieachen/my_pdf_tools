import os
import PySimpleGUI as sg

from my_pdf_tools.pdf_core.merge_pdfs import merge_pdfs


def main():

    # sg.theme('DarkAmber')  # 设置当前主题

    title = '合并pdf（最多3个）'

    # 界面布局，将会按照列表顺序从上往下依次排列，二级列表中，从左往右依此排列
    layout = [
        [sg.Text(title, justification='center')],

        [sg.Text('-----------------')], 

        [sg.Text('选择待合并的 pdf 文件 1：')],  # T = Text
        [sg.InputText(key='pdf_1', visible=True)],  # InputText = Input = In = I
        [sg.FileBrowse(key='_BUTTON_KEY_1', target='pdf_1', file_types=[('pdf files', '*.pdf')])],

        [sg.Text('选择待合并的 pdf 文件 2：')],  # T = Text
        [sg.InputText(key='pdf_2', visible=True)],  # InputText = Input = In = I
        [sg.FileBrowse(key='_BUTTON_KEY_2', target='pdf_2', file_types=[('pdf files', '*.pdf')])],

        [sg.Text('选择待合并的 pdf 文件 3：')],  # T = Text
        [sg.InputText(key='pdf_3', visible=True)],  # InputText = Input = In = I
        [sg.FileBrowse(key='_BUTTON_KEY_3', target='pdf_3', file_types=[('pdf files', '*.pdf')])],


        [sg.Text('-----------------')], 

        [sg.Text('保存目录')], 
        [sg.InputText(key='merge_folder', visible=True)],  # InputText = Input = In = I
        [sg.FolderBrowse(key='_BUTTON_KEY_MERGED', target='merge_folder')],

        [sg.Text('保存文件名')], 
        [sg.InputText(key='merge_file_name', visible=True)],  # InputText = Input = In = I
        # [sg.FolderBrowse(key='_BUTTON_KEY_MERGED', target='merge_file_name')],

        [sg.Text('-----------------')], 

        # [sg.Text('你选择的文件夹是:',font=("宋体", 10)),sg.Text('',key='pic_folder',size=(50,1),font=("宋体", 10))],

        [sg.Text('点击“开始”按钮')], 
        [sg.Button('开始', tooltip='执行合并'), sg.Button('取消', tooltip='关闭'), sg.Button('清空', tooltip='清空文件选择')],

        [sg.Output(size=(60, 15))]
    ]

    # 创造窗口
    window = sg.Window('合并pdf', layout)
    # 事件循环并获取输入值

    while True:
        event, values = window.read()
        if event in (None, '取消'):  # 如果用户关闭窗口或点击`Cancel`
            break

        if event == '开始':

            pdf_files_list = []
            for name in ['pdf_1', 'pdf_2', 'pdf_3']:
                if values[name]:
                    pdf_files_list.append(values[name])

            if values['merge_folder'] and values['merge_file_name']:

                # 文件名自动添加 .pdf 结尾
                merge_file_name = str(values['merge_file_name'])
                if merge_file_name.endswith('.pdf'):
                    merge_file_name += '.pdf'

                output_file_path = os.path.join(values['merge_folder'], merge_file_name)
                if os.path.exists(output_file_path):
                    print('警告：pdf保存路径已存在，将覆盖')
            else:
                print('未填写pdf保存路径，请填写')
                continue

            merge_pdfs(pdf_files_list, output_file_path)

            # print(values['merge_file_name'])
            # print(type(values['merge_file_name']))
            # print(pdf_files_list)

        if event == '清空':
            window['pdf_1'].Update('')
            window['pdf_2'].Update('')
            window['pdf_3'].Update('')
            window['merge_folder'].Update('')
            window['merge_file_name'].Update('')

    window.close()


if __name__ == '__main__':
    main()
