import ultralytics
from ultralytics import YOLO
from pypdf import PdfReader
import os
import docx2txt
import numpy as np
import easyocr
import cv2
import pandas as pd

def parsing_pdf(file_name, directory_name):

  reader = PdfReader(directory_name+ "/" + file_name + ".pdf")
  for page in reader.pages:
      for image in page.images:
          with open(directory_name + "/" + file_name + ".jpg" , "wb") as fp:
              fp.write(image.data)
  return file_name + ".jpg"

def parsing_docx(file_name, directory_name):
  text = docx2txt.process(directory_name + "/" + file_name, directory_name)
  if not os.path.exists(directory_name + "/" + file_name[:-4] + "png"):
    os.rename(directory_name+ "/image1.png", directory_name + "/" + file_name[:-4] + "png")
  return file_name[:-4] + "png"

def photo_handling(reader, model,filepath ,ok_extension):
  resultAnswers = []
  name = filepath.split(".")[0]
  file_extension = filepath.split(".")[1]

  if file_extension in ok_extension:

    if file_extension == "docx":
      filepath = parsing_docx(filepath)

    if file_extension == "pdf":
      filepath = parsing_pdf(name)

    results = model(filepath)

    for r in results:
      boxes = r.boxes
      if len(boxes) == 0:
        resultAnswers.append("Данные для аналитики не найдены")
      else:
        for box in boxes:
          x_0 = int(box.xyxy[0][0])
          y_0 = int(box.xyxy[0][1])
          x_1 = int(box.xyxy[0][2])
          y_1 = int(box.xyxy[0][3])
          img = r.orig_img[y_0:y_1, x_0:x_1]

          cv2.imwrite("tmp.jpg", img)
          ans = reader.readtext("tmp.jpg")

          if len(ans) == 0:
            filename_def, zn_def = contrast(filepath, reader)
            resultAnswers.append(zn_def)
          else:
            for a in ans:
              resultAnswers.append(a[1])
  return resultAnswers



def folder_handling(mode,reader, model,photos, directory_name, ok_extension):
  #Работа с папкой
  column_folder = []
  column_folder_zn = []
  for filename in photos:
    file_extension = filename.split(".")[1]

    name = filename.split(".")[0]

    if file_extension in ok_extension:
      if file_extension == "docx":
        filename = parsing_docx(filename,directory_name)

      if file_extension == "pdf":
        filename = parsing_pdf(name,directory_name)
      path_to_img = directory_name + "/" + filename

      results = model(path_to_img)

      for r in results:
        boxes = r.boxes
        if len(boxes) == 0:
          column_folder.append(filename)
          column_folder_zn.append("Данные для аналитики не найдены")
        else:
          for box in boxes:
            x_0 = int(box.xyxy[0][0])
            y_0 = int(box.xyxy[0][1])
            x_1 = int(box.xyxy[0][2])
            y_1 = int(box.xyxy[0][3])
            img = r.orig_img[y_0:y_1, x_0:x_1]

            cv2.imwrite("tmp.jpg", img)
            ans = reader.readtext("tmp.jpg")

            if len(ans) == 0:
              filename_def, zn_def = contrast(filename,reader)
              column_folder.append(filename_def)
              column_folder_zn.append(zn_def)
            else:
              for a in ans:
                # print(filename, a[1])
                column_folder.append(filename)
                column_folder_zn.append(a[1])
  find_parametr = ""
  final_filename = ""
  if mode == "Дзен":
    find_parametr = "Дочитывания"
    final_filename = "./zn.xlsx"
  elif mode == "VK":
    find_parametr = "Подписчики"
    final_filename = "./vk.xlsx"
  elif mode == "Telegram":
    find_parametr = "ERR/VR"
    final_filename = "./tg.xlsx"
  elif mode == "yt1":
    find_parametr = "Подписчики"
    final_filename = "./yt1.xlsx"
  elif mode == "yt2":
    find_parametr = "Просмотры"
    final_filename = "./yt2.xlsx"

  df = pd.DataFrame({"Имя файла" : column_folder,
                    find_parametr : column_folder_zn})
  df.to_excel(final_filename, index=False)


def contrast(filename,reader):
  # Это контрастность и яркость, применяется, если ocr ничего не распознал
  image_bgr = cv2.imread("tmp.jpg", cv2.IMREAD_COLOR)
  image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
  contrast_matrix = np.ones(image_rgb.shape) * 1.9
  brightness_matrix = np.ones(image_rgb.shape, dtype="uint8") * 140
  image_rgb_br = cv2.subtract(image_rgb, brightness_matrix)
  image_rgb_con = np.uint8(np.clip(cv2.multiply(np.float64(image_rgb_br), contrast_matrix), 0, 255))
  ans = reader.readtext(image_rgb_con)

  if len(ans) == 0:
    ans = reader.readtext(image_rgb_br)
    if len(ans) == 0:
      return (filename, "Данные не распознаны")
    else:
      for a in ans:
        return (filename, a[1])
  else:
    for a in ans:
      return (filename, a[1])

def process_photo(mode,content, directory_name):

  reader = easyocr.Reader(['ru', 'en'], gpu = True) #Подключаю EasyOCR
  if content == "folder":
    photos = os.listdir(directory_name)
  ok_extension = ["jpg", "png", "jpeg", "docx", "pdf"]
  if mode == "Дзен":

    model_name = 'сети/yolov8s-zn-gpu-15e.pt' # Выбрал модель для Дзена
    model = YOLO(model_name)

    if content == "folder":
      folder_handling(mode,reader, model,photos, directory_name,ok_extension)

    if content == "photo":
      result = photo_handling(reader, model, directory_name, ok_extension)
      return result


  elif mode == "VK":

    model_name = 'сети/yolov8m-vk-30e.pt' # Выбрал модель для ВК
    model = YOLO(model_name)

    if content == "folder":
      folder_handling(mode,reader, model,photos, directory_name,ok_extension)
    if content == "photo":
      result = photo_handling(reader, model, directory_name, ok_extension)
      return result

  elif mode == "Telegram":

    model_name = 'сети/yolov8m-tg_v2-30e.pt' # Выбрал модель для Телеграма
    model = YOLO(model_name)

    if content == "folder":
      folder_handling(mode,reader, model,photos, directory_name,ok_extension)

    if content == "photo":
      result = photo_handling(reader, model, directory_name, ok_extension)
      return result

  elif mode == "YouTube":

    model_name = 'сети/yolov8m-yt1_v5-30e.pt' # Выбрал модель для Ютуба
    model = YOLO(model_name)

    if content == "folder":
      folder_handling("yt1",reader, model,photos, directory_name,ok_extension)

      model_name = 'сети/yolov8m-yt2_v3-30e.pt'  # Выбрал модель для Ютуба
      model = YOLO(model_name)

      folder_handling("yt2",reader, model,photos, directory_name,ok_extension)

    if content == "photo":
      result1 = photo_handling(reader, model, directory_name, ok_extension)
      model_name = 'сети/yolov8m-yt2_v3-30e.pt'  # Выбрал модель для Ютуба
      model = YOLO(model_name)
      result2 = photo_handling(reader, model, directory_name, ok_extension)
      return (result1,result2)


