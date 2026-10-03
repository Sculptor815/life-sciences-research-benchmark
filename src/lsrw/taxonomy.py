DOMAINS = ("molecular_biology", "biochemistry", "neuroscience", "bioinformatics")
ABILITIES = ("knowledge", "experimental_design", "research_reasoning", "paper_appraisal")
DIMENSIONS = {
    "experimental_design": ("hypothesis_measurement", "controls", "replication_statistics", "confounds_feasibility", "interpretation"),
    "research_reasoning": ("question_definition", "competing_hypotheses", "discriminating_predictions", "information_value", "falsification_updating"),
    "paper_appraisal": ("source_verification", "evidence_localization", "methods_evaluation", "inferential_scope", "uncertainty_validation"),
}
TOPICS = {
    "molecular_biology": ("gene_expression", "ko_knockdown_rescue", "wb_antibody_specificity", "immunofluorescence", "protein_purification_interactions"),
    "biochemistry": ("metabolic_pathways", "enzyme_kinetics", "inhibition_allostery", "metabolic_flux", "assay_interference", "macromolecule_biosynthesis"),
    "neuroscience": ("circuit_structure", "activity_measurement", "optogenetics_causality", "behavior", "motor_sensory_stress_confounds"),
    "bioinformatics": ("multiomics_integration", "enrichment", "pseudotime", "gwas", "whole_genome_sequencing"),
}
SOURCE_STATES = ("real_and_matching", "citation_mismatch", "known_fabrication", "insufficient_to_verify")
SUPPORT_STATES = ("supported", "partially_supported", "unsupported", "insufficient_evidence")
CELL_COUNTS = {("public", "text"): 3, ("public", "image"): 1, ("heldout", "text"): 13, ("heldout", "image"): 3}
SCHEMA_VERSION = "1.0"
PROMPT_VERSION = "1.0"
