class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

test_image_pixels = """[[0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0],
 [0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0],
 [0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0],
 [0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0],
 [0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0],
 [0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0],
 [0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0],
 [0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.011764705882352941,
  0.00392156862745098,
  0.0,
  0.0,
  0.027450980392156862,
  0.0,
  0.1450980392156863,
  0.0,
  0.0],
 [0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.00392156862745098,
  0.00784313725490196,
  0.0,
  0.10588235294117647,
  0.32941176470588235,
  0.043137254901960784,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.4666666666666667,
  0.0,
  0.0],
 [0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.00392156862745098,
  0.0,
  0.0,
  0.34509803921568627,
  0.5607843137254902,
  0.43137254901960786,
  0.0,
  0.0,
  0.0,
  0.0,
  0.08627450980392157,
  0.36470588235294116,
  0.41568627450980394,
  0.0,
  0.0],
 [0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.01568627450980392,
  0.0,
  0.20784313725490197,
  0.5058823529411764,
  0.47058823529411764,
  0.5764705882352941,
  0.6862745098039216,
  0.615686274509804,
  0.6509803921568628,
  0.5294117647058824,
  0.6039215686274509,
  0.6588235294117647,
  0.5490196078431373,
  0.0,
  0.0],
 [0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.00784313725490196,
  0.0,
  0.043137254901960784,
  0.5372549019607843,
  0.5098039215686274,
  0.5019607843137255,
  0.6274509803921569,
  0.6901960784313725,
  0.6235294117647059,
  0.6549019607843137,
  0.6980392156862745,
  0.5843137254901961,
  0.592156862745098,
  0.5647058823529412,
  0.0,
  0.0],
 [0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.00392156862745098,
  0.0,
  0.00784313725490196,
  0.00392156862745098,
  0.0,
  0.011764705882352941,
  0.0,
  0.0,
  0.45098039215686275,
  0.4470588235294118,
  0.41568627450980394,
  0.5372549019607843,
  0.6588235294117647,
  0.6,
  0.611764705882353,
  0.6470588235294118,
  0.6549019607843137,
  0.5607843137254902,
  0.615686274509804,
  0.6196078431372549,
  0.043137254901960784,
  0.0],
 [0.0,
  0.0,
  0.0,
  0.0,
  0.00392156862745098,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.011764705882352941,
  0.0,
  0.0,
  0.34901960784313724,
  0.5450980392156862,
  0.35294117647058826,
  0.3686274509803922,
  0.6,
  0.5843137254901961,
  0.5137254901960784,
  0.592156862745098,
  0.6627450980392157,
  0.6745098039215687,
  0.5607843137254902,
  0.6235294117647059,
  0.6627450980392157,
  0.18823529411764706,
  0.0],
 [0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.00784313725490196,
  0.01568627450980392,
  0.00392156862745098,
  0.0,
  0.0,
  0.0,
  0.3843137254901961,
  0.5333333333333333,
  0.43137254901960786,
  0.42745098039215684,
  0.43137254901960786,
  0.6352941176470588,
  0.5294117647058824,
  0.5647058823529412,
  0.5843137254901961,
  0.6235294117647059,
  0.6549019607843137,
  0.5647058823529412,
  0.6196078431372549,
  0.6627450980392157,
  0.4666666666666667,
  0.0],
 [0.0,
  0.0,
  0.00784313725490196,
  0.00784313725490196,
  0.00392156862745098,
  0.00784313725490196,
  0.0,
  0.0,
  0.0,
  0.0,
  0.10196078431372549,
  0.4235294117647059,
  0.4588235294117647,
  0.38823529411764707,
  0.43529411764705883,
  0.4588235294117647,
  0.5333333333333333,
  0.611764705882353,
  0.5254901960784314,
  0.6039215686274509,
  0.6039215686274509,
  0.611764705882353,
  0.6274509803921569,
  0.5529411764705883,
  0.5764705882352941,
  0.611764705882353,
  0.6980392156862745,
  0.0],
 [0.011764705882352941,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.08235294117647059,
  0.20784313725490197,
  0.3607843137254902,
  0.4588235294117647,
  0.43529411764705883,
  0.403921568627451,
  0.45098039215686275,
  0.5058823529411764,
  0.5254901960784314,
  0.5607843137254902,
  0.6039215686274509,
  0.6470588235294118,
  0.6666666666666666,
  0.6039215686274509,
  0.592156862745098,
  0.6039215686274509,
  0.5607843137254902,
  0.5411764705882353,
  0.5882352941176471,
  0.6470588235294118,
  0.16862745098039217],
 [0.0,
  0.0,
  0.09019607843137255,
  0.21176470588235294,
  0.2549019607843137,
  0.2980392156862745,
  0.3333333333333333,
  0.4627450980392157,
  0.5019607843137255,
  0.4823529411764706,
  0.43529411764705883,
  0.44313725490196076,
  0.4627450980392157,
  0.4980392156862745,
  0.49019607843137253,
  0.5450980392156862,
  0.5215686274509804,
  0.5333333333333333,
  0.6274509803921569,
  0.5490196078431373,
  0.6078431372549019,
  0.6313725490196078,
  0.5647058823529412,
  0.6078431372549019,
  0.6745098039215687,
  0.6313725490196078,
  0.7411764705882353,
  0.24313725490196078],
 [0.0,
  0.26666666666666666,
  0.3686274509803922,
  0.35294117647058826,
  0.43529411764705883,
  0.4470588235294118,
  0.43529411764705883,
  0.4470588235294118,
  0.45098039215686275,
  0.4980392156862745,
  0.5294117647058824,
  0.5333333333333333,
  0.5607843137254902,
  0.49411764705882355,
  0.4980392156862745,
  0.592156862745098,
  0.6039215686274509,
  0.5607843137254902,
  0.5803921568627451,
  0.49019607843137253,
  0.6352941176470588,
  0.6352941176470588,
  0.5647058823529412,
  0.5411764705882353,
  0.6,
  0.6352941176470588,
  0.7686274509803922,
  0.22745098039215686],
 [0.27450980392156865,
  0.6627450980392157,
  0.5058823529411764,
  0.40784313725490196,
  0.3843137254901961,
  0.39215686274509803,
  0.3686274509803922,
  0.3803921568627451,
  0.3843137254901961,
  0.4,
  0.4235294117647059,
  0.41568627450980394,
  0.4666666666666667,
  0.47058823529411764,
  0.5058823529411764,
  0.5843137254901961,
  0.611764705882353,
  0.6549019607843137,
  0.7450980392156863,
  0.7450980392156863,
  0.7686274509803922,
  0.7764705882352941,
  0.7764705882352941,
  0.7333333333333333,
  0.7725490196078432,
  0.7411764705882353,
  0.7215686274509804,
  0.1411764705882353],
 [0.06274509803921569,
  0.49411764705882355,
  0.6705882352941176,
  0.7372549019607844,
  0.7372549019607844,
  0.7215686274509804,
  0.6705882352941176,
  0.6,
  0.5294117647058824,
  0.47058823529411764,
  0.49411764705882355,
  0.4980392156862745,
  0.5725490196078431,
  0.7254901960784313,
  0.7647058823529411,
  0.8196078431372549,
  0.8156862745098039,
  1.0,
  0.8196078431372549,
  0.6941176470588235,
  0.9607843137254902,
  0.9882352941176471,
  0.984313725490196,
  0.984313725490196,
  0.9686274509803922,
  0.8627450980392157,
  0.807843137254902,
  0.19215686274509805],
 [0.0,
  0.0,
  0.0,
  0.047058823529411764,
  0.2627450980392157,
  0.41568627450980394,
  0.6431372549019608,
  0.7254901960784313,
  0.7803921568627451,
  0.8235294117647058,
  0.8274509803921568,
  0.8235294117647058,
  0.8156862745098039,
  0.7450980392156863,
  0.5882352941176471,
  0.3215686274509804,
  0.03137254901960784,
  0.0,
  0.0,
  0.0,
  0.6980392156862745,
  0.8156862745098039,
  0.7372549019607844,
  0.6862745098039216,
  0.6352941176470588,
  0.6196078431372549,
  0.592156862745098,
  0.043137254901960784],
 [0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0],
 [0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0],
 [0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0],
 [0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0],
 [0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0],
 [0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0]""" 

test_image_label = "Ankle boot" 
classifier_param = {"img": test_image_pixels}