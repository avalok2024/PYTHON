from flet import *
from custom_chekbox import CustomCheckBox


def main(page: Page):
    BG = '#041955'
    FWG = '#97b4ff'
    FG = '#3450a1'
    PINK = '#eb06ff'

    circle = Stack(
        controls=[
            Container(
                width=100,
                height=100,
                border_radius=50,
                bgcolor="white12"
            ),
            Container(
                gradient=SweepGradient(
                    center=alignment.center,
                    start_angle=0.0,
                    end_angle=3,
                    stops=[0.5, 0.5],
                    colors=['#00000000', PINK]
                ),
                width=100,
                height=100,
                border_radius=50,
                content=Row(alignment="center",
                            controls=[
                                Container(padding=padding.all(5),
                                          bgcolor=BG,
                                          width=90,
                                          height=90,
                                          border_radius=50,
                                          content=Container(
                                    bgcolor=FG,
                                    height=80, width=80,
                                    border_radius=40,
                                    content=CircleAvatar(opacity=0.8,
                                                         foreground_image_url="https://www.google.com/url?sa=i&url=https%3A%2F%2Funsplash.com%2Fs%2Fphotos%2Fimage&psig=AOvVaw1FY8AaZxzfpb-QF2QtFq7J&ust=1706872738104000&source=images&cd=vfe&opi=89978449&ved=0CBMQjRxqFwoTCPDWgcyCioQDFQAAAAAdAAAAABAE")

                                ))
                            ])
            )
        ]
    )

    first_page_contents = Container(
        content=Column(
            controls=[
                Row(alignment="spaceBetween",
                    controls=[
                        Container(
                            content=Icon(
                                icons.MENU
                            )
                        ),
                        Row(
                            contorls=[
                                Icon(icons.SEARCH),
                                Icon(icons.NOTIFICATION_ADD_OUTLINED)
                            ]
                        )
                        ]
                    ),
                Container(height=20),
                Text(
                    value="What's Av alok"
                ),

                Container(
                    padding=padding.only(top=10,bottom=20,),
                    # content=categories_card
                ),
                Container(height=20),
                Text("Today's Tasks"),
                Stack(
                    controls=[FloatingActionButton(bottom=2, right=20),
                              icon = icons.NOTIFICATION_ADD_OUTLINED]
                )


            ]
        )
    )

    page_1 = Container(
        width=400,
        height=850,
        bgcolor=BG,
        border_radius=35,
        padding= padding.only(left=50, top=60,right=200),

        content=Column(controls=[
            Row(alignment="end",controls=[
                Container(
                    border_radius=25,
                    padding=padding.only(
                        top=13, left=13
                    ),
                    height=50,
                    width=50,
                    border = border.all(color="white", width=1),
                    content = Text("<")
                )
            ])
        ])
    )