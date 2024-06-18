# from g4f.client import Client
# from g4f.cookies import set_cookies
# client = Client()
# set_cookies(".google.com", {
#   "__Secure-1PSID": "g.a000kwgx-lxgcT0G6NmSF1a6aMp5ix0caPIV4-G4XHQ3Q4z73YwmpANPR-vzjsxy1A1-e943JgACgYKAXsSARASFQHGX2Mi1GUt5A1NA-beFKZzDowsFxoVAUF8yKrFYgarVbCsa9FauvbmxYne0076",
#   "__Secure-1PSIDCC": "AKEyXzVOZD_XuFRCxvuiT-MgMs15wRstqoqC71hs7FkTT5PgjgsNQovtqa6F0qAwEDFuYD_CcWU",
#   "__Secure-1PSIDTS": "sidts-CjEB3EgAEteciW7Tm14RRuxboq1aUpN2GY6IhDiH7RecUpWTVmOaxsv-raT-lRbYaDugEAA"
# })

# def g4f_generate_image():


#   client = Client()
#   query_en = "illustration of time"

#   response = client.images.generate(
#       model="gemini",
#       prompt=query_en,
#   )
#   image_url = response.data[0].url
#   return image_url

# g4f_generate_image()
import asyncio
from gemini import Gemini, GeminiImage
cookies = {}
async def save_generated_images(generated_images, save_path="output", cookies=cookies):
    image_data_dict = await GeminiImage.fetch_images_dict(generated_images, cookies)  # Get bytes images dict asynchronously
    await GeminiImage.save_images(image_data_dict, save_path=save_path)  

# Run the async function
if __name__ == "__main__":
    cookies = {}
    client = Gemini(cookies=cookies)

    response = client.generate_content("Create illustrations of Seoul, South Korea.")

    generated_images = response.generated_images 
    asyncio.run(save_generated_images(generated_images, save_path="output", cookies=cookies))