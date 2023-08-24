from windows_toasts import Toast, WindowsToaster

toaster = WindowsToaster('Yash Notification')


newToast = Toast()
newToast.text_fields = ["Hey This is a system generated notification"]
toaster.show_toast(newToast)