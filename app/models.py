from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from app import app, db
from sqlalchemy.exc import IntegrityError


class Participant(db.Model):
    __tablename__ = 'participant'
    __table_args__ = {'extend_existing': True}
    par_id = db.Column(db.Integer, primary_key=True)
    sex = db.Column(db.String(6), nullable=False)
    num_visits = db.Column(db.Integer, nullable=False)

    def __init__(self, id, sex, num):
        self.par_id = id
        self.sex = sex
        self.num_visits = num

    def __repr__(self):
        return f"Participant: ('{self.par_id}', '{self.sex}, '{self.num_visits}')"


class Visit0(db.Model):
    __tablename__ = 'visit0'
    __table_args__ = {'extend_existing': True}

    visit_id = db.Column('visit_id', db.Integer, primary_key=True)
    par_id = db.Column('par_id', db.Integer, db.ForeignKey('participant.par_id'))
    age = db.Column('age', db.Integer)
    sex = db.Column('sex', db.String(6), nullable=False)
    group = db.Column('group', db.String(30), nullable=False)
    education = db.Column('education', db.Integer)
    visit = db.Column('visit', db.Integer, nullable=False)
    mmse = db.Column('mmse', db.Integer)
    mmse1 = db.Column('mmse1', db.Integer)
    mmse2 = db.Column('mmse2', db.Integer)
    mmse3 = db.Column('mmse3', db.Integer)
    mmse4 = db.Column('mmse4', db.Integer)
    category = db.Column('category', db.Integer)
    word_count = db.Column('word_count', db.Integer, nullable=False)
    pronoun_count = db.Column('pronoun_count', db.Integer, nullable=False)
    noun_count = db.Column('noun_count', db.Integer, nullable=False)
    verb_count = db.Column('verb_count', db.Integer, nullable=False)
    adj_count = db.Column('adj_count', db.Integer, nullable=False)
    adv_count = db.Column('adv_count', db.Integer, nullable=False)
    pauses = db.Column('pauses', db.Integer, nullable=False)
    retracings = db.Column('retracings', db.Integer, nullable=False)
    low_img_verbs = db.Column('low_img_verbs', db.Integer, nullable=False)
    indefinites = db.Column('indefinites', db.Integer, nullable=False)
    trailoffs = db.Column('trailoffs', db.Integer, nullable=False)
    framgents = db.Column('fragments', db.Integer, nullable=False)
    unintelligibles = db.Column('unintelligibles', db.Integer, nullable=False)
    shortenings = db.Column('shortenings', db.Integer, nullable=False)
    runtime = db.Column('runtime', db.Float, nullable=False)

    def __init__(self, par_id, sex, mmse):
        self.par_id = par_id
        self.sex = sex
        self.mmse = mmse

    def __repr__(self):
        return f"Visit0: ('{self.id}', {self.par_id}', '{self.sex}, '{self.mmse}')"

class Visit1(db.Model):
    __tablename__ = 'visit1'
    __table_args__ = {'extend_existing': True}

    visit_id = db.Column('visit_id', db.Integer, primary_key=True)
    par_id = db.Column('par_id', db.Integer, db.ForeignKey('participant.par_id'))
    age = db.Column('age', db.Integer)
    sex = db.Column('sex', db.String(6), nullable=False)
    group = db.Column('group', db.String(30), nullable=False)
    education = db.Column('education', db.Integer)
    visit = db.Column('visit', db.Integer, nullable=False)
    mmse = db.Column('mmse', db.Integer)
    mmse1 = db.Column('mmse1', db.Integer)
    mmse2 = db.Column('mmse2', db.Integer)
    mmse3 = db.Column('mmse3', db.Integer)
    mmse4 = db.Column('mmse4', db.Integer)
    category = db.Column('category', db.Integer)
    word_count = db.Column('word_count', db.Integer, nullable=False)
    pronoun_count = db.Column('pronoun_count', db.Integer, nullable=False)
    noun_count = db.Column('noun_count', db.Integer, nullable=False)
    verb_count = db.Column('verb_count', db.Integer, nullable=False)
    adj_count = db.Column('adj_count', db.Integer, nullable=False)
    adv_count = db.Column('adv_count', db.Integer, nullable=False)
    pauses = db.Column('pauses', db.Integer, nullable=False)
    retracings = db.Column('retracings', db.Integer, nullable=False)
    low_img_verbs = db.Column('low_img_verbs', db.Integer, nullable=False)
    indefinites = db.Column('indefinites', db.Integer, nullable=False)
    trailoffs = db.Column('trailoffs', db.Integer, nullable=False)
    framgents = db.Column('fragments', db.Integer, nullable=False)
    unintelligibles = db.Column('unintelligibles', db.Integer, nullable=False)
    shortenings = db.Column('shortenings', db.Integer, nullable=False)
    runtime = db.Column('runtime', db.Float, nullable=False)

    def __init__(self, par_id, sex, mmse):
        self.par_id = par_id
        self.sex = sex
        self.mmse = mmse

    def __repr__(self):
        return f"Visit1: ('{self.id}', {self.par_id}', '{self.sex}, '{self.mmse}')"

class Visit2(db.Model):
    __tablename__ = 'visit2'
    __table_args__ = {'extend_existing': True}

    visit_id = db.Column('visit_id', db.Integer, primary_key=True)
    par_id = db.Column('par_id', db.Integer, db.ForeignKey('participant.par_id'))
    age = db.Column('age', db.Integer)
    sex = db.Column('sex', db.String(6), nullable=False)
    group = db.Column('group', db.String(30), nullable=False)
    education = db.Column('education', db.Integer)
    visit = db.Column('visit', db.Integer, nullable=False)
    mmse = db.Column('mmse', db.Integer)
    mmse1 = db.Column('mmse1', db.Integer)
    mmse2 = db.Column('mmse2', db.Integer)
    mmse3 = db.Column('mmse3', db.Integer)
    mmse4 = db.Column('mmse4', db.Integer)
    category = db.Column('category', db.Integer)
    word_count = db.Column('word_count', db.Integer, nullable=False)
    pronoun_count = db.Column('pronoun_count', db.Integer, nullable=False)
    noun_count = db.Column('noun_count', db.Integer, nullable=False)
    verb_count = db.Column('verb_count', db.Integer, nullable=False)
    adj_count = db.Column('adj_count', db.Integer, nullable=False)
    adv_count = db.Column('adv_count', db.Integer, nullable=False)
    pauses = db.Column('pauses', db.Integer, nullable=False)
    retracings = db.Column('retracings', db.Integer, nullable=False)
    low_img_verbs = db.Column('low_img_verbs', db.Integer, nullable=False)
    indefinites = db.Column('indefinites', db.Integer, nullable=False)
    trailoffs = db.Column('trailoffs', db.Integer, nullable=False)
    framgents = db.Column('fragments', db.Integer, nullable=False)
    unintelligibles = db.Column('unintelligibles', db.Integer, nullable=False)
    shortenings = db.Column('shortenings', db.Integer, nullable=False)
    runtime = db.Column('runtime', db.Float, nullable=False)

    def __init__(self, par_id, sex, mmse):
        self.par_id = par_id
        self.sex = sex
        self.mmse = mmse

    def __repr__(self):
        return f"Visit2: ('{self.id}', {self.par_id}', '{self.sex}, '{self.mmse}')"

class Visit3(db.Model):
    __tablename__ = 'visit3'
    __table_args__ = {'extend_existing': True}

    visit_id = db.Column('visit_id', db.Integer, primary_key=True)
    par_id = db.Column('par_id', db.Integer, db.ForeignKey('participant.par_id'))
    age = db.Column('age', db.Integer)
    sex = db.Column('sex', db.String(6), nullable=False)
    group = db.Column('group', db.String(30), nullable=False)
    education = db.Column('education', db.Integer)
    visit = db.Column('visit', db.Integer, nullable=False)
    mmse = db.Column('mmse', db.Integer)
    mmse1 = db.Column('mmse1', db.Integer)
    mmse2 = db.Column('mmse2', db.Integer)
    mmse3 = db.Column('mmse3', db.Integer)
    mmse4 = db.Column('mmse4', db.Integer)
    category = db.Column('category', db.Integer)
    word_count = db.Column('word_count', db.Integer, nullable=False)
    pronoun_count = db.Column('pronoun_count', db.Integer, nullable=False)
    noun_count = db.Column('noun_count', db.Integer, nullable=False)
    verb_count = db.Column('verb_count', db.Integer, nullable=False)
    adj_count = db.Column('adj_count', db.Integer, nullable=False)
    adv_count = db.Column('adv_count', db.Integer, nullable=False)
    pauses = db.Column('pauses', db.Integer, nullable=False)
    retracings = db.Column('retracings', db.Integer, nullable=False)
    low_img_verbs = db.Column('low_img_verbs', db.Integer, nullable=False)
    indefinites = db.Column('indefinites', db.Integer, nullable=False)
    trailoffs = db.Column('trailoffs', db.Integer, nullable=False)
    framgents = db.Column('fragments', db.Integer, nullable=False)
    unintelligibles = db.Column('unintelligibles', db.Integer, nullable=False)
    shortenings = db.Column('shortenings', db.Integer, nullable=False)
    runtime = db.Column('runtime', db.Float, nullable=False)

    def __init__(self, par_id, sex, mmse):
        self.par_id = par_id
        self.sex = sex
        self.mmse = mmse

    def __repr__(self):
        return f"Visit3: ('{self.id}', {self.par_id}', '{self.sex}, '{self.mmse}')"

class Visit4(db.Model):
    __tablename__ = 'visit4'
    __table_args__ = {'extend_existing': True}

    visit_id = db.Column('visit_id', db.Integer, primary_key=True)
    par_id = db.Column('par_id', db.Integer, db.ForeignKey('participant.par_id'))
    age = db.Column('age', db.Integer)
    sex = db.Column('sex', db.String(6), nullable=False)
    group = db.Column('group', db.String(30), nullable=False)
    education = db.Column('education', db.Integer)
    visit = db.Column('visit', db.Integer, nullable=False)
    mmse = db.Column('mmse', db.Integer)
    mmse1 = db.Column('mmse1', db.Integer)
    mmse2 = db.Column('mmse2', db.Integer)
    mmse3 = db.Column('mmse3', db.Integer)
    mmse4 = db.Column('mmse4', db.Integer)
    category = db.Column('category', db.Integer)
    word_count = db.Column('word_count', db.Integer, nullable=False)
    pronoun_count = db.Column('pronoun_count', db.Integer, nullable=False)
    noun_count = db.Column('noun_count', db.Integer, nullable=False)
    verb_count = db.Column('verb_count', db.Integer, nullable=False)
    adj_count = db.Column('adj_count', db.Integer, nullable=False)
    adv_count = db.Column('adv_count', db.Integer, nullable=False)
    pauses = db.Column('pauses', db.Integer, nullable=False)
    retracings = db.Column('retracings', db.Integer, nullable=False)
    low_img_verbs = db.Column('low_img_verbs', db.Integer, nullable=False)
    indefinites = db.Column('indefinites', db.Integer, nullable=False)
    trailoffs = db.Column('trailoffs', db.Integer, nullable=False)
    framgents = db.Column('fragments', db.Integer, nullable=False)
    unintelligibles = db.Column('unintelligibles', db.Integer, nullable=False)
    shortenings = db.Column('shortenings', db.Integer, nullable=False)
    runtime = db.Column('runtime', db.Float, nullable=False)

    def __init__(self, par_id, sex, mmse):
        self.par_id = par_id
        self.sex = sex
        self.mmse = mmse

    def __repr__(self):
        return f"Visit4 ('{self.id}', {self.par_id}', '{self.sex}, '{self.mmse}')"