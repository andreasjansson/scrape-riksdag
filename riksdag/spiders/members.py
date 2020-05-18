import scrapy

from riksdag.items import Member


class MembersSpider(scrapy.Spider):
    name = "members"

    def start_requests(self):
        yield scrapy.Request(url="https://www.riksdagen.se/sv/ledamoter-partier/")

    def parse(self, response):
        member_links = response.css(".fellow-item a")
        yield from response.follow_all(member_links, self.parse_member)

    def parse_member(self, response):
        name = response.css(".biggest.fellow-name::text").get()
        name = name.split(" (")[0].strip()

        items = response.css("#main-content-read .component-fellow-intro .fellow-item")
        member = {}
        for item in items:
            texts = [t.get().strip() for t in item.css("::text")]
            texts = [t for t in texts if len(t) > 0]
            if (
                texts[0] == "Ladda hem högupplöst bild"
                or texts[0] == "Sociala medier:"
                or texts[0] == "Adress"
            ):
                continue

            key, value = texts
            if key == "E-post":
                value = value.replace("[på]", "@")
            member[key] = value

        valkrets, plats = member.get("Valkrets").split(", plats ")

        yield Member(
            namn=name,
            valkrets=valkrets,
            epost=member.get("E-post"),
            parti=member.get("Parti"),
            titel=member.get("Titel"),
            fodelsear=member.get("Född år"),
            telefon=member.get("Telefon"),
            plats=plats,
        )
