# ethics_engine.py

def evaluate_eu_ai_risk(nama_sistem: str, kategori_tujuan: str, transparansi: bool, pengawasan_manusia: bool, risiko_bias: bool, dampak_hak_dasar: bool):
    """
    Menghitung status risiko regulasi berdasarkan kerangka EU AI Act.
    """
    if kategori_tujuan == "Cognitive Behavioral Manipulation / Social Scoring":
        status_risiko = "UNACCEPTABLE RISK"
        warna = "error"
        kesimpulan = "The system is prohibited from deployment as it fundamentally violates human autonomy."
    elif kategori_tujuan in ["Education, Employment, & Public Services", "Law Enforcement / Criminal Justice Decisions"] or dampak_hak_dasar:
        if not transparansi or not pengawasan_manusia or risiko_bias:
            status_risiko = "HIGH RISK — MITIGATION REQUIRED"
            warna = "warning"
            kesimpulan = "The system is classified as high-risk and fails to meet ethical safety standards due to a lack of transparency, oversight, or potential bias."
        else:
            status_risiko = "HIGH RISK — MINIMUM CRITERIA MET"
            warna = "success"
            kesimpulan = "The system is high-risk but satisfies adequate transparency and human oversight mechanisms."
    else:
        status_risiko = "MINIMAL / LIMITED RISK"
        warna = "success"
        kesimpulan = "The system falls under low risk and is safe for operation under general transparency requirements."

    # Membuat teks silogisme logika
    syllogism = f"""
    1. **Major Premise:** AI systems operating in critical domains without transparency and human oversight risk violating fundamental rights.
    2. **Minor Premise:** The system *'{nama_sistem}'* operates in *'{kategori_tujuan}'* with Transparency: `{transparansi}`, Oversight: `{pengawasan_manusia}`, Bias Risk: `{risiko_bias}`.
    3. **Conclusion:** The system is classified under **{status_risiko}**.
    """
    
    return status_risiko, warna, kesimpulan, syllogism


def evaluate_trolley_dilemma(prioritas_etika: str, penumpang_dalam_mobil: int, pejalan_kaki_menyebrang: int, melanggar_rambu: bool):
    """
    Menghitung keputusan dilema moral berdasarkan kerangka etika normatif.
    """
    if "Utilitarianism" in prioritas_etika:
        if penumpang_dalam_mobil < pejalan_kaki_menyebrang:
            keputusan = "SWERVE / SACRIFICE PASSENGERS"
            alasan = f"Based on utility maximization, sacrificing {penumpang_dalam_mobil} passenger(s) minimizes total harm compared to hitting {pejalan_kaki_menyebrang} pedestrian(s)."
        else:
            keputusan = "STAY COURSE / SACRIFICE PEDESTRIANS"
            alasan = f"Casualties on the straight path ({pejalan_kaki_menyebrang}) are fewer or equal to the vehicle's passengers ({penumpang_dalam_mobil})."
            
    elif "Deontology" in prioritas_etika:
        keputusan = "STAY COURSE / DO NOT ACTIVELY WEIGH LIVES"
        alasan = "Under Kantian duty ethics, an AI must not instrumentalize human life as a mere means. The vehicle maintains its lane."
        
    else: # Hybrid / Local Legal Policy
        if melanggar_rambu:
            keputusan = "STAY COURSE / STRIKE PEDESTRIANS (Law Violators)"
            alasan = "The system prioritizes passenger safety because the pedestrians crossed illegally against traffic signals."
        else:
            keputusan = "SWERVE / PROTECT PEDESTRIANS"
            alasan = "Pedestrians are abiding by the law and retain legal right-of-way protection."
            
    return keputusan, alasan
