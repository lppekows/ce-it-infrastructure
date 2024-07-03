from typing import Optional

from sqlalchemy import CHAR, Date, DateTime, Enum, Index, String, TIMESTAMP, Text, Time, text
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import datetime

class Base(DeclarativeBase):
    pass


class Author(Base):
    __tablename__ = 'Author'
    __table_args__ = (
        Index('Name', 'LastName'),
    )

    AuthorID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    FirstName: Mapped[str] = mapped_column(String(100))
    LastName: Mapped[str] = mapped_column(String(100))
    InstitutionID: Mapped[int] = mapped_column(INTEGER(11), server_default=text('0'))
    TimeStamp: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, server_default=text('current_timestamp() ON UPDATE current_timestamp()'))
    MiddleInitials: Mapped[Optional[str]] = mapped_column(String(16))
    Active: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text('1'))
    AuthorAbbr: Mapped[Optional[str]] = mapped_column(String(10), comment='Used in the Old DCC')
    FullAuthorName: Mapped[Optional[str]] = mapped_column(String(256), comment='Used in the Old DCC')


class AuthorGroupDefinition(Base):
    __tablename__ = 'AuthorGroupDefinition'

    AuthorGroupID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    AuthorGroupName: Mapped[str] = mapped_column(String(32))
    Description: Mapped[Optional[str]] = mapped_column(String(64))


class AuthorGroupList(Base):
    __tablename__ = 'AuthorGroupList'

    AuthorGroupListID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    AuthorGroupID: Mapped[int] = mapped_column(INTEGER(11))
    AuthorID: Mapped[int] = mapped_column(INTEGER(11))


class AuthorHint(Base):
    __tablename__ = 'AuthorHint'
    __table_args__ = (
        Index('SessionTalkID', 'SessionTalkID'),
    )

    AuthorHintID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    TimeStamp: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, server_default=text('current_timestamp() ON UPDATE current_timestamp()'))
    SessionTalkID: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    AuthorID: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class Conference(Base):
    __tablename__ = 'Conference'
    __table_args__ = (
        Index('EndDate', 'EndDate'),
        Index('StartDate', 'StartDate')
    )

    ConferenceID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    Location: Mapped[str] = mapped_column(String(64), server_default=text("''"))
    TimeStamp: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, server_default=text('current_timestamp() ON UPDATE current_timestamp()'))
    URL: Mapped[Optional[str]] = mapped_column(String(240))
    StartDate: Mapped[Optional[datetime.date]] = mapped_column(Date)
    EndDate: Mapped[Optional[datetime.date]] = mapped_column(Date)
    Title: Mapped[Optional[str]] = mapped_column(String(128))
    Preamble: Mapped[Optional[str]] = mapped_column(Text)
    Epilogue: Mapped[Optional[str]] = mapped_column(Text)
    ShowAllTalks: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    EventGroupID: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    LongDescription: Mapped[Optional[str]] = mapped_column(Text)
    AltLocation: Mapped[Optional[str]] = mapped_column(String(255))


class ConfigSetting(Base):
    __tablename__ = 'ConfigSetting'
    __table_args__ = (
        Index('ConfigGroup', 'ConfigGroup'),
        Index('ForeignID', 'ForeignID'),
        Index('Sub1Group', 'Sub1Group')
    )

    ConfigSettingID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    TimeStamp: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, server_default=text('current_timestamp() ON UPDATE current_timestamp()'))
    Project: Mapped[Optional[str]] = mapped_column(String(32))
    ConfigGroup: Mapped[Optional[str]] = mapped_column(String(64))
    Sub1Group: Mapped[Optional[str]] = mapped_column(String(64))
    Sub2Group: Mapped[Optional[str]] = mapped_column(String(64))
    Sub3Group: Mapped[Optional[str]] = mapped_column(String(64))
    Sub4Group: Mapped[Optional[str]] = mapped_column(String(64))
    ForeignID: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Value: Mapped[Optional[str]] = mapped_column(String(64))
    Sub1Value: Mapped[Optional[str]] = mapped_column(String(64))
    Sub2Value: Mapped[Optional[str]] = mapped_column(String(64))
    Sub3Value: Mapped[Optional[str]] = mapped_column(String(64))
    Sub4Value: Mapped[Optional[str]] = mapped_column(String(64))
    Sub5Value: Mapped[Optional[str]] = mapped_column(String(64))
    Description: Mapped[Optional[str]] = mapped_column(Text)
    Constrained: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class ConfigValue(Base):
    __tablename__ = 'ConfigValue'
    __table_args__ = (
        Index('ConfigSettingID', 'ConfigSettingID'),
    )

    ConfigValueID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    TimeStamp: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, server_default=text('current_timestamp() ON UPDATE current_timestamp()'))
    ConfigSettingID: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Value: Mapped[Optional[str]] = mapped_column(String(64))
    Description: Mapped[Optional[str]] = mapped_column(Text)


class DocXRef(Base):
    __tablename__ = 'DocXRef'
    __table_args__ = (
        Index('DocRevID', 'DocRevID'),
        Index('DocumentID', 'DocumentID')
    )

    DocXRefID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    TimeStamp: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, server_default=text('current_timestamp() ON UPDATE current_timestamp()'))
    DocRevID: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    DocumentID: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Version: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Project: Mapped[Optional[str]] = mapped_column(String(32))


class Document(Base):
    __tablename__ = 'Document'
    __table_args__ = (
        Index('Alias', 'Alias'),
        Index('Requester', 'RequesterID')
    )

    DocumentID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    RequesterID: Mapped[int] = mapped_column(INTEGER(11), server_default=text('0'))
    TimeStamp: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, server_default=text('current_timestamp() ON UPDATE current_timestamp()'))
    RequestDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    DocHash: Mapped[Optional[str]] = mapped_column(CHAR(32))
    Alias: Mapped[Optional[str]] = mapped_column(String(255))


class DocumentFile(Base):
    __tablename__ = 'DocumentFile'
    __table_args__ = (
        Index('DocRevID', 'DocRevID'),
    )

    DocFileID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    DocRevID: Mapped[int] = mapped_column(INTEGER(11), server_default=text('0'))
    FileName: Mapped[str] = mapped_column(String(255), server_default=text("''"))
    TimeStamp: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, server_default=text('current_timestamp() ON UPDATE current_timestamp()'))
    Date_: Mapped[Optional[datetime.datetime]] = mapped_column('Date', DateTime)
    RootFile: Mapped[Optional[int]] = mapped_column(TINYINT(4), server_default=text('1'))
    Description: Mapped[Optional[str]] = mapped_column(String(128))


class DocumentReview(Base):
    __tablename__ = 'DocumentReview'

    DocReviewID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    DocumentID: Mapped[int] = mapped_column(INTEGER(11))
    VersionNumber: Mapped[int] = mapped_column(INTEGER(11))
    ReviewState: Mapped[int] = mapped_column(TINYINT(4), server_default=text('0'), comment='0=NOT_SUBMITTED; 1=RECEIVED; 2=UNDER_REVIEW; 3=ACCEPTED; 4= WITHDRAWN')
    TimeStamp: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, server_default=text('current_timestamp() ON UPDATE current_timestamp()'))
    EmployeeNumber: Mapped[int] = mapped_column(INTEGER(11), comment='Actor')
    Obsolete: Mapped[Optional[int]] = mapped_column(TINYINT(4), server_default=text('0'))


class DocumentRevision(Base):
    __tablename__ = 'DocumentRevision'
    __table_args__ = (
        Index('DocumentID', 'DocumentID'),
        Index('DocumentTitle', 'DocumentTitle'),
        Index('VersionNumber', 'VersionNumber')
    )

    DocRevID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    DocumentID: Mapped[int] = mapped_column(INTEGER(11), server_default=text('0'))
    SubmitterID: Mapped[int] = mapped_column(INTEGER(11), server_default=text('0'))
    DocumentTitle: Mapped[str] = mapped_column(String(255), server_default=text("''"))
    VersionNumber: Mapped[int] = mapped_column(INTEGER(11), server_default=text('0'))
    TimeStamp: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, server_default=text('current_timestamp() ON UPDATE current_timestamp()'))
    PublicationInfo: Mapped[Optional[str]] = mapped_column(Text)
    Abstract: Mapped[Optional[str]] = mapped_column(Text)
    RevisionDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    Obsolete: Mapped[Optional[int]] = mapped_column(TINYINT(4), server_default=text('0'))
    Keywords: Mapped[Optional[str]] = mapped_column(String(400))
    Note: Mapped[Optional[str]] = mapped_column(Text)
    Demanaged: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    DocTypeID: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    QAcheck: Mapped[Optional[int]] = mapped_column(TINYINT(4), server_default=text('0'), comment='flag when QA verifies rev')
    Migrated: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text('0'), comment='0=not_migrated 1=created 2=updated')
    ParallelSignoff: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text('0'))


class DocumentType(Base):
    __tablename__ = 'DocumentType'

    DocTypeID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    TimeStamp: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, server_default=text('current_timestamp() ON UPDATE current_timestamp()'))
    ShortType: Mapped[Optional[str]] = mapped_column(String(32))
    LongType: Mapped[Optional[str]] = mapped_column(String(255))
    NextDocNumber: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class DocumentTypeSecurity(Base):
    __tablename__ = 'DocumentTypeSecurity'

    DocTypeSecID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    DocTypeID: Mapped[int] = mapped_column(INTEGER(11))
    GroupID: Mapped[int] = mapped_column(INTEGER(11))
    IncludeType: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text('1'), comment='0 = exclude, 1 = include')


class EmailUser(Base):
    __tablename__ = 'EmailUser'

    EmailUserID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    Username: Mapped[str] = mapped_column(CHAR(255))
    Password: Mapped[str] = mapped_column(CHAR(32), server_default=text("''"))
    Name: Mapped[str] = mapped_column(CHAR(255))
    EmailAddress: Mapped[str] = mapped_column(CHAR(255))
    PreferHTML: Mapped[int] = mapped_column(INTEGER(11), server_default=text('0'))
    TimeStamp: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, server_default=text('current_timestamp() ON UPDATE current_timestamp()'))
    CanSign: Mapped[int] = mapped_column(INTEGER(11), server_default=text('0'))
    Verified: Mapped[int] = mapped_column(INTEGER(11), server_default=text('0'))
    AuthorID: Mapped[int] = mapped_column(INTEGER(11), server_default=text('0'))
    EmployeeNumber: Mapped[int] = mapped_column(INTEGER(11), server_default=text('0'))


class EventGroup(Base):
    __tablename__ = 'EventGroup'

    EventGroupID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    ShortDescription: Mapped[str] = mapped_column(String(32), server_default=text("''"))
    TimeStamp: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, server_default=text('current_timestamp() ON UPDATE current_timestamp()'))
    LongDescription: Mapped[Optional[str]] = mapped_column(Text)


class EventTopic(Base):
    __tablename__ = 'EventTopic'
    __table_args__ = (
        Index('Event', 'EventID'),
        Index('SepKey', 'SessionSeparatorID'),
        Index('Session', 'SessionID'),
        Index('Topic', 'TopicID')
    )

    EventTopicID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    TopicID: Mapped[int] = mapped_column(INTEGER(11), server_default=text('0'))
    EventID: Mapped[int] = mapped_column(INTEGER(11), server_default=text('0'))
    SessionID: Mapped[int] = mapped_column(INTEGER(11), server_default=text('0'))
    SessionSeparatorID: Mapped[int] = mapped_column(INTEGER(11), server_default=text('0'))
    TimeStamp: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, server_default=text('current_timestamp() ON UPDATE current_timestamp()'))


class ExternalDocDB(Base):
    __tablename__ = 'ExternalDocDB'

    ExternalDocDBID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    TimeStamp: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, server_default=text('current_timestamp() ON UPDATE current_timestamp()'))
    Project: Mapped[Optional[str]] = mapped_column(String(32))
    Description: Mapped[Optional[str]] = mapped_column(String(255))
    PublicURL: Mapped[Optional[str]] = mapped_column(String(255))
    PrivateURL: Mapped[Optional[str]] = mapped_column(String(255))


class GroupHierarchy(Base):
    __tablename__ = 'GroupHierarchy'

    HierarchyID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    ChildID: Mapped[int] = mapped_column(INTEGER(11), server_default=text('0'))
    ParentID: Mapped[int] = mapped_column(INTEGER(11), server_default=text('0'))
    TimeStamp: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, server_default=text('current_timestamp() ON UPDATE current_timestamp()'))


class Institution(Base):
    __tablename__ = 'Institution'

    InstitutionID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    ShortName: Mapped[str] = mapped_column(String(40), server_default=text("''"))
    LongName: Mapped[str] = mapped_column(String(80), server_default=text("''"))
    TimeStamp: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, server_default=text('current_timestamp() ON UPDATE current_timestamp()'))


class Journal(Base):
    __tablename__ = 'Journal'

    JournalID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    Abbreviation: Mapped[str] = mapped_column(String(64), server_default=text("''"))
    Name: Mapped[str] = mapped_column(String(128), server_default=text("''"))
    Publisher: Mapped[str] = mapped_column(String(64), server_default=text("''"))
    TimeStamp: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, server_default=text('current_timestamp() ON UPDATE current_timestamp()'))
    URL: Mapped[Optional[str]] = mapped_column(String(240))
    Acronym: Mapped[Optional[str]] = mapped_column(String(8))


class Keyword(Base):
    __tablename__ = 'Keyword'

    KeywordID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    TimeStamp: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, server_default=text('current_timestamp() ON UPDATE current_timestamp()'))
    ShortDescription: Mapped[Optional[str]] = mapped_column(String(32))
    LongDescription: Mapped[Optional[str]] = mapped_column(Text)


class KeywordGroup(Base):
    __tablename__ = 'KeywordGroup'

    KeywordGroupID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    TimeStamp: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, server_default=text('current_timestamp() ON UPDATE current_timestamp()'))
    ShortDescription: Mapped[Optional[str]] = mapped_column(String(32))
    LongDescription: Mapped[Optional[str]] = mapped_column(Text)


class KeywordGrouping(Base):
    __tablename__ = 'KeywordGrouping'
    __table_args__ = (
        Index('KeywordGroupID', 'KeywordGroupID'),
        Index('KeywordID', 'KeywordID')
    )

    KeywordGroupingID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    TimeStamp: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, server_default=text('current_timestamp() ON UPDATE current_timestamp()'))
    KeywordGroupID: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    KeywordID: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class MeetingModify(Base):
    __tablename__ = 'MeetingModify'
    __table_args__ = (
        Index('ConferenceID', 'ConferenceID'),
    )

    MeetingModifyID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    TimeStamp: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, server_default=text('current_timestamp() ON UPDATE current_timestamp()'))
    ConferenceID: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    GroupID: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class MeetingOrder(Base):
    __tablename__ = 'MeetingOrder'
    __table_args__ = (
        Index('SessionID', 'SessionID'),
        Index('SessionSeparatorID', 'SessionSeparatorID')
    )

    MeetingOrderID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    TimeStamp: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, server_default=text('current_timestamp() ON UPDATE current_timestamp()'))
    SessionOrder: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    SessionID: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    SessionSeparatorID: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class MeetingSecurity(Base):
    __tablename__ = 'MeetingSecurity'
    __table_args__ = (
        Index('ConferenceID', 'ConferenceID'),
    )

    MeetingSecurityID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    TimeStamp: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, server_default=text('current_timestamp() ON UPDATE current_timestamp()'))
    ConferenceID: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    GroupID: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class Moderator(Base):
    __tablename__ = 'Moderator'
    __table_args__ = (
        Index('Author', 'AuthorID'),
        Index('Event', 'EventID'),
        Index('SepKey', 'SessionSeparatorID'),
        Index('Session', 'SessionID')
    )

    ModeratorID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    AuthorID: Mapped[int] = mapped_column(INTEGER(11), server_default=text('0'))
    EventID: Mapped[int] = mapped_column(INTEGER(11), server_default=text('0'))
    SessionID: Mapped[int] = mapped_column(INTEGER(11), server_default=text('0'))
    SessionSeparatorID: Mapped[int] = mapped_column(INTEGER(11), server_default=text('0'))
    TimeStamp: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, server_default=text('current_timestamp() ON UPDATE current_timestamp()'))


class Notification(Base):
    __tablename__ = 'Notification'
    __table_args__ = (
        Index('EmailUserID', 'EmailUserID'),
        Index('ForeignID', 'ForeignID')
    )

    NotificationID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    TimeStamp: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, server_default=text('current_timestamp() ON UPDATE current_timestamp()'))
    EmailUserID: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Type: Mapped[Optional[str]] = mapped_column(String(32))
    ForeignID: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Period: Mapped[Optional[str]] = mapped_column(String(32))
    TextKey: Mapped[Optional[str]] = mapped_column(String(255))


class RemoteUser(Base):
    __tablename__ = 'RemoteUser'
    __table_args__ = (
        Index('Name', 'RemoteUserName'),
    )

    RemoteUserID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    RemoteUserName: Mapped[str] = mapped_column(CHAR(255))
    EmailUserID: Mapped[int] = mapped_column(INTEGER(11), server_default=text('0'))
    EmailAddress: Mapped[str] = mapped_column(CHAR(255))


class RevisionAuthor(Base):
    __tablename__ = 'RevisionAuthor'
    __table_args__ = (
        Index('AuthorID', 'AuthorID'),
        Index('DocRevID', 'DocRevID')
    )

    RevAuthorID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    DocRevID: Mapped[int] = mapped_column(INTEGER(11), server_default=text('0'))
    AuthorID: Mapped[int] = mapped_column(INTEGER(11), server_default=text('0'))
    TimeStamp: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, server_default=text('current_timestamp() ON UPDATE current_timestamp()'))
    AuthorOrder: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text('0'))


class RevisionAuthorGroup(Base):
    __tablename__ = 'RevisionAuthorGroup'

    RevAuthorGroupID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    AuthorGroupID: Mapped[int] = mapped_column(INTEGER(11))
    DocRevID: Mapped[int] = mapped_column(INTEGER(11))


class RevisionEvent(Base):
    __tablename__ = 'RevisionEvent'
    __table_args__ = (
        Index('DocRevID', 'DocRevID'),
        Index('MinorTopicID', 'ConferenceID')
    )

    RevEventID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    DocRevID: Mapped[int] = mapped_column(INTEGER(11), server_default=text('0'))
    ConferenceID: Mapped[int] = mapped_column(INTEGER(11), server_default=text('0'))
    TimeStamp: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, server_default=text('current_timestamp() ON UPDATE current_timestamp()'))


class RevisionModify(Base):
    __tablename__ = 'RevisionModify'
    __table_args__ = (
        Index('DocRevID', 'DocRevID'),
        Index('GroupID', 'GroupID')
    )

    RevModifyID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    TimeStamp: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, server_default=text('current_timestamp() ON UPDATE current_timestamp()'))
    GroupID: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    DocRevID: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class RevisionReference(Base):
    __tablename__ = 'RevisionReference'
    __table_args__ = (
        Index('DocRevID', 'DocRevID'),
        Index('JournalID', 'JournalID')
    )

    ReferenceID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    TimeStamp: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, server_default=text('current_timestamp() ON UPDATE current_timestamp()'))
    DocRevID: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    JournalID: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Volume: Mapped[Optional[str]] = mapped_column(CHAR(32))
    Page: Mapped[Optional[str]] = mapped_column(CHAR(32))


class RevisionSecurity(Base):
    __tablename__ = 'RevisionSecurity'
    __table_args__ = (
        Index('Grp', 'GroupID'),
        Index('Revision', 'DocRevID')
    )

    RevSecurityID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    GroupID: Mapped[int] = mapped_column(INTEGER(11), server_default=text('0'))
    DocRevID: Mapped[int] = mapped_column(INTEGER(11), server_default=text('0'))
    TimeStamp: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, server_default=text('current_timestamp() ON UPDATE current_timestamp()'))


class RevisionTopic(Base):
    __tablename__ = 'RevisionTopic'
    __table_args__ = (
        Index('DocRevID', 'DocRevID'),
        Index('TopicID', 'TopicID')
    )

    RevTopicID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    DocRevID: Mapped[int] = mapped_column(INTEGER(11), server_default=text('0'))
    TimeStamp: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, server_default=text('current_timestamp() ON UPDATE current_timestamp()'))
    TopicID: Mapped[int] = mapped_column(INTEGER(11), server_default=text('0'))


class SecurityGroup(Base):
    __tablename__ = 'SecurityGroup'

    GroupID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    Name: Mapped[str] = mapped_column(CHAR(32))
    TimeStamp: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, server_default=text('current_timestamp() ON UPDATE current_timestamp()'))
    DisplayInList: Mapped[str] = mapped_column(Enum('0', '1', '2', '3'), server_default=text("'1'"), comment="0=don't_display 1=display everywhere 2=force_display_in_specific_list 3=display only in group membership")
    Description: Mapped[Optional[str]] = mapped_column(CHAR(64))
    CanCreate: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text('0'))
    CanAdminister: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text('0'))
    CanView: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text('1'))
    CanConfig: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text('0'))


class Session(Base):
    __tablename__ = 'Session'
    __table_args__ = (
        Index('ConferenceID', 'ConferenceID'),
    )

    SessionID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    TimeStamp: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, server_default=text('current_timestamp() ON UPDATE current_timestamp()'))
    ConferenceID: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    StartTime: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    Title: Mapped[Optional[str]] = mapped_column(String(128))
    Description: Mapped[Optional[str]] = mapped_column(Text)
    Location: Mapped[Optional[str]] = mapped_column(String(128))
    AltLocation: Mapped[Optional[str]] = mapped_column(String(255))
    ShowAllTalks: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text('0'))


class SessionOrder(Base):
    __tablename__ = 'SessionOrder'
    __table_args__ = (
        Index('SessionTalkID', 'SessionTalkID'),
        Index('TalkSeparatorID', 'TalkSeparatorID')
    )

    SessionOrderID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    TimeStamp: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, server_default=text('current_timestamp() ON UPDATE current_timestamp()'))
    TalkOrder: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    SessionTalkID: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    TalkSeparatorID: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class SessionSeparator(Base):
    __tablename__ = 'SessionSeparator'
    __table_args__ = (
        Index('ConferenceID', 'ConferenceID'),
    )

    SessionSeparatorID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    TimeStamp: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, server_default=text('current_timestamp() ON UPDATE current_timestamp()'))
    ConferenceID: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    StartTime: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    Title: Mapped[Optional[str]] = mapped_column(String(128))
    Description: Mapped[Optional[str]] = mapped_column(Text)
    Location: Mapped[Optional[str]] = mapped_column(String(128))


class SessionTalk(Base):
    __tablename__ = 'SessionTalk'
    __table_args__ = (
        Index('DocumentID', 'DocumentID'),
        Index('SessionID', 'SessionID')
    )

    SessionTalkID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    TimeStamp: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, server_default=text('current_timestamp() ON UPDATE current_timestamp()'))
    SessionID: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    DocumentID: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Confirmed: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Time_: Mapped[Optional[datetime.time]] = mapped_column('Time', Time)
    HintTitle: Mapped[Optional[str]] = mapped_column(String(128))
    Note: Mapped[Optional[str]] = mapped_column(Text)


class Signature(Base):
    __tablename__ = 'Signature'
    __table_args__ = (
        Index('EmailUserID', 'EmailUserID'),
        Index('SignoffID', 'SignoffID')
    )

    SignatureID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    TimeStamp: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, server_default=text('current_timestamp() ON UPDATE current_timestamp()'))
    EmailUserID: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    SignoffID: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Note: Mapped[Optional[str]] = mapped_column(Text)
    Signed: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class Signoff(Base):
    __tablename__ = 'Signoff'
    __table_args__ = (
        Index('DocRevID', 'DocRevID'),
    )

    SignoffID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    TimeStamp: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, server_default=text('current_timestamp() ON UPDATE current_timestamp()'))
    DocRevID: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Note: Mapped[Optional[str]] = mapped_column(Text)


class SignoffDependency(Base):
    __tablename__ = 'SignoffDependency'
    __table_args__ = (
        Index('PreSignoffID', 'PreSignoffID'),
        Index('SignoffID', 'SignoffID')
    )

    SignoffDependencyID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    TimeStamp: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, server_default=text('current_timestamp() ON UPDATE current_timestamp()'))
    SignoffID: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    PreSignoffID: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class Suppress(Base):
    __tablename__ = 'Suppress'
    __table_args__ = (
        Index('ForeignID', 'ForeignID'),
        Index('SecurityGroup', 'SecurityGroupID'),
        Index('TextKey', 'TextKey'),
        Index('Type', 'Type')
    )

    SuppressID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    SecurityGroupID: Mapped[int] = mapped_column(INTEGER(11), server_default=text('0'))
    Type: Mapped[Optional[str]] = mapped_column(String(32))
    ForeignID: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    TextKey: Mapped[Optional[str]] = mapped_column(String(255))
    ViewSetting: Mapped[Optional[str]] = mapped_column(String(32))
    ModifySetting: Mapped[Optional[str]] = mapped_column(String(32))


class TalkSeparator(Base):
    __tablename__ = 'TalkSeparator'
    __table_args__ = (
        Index('SessionID', 'SessionID'),
    )

    TalkSeparatorID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    TimeStamp: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, server_default=text('current_timestamp() ON UPDATE current_timestamp()'))
    SessionID: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    Time_: Mapped[Optional[datetime.time]] = mapped_column('Time', Time)
    Title: Mapped[Optional[str]] = mapped_column(String(128))
    Note: Mapped[Optional[str]] = mapped_column(Text)


class Topic(Base):
    __tablename__ = 'Topic'

    TopicID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    TimeStamp: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, server_default=text('current_timestamp() ON UPDATE current_timestamp()'))
    ShortDescription: Mapped[Optional[str]] = mapped_column(String(64), server_default=text("''"))
    LongDescription: Mapped[Optional[str]] = mapped_column(Text)


class TopicHierarchy(Base):
    __tablename__ = 'TopicHierarchy'
    __table_args__ = (
        Index('Parent', 'ParentTopicID'),
        Index('Topic', 'TopicID')
    )

    TopicHierarchyID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    TopicID: Mapped[int] = mapped_column(INTEGER(11), server_default=text('0'))
    ParentTopicID: Mapped[int] = mapped_column(INTEGER(11), server_default=text('0'))
    TimeStamp: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, server_default=text('current_timestamp() ON UPDATE current_timestamp()'))


class TopicHint(Base):
    __tablename__ = 'TopicHint'
    __table_args__ = (
        Index('SessionTalkID', 'SessionTalkID'),
    )

    TopicHintID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    TimeStamp: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, server_default=text('current_timestamp() ON UPDATE current_timestamp()'))
    TopicID: Mapped[int] = mapped_column(INTEGER(11), server_default=text('0'))
    SessionTalkID: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class UsersGroup(Base):
    __tablename__ = 'UsersGroup'
    __table_args__ = (
        Index('EmailUserID', 'EmailUserID'),
    )

    UsersGroupID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    TimeStamp: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, server_default=text('current_timestamp() ON UPDATE current_timestamp()'))
    EmailUserID: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    GroupID: Mapped[Optional[int]] = mapped_column(INTEGER(11))
