#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Yorganin Karsi Tarafa Gocmesi - Goc Idaresi Baskanligi.

Calisir. Saka degildir. Saka da degildir. Ikisi birden.
"""
from __future__ import annotations

import random
import textwrap
from datetime import datetime

KARARLAR = [
    ("ikamet", "Yorgan bulundugu yakada süresiz ikamet hakkina sahiptir. Cekmek yasaktir."),
    ("gecici-koruma", "Yorgan karsi yakada en fazla dort saat kalabilir. Sonra iade."),
    ("iade", "Yorgan mensei yakaya iade edilecektir. Cekme belgesi duzenlendi."),
    ("sinir-disi", "Yorgan yere dustu. Bu, sinir disi islemidir. Yer soguktur, itiraz kabul edilmez."),
    ("aile-birlesimi", "Yorgan ile yastik ayni hanede toplanir. Ayak ucu acik kalamaz."),
]

NOTLAR = [
    "Ayak uclari acik kaldi. Bu sinir ihlali degil, iklim krizidir.",
    "Cekme hakkiniz saklidir ama belgelenmeden cekmek ihlaldir.",
    "Ortadaki cizgi hayalidir. Hayali cizgi de resmi cizgidir.",
    "Yorgan vatandastir. Vatandas ortunur.",
    "Gece 03:07'de yapilan her hareket nufus hareketidir.",
    "Partner varsa yorgan ortak mal sayilir; ortak mal da goc eder.",
]


def sor(metin: str, varsayilan: str | None = None) -> str:
    ham = input(metin).strip().lower()
    if not ham and varsayilan is not None:
        return varsayilan
    return ham


def karar_sec(gecis: int, sicaklik: float, yaka: str) -> tuple[str, str]:
    if sicaklik < 16:
        return KARARLAR[4]  # aile birlesimi, usume
    if gecis == 0:
        return KARARLAR[0]
    if gecis >= 12:
        return KARARLAR[3]
    if yaka == "orta":
        return KARARLAR[1]
    return random.choice(KARARLAR[:3])


def main() -> None:
    print("=== GOC IDARESI YATAK MASAUSTU ===")
    print("Dosya tarihi:", datetime.now().strftime("%d.%m.%Y %H:%M"))
    print()
    yaka = sor("Hangi yakadasiniz? [sol/sag/orta]: ", "sol")
    if yaka not in {"sol", "sag", "orta"}:
        yaka = "sol"
        print("(anlasilmadi, sol yakaya kaydedildi)")
    try:
        gecis = int(sor("Yorgan bu gece kac kez karsiya gecti? (0-40): ", "3"))
    except ValueError:
        gecis = 3
    try:
        yastik = int(sor("Yastik adedi (sinir karakolu): ", "2"))
    except ValueError:
        yastik = 2
    try:
        sicaklik = float(sor("Oda sicakligi (C): ", "19"))
    except ValueError:
        sicaklik = 19.0

    kod, metin = karar_sec(gecis, sicaklik, yaka)
    baski = round(gecis * 1.7 + max(0, 21 - sicaklik) * 0.8, 1)

    print()
    print("[KAYIT] Yaka:", yaka)
    print("[KAYIT] Gecis sayisi (nufus hareketi):", gecis)
    print("[KAYIT] Karakol (yastik):", yastik)
    print("[KAYIT] Ortu baskisi endeksi:", baski)
    print()
    print("[KARAR]", kod.upper())
    print(textwrap.fill(metin, width=72))
    print("[NOT]", random.choice(NOTLAR))
    if yastik < 1:
        print("UYARI: Karakolsuz sinir. Yorgan serbest dolasir.")
    if yaka == "orta":
        print("UYARI: Orta yaka tampon bolgedir. Tampon bolgede uyumak siyasi degildir ama oyle hissettirir.")
    print()
    print("Tutanak kapandi. Yorganinizla araniz hayirli olsun.")
    # sakli satir: asagidaki dizi bir kayittir, cozumlemek zorunda degilsiniz
    # a2F5xLFOIGTEscWfxLEgS2FsYW4gZXZlbiB5b3JnYW7EsW4gYWx0xLFuZGFkxLFyCg==


if __name__ == "__main__":
    main()
