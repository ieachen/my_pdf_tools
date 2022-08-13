import os
import fitz


def merge_pdfs(pdf_file_paths: list, output_file_path):

    if not pdf_file_paths:
        return

    if len(pdf_file_paths) == 1:
        print('仅有一个pdf文件，无需合并。')
        return

    for x in pdf_file_paths:
        if not str(x).endswith('.pdf'):
            raise ValueError('错误：有文件不是以 .pdf 结尾')

    if not str(output_file_path).endswith('.pdf'):
        raise ValueError('错误：保存的文件名不是以 .pdf 结尾')

    n = len(pdf_file_paths)
    print('\n')
    print(f' 正在合并pdf（1/{n}）：{os.path.basename(pdf_file_paths[0])}')

    doc1 = fitz.open(pdf_file_paths[0])  # open file 1
    # toc1 = doc1.getToC(False)  # its table of contents (list)
    # pc1 = len(doc1)  # number of its pages

    ii = 0
    for file_path in pdf_file_paths[1:]:

        ii += 1

        print(f' 正在合并pdf（{ii}/{n}）：{os.path.basename(file_path)}')

        doc2 = fitz.open(file_path)  # open file 2
        # toc2 = doc2.getToC(False)  # its table of contents

        # new_toc2 = []  # modified toc2 with increased page numbers
        # for line in toc2:  # read to 2nd TOC to update its page numbers
        #     line[2] += pc1  # add file 1 page count to this page number
        #     new_toc2.append(line)

        doc1.insert_pdf(doc2)  # append file 2 to file 1
        # doc1.setToC(toc1 + new_toc2)  # set table of contents for the result

    doc1.save(output_file_path)  # save result to new file

    print('\n')
    print(f'合并完成，保存到: {output_file_path} \n')

    return


if __name__ == '__main__':

    from pathlib import Path

    folder = Path(r'D:\source\pdf\test_files')

    pdfs = [
        folder / 'a1.pdf',
        folder / 'a2.pdf',
        folder / 'all-my-inserted-pics.pdf',
    ]

    output = folder / '_tmp.pdf'

    merge_pdfs(pdfs, output)
