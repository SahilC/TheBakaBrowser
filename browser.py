from gi.repository import Gtk,WebKit
webview=WebKit.WebView()

def browser():
	win=Gtk.Window()
	screen=win.get_screen()
	win.set_title("The Baka Browser")
	win.connect("delete-event",Gtk.main_quit)
	win.set_default_size(screen.get_width(),screen.get_height())
	val=Gtk.Table(4,2,True)
	val.set_border_width(5)
	box=Gtk.Entry()
	wind=Gtk.ScrolledWindow()
	wind.add(webview)
	button=Gtk.Button("Go to==>")
	button1=Gtk.Button("==>")
	button2=Gtk.Button("<==")
	button2.connect("clicked",lambda x: webview.go_back())
	button1.connect("clicked",lambda x: webview.go_forward())
	button.connect("clicked",lambda x: webview.load_uri(box.get_text() if "http://" in box.get_text() else "http://"+box.get_text() ))
	button.set_size_request(20,20)	
	box.connect("activate",load)
	val.attach(box,2, 5,0,1)
	val.attach(button2, 0, 1, 0, 1,xoptions=Gtk.AttachOptions.FILL,yoptions=Gtk.AttachOptions.SHRINK)
	val.attach(button1, 1, 2, 0, 1,xoptions=Gtk.AttachOptions.FILL,yoptions=Gtk.AttachOptions.SHRINK)
	val.attach(button, 5, 6, 0, 1,xoptions=Gtk.AttachOptions.FILL,yoptions=Gtk.AttachOptions.SHRINK)
	val.attach(wind,0,6 , 1, 6)
	win.add(val)	
	win.show_all()

def load(entry):
	load2(entry.get_text())

def load2(url):
	if "http://" not in url:
		url="http://"+url
	webview.load_uri(url)

if __name__=='__main__':
	browser()
	webview.load_uri("http://www.google.com")
	Gtk.main()
	
	
	
