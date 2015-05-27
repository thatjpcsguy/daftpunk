## Daft Punk
### Simple library for controlling lots of phillips hue


####Step 1 - Setup####

- First find your bridges IP address (i'll let you figure this part)
- Add your bridges to your config file


      "bridges": {
          "bedroom": {"ip": "10.0.1.50", "user": "newdeveloper"},
          "kitchen": {"ip": "10.0.1.51", "user": "newdeveloper"}
      }     

- Create new users on the bridges to be used by the api
	1. go to `http://<bridge_ip>/debug/clip.html` in your favourite web browser (chrome).
	2. press the `link` button on your bridge (the big lit up blue one)
	3. send a POST request to /api with `{"devicetype":"test user","username":"newdeveloper"}` in the body - this will create a new user on the bridge, you dont need to think to hard about this, you wont need it again
	
- Before closing the CLIP debugger, send a get request to `/api/newdeveloper/lights`. This will help you by showing all the lights currently on the bridge. consult the official hue documentation here `http://www.developers.meethue.com/documentation/getting-started` to find out more about connecting new lights etc.
- Add your lights from the previous step to the config file. It should look something like:
        
        "lights": {
            "roof1": {"bridge": "bedroom", "id": 1},
            "roof2": {"bridge": "bedroom", "id": 3},
            "lamp1": {"bridge": "bedroom", "id": 2}
        }
        

- `TODO:` Now go ahead and add any groups you would like to define. You will also be able to define groups programmatically later on.



####Step 2 - Python###

- First install the dependencies

      pip install beautifulhue
      pip install colour

- Now run `python api.py --config config/default.conf`
- Try it out

      ➜  ~  curl http://127.0.0.1:5000/colour?light=roof1&colour=blue

Yay!

#### TODO - Write more docs ####