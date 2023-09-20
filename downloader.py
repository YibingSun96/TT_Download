# # Download Videos from Tiktok
# Created by: Yibing Sun (ysun326@wisc,edu)
# Time: Sep. 6th, 2021

## Loading Packages
# ### In terminal or use !pip3
# pip3 install TikTokApi
# python -m playwright install 

from TikTokApi import TikTokApi
import random
import string

# ### Get your s_v_web_id
# Use Chrome to open tiktok and sign in.
# Click on the *the lock icon* before the link *tiktok.com/en/*.
# Click on *www.tiktok.com*, *Coockies*, *s_v_web_id*, copy and paste *Content*.

erifyFp="ENTER YOURS HERE"
did = str(random.randint(10000, 999999999))
api = TikTokApi(custom_verifyFp=verifyFp, use_test_endpoints=True, custom_device_id = did)

## Demo Test_Sample
o_dir = 'OUTPUT DIR'
test = api.video(id='VIDEO ID HERE')
video_bytes = test.bytes()
with open("test.mp4", 'wb') as o:
    o.write(video_bytes) 


#If succeed, continue in loop:


## Loading Packages
import pandas as pd
import os

for i in range(len(df)):
    df["video_id"][i] = df["Link"].str.split("video/")[i][1]

for i in range(len(df)):
    try: 
        video_id = df['video_id'][i]
        tiktok = api.get_tiktok_by_id(id = video_id)
        video_bytes = api.get_video_by_tiktok(tiktok)
        filename = str(df['ID'][I]) + '.mp4'
        o_path = os.path.join(o_dir, filename)
        with open(o_path, 'wb') as o:
            o.write(video_bytes)
        print('finished id' + str(i+1))
    except:
        print('problem regarding' + str(i+1))
        pass
