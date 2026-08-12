"""
ethics_engine.py
Core deterministic reasoning engine for EU AI Act compliance classification
and normative machine ethics dilemma resolution.
"""

from typing import Tuple


def evaluate_eu_ai_risk(
    system_name: str,
    target_category: str,
    has_transparency: bool,
    has_human_oversight: bool,
    has_bias_risk: bool,
    impacts_fundamental_rights: bool,
) -> Tuple[str, str, str, str]:
    """
    Evaluates the regulatory risk classification based on the EU AI Act framework.
    """
    if target_category == "Cognitive Behavioral Manipulation / Social Scoring":
        risk_status = "UNACCEPTABLE RISK"
        badge_color = "error"
        conclusion = "The system is prohibited from deployment as it fundamentally violates human autonomy."
    elif (
        target_category in [
            "Education, Employment, & Public Services",
            "Law Enforcement / Criminal Justice Decisions",
        ]
        or impacts_fundamental_rights
    ):
        if not has_transparency or not has_human_oversight or has_bias_risk:
            risk_status = "HIGH RISK — MITIGATION REQUIRED"
            badge_color = "warning"
            conclusion = (
                "The system is classified as high-risk and fails to meet ethical safety "
                "standards due to a lack of transparency, oversight, or potential bias."
            )
        else:
            risk_status = "HIGH RISK — MINIMUM CRITERIA MET"
            badge_color = "success"
            conclusion = (
                "The system is high-risk but satisfies adequate transparency and "
                "human oversight mechanisms."
            )
    else:
        risk_status = "MINIMAL / LIMITED RISK"
        badge_color = "success"
        conclusion = (
            "The system falls under low risk and is safe for operation under general "
            "transparency requirements."
        )

    # Construct formal deontic syllogism
    syllogism = f"""
    1. **Major Premise:** AI systems operating in critical domains without transparency and human oversight risk violating fundamental rights.
    2. **Minor Premise:** The system *'{system_name}'* operates in *'{target_category}'* with Transparency: `{has_transparency}`, Oversight: `{has_human_oversight}`, Bias Risk: `{has_bias_risk}`.
    3. **Conclusion:** The system is classified under **{risk_status}**.
    """

    return risk_status, badge_color, conclusion, syllogism


def evaluate_trolley_dilemma(
    ethical_priority: str,
    passenger_count: int,
    pedestrian_count: int,
    violates_traffic_rules: bool,
) -> Tuple[str, str]:
    """
    Calculates moral dilemma resolutions based on normative ethical frameworks.
    """
    if "Utilitarianism" in ethical_priority:
        if passenger_count < pedestrian_count:
            decision = "SWERVE / SACRIFICE PASSENGERS"
            rationale = (
                f"Based on utility maximization, sacrificing {passenger_count} passenger(s) "
                f"minimizes total harm compared to hitting {pedestrian_count} pedestrian(s)."
            )
        else:
            decision = "STAY COURSE / SACRIFICE PEDESTRIANS"
            rationale = (
                f"Casualties on the straight path ({pedestrian_count}) are fewer or equal "
                f"to the vehicle's passengers ({passenger_count})."
            )

    elif "Deontology" in ethical_priority:
        decision = "STAY COURSE / DO NOT ACTIVELY WEIGH LIVES"
        rationale = (
            "Under Kantian duty ethics, an AI must not instrumentalize human life as a mere means. "
            "The vehicle maintains its lane."
        )

    else:  # Hybrid / Local Legal Policy
        if violates_traffic_rules:
            decision = "STAY COURSE / STRIKE PEDESTRIANS (Law Violators)"
            rationale = (
                "The system prioritizes passenger safety because the pedestrians crossed "
                "illegally against traffic signals."
            )
        else:
            decision = "SWERVE / PROTECT PEDESTRIANS"
            rationale = (
                "Pedestrians are abiding by the law and retain legal right-of-way protection."
            )

    return decision, rationale
