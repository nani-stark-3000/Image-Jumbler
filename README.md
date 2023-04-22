# Image-Jumbler

This is a Python script that reads an image file, crops it into 5 equal parts, and then concatenates the cropped parts in a different order to create a jumbled image. 

## Requirements
- Python 3
- OpenCV (`cv2`)

## Usage
1. Place the image file you want to crop and jumble in the same directory as the script.
2. Replace `img9.jpg` in the script with the name of your image file.
3. Run the script.

```python
python image_crop_and_concat.py
```

4. The output jumbled image will be saved in the same directory as `img9jumbled.jpg`. 
5. Optionally, you can uncomment the code block to show the original image and each of the cropped images separately.

##Images

1. Original Image

![i](https://github.com/nani-stark-3000/Image-Jumbler/blob/d6c7804c43641bb417fe8d14c7601f0ecc3810a9/img6.jpg)

2. Jumbled Image

![Ji](https://github.com/nani-stark-3000/Image-Jumbler/blob/d6c7804c43641bb417fe8d14c7601f0ecc3810a9/img6jumbled.jpg)

## Notes
- The script crops the image into 5 equal horizontal parts.
- The cropped parts are concatenated in the following order: bottom, middle-right, middle-left, top-right, top-left.
- The original image is not modified. The jumbled image is saved as a new file.
