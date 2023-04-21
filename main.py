from winotify import Notification

toast = Notification(app_id="NeuralNine Script",
                     title="Important Info",
                     msg="Learn Python & Machine Learning",
                     duration="long")

toast.add_actions(label="Click Me!", launch="https://academyclub.co")

toast.show()
