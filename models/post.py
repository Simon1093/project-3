from datetime import datetime


class Post():
    def __init__(self, attrs):
        for key in self.get_model_keys():
            setattr(self, key, attrs.get(key))
        setattr(self, '_id', attrs.get('_id'))
        if attrs.get('_id') is not None:
            self._id = str(attrs['_id'])

    def get_model_keys(self):
        model_keys = ['title', 'text', 'datetime']
        return model_keys

    def to_doc(self):
        doc = {}
        for key in self.get_model_keys():
            doc[key] = getattr(self, key)
        return doc

    def to_json(self):
        json = {}
        for key in self.get_model_keys():
            json[key] = getattr(self, key)
        if isinstance(json['datetime'], datetime):
            json['datetime'] = json['datetime'].strftime('%Y-%m-%d %H:%M:%S')
        if self._id is not None:
            json['id'] = self._id
        return json
