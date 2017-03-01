import hug
import twilio.twiml

@hug.get(output=hug.output_format.text)
def sms(Body):
    print(Body)
    return Body
        
