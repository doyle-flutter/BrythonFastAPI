if __name__ == "__main__":
    from browser import document, alert, html, timer

    body = document.select("#body")

    headerWrapper = html.DIV(id="headerWrapper")
    headerWrapper["style"] = "margin: 10px; text-align: center;"
    headerTitle = html.H1("James DEV", id="headerTitle", class_name="headerTitle")
    headerWrapper <= headerTitle
    body[0] <= headerWrapper

    navWrapper = html.DIV(id="navWrapper", class_name="navWrapper")
    navWrapper["style"] = "background-color: grey;"
    navItemList = ["Home", "Menu1", "Menu2", "Menu3", "Menu4", "Settings"]
    navItems = []
    for i in navItemList:
        itemDiv = html.DIV(i, id=f"nav_{i}", class_name="navItem")
        itemDiv[
            "style"] = f"padding: 10px 0; display: inline-block; width: {(100 / len(navItemList))}%; text-align: center; color: white; font-weight: bold;cursor: pointer;"


        def mOn(ev):
            ev.target.style.backgroundColor = 'red'


        def mOff(ev):
            ev.target.style.backgroundColor = 'grey'


        itemDiv.bind("mouseenter", mOn)
        itemDiv.bind("mouseleave", mOff)
        navItems.append(itemDiv)
    navWrapper <= navItems
    body[0] <= navWrapper

    contentWrapper = html.DIV(id="contentWrapper", class_name="contentWrapper")
    contentList = [
        "https://cdn.pixabay.com/photo/2017/12/27/14/02/friends-3042751__340.jpg",
        "https://cdn.pixabay.com/photo/2016/01/05/17/51/maltese-1123016__340.jpg",
        "https://cdn.pixabay.com/photo/2016/07/15/15/55/dachshund-1519374__340.jpg",
        "https://cdn.pixabay.com/photo/2016/02/26/16/32/bulldog-1224267__340.jpg",
        "https://cdn.pixabay.com/photo/2014/08/21/14/51/dog-423398__340.jpg",
        "https://cdn.pixabay.com/photo/2018/10/01/09/21/pets-3715733__340.jpg",
        "https://cdn.pixabay.com/photo/2017/08/07/18/57/dog-2606759__340.jpg",
        "https://cdn.pixabay.com/photo/2016/02/19/15/46/labrador-retriever-1210559__340.jpg"
    ]
    contentItems = []
    for url in contentList:
        contentItem = html.DIV(id="contentDiv", class_name="contentDiv")
        contentItem['style'] = "width: 40%; margin: 5%; display: inline-block; font-size: 0"
        contentItemImage = html.IMG(src=url)
        contentItemImage['style'] = "width: 100%;"
        contentItem <= contentItemImage
        contentItems.append(contentItem)
    contentWrapper <= contentItems
    body[0] <= contentWrapper