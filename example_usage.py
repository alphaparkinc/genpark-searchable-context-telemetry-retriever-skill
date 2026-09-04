from client import SearchableContextTelemetryRetrieverClient

def main():
    client = SearchableContextTelemetryRetrieverClient()
    res = client.query_prior_window_telemetry('PYTEST_FAILURE')
    print('Searchable Telemetry Retriever: ' + res['retrieval_id'])
    print('Matched Window: ' + str(res['matched_prior_window_index']) + ' | Fidelity: ' + str(res['fidelity_score']))
    print('Snippet: ' + res['raw_tool_output_snippet'][:60] + '...')
    print('Archive URL: ' + res['telemetry_archive_url'])

if __name__ == '__main__':
    main()
