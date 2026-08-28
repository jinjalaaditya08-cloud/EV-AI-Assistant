"""
Basic unit tests for AIProvider implementations (Phase 2)
Run with pytest.
"""

from ai_provider.local_provider import LocalProvider

def test_local_provider_generate():
    lp = LocalProvider()
    res = lp.generate('Hello world')
    assert isinstance(res, dict)
    assert 'text' in res
    assert res['text'].startswith('[LocalProvider]')
    assert res.get('meta', {}).get('provider') == 'local'

def test_local_provider_intent():
    lp = LocalProvider()
    intent = lp.classify_intent('Please research quantum computing')
    assert intent == 'research'
