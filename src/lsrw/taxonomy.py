DOMAINS = ("molecular_biology", "biochemistry", "neuroscience", "bioinformatics")
ABILITIES = ("essay", "experimental_design", "research_reasoning")
LEGACY_ABILITIES = ("knowledge", "paper_appraisal")
DIMENSIONS = {a: ("concept_coverage", "logic_chain", "task_detail", "controls_uncertainty", "conclusion_alignment") for a in ABILITIES}
WEIGHTS = {
    "essay": (30, 40, 10, 10, 10),
    "experimental_design": (20, 30, 30, 10, 10),
    "research_reasoning": (15, 30, 30, 10, 15),
}
FOLLOWUP_FIELDS = ("biological_question", "mechanism", "intervention", "readout", "predicted_outcome")
REFERENCE_MIN_WORDS = {"essay": 301, "experimental_design": 901, "research_reasoning": 1201}
SAMPLES = {"essay": 1, "experimental_design": 1, "research_reasoning": 5}
TOPICS = {
    "molecular_biology": ("gene_expression", "ko_knockdown_rescue", "wb_antibody_specificity", "immunofluorescence", "protein_purification_interactions"),
    "biochemistry": ("metabolic_pathways", "enzyme_kinetics", "inhibition_allostery", "metabolic_flux", "assay_interference", "macromolecule_biosynthesis"),
    "neuroscience": ("circuit_structure", "activity_measurement", "optogenetics_causality", "behavior", "motor_sensory_stress_confounds"),
    "bioinformatics": ("multiomics_integration", "enrichment", "pseudotime", "gwas", "whole_genome_sequencing"),
}
SOURCE_STATES = ("real_and_matching", "citation_mismatch", "known_fabrication", "insufficient_to_verify")
SUPPORT_STATES = ("supported", "partially_supported", "unsupported", "insufficient_evidence")
CELL_COUNTS = {("public", "text"): 3, ("public", "image"): 1, ("heldout", "text"): 13, ("heldout", "image"): 3}
SCHEMA_VERSION = "2.0"
PROMPT_VERSION = "2.0"
