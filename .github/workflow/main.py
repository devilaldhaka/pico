from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import webbrowser
import bluetooth
from kivy.uix.spinner import Spinner


class TwoLabelsApp(App):
    def build(self):
        self.cols = 2
        layout = BoxLayout(orientation='vertical', padding=0.00001, spacing=0.1)
        label1 = Label(text='A:=',size_hint=(.1, 1.8),
                      pos_hint={'rightcorner_x': .1, 'rightcorner_y': .20}) 
        button1 = Button(text='measure1',size_hint=(.1, 1.8),
                      pos_hint={'center_x': .5, 'center_y': 1.20})
        button1.bind(on_press=self.on_button_press) 
        label2 = Label(text='B:=',size_hint=(.1, 1.8),
                      pos_hint={'rightcorner_x': .1, 'rightcorner_y': .20})
        button2 = Button(text='measure2',size_hint=(.1, 1.8),
                      pos_hint={'center_x': .5, 'rightcorner_y': 1.20})
        button2.bind(on_press=self.on_button_press)
        label3 = Label(text='C:=',size_hint=(.1, 1.8),
                      pos_hint={'rightcorner_x': .1, 'rightcorner_y': .20})
        button3 = Button(text='measure3',size_hint=(.1, 1.8),
                      pos_hint={'center_x': .5, 'center_y': .20})
        button3.bind(on_press=self.on_button_press)
        label4 = Label(text='D:=',size_hint=(.1, 1.8),
                      pos_hint={'rightcorner_x': .1, 'rightcorner_y': .20})
        button4 = Button(text='measure4',size_hint=(.1, 1.8),
                      pos_hint={'center_x': .5, 'rightcorner_y': .20})
        button4.bind(on_press=self.on_button_press)
        label5 = Label(text='E:=',size_hint=(.1, 1.8),
                      pos_hint={'rightcorner_x': .1, 'rightcorner_y': .20})
        button5 = Button(text='measure5',size_hint=(.1, 1.8),
                      pos_hint={'center_x': .5, 'rightcorner_y': .20})
        button5.bind(on_press=self.on_button_press)
        label6 = Label(text='F:=',size_hint=(.1, 1.8),
                      pos_hint={'rightcorner_x': .1, 'rightcorner_y': .20}) 
        button6 = Button(text='measure6',size_hint=(.1, 1.8),
                      pos_hint={'center_x': .5, 'rightcorner_y': .20})
        button6.bind(on_press=self.on_button_press)
        label7 = Label(text='G:=',size_hint=(.1, 1.8),
                      pos_hint={'rightcorner_x': .1, 'rightcorner_y': .20})
        button7 = Button(text='measure7',size_hint=(.1, 1.8),
                      pos_hint={'center_x': .5, 'rightcorner_y': .20})
        button7.bind(on_press=self.on_button_press)
        label8 = Label(text='H:=',size_hint=(.1, 1.8),
                      pos_hint={'rightcorner_x': .1, 'rightcorner_y': .20})
        button8 = Button(text='measure8',size_hint=(.1, 1.8),
                      pos_hint={'center_x': .5, 'rightcorner_y': .20})
        button8.bind(on_press=self.on_button_press)
        label9 = Label(text='I:=',size_hint=(.1, 1.8),
                      pos_hint={'rightcorner_x': .1, 'rightcorner_y': .20})
        button9 = Button(text='measure9',size_hint=(.1, 1.8),
                      pos_hint={'center_x': .5, 'rightcorner_y': .20})
        button9.bind(on_press=self.on_button_press)
        label10 = Label(text='J:=',size_hint=(.1, 1.8),
                      pos_hint={'rightcorner_x': .1, 'rightcorner_y': .20})
        button10 = Button(text='measure10',size_hint=(.1, 1.8),
                      pos_hint={'center_x': .5, 'rightcorner_y': .20})
        button10.bind(on_press=self.on_button_press)
        label11 = Label(text='K:=',size_hint=(.1, 1.8),
                      pos_hint={'rightcorner_x': .1, 'rightcorner_y': .20})
        button11 = Button(text='measure11',size_hint=(.1, 1.8),
                      pos_hint={'center_x': .5, 'rightcorner_y': .20})
        button11.bind(on_press=self.on_button_press)
        label12 = Label(text='L:=',size_hint=(.1, 1.8),
                      pos_hint={'rightcorner_x': .1, 'rightcorner_y': .20}) 
        button12 = Button(text='measure12',size_hint=(.1, 1.8),
                      pos_hint={'center_x': .5, 'rightcorner_y': .20})
        button12.bind(on_press=self.on_button_press)
        label13 = Label(text='M:=',size_hint=(.1, 1.8),
                      pos_hint={'rightcorner_x': .1, 'rightcorner_y': .20}) 
        button13 = Button(text='measure13',size_hint=(.1, 1.8),
                      pos_hint={'center_x': .5, 'rightcorner_y': .20})
        button13.bind(on_press=self.on_button_press)
        button14 = Button(text='upload',size_hint=(.1, 1.9),
                          pos_hint={'center_x': .5, 'rightcorner_y': .20})
        button14.bind(on_press=self.open_website)

        self.scan_button15 = Button(text='Scan for Devices',size_hint=(.2, 1.9),
                          pos_hint={'center_x': .5, 'rightcorner_y': .25})
        self.scan_button15.bind(on_press=self.scan_for_devices)
        layout.add_widget(self.scan_button15)
        
        self.device_spinner = Spinner(text='Select Device', values=(),size_hint=(.2,1.9),pos_hint={'center_x': .5, 'rightcorner_y': .25})
        layout.add_widget(self.device_spinner)
        
        self.connect_button16 = Button(text='Connect', disabled=True,size_hint=(.2, 1.9),
                          pos_hint={'center_x': .5, 'rightcorner_y': .30})
        self.connect_button16.bind(on_press=self.connect_to_device)
        layout.add_widget(self.connect_button16)
        
        self.status_label = Label(text='Status: Not connected',size_hint=(.1, 1.9),
                          pos_hint={'center_x': .5, 'rightcorner_y': .20})
        layout.add_widget(self.status_label)

        layout.add_widget(label1)
        layout.add_widget(button1)
        layout.add_widget(label2)
        layout.add_widget(button2)
        layout.add_widget(label3)
        layout.add_widget(button3)
        layout.add_widget(label4)
        layout.add_widget(button4)
        layout.add_widget(label5)
        layout.add_widget(button5)
        layout.add_widget(label6)
        layout.add_widget(button6)
        layout.add_widget(label7)
        layout.add_widget(button7)
        layout.add_widget(label8)
        layout.add_widget(button8)
        layout.add_widget(label9)
        layout.add_widget(button9)
        layout.add_widget(label10)
        layout.add_widget(button10)
        layout.add_widget(label11)
        layout.add_widget(button11)
        layout.add_widget(label12)
        layout.add_widget(button12)
        layout.add_widget(label13)
        layout.add_widget(button13)
        layout.add_widget(button14)
       
    


            
        return layout
    
    def open_website(self, instance):
        webbrowser.open('http://127.0.0.1:5500/index.html#')
    

    def on_button_press(self, instance):
        print("measure value")

    def scan_for_devices(self, instance):
        self.status_label.text = 'Scanning for devices...'
        nearby_devices = bluetooth.discover_devices(lookup_names=True)
        device_names = [f"{name} ({addr})" for addr, name in nearby_devices]
        self.device_spinner.values = device_names
        if device_names:
            self.device_spinner.text = device_names[0]
            self.connect_button.disabled = False
            self.status_label.text = 'Devices found. Select a device to connect.'
        else:
            self.status_label.text = 'No devices found. Try again.'

    def connect_to_device(self, instance):
        selected_device = self.device_spinner.text
        if selected_device == 'Select Device':
            self.status_label.text = 'Please select a device to connect.'
            return
        
        addr = selected_device.split('(')[-1][:-1]  # Extract the address from the selected text
        self.status_label.text = f'Connecting to {addr}...'
        
        # Example of connecting to a Bluetooth device
        # You'll need to replace the service and protocol with actual values
        try:
            service_matches = bluetooth.find_service(address=addr)
            if len(service_matches) == 0:
                self.status_label.text = 'Could not find the service.'
                return
            
            first_match = service_matches[0]
            port = first_match["port"]
            name = first_match["name"]
            host = first_match["host"]    
            sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            sock.connect((host, port))
            
            self.status_label.text = f'Connected to {name} on {host}'
            sock.close()
        except Exception as e:
            self.status_label.text = f'Failed to connect: {e}'


if __name__ == '__main__':
    TwoLabelsApp().run()
