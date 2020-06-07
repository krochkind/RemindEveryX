# RemindEveryX
Sends a text message on recurring events that occur on specific days of the week (ex. the first Saturday in April, every Wednseday in February)

## Why?
I don't know about you but I kept running into the situation where I had to do different tasks on different days of different months - like, change my house air filters the first Saturday of January and June.  Or trim my trees the last Saturday of February.  Usually, it was a things for me to do around the house, now that it was a weekend.  I also have over 20 fruit trees, and keeping track of which trees need fertilizing which months required my remebering to look at a google sheet every month.

This wasn't working out... as evidence by my Peach curl (a disease that happens when you forget to spray your peach trees).  Could I have set up each of these monthly events as recurring annual appointments in Outlook?  Of course.  Could I have done this with cronjobs?  Yes.  But I thought, I could create a script that runs every day to look at a list of events and send me a text message reminder the tasks I needed to do that day.  That way, if I want to update any alerts, all I need to do is tweak a json file.  So I set it up on my Raspberry Pi as a cron job that runs every day at noon, and Bob's your uncle.

## How Does It Work?
The script uses Gmail to send text messages as email, so it requires a Gmail account.  I set it up as a cron job to run every day at noon

Use the *config.json* file to set your configuration settings
* gmail_login: The Gmail login to send text messages
* gmail_pwd: The password of the Gmail account
* send_alerts_to: Array of phone numbers that get text messages
  * phone_number: Phone number that receives the text (parentheses or hyphens are optional - they will be stripped out)
  * wireless_carrier: The service carrier that the phone number uses (must match the *sms_codes* object)

Use the *events.json* file to set your alerts (both the text and frequency)
* If you don't have any events for a day or month, you can remove them from the file.  I just left them for clarity
```
"January": {
        "Sunday": {
            "First": "This runs on the First Sunday of January"
        },
        "Thursday": {
            "Last": "This runs on the Last Sunday of January"
        },
},
"May": {
    "Friday": {
            "Every": "This runs Every Friday in May"
        },
}
```
