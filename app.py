from flask import Flask, render_template, request, Response
import uuid

app = Flask(__name__)


class VideoGame:
    def __init__(self, title, platform):
        self.title = title
        self.platform = platform

    def from_json(cls, videogame_entry):
        # Acquire json dictionary and output as string
        json_dict = json.loads(videogame_entry)
        return cls(**json_dict)


@app.route('/videogames')
def videogame_GET():
    return "Main page for video game directory."


@app.route('/videogames', methods=['POST'])
def videogame_POST():
    # try:
    if request.is_json:
        # Process the json data from the message body and store in data variable

        data = request.get_json()

        # Evaluate if key in data set
        if "title" in data.keys() and "platform" in data.keys():
            videogame = VideoGame(data["title"], data["platform"])
            print(videogame["title"])
            # Generate uuid for each new videogame entry
            videogame_uuid = uuid.uuid4()

            # Produce successful submission of entry
            print(videogame_uuid)
            return Response("{'title': 'videogame['title']','platform': 'videogame['platform']','uuid': 'uuid here','resource_path': '/endpoint/goes/here/uuid'}",
                            status=201, mimetype='application/json')
            # f"Successful submission of {videogame.title} and {videogame.platform} to the database."

        elif "title" in data.keys() and "platform" not in data.keys():
            print("Title wasn't included in data set submission")
            return Response("{'message': 'Title wasn't included in data set submission', 'endpoint': '/videogames'}",
                            status=400, mimetype='application/json')

        elif "title" not in data.keys() and "platform" in data.keys():
            print("Platform wasn't included in data set submission")
            return Response("{'message': 'Platform wasn't included in data set submission', 'endpoint': '/videogames'}",
                            status=400, mimetype='application/json')

        else:
            return 'Request not being understood. Check previous if and elif statements'

        # for key in data:
            '''if key in VideoGame.keys():
                # breakpoint("Stop 2")
                videogame = VideoGame(data["title"], data["platform"])
                print(videogame)
                # Produce an output to the server on the terminal side to know that the job was done.
                return f"Successful submission of {videogame.title} and {videogame.platform} to the database."
            else:
                print("Error handling stopped here")
                return f'Issues with handling {data}'''
    # except:
    #     print(f"Error. Database wasn't updated properly.")
    #     return f"Error. Database wasn't updated properly."

    # Successful POST: curl -X POST http://127.0.0.1:5000/videogames -H "Content-Type: application/json" -d '{"title":"Spiderman 2", "platform":"PlayStation"}'
    # Inaccurate JSON file: curl -X POST http://127.0.0.1:5000/videogames -H "Content-Type: application/json" -d '{"name":"Spiderman 2", "platform":"PlayStation 2"}'


@app.route('/videogames/<uuid>', methods=['GET', 'PATCH', 'DELETE'])
def unique_info(uuid):
    assert resource == request.view_args['uuid']
    return "Pull specific info on video games in database."


if __name__ == '__main__':
    app.run()
