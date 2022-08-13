
from my_pdf_tools.ui.merge_pdfs import main as main_merge_pdfs
from my_pdf_tools.ui.pdf_save_each_page_to_picture import main as main_pdf_save_each_page_to_picture


def main():
    print('\n')
    print('----------- my pdf tools ---------')
    print('\n')

    print('输出数字，按回车')

    print('\n    数字对应的功能如下：\n')
    print('1: 合并多个pdf为一个')
    print('2: pdf保存每页为图片')

    print('若要退出，请叉掉窗口')
    print('\n')

    while True:

        a = input()  # input() always returns a string

        if a == '1':
            main_merge_pdfs()
            print('结束')

        elif a == '2':
            main_pdf_save_each_page_to_picture()

        else:
            print('请重新输入')
            continue

        print('请继续输入')


if __name__ == '__main__':
    main()
