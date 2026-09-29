"""Regression checks for misleading displayed cost examples."""
from pathlib import Path
import unittest
from cost_check import check_cost_tables

ROOT = Path(__file__).resolve().parents[1]


class PublishedCostChecks(unittest.TestCase):
    def setUp(self):
        self.example = (ROOT / 'docs/cost-and-evaluation.md').read_text(encoding='utf-8')
        self.models = (ROOT / 'docs/models-and-effort.md').read_text(encoding='utf-8')

    def test_current_documents_reconcile(self):
        self.assertEqual(check_cost_tables(self.example, self.models), [])

    def test_rejects_wrong_displayed_total(self):
        changed = self.example.replace('| $0.002 |', '| $999.000 |')
        self.assertNotEqual(changed, self.example)
        self.assertTrue(any('displayed total' in e for e in check_cost_tables(changed, self.models)))

    def test_rejects_rate_drift_between_documents(self):
        changed = self.models.replace('$0.10 / $0.01 / $0.50', '$0.20 / $0.01 / $0.50')
        self.assertNotEqual(changed, self.models)
        self.assertTrue(any('rates differ' in e for e in check_cost_tables(self.example, changed)))

    def test_rejects_table_tokens_that_disagree_with_prose(self):
        changed = self.example.replace('| Luna | 10,000 /', '| Luna | 20,000 /')
        self.assertNotEqual(changed, self.example)
        self.assertTrue(any('token counts differ' in e for e in check_cost_tables(changed, self.models)))

    def test_rejects_duplicate_model_rate_row(self):
        luna = next(line for line in self.models.splitlines() if line.startswith('| [`gpt-6-luna`]'))
        changed = self.models.replace(luna, luna.replace('$0.10 /', '$999.00 /') + '\n' + luna)
        self.assertTrue(any('unique model-rate rows' in e for e in check_cost_tables(self.example, changed)))


if __name__ == '__main__':
    unittest.main()
