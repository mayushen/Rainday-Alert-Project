import requests
# import smtplib as smtp
from twilio.rest import Client

# MY_EMAIL = "YOUR_EMAIL"
# PASSWORD = "YOUR_PASSWORD"
account_sid = "ACb3a2c0ef2d9c56f61660b6ccdf6c5d21"
auth_token = "YOUR_AUTH_TOKEN"

api_keys = "YOUR_API_KEYS"
END_POINT = "https://api.openweathermap.org/data/2.5/onecall"
# Taipei Location
lat = 25.0478
lon = 121.5319
qsp = {
    "lat": lat,
    "lon": lon,
    "exclude": "current,minutely,daily,alerts",
    "appid": api_keys
}

r = requests.get(END_POINT, params=qsp)
r.raise_for_status()
weather_data = r.json()
weather_data = weather_data["hourly"][0: 13]

will_rain = False
for hr_data in weather_data:
    weather_id = hr_data["weather"][0]["id"]
    if weather_id < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    sender_number = "YOUR_SENDER_NUMBER"
    receiver_number = "YOUR_PHONE_NUMBER"
    msg = client.messages \
        .create(
            body="\nIt's going to rain today! \nRainy Day ALERT! Be sure to bring an umbrella when you go outside☔.️",
            from_=sender_number,
            to=receiver_number
        )
    print(msg.status)
    
    # with smtp.SMTP("smtp.gmail.com") as conn:
    #     conn.starttls()
    #     conn.login(user=MY_EMAIL, password=PASSWORD)
    #     conn.sendmail(from_addr=MY_EMAIL, to_addrs="YOUR_EMAIL",
    #                   msg="Subject : Rainy Day ALERT!!"
    #                       "\n\n今天上班時段會下雨，出門前記得帶把傘唷！".encode("utf-8"))
    #     conn.close()
