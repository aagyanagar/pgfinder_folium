import folium

pgs = []

with open("pg.txt","r", encoding = "utf-8") as f:
    for line in f:
        name, area, price, wifi, lat, lon = [x.strip() for x in line.split(",")]
        pgs.append({
        "name" : name,
        "area" : area,
        "price" : int(price),
        "wifi" : wifi,
        "lat" : float(lat),
        "lon" : float(lon)
       })
m = folium.Map(location=[23.0225, 72.5714], zoom_start=13)

for pg in pgs:
    popup = f"{pg['name']}<br>{pg['area']}<br>Price: {pg['price']}<br>Wifi: {pg['wifi']}"1
    folium.Marker([pg["lat"], pg["lon"]], popup=popup).add_to(m)

m.save("pg_map.html")
print("Map , Open pg_map.html in your browser")

while True:
    print("Show all pgs")
    print("1 - Filter by area")
    print("2 - Filter by price")
    print("3 - Filter by wifi")
    print("4 - exit")

    choice = input("Enter choice: ")

    if choice == "1":
        area = input("Enter Area: ").strip().lower()
        for pg in pgs:
            if pg["area"].lower() == area:
                print(pg)

    elif choice == "2":
        try:
            price = int(input("Enter Price: ").strip())
        except ValueError:
            print("Enter a valid number")
            continue
        for pg in pgs:
            if pg["price"] == price:
                print(pg)

    elif choice == "3":
        wifi = input("Need wifi? (Yes/No): ").strip().lower()
        for pg in pgs:
            if pg["wifi"].lower() == wifi:
                print(pg)

    elif choice == "4":
        break

    else:
        print("Invalid choice")