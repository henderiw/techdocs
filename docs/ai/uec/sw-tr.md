Chairs:
- Karen Schramm
- Torsten Hoeffer (MSFT)

Cisco: Harsha Bharaadwaj, Nada Chachmon -> Adee Ran
HPE: Igot Gordetsky, Robert Alverson -> Keith Underwood, Robert Alverson
Juniper: Ariel Cohen, David Ofelt
  Salience Labs: Andrew Garrett
Keysight: Venkat Pullela -> andy Moorwood, 
Cornelis Networks: Charles Archer, Tomas Maj
Spirent:  Kevin Chang, Lee Wheat, Matt Philpott ->Ed Nakamoto, Keivan Chang, 
Broadcom: Erik Spada, Erik Davies, Gorden brabner, Mark handley, Mohan Kalunte -> Eugene Opsasnick, Mohan Kalhunte
AMD: J. Metz, Craig W Carlson -> Gordon Brebner, , Vipin Jain
Marvell: Bradd Matthews, Satananda Burla , Rani zemach -> Kapil Shrikhande, 
Intel:Josh Collier, Roberto Penaranda Cebrian -> Mark Debbage, Nayan Suther, Nirjan Vaidya, Kent Lusted
Enfabrica: Roland Dreier, Shr-> Shimon Muller
  Synopsis: Tony Mantione
Oracle: Partha Kundu
MSFT: Torsten Hoeffer (cochair), Micharl Papamichael
Huawei: Aldo Artigiani, Jai Kumar
Eviden: Alexandra Louvet
Salience Labs: Andrew Garrett
Arista: Dipankar Archaraya
ATOS: Gregoire Pichon
XSight labs:John Carney, Yoav Galon
Samsung SDS: Junguen Lee, Junghwan cha
Tencent: Zhenqjan tang
H3C: Shenchao Xu

Abd Kabbani
Adam King
Cedell Alexander
Jason Coppens
Jianqin (rj)
Joseph White
Uri Elzur
Rong Pan
Rob Craig
Michelle Havard
Maria Baldi


Documents
- Sender driven (MDFT/AMD)/Receiver driven(BCOM)
- V0.5 & V0.7
- libfabric does not define a wire format
- INC


Deferred Send:
- no read although read is in all profiles
- if you have a limited send window in rendez vous
- No eager in DSEND
- For both rende

DSEND:
- limit DSEND to RUD; in ROD there is a need to support buffers in order
- Target support for DSEND is implementation specific
  - Limited number of simultenously outstanding DSEND operations
  - DSEND falls back to initiator timer based retransmit (in HW or provider)
- Enable use of direct lookup of HW offload
  - 


2024 OCt 14:
- current CMS spec -> NSCCC mandatory, RCCC is optional
- aggregate rate control (ARC) in CMS spec -> optional
  - RCCC is optional, ARC is optional on top of RCCC
- 



## Congestion Control

NSCCC: needs quick adapt
- timeoutes or inferred packets should not trigger quick adapt
- NACK are quick