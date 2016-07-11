from google.appengine.ext import ndb

class Post(ndb.Model):
    post_title = ndb.StringProperty(required = True)
    post_content = ndb.TextProperty(required = True)
    post_author = ndb.StringProperty(required = True)
    post_created = ndb.DateTimeProperty(auto_now_add = True)
    post_last_updated = ndb.DateTimeProperty(auto_now = True)

    @classmethod
    def addPost(cls, title, content, author):
        p = Post(post_title = title, post_content = content,
                 post_author = author)
        p.put()
        return p.key.id()

    @classmethod
    def getPost(cls, post_id):
        return Post.get_by_id(int(post_id))

    @classmethod
    def deletePost(cls, post_id):
        post = Post.get_by_id(int(post_id))
        if post:
            post.key.delete()
            return True
        else:
            return False

#ndb.delete_multi(Post.query().fetch(keys_only=True))



class User(ndb.Model):
    user_name = ndb.StringProperty(required = True)
    user_password_hash = ndb.TextProperty(required = True)

    @classmethod
    def addUser(cls, name, password_hash):
        u = User(user_name = name, user_password_hash = password_hash)
        u.put()
        return u.key.id()

    @classmethod
    def getUserByName(cls, name):
        user = User.query(User.user_name==name).fetch(1)
        for u in user:
            return u
            
    @classmethod
    def getUserById(cls, user_id):
        return User.get_by_id(int(user_id))

    @classmethod
    def getUserByNameAndPassword(cls, name, password_hash):
        user = User.query(User.user_name==name).fetch(1)
        for u in user:
            if u.user_password_hash == password_hash:
                return u
            else:
                return False

    @classmethod
    def getUserId(cls, user):
        return user.key.id()


class LikePost(ndb.Model):
    post_id = ndb.StringProperty(required = True)
