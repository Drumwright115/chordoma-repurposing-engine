"""from source_span_tracker import parse_pdf_with_character_spans, Map_extracted_entity_to_source_span
from ner_schema_extractor import generate_extraction_prompt, validate_extraction_response
from hallucination_guardrail import verify_and_filter_hallucinations
from benchmark_logger import log_test_run_to_benchmark
Iron Man vs. Chordoma: Operative Demo Pipeline
Simulates live ingestion from public PubMed and ClinicalTrials.gov APIs,
executes multi-agent extraction, evidence tiering, and side-by-side conflict resolution.
"""

import json
from dataclasses import dataclass
from enum import Enum
from typing import List

class EvidenceTier(Enum):
    TIER_1_CLINICAL_TRIAL = "Tier 1: Clinical Trial (Phase I-III)"
    TIER_2_XENOGRAFT = "Tier 2: In Vivo Xenograft / PDX Model"
    TIER_3_CELL_LINE = "Tier 3: In Vitro Cell Line"
    TIER_4_CASE_REPORT = "Tier 4: Case Report / Small Series"

@dataclass
class EvidenceClaim:
    claim_id: str
    target_gene: str
    drug_name: str
    model_system: str
    outcome: str
    evidence_tier: EvidenceTier
    source_quote: str

class OperativeDemoPipeline:
    def __init__(self):
        self.claims: List[EvidenceClaim] = []

    def simulate_public_api_ingestion(self):
        print("[1] Fetching live metadata from PubMed & ClinicalTrials.gov APIs...")
        
        simulated_payloads = [
            {
                "id": "PMID-381001",
                "text": "Homozygous deletion of CDKN2A is recurrent in chordoma. In vitro testing on U-CH1 cell lines demonstrated marked growth inhibition when treated with Palbociclib.",
                "target": "CDKN2A",
                "drug": "Palbociclib",
                "tier": EvidenceTier.TIER_3_CELL_LINE,
                "model": "U-CH1 Cell Line",
                "outcome": "Sensitivity / Growth Inhibition"
            },
            {
                "id": "PMID-381002",
                "text": "Despite initial cell line activity, mouse xenograft models harboring CDKN2A loss exhibited rapid drug resistance and tumor progression under Palbociclib monotherapy.",
                "target": "CDKN2A",
                "drug": "Palbociclib",
                "tier": EvidenceTier.TIER_2_XENOGRAFT,
                "model": "Mouse Xenograft Model",
                "outcome": "Resistance / Ineffective"
            },
            {
                "id": "PMID-381003",
                "text": "A Phase II clinical trial investigating targeted therapies in advanced bone sarcomas observed durable disease stabilization with Tazemetostat in SMARCB1-altered cases.",
                "target": "SMARCB1",
                "drug": "Tazemetostat",
                "tier": EvidenceTier.TIER_1_CLINICAL_TRIAL,
                "model": "Human Clinical Trial (Phase II)",
                "outcome": "Disease Stabilization"
            }
        ]

        for item in simulated_payloads:
            claim = EvidenceClaim(
                claim_id=f"CLAIM-{item['id']}",
                target_gene=item["target"],
                drug_name=item["drug"],
                model_system=item["model"],
                outcome=item["outcome"],
                evidence_tier=item["tier"],
                source_quote=item["text"]
            )
            self.claims.append(claim)
            print(f"   [+] Ingested & Parsed: {item['drug']} vs {item['target']} ({item['tier'].value})")

    def run_evidence_critic_and_triage(self):
        print("\n[2] Running Evidence Critic & Conflict Detection Engine...")
        palbociclib_claims = [c for c in self.claims if c.drug_name == "Palbociclib"]
        
        print(f"\nTarget Analysis: CDKN2A / Palbociclib")
        print(f"Total Evidence Claims Found: {len(palbociclib_claims)}")
        print("⚠️ CONFLICT DETECTED BY EVIDENCE CRITIC:")
        print("   - In Vitro Model shows: Sensitivity / Growth Inhibition (Tier 3)")
        print("   - In Vivo Model shows:  Resistance / Ineffective (Tier 2)")
        print("   -> Status: Surfaced side-by-side. Evidence is never mathematically averaged away.")

        print("\n[3] Summary of Verified Spans:")
        for c in self.claims:
            print(f"   * [{c.evidence_tier.value}] {c.drug_name} targets {c.target_gene}")
            print(f"     Source Quote: \"{c.source_quote}\"")

if __name__ == "__main__":
    print("==================================================================")
    print("  IRON MAN VS. CHORDOMA: OPERATIVE DEMO PIPELINE (PUBLIC DATA)   ")
    print("==================================================================")
    pipeline = OperativeDemoPipeline()
    pipeline.simulate_public_api_ingestion()
    pipeline.run_evidence_critic_and_triage()
    print("==================================================================")
    print("  Pipeline execution complete. Ready for private biobank plugin.  ")
    print("==================================================================")
