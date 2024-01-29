from flet import *

def main(page : Page):
    
    # colors for web applicaiton
    BG = '#041955'
    FWG = '#97b4ff'
    FG = '#3450a1'
    PINK = '#eb06ff'

    # creating the content pages

    first_page_contents = Container(
        content=Column(
            controls=[
                Row(
                    alignment="spaceBetween",
                    Container(height=20),
                Text(value="What's av alok")


                )
            ]
        )
    )

    # creating the pages 
    page_1 = Container()
    page_2 = Row(
        controls=[
            Container(
                width=400,
                height=850,
                bgcolor=FG,
                border_radius=35,
                padding=padding.only(
                    top=50, left=20,
                    bottom=5, right=20
                ),content=Column(
                    controls=[
                        first_page_contents
                    ]
                )

            )
        ]
    )

    # creating the containers 
    container = Container(
        width=400,
        height=850,
        border_radius=35,
        bgcolor=BG,
        content= Stack(
            controls=[
                page_1,
                page_2
            ]
        )
    )

    page.add(container)

app(target=main)