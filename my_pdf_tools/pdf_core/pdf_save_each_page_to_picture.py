
from pathlib import Path
import fitz


def pdf_save_each_page_to_picture(pdf_file_path, output_pic_folder):

    pdf_file_path = Path(pdf_file_path)
    output_pic_folder = Path(output_pic_folder)

    # 要求路径存在
    if not pdf_file_path.exists():
        print('pdf路径不正确，请重试')
        return
    if not output_pic_folder.exists():
        print('图片保存目录不存在，请重试')
        return

    # 要求路径以 .pdf 结尾
    if not str(pdf_file_path).endswith('.pdf'):
        print('pdf路径不是以 .pdf 结尾，请重试')
        return

    print('\n --------- pdf 保存每一页为图片 -------\n')

    print('pdf 路径： ' + str(pdf_file_path))
    print('图片保存目录： ' + str(output_pic_folder))

    pdf_name_with_no_extension = pdf_file_path.name.split('.')[0]

    doc = fitz.open(pdf_file_path)  # 打开pdf

    total_page_number = doc.page_count  # 总页数，或者len(doc)
    total_page_number_digit = len(str(total_page_number))  # 总页数是几位数字，用于 zfill

    for ii in range(doc.page_count):  # 或者直接 for page in doc:
        print(f'  保存图片：第 {ii} 页')

        ii_str = str(ii).zfill(total_page_number_digit)  # zfill的目的为了在文件管理器里排序正常

        output_file_path = output_pic_folder /  f"{pdf_name_with_no_extension}_{ii_str}.png"

        page = doc.load_page(ii)
        pix = page.get_pixmap()
        pix.save(output_file_path)

    doc.close()

    print('\n 完成！')

    return
