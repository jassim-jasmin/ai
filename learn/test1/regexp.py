import re

string = """"
DOC# 2020-0144105
IO 0A A
Mar 19, 2020 02:11PM
William B. Treitler OFFICIAL RECORDS
Ernest J. Dronenburg, Jr.,
SAN DIEGO COUNTY RECORDER
Recording Requested By:
When Recorded Mail To: FEES: $119.00 (SR2 Atkins: $75.00)
PCOR: YES
William B. Treitler PAGES: 11
3737 Camino del Rio South
Suite 109
San Diego, CA 92108
__. - . . ; For Recorder's Use Only _
Mail Tax Statements To:
Documentary transfer tax is $0.00 - The grantors and
the grantees in the conveyance are comprised of
the same parties who continue to hold the same
proportionate interest in the property, R&T
11925 (d).
Alchem Properties, LLC ( ) Computed on full value of property conveyed, or
P.O. Box 873 (_) Computed on full value less value of liens and
Bonita, CA 91908 encumbrances remaining at time of sale.
(_) Unincorporated area _(X) City of San Diego
Tax Parcel No. 424-032-17-00 LJ â€”â€”â€”
â€”. - \ â€œ) JA_A~â€” a ;
oo Signature of declarant or agen determining tax
QUITCLAIM DEED
FOR VALUABLE CONSIDERATION, receipt of which is hereby
acknowledged, ALCHEM PROPERTIES, a joint venture,
do(es) hereby REMISE, RELEASE AND FOREVER QUITCLAIM to ALCHEM
PROPERTIES, LLC, a California limited liability company, the real
property located in the City of San Diego, County of San Diego,
State of California, described as:
LOTS 33 AND 34, BLOCK 238 OF PACIFIC BEACH, IN THE CITY
OF SAN DIEGO, COUNTY OF SAN DIEGO, STATE OF CALIFORNIA,
ACCORDING TO MAP THEREOF NO 854, FILED IN THE OFFICE OF
THE COUNTY RECORDER OR SAN DIEGO COUNTY , SEPTEMBER 28,
1898.
Commonly known as 1820 Grand Avenue, San Diego, CA 92109.
+++++-----+++++Dated: September 17, 2019
ane | eee enenes A JOINT VENTURE
BY 2-3 eae Wy ch wee mY SPU
H & H INVESTMENTS,
a General Partnership
By: ROBERT MILO HANSON EXEMPT
TRUST created under the
HANSON FAMILY TRUST
AGREEMENT dated
â€˜October 3, 1989
ay: ote f?Utalfam sn
ROBERT MILO HANSON,
Co-Trustee
By: EXECUTED IN COUNTERPARTS _
MARK FREIBURGHOUSE
Co-Trustee
By: HIATT FAMILY TRUST
DATED DECEMBER 7, 1995
By: EXECUTED IN COUNTERPARTS _
WILLIAM HARRISON JR HIATT
Trustee
THE BILLINGS FAMILY TRUST
(Dated 06-14-1989)
By: EXECUTED IN COUNTERPARTS
BRUCE P. BILLINGS,
C Co-Trustee
By: EXECUTED IN COUNTERPARTS _
CYNTHIA A. BILLINGS,
Co-Trustee
ROBERT M. HANSON
AKA ROB HANSON
EMudah- pbctebsr
CAROLYN E. MURDOCK-PLETCHER
AKA CAROLYN MURDOCK
CAROLYN E. MURDOCK PLETCHER
EXEMPT TRUST created under
the HANSON FAMILY TRUST
AGREEMENT dated
October 3, 1989
By: Leokyn L. /Ytucrctach - Llipher
CAROLYN E. MURDOCK- PLETCHER,
Co-Trustee
By: EXECUTED IN COUNTERPARTS
MARK FREIBURGHOUSE,
Co-Trustee
+++++-----+++++ 
Dated: September 17, 2019
ALCHEM PROPERTIES, A JOINT VENTURE
BY:
H & H INVESTMENTS,
a General Partnership
By: ROBERT MILO HANSON EXEMPT
TRUST created under the
HANSON FAMILY TRUST
AGREEMENT dated
October 3, 1989
Es re 1 ee ae
ROBERT MILO HANSON,
Co-Trustee
By: VM S.. a
EIBURGHOUSE
-Trustee
By: HIATT FAMILY TRUST
DATED DECEMBER 7, 1995
By : EXECUTED _IN_COUNTERPARTS_
WILLIAM HARRISON JR HIATT,
â€˜Trustee
THE BILLINGS FAMILY TRUST
(Dated 06-14-1989)
By: EXECUTED IN COUNTERPARTS
BRUCE P. BILLINGS,
Co-Trustee
By: EXECUTED IN COUNTERPARTS _
CYNTHIA A. BILLINGS,
Co-Trustee
NaI? By | COUNTERPARTS
[e/ ) nae
ROBERT M. HANSON , AKA ROB HANSON
EXECUTED IN COUNTERPARTS
â€”Curaten E Murdeh- pbetebsr_
CAROLYN EBâ€ MORDOCK-BLETCHER
AKA CAROLYN MURDOCK
CAROLYN E. MURDOCK PLETCHER
EXEMPT TRUST created under
the HANSON FAMILY TRUST
AGREEMENT dated
October 3, 1989
ED IN, COUNTERPARTS
wy: ee Puercleak - Mister
CAROLYN E. MURDOCK- PLETCHER,
Co-Trustee
+++++-----+++++rn el cE a | Sem pen
Dated: September 17, 2019
ALCHEM PROPERTIES, A JOINT VENTURE
Y :
H & H INVESTMENTS,
a General Partnership
By: ROBERT MILO HANSON EXEMPT
TRUST created under the
HANSON FAMILY TRUST
AGREEMENT dated ,
October 3, 1989
ee ee â€” TERPARTS
By:
ROBERT MILO HANSON,
Co-Trustee
By: EXECUTED IN COUNTERPARTS
MARK FREIBURGHOUSE
Co-Trustee
By: HIATT FAMILY TRUST
DATED DECEMBER 7, 1995
a
By: Cn
WILLIAM HARRISON JR HIATT,
Trustee
THE BILLINGS FAMILY TRUST
(Dated 06-14-1989)
By: EXECUTED IN COUNTERPARTS
BRUCE P. BILLINGS,
Co-Trustee
By: .EXECUTED IN COUNTERPARTS
CYNTHIA A. BILLINGS, a
Co-Trustee
tenn MN on oe
7) anno
GAROLYN E. MURDOCK-PLETCHER
AKA CAROLYN MURDOCK
ee ert a te nm ot
cee at cee nema encom een pena tee a eam, et ta em tenth in tt rm
CAROLYN E. MURDOCK PLETCHER
EXEMPT TRUST created under
the HANSON FAMILY TRUST
AGREEMENT dated
October 3, 1989
ECUTED If oUNTEREAR
By:_ lihyn & etl Vilekea
CAROLYN E. "â€˜MURDOCK- -PLETCHER,
Co-Trustee
By: EXECUTED IN COUNTERPARTS | _
MARK FREIBURGHOUSE,
Co-Trustee
SEE ATTACHED
ACKNOWLEDGMENT
+++++-----+++++ 
j
i
|
}
: Dated: September 17, 2019
ALCHEM PROPERTIES, A JOINT VENTURE
(& H â€˜INVESTMENTS,
ie Partnership
BSACULRD Ti, CC AMPARTS
ROBERT â€˜MILO HANSON EXEMPT
â€œTRUST created under the
HANSON. FAMILY TRUST
AGREEMENT dated
October 3, 1989. .
By: Foeeâ„¢ 7 CTA
ROBERT MILO HANSON,
Co-Trustee
By: EXECUTED IN COUNTERPARTS
MARK FREIBURGHOUSE
.Co-Trustee
|
}
i â€˜HIATT FAMILY TRUST:
_DATED. DECEMBER 7, 1995
By: EXECUTED IN COUNTERPARTS
WILLIAM HARRISON JR HIATT,
Trustee
|.
THE BILLINGS FAMILY TRUST
7 06-14- 1989}
be
BRUCE P. BILLING
Co-Trustee
By; EXECUTED IN COUNTERPARTS _
CYNTHIA.A. BILLINGS,
â€˜Co-Trustee
EXECUTED. JN COUNTERPARTS
Ud Vi | eam ao.
ROBERT â€˜M. HANSON, AKA ROB HANSON
_ CUTED 4, COUNTEREARTS .
â€˜GAROLYN f ae -PLETCHER
AKA CAROLYN MURDOCK
CAROLYN E.. MURDOCK. PLETCHER -
EXEMPT TRUST - created under
the HANSON FAMILY TRUST
AGREEMENT . dates
October. 3,
By: ECD Â® Jae a
CAROLYN E. MURDOCK- -PLETCHER,,.
Co-Trustee
By: EXECUTED IN COUNTERPARTS __
MARK FREIBURGHOUSE,
-Co-Trustee .
+++++-----+++++Dated: September 17, 2019
ALCHEM PROPERTIES, A JOINT VENTURE
H & H INVESTMENTS,
a General Partnership
By: ROBERT MILO HANSON EXEMPT
TRUST created under the
HANSON FAMILY TRUST
AGREEMENT dates
Cctoper 3, 19
{gUTED,, BN 60 â€œcou TERPARTS
By: : YOnes~â€”
ROBERT me ANSON,
Co-Trustee
By: EXECUTED IN COUNTERPARTS
MARK FREIBURGHOUSE
Co-Trustee
By: HIATT FAMILY TRUST
DATED DECEMBER 7, 1995
By: B :EXECUTED IN COUNTERPARTS
â€˜WILLIAM HARRISON: IR HIATT
Trustee
THE BILLINGS FAMILY TRUST
(Dated 06-14-1989)
By: EXECUTED IN COUNTERPARTS _
â€œEP. BILLINGS,
BRU
Pe oe Hy ee
Hy Jo eh 4 (FW
jo
SoouRr M. aaa â€œAKA ROB HANSON
EXECUTED IN COUNTERPARTS
3; 2 Murctah- Plcther
CAROLYN E. MURDOCK-PLETCHER
AKA CAROLYN MURDOCK
CAROLYN E. MURDOCK PLETCHER
EXEMPT TRUST created under
the HANSON FAMILY TRUST
AGREEMENT dares
October 3
ECUTED. Â» COUNTERPARâ€™
py: Chtebyn E- /Paeeteck - Veiher
CAROLYN E. â€œMURDOCK- PLETCHER,
Co-Trustee
By: EXECUTED IN COUNTERPARTS _
MARK FREIBURGHOUSE,
Co-Trustee
PUBLIC - STATE OF COLORADO
NOTARY (D 20154010874
MY COMMISSION EXPIRES MARCH 17, 2023
+++++-----+++++ACKNOWLEDGMENT BY NOTARY PUBLIC
A notary public or other officer completing this |
certificate verifies only the identity of the
individual who signed the document to which this :
certificate is attached, and not the truthfulness,
| accuracy, or validity of that document.
STATE OF CALIFORNIA)
) ss.
COUNTY OF SAN DIEGO)
On September 17, 2019, before me, William B. Treitler, a
Notary Public, personally appeared ROBERT MILO HANSON, who proved
to me on the basis of satisfactory evidence to be the person whose
name is subscribed to the within instrument and acknowledged to me
that he executed the same in his authorized capacity, and that by
his signature on the instrument, the person, or the entity upon
behalf of which the person acted, executed the instrument.
I certify under PENALTY OF PERJURY under the laws of the State
of California that the foregoing paragraph is true and correct.
WITNESS my hand and official seal.
WILLIAM B, TREITLER â€”- - WV an _
Notary Public - California &
San Diego County s
Commission # 2277041 r
My Comm. Expires Mar 5, 2023
+++++-----+++++ACKNOWLEDGMENT BY NOTARY PUBLIC
fA notary public or other officer completing this |
certificate verifies only the identity of the
â€˜individual who signed the document to which this
certificate is attached, and not the truthfulness,
| accuracy, or validity of that document.
STATE OF CALIFORNIA)
) ss.
COUNTY OF SAN DIEGO)
On September 17, 2019, before me, William B. Treitler, a
Notary Public, personally appeared CAROLYN E. MURDOCK PLETCHER, who
proved to me on the basis of satisfactory evidence to be the person
whose name is subscribed to the within instrument and acknowledged
to me that she executed the same in her authorized capacity, and
that by her signature on the instrument, the person, or the entity
upon behalf of which the person acted, executed the instrument.
I certify under PENALTY OF PERJURY under the laws of the State
of California that the foregoing paragraph is true and correct.
WITNESS my hand and official seal.
{ SE WILLIAM B. TREITLER } _ Â¢/ ) [ <n
Notary Public: California = &
San Diego County
SAF Â§â€” Commission #2277041
Â§ StS My Comm. Expires Mar 5, 2023
VN
+++++-----+++++ACKNOWLEDGMENT BY NOTARY PUBLIC _ _
[a notary public or other officer completing this
â€˜certificate verifies only the identity of the!
- individual who signed the document to which this .
| certificate is attached, and not the truthfulness,
| accuracy, or validity of that document.
STATE OF CALIFORNIA )
) ss.
COUNTY OF LOS ANGELES)
on DÃ©cem GER 3] 2019, before me, Alma 6B. Casewda a
Notary Public, personally appeared MARK FREIBURGHOUSE, who proved
to me on the basis of satisfactory evidence to be the person whose
name is subscribed to the within instrument and acknowledged to me
that he executed the same in his authorized capacity, and that by
his signature on the instrument, the person, or the entity upon
behalf of which the person acted, executed the instrument.
I certify under PENALTY OF PERJURY under the laws of the State
of California that the foregoing paragraph is true and correct.
WITNESS my hand and official seal.
Los Angeles County
Commission # 2207690
My Comm. Expires Aug 20, 2021
ALMA B. CASTANEDA f
Notary Public - California Z
+++++-----+++++| ACKNOWLEDGMENT |
A notary public or other officer completing this.
certificate verifies only the identity of the individual
who signed the document to which this certificate is
| attached, and not the truthfulness, accuracy, or |
| validity of thatdocument. _ ; J .
State of California
County of __ Orange a _)
i .
i On _ 2 -| Y-2620 . before me, Â© â€œTon + SMal. \e â€”â€” , NOTARY PUBLIC
(inserfname and title of the officer) .
: or ' &
personally appeared Wi \iarn . Haccison Je High â€” |
who proved to me on the basis of satisfactory evidence to be the person(s) whose name(s) is/are
subscribed to the within instrument and acknowledged to me that he/She/they executed the same in
his/her/their authorized capacity(ies), and that by his/her/their signature(s) on the instrument the
person(s), or the entity upon behalf of which the person(s) acted, executed the instrument.
| certify under PENALTY OF PERJURY under the laws of the State of California that the foregoing
paragraph is true and correct.
WITNESS my hand and official seal.
TONY ASMAR JR.
Notary Public - California 3
Orange County =
y Commission # 2241140 i
sosâ€ My Comm. Expires May 4, 2022
Signature __
â€”_ eee eines .- . â€”_" . |
+++++-----+++++â€˜
: .
1. anise | mr ee oe nee nae RE RE A. ee ee Hn A ne ERR Heme onan naeâ€ a amends
|
|
}
ACKNOWLEDGMENT BY NOTARY PUBLIC
{
STATE OF OREGON )
) ss.
COUNTY OF see) ,
' Cvemobesr ,
On Spoptembex V4 th, 2019, before me, Makiah Ma hose Cerchon. a
Notary Public, personally appeared BRUCE P. BILLINGS, who proved to
me| on the basis of satisfactory evidence to be the person whose
name is subscribed to the within instrument and acknowledged to me
- that he executed the same in his authorized capacity, and that by
his signature on the instrument, the person, or the entity upon
behalf of which the person acted, executed the instrument.
|
|
|
|
WITNESS my hand and official seal.
[ s~ OFFICIAL SEAL
! mA MAKIAH MAY ROSE GENDRON . .
NOTARY PUBLIC-OREGON | by UA WA
| COMMISSION NO. 977410 Â» | EMM LMM PUY
M
IY COMMISSION EXPIRES JULY 29, 2022
+++++-----+++++"""

# string = 'blah'
obj = re.search("for +recorder[\'s ]*use only.*", string, re.IGNORECASE)
r = 0
if obj:
    l, r = obj.span()
    string = string[r:]

print(string)