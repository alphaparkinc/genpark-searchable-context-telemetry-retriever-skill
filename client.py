class SearchableContextTelemetryRetrieverClient:
    def query_prior_window_telemetry(self, search_query='FAILED_ASSERTION_USER_MODEL', window_lookback_steps=5):
        return {
            'retrieval_id': 'sch_tel_7721',
            'search_query': search_query,
            'matched_prior_window_index': 3,
            'raw_tool_output_snippet': 'AssertionError: user.is_active expected True but got False at test_auth.py:44',
            'exact_token_offset': 18420,
            'fidelity_score': 1.0,
            'telemetry_archive_url': 'https://astra.telemetry.genpark.ai/searches/7721.json'
        }
