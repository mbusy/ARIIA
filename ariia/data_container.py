# -*- coding: utf-8 -*-
# !/usr/bin/env python

# MIT License
#
# Copyright (c) 2017 Maxime Busy
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

HOUR     = "hour"
DATE     = "date"
METEO    = "meteo"
HISTORY  = "history"
SHOPPING = "shopping"

TRIGGER_DICT = {"hour" 		: [["heure", "est"], ["donne-moi","l'heure"], ["heure","est-il"]],
				"date" 		: [["date","est"],["donne-moi","date"],["jour","sommes-nous"],["jour","est-il"]],
				"meteo" 	: [["donne-moi","météo"],["quelle","est","météo"],["quel","temps","fait-il"]],
				"history"	: [["qui", "était"]],
				"shopping"	: [["liste", "de", "courses"]]
				}

KEYWORDS_DICT = {"date"			:False,
				 "liste" 		:False,
				 "jour"		    :False,
				 "heure"	    :False,
				 "matin"	    :False,
				 "l'après-midi" :False,
				 "météo"	    :False,
				 "l'heure"	    :False,
				 "temps"	    :False,
				 "monde" 	    :False,
				 "informations" :False,
				 "yeux"		    :False,
				 "musique"      :False,
				 "utilisateur"  :False,
				 "station"		:False,
				 "vidéo"		:False,
				 "vidéos"		:False,
				 "bonjour"		:False,
				 "salut"		:False,
				 "calendrier"   :False,
				 "besoin"	    :False,
				 "mode"  	    :False,
				 "exploration"  :False,
				 "carte"		:False,
				 "pièce"		:False,
				 "courses"		:False,

				 "pleuvoir"	    :False,
				 "écouter"      :False,
				 "charger"      :False,
				 "recharger"    :False,
				 "enregistrer"  :False,
				 "m'enregistrer":False,
				 "regarder" 	:False,

				 "est"		    :False,
				 "c'est" 		:False,
				 "regarde"	    :False,
				 "est-ce"	    :False,
				 "est-il"	    :False,
				 "est-on"	    :False,
				 "es"		    :False,
				 "sommes-nous"  :False,
				 "fait-il"	    :False,
				 "va-t-il"	    :False,
				 "passe-t-il"   :False,
				 "va"		    :False,
				 "vas"		    :False,
				 "es-tu"	    :False,
				 "suis-je"	    :False,
				 "était"	    :False,
				 "t'appelles"   :False,
				 "donne-moi"    :False,
				 "cache-toi"    :False,
				 "tourne-toi"   :False,
				 "réveille-toi" :False,
				 "dors"  	    :False,
				 "arrête" 		:False,
				 "sors"			:False,
				 "repose-toi"   :False,
				 "lève-toi"     :False,
				 "baisse-toi"   :False,
				 "montre-moi" 	:False,
				 "présente-toi" :False,
				 "présente"	    :False,
				 "viens"		:False,
				 "rapproche-toi":False,
				 "suis-moi" 	:False,
				 "laisse-moi"	:False,

				 "rappelle-moi" :False,
				 "sais"		    :False,

				 "comment"	    :False,
				 "qui"		    :False,
				 "quelle"	    :False,
				 "quel"		    :False,
				 "que"		    :False,
				 "pas"		    :False,

				 "faire"	    :False,

				 "je"		    :False,
				 "tu"		    :False,
				 "on"		    :False,
				 "te"		    :False,
				 "toi"			:False,

				 "de"		    :False,
				 "se"		    :False,
				 "le"		    :False,

				 "haut"		    :False,
				 "bas"		    :False,
				 "bon" 			:False,
				 "plus"		    :False,
				 "ici"			:False,
				 "près"			:False,
}
