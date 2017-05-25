from ravenpackapi.core import RPApi
from ravenpackapi.tests.known_facts import APPLE_RP_ENTITY_ID


def test_analytics_news_type():
    api = RPApi()
    entities = ['D8442A', '619882', '14BA06']
    news_types = ['RNS-SEC10K', 'RNS-SEC10Q']
    analytics = api.get_analytics_inline(
        start_date='2016-01-01',
        end_date='2017-05-01',
        entities=entities,
        filters=dict(
            NEWS_TYPE={'$in': news_types}
        ),
        return_type='preview',
    )
    for a in analytics:
        assert a['RP_ENTITY_ID'] in entities, 'Analytics should be of the requested entities only'
        assert a['NEWS_TYPE'] in news_types, 'Analytics should be of the requested news_types only'
    assert len(analytics) == 11, 'We expect 11 analytics row passing'


def test_analytics_file_download():
    # TODO: This is generating a mail notification, would be nice to be able to disable it
    entities = [APPLE_RP_ENTITY_ID]
    api = RPApi()
    analytics = api.get_analytics_inline(
        start_date='2017-05-01',
        end_date='2017-05-02',
        entities=entities,
    )
    assert len(list(analytics))  # analytics is an iterable
