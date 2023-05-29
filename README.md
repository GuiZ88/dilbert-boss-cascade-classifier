<a name="readme-top"></a>

<br />
<div align="center">
  <h3 align="center">Dilbert and Boss - Cascade Classifier</h3>

  <p align="center">
    The goal of this repository is to merge the two classifiers created (Dilbert and Boss) to locate them together in a single panel.    
</div>

<!-- ABOUT THE PROJECT -->
## About The Project

After creating a classifier for both Dilbert and the Boss and thus obtaining the 'cascade.xml'.
(Using the methodology at the repository [dilbert-cascade-classifier by GuiZ88](project https://github.com/GuiZ88/dilbert-cascade-classifier) ​​)

We proceed to create a small script "detect_dilbert_boss.py" where the cascade paths and that of the 'undefined' directory containing generic cartoons are specified, which are processed to identify the two subjects and, where found, moved to the 'detected' directory, enclosing the subjects in rectangles.

```python
# declare the classifiers for dilbert and boss
dilbert_cascade = cv2.CascadeClassifier('dilbert/data/cascade.xml')
dogbert_cascade = cv2.CascadeClassifier('ponty-haired-boss/data/cascade.xml')
```
```sh
python3 detect_dilbert_boss.py
```

![Boss & Dilbert detected](detected/2021-05-19_0.png?raw=true "Boss & Dilbert detected")

This also generates a file 'detect_dilbert_boss.txt' where the name of the file and the coordinates of the identified rectangles are present on each line. The first two for Dilbert the second two for the boss. (There are only 4 coordinates for two characters as they can only appear once!)

```txt
2017-11-19_0.png 187.5 154.5 58.5 192.5
2015-04-26_2.png 137.5 129.5 37.0 113.0
2019-05-22_2.png 184.0 176.0 47.5 155.5
2011-02-20_2.png 178.5 120.5 119.5 140.5
```

<u><b>In this repositories there are only some sample images for each folder.</b></u>

<p align="right">(<a href="#readme-top">back to top</a>)</p>