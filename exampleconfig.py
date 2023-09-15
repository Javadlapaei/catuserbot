from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 21609328
    API_HASH = "a4b9bbdffa3b5602e0e940ba1fd653d9"
    # the name to display in your alive message
    ALIVE_NAME = "kourosh"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://fustzhcb:plaC_TKUgoJNEyFtC-RqzY3Qf-RYgbSM@silly.db.elephantsql.com/fustzhcb"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1AZWarzsBu5AHInbgulgFCd3kYGWtmLUbei9gdAUa6voLjfWV2KxS2kgwNQTVLolHk98ix9cUSVIJq9j-arNAbSjxVgOI9B5w61PGOxwFoH8LkggVZP208t4Vm2UDONTbzodsKIoxgmhfAaBJbCmGnlX2gpW4WpThU3zTKNEdaDJftaeOr2TNN0AlEpEXUHfdaPbq4duoDubwPSzY76eCapu7A4KIb2R6jEJd-F--oaLWcO4EAnmA6skigIc7rH6-gt6pk5ZFP9EfBmqrZFHl33e9tnnVLYP_ZT8gGPZWjmqHXB6rL1VSzBs40IBbFkCO7UorLsBu1kbnNt99Kn-HWhlysEaDkBI="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "6653543487:AAFnnrF3iDkLd3lBTXo7sW5ZP9O8V421bCk"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1001877478696
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "True"
