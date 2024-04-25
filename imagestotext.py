from google.colab import drive
drive.mount('/content/drive')
import keras_ocr
import matplotlib.pyplot as plt
images = [
    keras_ocr.tools.read(img) for img in ['/content/drive/MyDrive/images/Padilla - Nobleza virtuosa_testExtract (2)_pages-to-jpg-0001.jpg',
                                          '/content/drive/MyDrive/images/Padilla - Nobleza virtuosa_testExtract (2)_pages-to-jpg-0002.jpg',
    ]
]
# Check image objects for images
from PIL import Image
# create figure
fig = plt.figure(figsize=(20, 10))

rows = 1
columns =2

Image1 = Image.open('/content/drive/MyDrive/images/Padilla - Nobleza virtuosa_testExtract (2)_pages-to-jpg-0001.jpg')
Image2 = Image.open('/content/drive/MyDrive/images/Padilla - Nobleza virtuosa_testExtract (2)_pages-to-jpg-0002.jpg')

fig.add_subplot(rows, columns, 1)
plt.imshow(Image1)
plt.axis('off')
plt.title ("Handwritten Text")

fig.add_subplot(rows, columns, 2)
plt.imshow(Image2)
plt.axis('off')
plt.title ("Image with Text")
prediction_groups = pipeline.recognize(images)
# plot the text predictions
fig, axs = plt.subplots(ncols=len(images), figsize=(25, 15))
for ax, image, predictions in zip(axs, images, prediction_groups):
    keras_ocr.tools.drawAnnotations(image=image,
                                    predictions=predictions,
                                    ax=ax)
  predicted_image_1 = prediction_groups[0]
for text, box in predicted_image_1:
    print(text)
  letters_with_diacritics_lower = {
    'a': ['á', 'à', 'â', 'ä', 'ã', 'å', 'ā', 'ă', 'ą', 'ǎ', 'ǻ', 'ȁ', 'ȃ', 'ả', 'ạ', 'ấ', 'ầ', 'ẩ', 'ẫ', 'ậ', 'ắ', 'ằ', 'ẳ', 'ẵ', 'ặ'],
    'e': ['é', 'è', 'ê', 'ë', 'ẽ', 'ē', 'ĕ', 'ė', 'ę', 'ě', 'ȅ', 'ȇ', 'ȩ', 'ẻ', 'ẹ', 'ế', 'ề', 'ể', 'ễ', 'ệ'],
    'i': ['í', 'ì', 'î', 'ï', 'ĩ', 'ī', 'ĭ', 'į', 'ı', 'ǐ', 'ȉ', 'ȋ', 'ỉ', 'ị'],
    'o': ['ó', 'ò', 'ô', 'ö', 'õ', 'ō', 'ŏ', 'ő', 'ơ', 'ǒ', 'ǿ', 'ȍ', 'ȏ', 'ȫ', 'ȭ', 'ȯ', 'ȱ', 'ỏ', 'ọ', 'ố', 'ồ', 'ổ', 'ỗ', 'ộ', 'ớ', 'ờ', 'ở', 'ỡ', 'ợ'],
    'u': ['ú', 'ù', 'û', 'ü', 'ũ', 'ū', 'ŭ', 'ů', 'ű', 'ų', 'ư', 'ǔ', 'ǖ', 'ǘ', 'ǚ', 'ǜ', 'ȕ', 'ȗ', 'ủ', 'ụ', 'ứ', 'ừ', 'ử', 'ữ', 'ự'],
    'y': ['ý', 'ỳ', 'ŷ', 'ÿ', 'ȳ', 'ỷ', 'ỵ', 'ỹ'],
    'c': ['ç', 'ć', 'ĉ', 'ċ', 'č', 'ƈ', 'ȼ'],
    'n': ['ñ', 'ń', 'ņ', 'ň', 'ƞ', 'ȵ', 'ǹ'],
    's': ['ś', 'ŝ', 'ş', 'š', 'ș', 'ṡ', 'ṣ'],
    'z': ['ź', 'ż', 'ž', 'ƶ', 'ȥ', 'ẑ', 'ẓ', 'ẕ'],
}
def replace_in_text(a,b):
  for i in text:
    if(i == 'ç'):
      i = 'z'
  return text
  count = 0
for text,box in predicted_image_1:
  if 'ç' in text:
    text = replace_in_text('ç','z')
    count += 1
    print(count)
