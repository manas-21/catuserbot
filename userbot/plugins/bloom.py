"""
Time In Profile Pic.....
Command: `.Bloom`

Hmmmm U need to config RAVANA_LEELA var in Heroku with any telegraph image link

:::::Credit Time::::::
1) Coded By: @s_n_a_p_s
2) Ported By: @r4v4n4 (Noodz Lober)
3) End Game Help By: @spechide
4) Better Colour Profile Pic By @PhycoNinja13b

#curse: who ever edits this credit section will goto hell

⚠️DISCLAIMER⚠️

USING THIS PLUGIN CAN RESULT IN ACCOUNT BAN. WE DONT CARE ABOUT BAN, SO WE ARR USING THIS.
"""
import os
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon.tl import functions
from uniborg.util import admin_cmd
import asyncio
import shutil 
import random

FONT_FILE_TO_USE = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

@borg.on(admin_cmd(pattern="bloom ?(.*)", allow_sudo=True))
async def autopic(event): 
    await event.reply("Bloom colour profile pic have been enabled © @PhycoNinja13b") 
    downloaded_file_name = "./ravana/original_pic.png"
    downloader = SmartDL(Config.RAVANA_LEELA, downloaded_file_name, progress_bar=True)
    downloader.start(blocking=False)
    photo = "photo_pfp.png"
    while not downloader.isFinished():
        place_holder = None

    while True:
        #RIP Danger zone Here no editing here plox

        #Date/Time Colour
        R = random.randint(0,256)
        B = random.randint(0,256)
        G = random.randint(0,256)

        #Username Colour
        FR = (256 - R) 
        FB = (256 - B) 
        FG = (256 - G)

        #Optional Emoji Colour
        ER = (128 - FR)
        EB = (128 - FB)
        EG = (128 - FG)

        #Check, so that output is not negative 
        if ER<0:
            ER = ER*(-1)
        if EB<0:
            EB = EB*(-1)
        if EG<0:
            EG = EG*(-1)

        shutil.copy(downloaded_file_name, photo)
        image = Image.open(photo)
        image.paste( (R, G, B), [0,0,image.size[0],image.size[1]])
        image.save(photo)
        
        #Edit only Below part 🌚 Or esle u will be responsible 🤷‍♂
        current_time = datetime.now().strftime("\nTime: %H:%M:%S \n \nDate: %d/%m/%y")
        img = Image.open(photo)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 60)
        ofnt = ImageFont.truetype(FONT_FILE_TO_USE, 20)
        efnt = ImageFont.truetype(FONT_FILE_TO_USE, 250)
        drawn_text.text((120, 300), current_time, font=fnt, fill=(FR,FG,FB))
        drawn_text.text((120, 300), "© @PhycoNinja13b", font = ofnt, fill=(FR,FG,FB))
        drawn_text.text((250, 100), "    👾", font = efnt, fill=(ER,EG,EB))
        img.save(photo)
        file = await event.client.upload_file(photo)  # pylint:disable=E0602
        try:
            await event.client(functions.photos.UploadProfilePhotoRequest(  # pylint:disable=E0602
                file
            ))
            os.remove(photo)
            await asyncio.sleep(50)
        except:
            return