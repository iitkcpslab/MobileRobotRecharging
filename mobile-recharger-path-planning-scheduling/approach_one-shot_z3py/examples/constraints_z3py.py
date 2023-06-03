
from z3 import *

# geting interpretations from model
def get_model (*argv):
   print 'printing model--start'
   for x in argv:
      print x, '=', m.evaluate(x)
   print 'printing model--end'
   return m.evaluate(total_wait).as_long()


# incremental checking for sat
def check_sat (mid):
   print 'check total_wait <= %d --->' % mid,

   s.push()
   s.add(total_wait<=mid) # incremental constraint
   s.set('timeout', 900000)
   res=s.check()
   print res, '\n'

   if res==sat:
      global m
      m = s.model()
      val = get_model(total_wait, total_rech)
   else:
      val=0
   print '---------------------'
   s.pop()

   return val

# binary search for optimization
# this fn returns the val to which total_wait should be set
# to check satisfiability
def binarySearch_solving (left, right):
   val=-1
   while right>=left:
      mid = left+(right-left)//2
      mid1 = check_sat(mid)
      if mid1>=1:
         right = mid1-1
         val = mid1
      else: left = mid+1
   return val

# initializing solver
s = Solver()


# adding static constraints
# declaration : constants for workers
wtraj_1_1 = Int('wtraj_1_1')
wtraj_1_2 = Int('wtraj_1_2')
wtraj_1_3 = Int('wtraj_1_3')
wtraj_1_4 = Int('wtraj_1_4')
wtraj_1_5 = Int('wtraj_1_5')
wtraj_1_6 = Int('wtraj_1_6')
wtraj_1_7 = Int('wtraj_1_7')
wtraj_1_8 = Int('wtraj_1_8')
wtraj_1_9 = Int('wtraj_1_9')
wtraj_1_10 = Int('wtraj_1_10')
wtraj_1_11 = Int('wtraj_1_11')
wtraj_1_12 = Int('wtraj_1_12')
wtraj_1_13 = Int('wtraj_1_13')
wtraj_1_14 = Int('wtraj_1_14')
wtraj_1_15 = Int('wtraj_1_15')
wtraj_1_16 = Int('wtraj_1_16')
wtraj_1_17 = Int('wtraj_1_17')
wtraj_1_18 = Int('wtraj_1_18')
wtraj_1_19 = Int('wtraj_1_19')
wtraj_1_20 = Int('wtraj_1_20')
wtraj_1_21 = Int('wtraj_1_21')
wtraj_1_22 = Int('wtraj_1_22')
wtraj_1_23 = Int('wtraj_1_23')
wtraj_1_24 = Int('wtraj_1_24')
wtraj_1_25 = Int('wtraj_1_25')
wtraj_1_26 = Int('wtraj_1_26')
wtraj_1_27 = Int('wtraj_1_27')
wtraj_1_28 = Int('wtraj_1_28')
wtraj_1_29 = Int('wtraj_1_29')
wtraj_1_30 = Int('wtraj_1_30')
wtraj_1_31 = Int('wtraj_1_31')
wtraj_1_32 = Int('wtraj_1_32')
wtraj_1_33 = Int('wtraj_1_33')
wtraj_1_34 = Int('wtraj_1_34')
wtraj_1_35 = Int('wtraj_1_35')
wtraj_1_36 = Int('wtraj_1_36')
wtraj_1_37 = Int('wtraj_1_37')
wtraj_1_38 = Int('wtraj_1_38')
wtraj_1_39 = Int('wtraj_1_39')
wtraj_1_40 = Int('wtraj_1_40')
wtraj_1_41 = Int('wtraj_1_41')
wtraj_1_42 = Int('wtraj_1_42')
wtraj_1_43 = Int('wtraj_1_43')
wtraj_1_44 = Int('wtraj_1_44')
wtraj_1_45 = Int('wtraj_1_45')
wtraj_1_46 = Int('wtraj_1_46')
wtraj_1_47 = Int('wtraj_1_47')
wtraj_1_48 = Int('wtraj_1_48')
wtraj_1_49 = Int('wtraj_1_49')

wtraj_2_1 = Int('wtraj_2_1')
wtraj_2_2 = Int('wtraj_2_2')
wtraj_2_3 = Int('wtraj_2_3')
wtraj_2_4 = Int('wtraj_2_4')
wtraj_2_5 = Int('wtraj_2_5')
wtraj_2_6 = Int('wtraj_2_6')
wtraj_2_7 = Int('wtraj_2_7')
wtraj_2_8 = Int('wtraj_2_8')
wtraj_2_9 = Int('wtraj_2_9')
wtraj_2_10 = Int('wtraj_2_10')
wtraj_2_11 = Int('wtraj_2_11')
wtraj_2_12 = Int('wtraj_2_12')
wtraj_2_13 = Int('wtraj_2_13')
wtraj_2_14 = Int('wtraj_2_14')
wtraj_2_15 = Int('wtraj_2_15')
wtraj_2_16 = Int('wtraj_2_16')
wtraj_2_17 = Int('wtraj_2_17')
wtraj_2_18 = Int('wtraj_2_18')
wtraj_2_19 = Int('wtraj_2_19')
wtraj_2_20 = Int('wtraj_2_20')
wtraj_2_21 = Int('wtraj_2_21')
wtraj_2_22 = Int('wtraj_2_22')
wtraj_2_23 = Int('wtraj_2_23')
wtraj_2_24 = Int('wtraj_2_24')
wtraj_2_25 = Int('wtraj_2_25')
wtraj_2_26 = Int('wtraj_2_26')
wtraj_2_27 = Int('wtraj_2_27')
wtraj_2_28 = Int('wtraj_2_28')
wtraj_2_29 = Int('wtraj_2_29')
wtraj_2_30 = Int('wtraj_2_30')
wtraj_2_31 = Int('wtraj_2_31')
wtraj_2_32 = Int('wtraj_2_32')
wtraj_2_33 = Int('wtraj_2_33')
wtraj_2_34 = Int('wtraj_2_34')
wtraj_2_35 = Int('wtraj_2_35')
wtraj_2_36 = Int('wtraj_2_36')
wtraj_2_37 = Int('wtraj_2_37')
wtraj_2_38 = Int('wtraj_2_38')
wtraj_2_39 = Int('wtraj_2_39')
wtraj_2_40 = Int('wtraj_2_40')
wtraj_2_41 = Int('wtraj_2_41')
wtraj_2_42 = Int('wtraj_2_42')
wtraj_2_43 = Int('wtraj_2_43')
wtraj_2_44 = Int('wtraj_2_44')
wtraj_2_45 = Int('wtraj_2_45')
wtraj_2_46 = Int('wtraj_2_46')
wtraj_2_47 = Int('wtraj_2_47')
wtraj_2_48 = Int('wtraj_2_48')
wtraj_2_49 = Int('wtraj_2_49')

wtraj_3_1 = Int('wtraj_3_1')
wtraj_3_2 = Int('wtraj_3_2')
wtraj_3_3 = Int('wtraj_3_3')
wtraj_3_4 = Int('wtraj_3_4')
wtraj_3_5 = Int('wtraj_3_5')
wtraj_3_6 = Int('wtraj_3_6')
wtraj_3_7 = Int('wtraj_3_7')
wtraj_3_8 = Int('wtraj_3_8')
wtraj_3_9 = Int('wtraj_3_9')
wtraj_3_10 = Int('wtraj_3_10')
wtraj_3_11 = Int('wtraj_3_11')
wtraj_3_12 = Int('wtraj_3_12')
wtraj_3_13 = Int('wtraj_3_13')
wtraj_3_14 = Int('wtraj_3_14')
wtraj_3_15 = Int('wtraj_3_15')
wtraj_3_16 = Int('wtraj_3_16')
wtraj_3_17 = Int('wtraj_3_17')
wtraj_3_18 = Int('wtraj_3_18')
wtraj_3_19 = Int('wtraj_3_19')
wtraj_3_20 = Int('wtraj_3_20')
wtraj_3_21 = Int('wtraj_3_21')
wtraj_3_22 = Int('wtraj_3_22')
wtraj_3_23 = Int('wtraj_3_23')
wtraj_3_24 = Int('wtraj_3_24')
wtraj_3_25 = Int('wtraj_3_25')
wtraj_3_26 = Int('wtraj_3_26')
wtraj_3_27 = Int('wtraj_3_27')
wtraj_3_28 = Int('wtraj_3_28')
wtraj_3_29 = Int('wtraj_3_29')
wtraj_3_30 = Int('wtraj_3_30')
wtraj_3_31 = Int('wtraj_3_31')
wtraj_3_32 = Int('wtraj_3_32')
wtraj_3_33 = Int('wtraj_3_33')
wtraj_3_34 = Int('wtraj_3_34')
wtraj_3_35 = Int('wtraj_3_35')
wtraj_3_36 = Int('wtraj_3_36')
wtraj_3_37 = Int('wtraj_3_37')
wtraj_3_38 = Int('wtraj_3_38')
wtraj_3_39 = Int('wtraj_3_39')
wtraj_3_40 = Int('wtraj_3_40')
wtraj_3_41 = Int('wtraj_3_41')
wtraj_3_42 = Int('wtraj_3_42')
wtraj_3_43 = Int('wtraj_3_43')
wtraj_3_44 = Int('wtraj_3_44')
wtraj_3_45 = Int('wtraj_3_45')
wtraj_3_46 = Int('wtraj_3_46')
wtraj_3_47 = Int('wtraj_3_47')
wtraj_3_48 = Int('wtraj_3_48')
wtraj_3_49 = Int('wtraj_3_49')

wtraj_4_1 = Int('wtraj_4_1')
wtraj_4_2 = Int('wtraj_4_2')
wtraj_4_3 = Int('wtraj_4_3')
wtraj_4_4 = Int('wtraj_4_4')
wtraj_4_5 = Int('wtraj_4_5')
wtraj_4_6 = Int('wtraj_4_6')
wtraj_4_7 = Int('wtraj_4_7')
wtraj_4_8 = Int('wtraj_4_8')
wtraj_4_9 = Int('wtraj_4_9')
wtraj_4_10 = Int('wtraj_4_10')
wtraj_4_11 = Int('wtraj_4_11')
wtraj_4_12 = Int('wtraj_4_12')
wtraj_4_13 = Int('wtraj_4_13')
wtraj_4_14 = Int('wtraj_4_14')
wtraj_4_15 = Int('wtraj_4_15')
wtraj_4_16 = Int('wtraj_4_16')
wtraj_4_17 = Int('wtraj_4_17')
wtraj_4_18 = Int('wtraj_4_18')
wtraj_4_19 = Int('wtraj_4_19')
wtraj_4_20 = Int('wtraj_4_20')
wtraj_4_21 = Int('wtraj_4_21')
wtraj_4_22 = Int('wtraj_4_22')
wtraj_4_23 = Int('wtraj_4_23')
wtraj_4_24 = Int('wtraj_4_24')
wtraj_4_25 = Int('wtraj_4_25')
wtraj_4_26 = Int('wtraj_4_26')
wtraj_4_27 = Int('wtraj_4_27')
wtraj_4_28 = Int('wtraj_4_28')
wtraj_4_29 = Int('wtraj_4_29')
wtraj_4_30 = Int('wtraj_4_30')
wtraj_4_31 = Int('wtraj_4_31')
wtraj_4_32 = Int('wtraj_4_32')
wtraj_4_33 = Int('wtraj_4_33')
wtraj_4_34 = Int('wtraj_4_34')
wtraj_4_35 = Int('wtraj_4_35')
wtraj_4_36 = Int('wtraj_4_36')
wtraj_4_37 = Int('wtraj_4_37')
wtraj_4_38 = Int('wtraj_4_38')
wtraj_4_39 = Int('wtraj_4_39')
wtraj_4_40 = Int('wtraj_4_40')
wtraj_4_41 = Int('wtraj_4_41')
wtraj_4_42 = Int('wtraj_4_42')
wtraj_4_43 = Int('wtraj_4_43')
wtraj_4_44 = Int('wtraj_4_44')
wtraj_4_45 = Int('wtraj_4_45')
wtraj_4_46 = Int('wtraj_4_46')
wtraj_4_47 = Int('wtraj_4_47')
wtraj_4_48 = Int('wtraj_4_48')
wtraj_4_49 = Int('wtraj_4_49')


wprim_1_1 = Int('wprim_1_1')
wprim_1_2 = Int('wprim_1_2')
wprim_1_3 = Int('wprim_1_3')
wprim_1_4 = Int('wprim_1_4')
wprim_1_5 = Int('wprim_1_5')
wprim_1_6 = Int('wprim_1_6')
wprim_1_7 = Int('wprim_1_7')
wprim_1_8 = Int('wprim_1_8')
wprim_1_9 = Int('wprim_1_9')
wprim_1_10 = Int('wprim_1_10')
wprim_1_11 = Int('wprim_1_11')
wprim_1_12 = Int('wprim_1_12')
wprim_1_13 = Int('wprim_1_13')
wprim_1_14 = Int('wprim_1_14')
wprim_1_15 = Int('wprim_1_15')
wprim_1_16 = Int('wprim_1_16')
wprim_1_17 = Int('wprim_1_17')
wprim_1_18 = Int('wprim_1_18')
wprim_1_19 = Int('wprim_1_19')
wprim_1_20 = Int('wprim_1_20')
wprim_1_21 = Int('wprim_1_21')
wprim_1_22 = Int('wprim_1_22')
wprim_1_23 = Int('wprim_1_23')
wprim_1_24 = Int('wprim_1_24')
wprim_1_25 = Int('wprim_1_25')
wprim_1_26 = Int('wprim_1_26')
wprim_1_27 = Int('wprim_1_27')
wprim_1_28 = Int('wprim_1_28')
wprim_1_29 = Int('wprim_1_29')
wprim_1_30 = Int('wprim_1_30')
wprim_1_31 = Int('wprim_1_31')
wprim_1_32 = Int('wprim_1_32')
wprim_1_33 = Int('wprim_1_33')
wprim_1_34 = Int('wprim_1_34')
wprim_1_35 = Int('wprim_1_35')
wprim_1_36 = Int('wprim_1_36')
wprim_1_37 = Int('wprim_1_37')
wprim_1_38 = Int('wprim_1_38')
wprim_1_39 = Int('wprim_1_39')
wprim_1_40 = Int('wprim_1_40')
wprim_1_41 = Int('wprim_1_41')
wprim_1_42 = Int('wprim_1_42')
wprim_1_43 = Int('wprim_1_43')
wprim_1_44 = Int('wprim_1_44')
wprim_1_45 = Int('wprim_1_45')
wprim_1_46 = Int('wprim_1_46')
wprim_1_47 = Int('wprim_1_47')
wprim_1_48 = Int('wprim_1_48')
wprim_1_49 = Int('wprim_1_49')

wprim_2_1 = Int('wprim_2_1')
wprim_2_2 = Int('wprim_2_2')
wprim_2_3 = Int('wprim_2_3')
wprim_2_4 = Int('wprim_2_4')
wprim_2_5 = Int('wprim_2_5')
wprim_2_6 = Int('wprim_2_6')
wprim_2_7 = Int('wprim_2_7')
wprim_2_8 = Int('wprim_2_8')
wprim_2_9 = Int('wprim_2_9')
wprim_2_10 = Int('wprim_2_10')
wprim_2_11 = Int('wprim_2_11')
wprim_2_12 = Int('wprim_2_12')
wprim_2_13 = Int('wprim_2_13')
wprim_2_14 = Int('wprim_2_14')
wprim_2_15 = Int('wprim_2_15')
wprim_2_16 = Int('wprim_2_16')
wprim_2_17 = Int('wprim_2_17')
wprim_2_18 = Int('wprim_2_18')
wprim_2_19 = Int('wprim_2_19')
wprim_2_20 = Int('wprim_2_20')
wprim_2_21 = Int('wprim_2_21')
wprim_2_22 = Int('wprim_2_22')
wprim_2_23 = Int('wprim_2_23')
wprim_2_24 = Int('wprim_2_24')
wprim_2_25 = Int('wprim_2_25')
wprim_2_26 = Int('wprim_2_26')
wprim_2_27 = Int('wprim_2_27')
wprim_2_28 = Int('wprim_2_28')
wprim_2_29 = Int('wprim_2_29')
wprim_2_30 = Int('wprim_2_30')
wprim_2_31 = Int('wprim_2_31')
wprim_2_32 = Int('wprim_2_32')
wprim_2_33 = Int('wprim_2_33')
wprim_2_34 = Int('wprim_2_34')
wprim_2_35 = Int('wprim_2_35')
wprim_2_36 = Int('wprim_2_36')
wprim_2_37 = Int('wprim_2_37')
wprim_2_38 = Int('wprim_2_38')
wprim_2_39 = Int('wprim_2_39')
wprim_2_40 = Int('wprim_2_40')
wprim_2_41 = Int('wprim_2_41')
wprim_2_42 = Int('wprim_2_42')
wprim_2_43 = Int('wprim_2_43')
wprim_2_44 = Int('wprim_2_44')
wprim_2_45 = Int('wprim_2_45')
wprim_2_46 = Int('wprim_2_46')
wprim_2_47 = Int('wprim_2_47')
wprim_2_48 = Int('wprim_2_48')
wprim_2_49 = Int('wprim_2_49')

wprim_3_1 = Int('wprim_3_1')
wprim_3_2 = Int('wprim_3_2')
wprim_3_3 = Int('wprim_3_3')
wprim_3_4 = Int('wprim_3_4')
wprim_3_5 = Int('wprim_3_5')
wprim_3_6 = Int('wprim_3_6')
wprim_3_7 = Int('wprim_3_7')
wprim_3_8 = Int('wprim_3_8')
wprim_3_9 = Int('wprim_3_9')
wprim_3_10 = Int('wprim_3_10')
wprim_3_11 = Int('wprim_3_11')
wprim_3_12 = Int('wprim_3_12')
wprim_3_13 = Int('wprim_3_13')
wprim_3_14 = Int('wprim_3_14')
wprim_3_15 = Int('wprim_3_15')
wprim_3_16 = Int('wprim_3_16')
wprim_3_17 = Int('wprim_3_17')
wprim_3_18 = Int('wprim_3_18')
wprim_3_19 = Int('wprim_3_19')
wprim_3_20 = Int('wprim_3_20')
wprim_3_21 = Int('wprim_3_21')
wprim_3_22 = Int('wprim_3_22')
wprim_3_23 = Int('wprim_3_23')
wprim_3_24 = Int('wprim_3_24')
wprim_3_25 = Int('wprim_3_25')
wprim_3_26 = Int('wprim_3_26')
wprim_3_27 = Int('wprim_3_27')
wprim_3_28 = Int('wprim_3_28')
wprim_3_29 = Int('wprim_3_29')
wprim_3_30 = Int('wprim_3_30')
wprim_3_31 = Int('wprim_3_31')
wprim_3_32 = Int('wprim_3_32')
wprim_3_33 = Int('wprim_3_33')
wprim_3_34 = Int('wprim_3_34')
wprim_3_35 = Int('wprim_3_35')
wprim_3_36 = Int('wprim_3_36')
wprim_3_37 = Int('wprim_3_37')
wprim_3_38 = Int('wprim_3_38')
wprim_3_39 = Int('wprim_3_39')
wprim_3_40 = Int('wprim_3_40')
wprim_3_41 = Int('wprim_3_41')
wprim_3_42 = Int('wprim_3_42')
wprim_3_43 = Int('wprim_3_43')
wprim_3_44 = Int('wprim_3_44')
wprim_3_45 = Int('wprim_3_45')
wprim_3_46 = Int('wprim_3_46')
wprim_3_47 = Int('wprim_3_47')
wprim_3_48 = Int('wprim_3_48')
wprim_3_49 = Int('wprim_3_49')

wprim_4_1 = Int('wprim_4_1')
wprim_4_2 = Int('wprim_4_2')
wprim_4_3 = Int('wprim_4_3')
wprim_4_4 = Int('wprim_4_4')
wprim_4_5 = Int('wprim_4_5')
wprim_4_6 = Int('wprim_4_6')
wprim_4_7 = Int('wprim_4_7')
wprim_4_8 = Int('wprim_4_8')
wprim_4_9 = Int('wprim_4_9')
wprim_4_10 = Int('wprim_4_10')
wprim_4_11 = Int('wprim_4_11')
wprim_4_12 = Int('wprim_4_12')
wprim_4_13 = Int('wprim_4_13')
wprim_4_14 = Int('wprim_4_14')
wprim_4_15 = Int('wprim_4_15')
wprim_4_16 = Int('wprim_4_16')
wprim_4_17 = Int('wprim_4_17')
wprim_4_18 = Int('wprim_4_18')
wprim_4_19 = Int('wprim_4_19')
wprim_4_20 = Int('wprim_4_20')
wprim_4_21 = Int('wprim_4_21')
wprim_4_22 = Int('wprim_4_22')
wprim_4_23 = Int('wprim_4_23')
wprim_4_24 = Int('wprim_4_24')
wprim_4_25 = Int('wprim_4_25')
wprim_4_26 = Int('wprim_4_26')
wprim_4_27 = Int('wprim_4_27')
wprim_4_28 = Int('wprim_4_28')
wprim_4_29 = Int('wprim_4_29')
wprim_4_30 = Int('wprim_4_30')
wprim_4_31 = Int('wprim_4_31')
wprim_4_32 = Int('wprim_4_32')
wprim_4_33 = Int('wprim_4_33')
wprim_4_34 = Int('wprim_4_34')
wprim_4_35 = Int('wprim_4_35')
wprim_4_36 = Int('wprim_4_36')
wprim_4_37 = Int('wprim_4_37')
wprim_4_38 = Int('wprim_4_38')
wprim_4_39 = Int('wprim_4_39')
wprim_4_40 = Int('wprim_4_40')
wprim_4_41 = Int('wprim_4_41')
wprim_4_42 = Int('wprim_4_42')
wprim_4_43 = Int('wprim_4_43')
wprim_4_44 = Int('wprim_4_44')
wprim_4_45 = Int('wprim_4_45')
wprim_4_46 = Int('wprim_4_46')
wprim_4_47 = Int('wprim_4_47')
wprim_4_48 = Int('wprim_4_48')
wprim_4_49 = Int('wprim_4_49')


wx_1_1 = Int('wx_1_1')
wx_1_2 = Int('wx_1_2')
wx_1_3 = Int('wx_1_3')
wx_1_4 = Int('wx_1_4')
wx_1_5 = Int('wx_1_5')
wx_1_6 = Int('wx_1_6')
wx_1_7 = Int('wx_1_7')
wx_1_8 = Int('wx_1_8')
wx_1_9 = Int('wx_1_9')
wx_1_10 = Int('wx_1_10')
wx_1_11 = Int('wx_1_11')
wx_1_12 = Int('wx_1_12')
wx_1_13 = Int('wx_1_13')
wx_1_14 = Int('wx_1_14')
wx_1_15 = Int('wx_1_15')
wx_1_16 = Int('wx_1_16')
wx_1_17 = Int('wx_1_17')
wx_1_18 = Int('wx_1_18')
wx_1_19 = Int('wx_1_19')
wx_1_20 = Int('wx_1_20')
wx_1_21 = Int('wx_1_21')
wx_1_22 = Int('wx_1_22')
wx_1_23 = Int('wx_1_23')
wx_1_24 = Int('wx_1_24')
wx_1_25 = Int('wx_1_25')
wx_1_26 = Int('wx_1_26')
wx_1_27 = Int('wx_1_27')
wx_1_28 = Int('wx_1_28')
wx_1_29 = Int('wx_1_29')
wx_1_30 = Int('wx_1_30')
wx_1_31 = Int('wx_1_31')
wx_1_32 = Int('wx_1_32')
wx_1_33 = Int('wx_1_33')
wx_1_34 = Int('wx_1_34')
wx_1_35 = Int('wx_1_35')
wx_1_36 = Int('wx_1_36')
wx_1_37 = Int('wx_1_37')
wx_1_38 = Int('wx_1_38')
wx_1_39 = Int('wx_1_39')
wx_1_40 = Int('wx_1_40')
wx_1_41 = Int('wx_1_41')
wx_1_42 = Int('wx_1_42')
wx_1_43 = Int('wx_1_43')
wx_1_44 = Int('wx_1_44')
wx_1_45 = Int('wx_1_45')
wx_1_46 = Int('wx_1_46')
wx_1_47 = Int('wx_1_47')
wx_1_48 = Int('wx_1_48')
wx_1_49 = Int('wx_1_49')

wx_2_1 = Int('wx_2_1')
wx_2_2 = Int('wx_2_2')
wx_2_3 = Int('wx_2_3')
wx_2_4 = Int('wx_2_4')
wx_2_5 = Int('wx_2_5')
wx_2_6 = Int('wx_2_6')
wx_2_7 = Int('wx_2_7')
wx_2_8 = Int('wx_2_8')
wx_2_9 = Int('wx_2_9')
wx_2_10 = Int('wx_2_10')
wx_2_11 = Int('wx_2_11')
wx_2_12 = Int('wx_2_12')
wx_2_13 = Int('wx_2_13')
wx_2_14 = Int('wx_2_14')
wx_2_15 = Int('wx_2_15')
wx_2_16 = Int('wx_2_16')
wx_2_17 = Int('wx_2_17')
wx_2_18 = Int('wx_2_18')
wx_2_19 = Int('wx_2_19')
wx_2_20 = Int('wx_2_20')
wx_2_21 = Int('wx_2_21')
wx_2_22 = Int('wx_2_22')
wx_2_23 = Int('wx_2_23')
wx_2_24 = Int('wx_2_24')
wx_2_25 = Int('wx_2_25')
wx_2_26 = Int('wx_2_26')
wx_2_27 = Int('wx_2_27')
wx_2_28 = Int('wx_2_28')
wx_2_29 = Int('wx_2_29')
wx_2_30 = Int('wx_2_30')
wx_2_31 = Int('wx_2_31')
wx_2_32 = Int('wx_2_32')
wx_2_33 = Int('wx_2_33')
wx_2_34 = Int('wx_2_34')
wx_2_35 = Int('wx_2_35')
wx_2_36 = Int('wx_2_36')
wx_2_37 = Int('wx_2_37')
wx_2_38 = Int('wx_2_38')
wx_2_39 = Int('wx_2_39')
wx_2_40 = Int('wx_2_40')
wx_2_41 = Int('wx_2_41')
wx_2_42 = Int('wx_2_42')
wx_2_43 = Int('wx_2_43')
wx_2_44 = Int('wx_2_44')
wx_2_45 = Int('wx_2_45')
wx_2_46 = Int('wx_2_46')
wx_2_47 = Int('wx_2_47')
wx_2_48 = Int('wx_2_48')
wx_2_49 = Int('wx_2_49')

wx_3_1 = Int('wx_3_1')
wx_3_2 = Int('wx_3_2')
wx_3_3 = Int('wx_3_3')
wx_3_4 = Int('wx_3_4')
wx_3_5 = Int('wx_3_5')
wx_3_6 = Int('wx_3_6')
wx_3_7 = Int('wx_3_7')
wx_3_8 = Int('wx_3_8')
wx_3_9 = Int('wx_3_9')
wx_3_10 = Int('wx_3_10')
wx_3_11 = Int('wx_3_11')
wx_3_12 = Int('wx_3_12')
wx_3_13 = Int('wx_3_13')
wx_3_14 = Int('wx_3_14')
wx_3_15 = Int('wx_3_15')
wx_3_16 = Int('wx_3_16')
wx_3_17 = Int('wx_3_17')
wx_3_18 = Int('wx_3_18')
wx_3_19 = Int('wx_3_19')
wx_3_20 = Int('wx_3_20')
wx_3_21 = Int('wx_3_21')
wx_3_22 = Int('wx_3_22')
wx_3_23 = Int('wx_3_23')
wx_3_24 = Int('wx_3_24')
wx_3_25 = Int('wx_3_25')
wx_3_26 = Int('wx_3_26')
wx_3_27 = Int('wx_3_27')
wx_3_28 = Int('wx_3_28')
wx_3_29 = Int('wx_3_29')
wx_3_30 = Int('wx_3_30')
wx_3_31 = Int('wx_3_31')
wx_3_32 = Int('wx_3_32')
wx_3_33 = Int('wx_3_33')
wx_3_34 = Int('wx_3_34')
wx_3_35 = Int('wx_3_35')
wx_3_36 = Int('wx_3_36')
wx_3_37 = Int('wx_3_37')
wx_3_38 = Int('wx_3_38')
wx_3_39 = Int('wx_3_39')
wx_3_40 = Int('wx_3_40')
wx_3_41 = Int('wx_3_41')
wx_3_42 = Int('wx_3_42')
wx_3_43 = Int('wx_3_43')
wx_3_44 = Int('wx_3_44')
wx_3_45 = Int('wx_3_45')
wx_3_46 = Int('wx_3_46')
wx_3_47 = Int('wx_3_47')
wx_3_48 = Int('wx_3_48')
wx_3_49 = Int('wx_3_49')

wx_4_1 = Int('wx_4_1')
wx_4_2 = Int('wx_4_2')
wx_4_3 = Int('wx_4_3')
wx_4_4 = Int('wx_4_4')
wx_4_5 = Int('wx_4_5')
wx_4_6 = Int('wx_4_6')
wx_4_7 = Int('wx_4_7')
wx_4_8 = Int('wx_4_8')
wx_4_9 = Int('wx_4_9')
wx_4_10 = Int('wx_4_10')
wx_4_11 = Int('wx_4_11')
wx_4_12 = Int('wx_4_12')
wx_4_13 = Int('wx_4_13')
wx_4_14 = Int('wx_4_14')
wx_4_15 = Int('wx_4_15')
wx_4_16 = Int('wx_4_16')
wx_4_17 = Int('wx_4_17')
wx_4_18 = Int('wx_4_18')
wx_4_19 = Int('wx_4_19')
wx_4_20 = Int('wx_4_20')
wx_4_21 = Int('wx_4_21')
wx_4_22 = Int('wx_4_22')
wx_4_23 = Int('wx_4_23')
wx_4_24 = Int('wx_4_24')
wx_4_25 = Int('wx_4_25')
wx_4_26 = Int('wx_4_26')
wx_4_27 = Int('wx_4_27')
wx_4_28 = Int('wx_4_28')
wx_4_29 = Int('wx_4_29')
wx_4_30 = Int('wx_4_30')
wx_4_31 = Int('wx_4_31')
wx_4_32 = Int('wx_4_32')
wx_4_33 = Int('wx_4_33')
wx_4_34 = Int('wx_4_34')
wx_4_35 = Int('wx_4_35')
wx_4_36 = Int('wx_4_36')
wx_4_37 = Int('wx_4_37')
wx_4_38 = Int('wx_4_38')
wx_4_39 = Int('wx_4_39')
wx_4_40 = Int('wx_4_40')
wx_4_41 = Int('wx_4_41')
wx_4_42 = Int('wx_4_42')
wx_4_43 = Int('wx_4_43')
wx_4_44 = Int('wx_4_44')
wx_4_45 = Int('wx_4_45')
wx_4_46 = Int('wx_4_46')
wx_4_47 = Int('wx_4_47')
wx_4_48 = Int('wx_4_48')
wx_4_49 = Int('wx_4_49')


wy_1_1 = Int('wy_1_1')
wy_1_2 = Int('wy_1_2')
wy_1_3 = Int('wy_1_3')
wy_1_4 = Int('wy_1_4')
wy_1_5 = Int('wy_1_5')
wy_1_6 = Int('wy_1_6')
wy_1_7 = Int('wy_1_7')
wy_1_8 = Int('wy_1_8')
wy_1_9 = Int('wy_1_9')
wy_1_10 = Int('wy_1_10')
wy_1_11 = Int('wy_1_11')
wy_1_12 = Int('wy_1_12')
wy_1_13 = Int('wy_1_13')
wy_1_14 = Int('wy_1_14')
wy_1_15 = Int('wy_1_15')
wy_1_16 = Int('wy_1_16')
wy_1_17 = Int('wy_1_17')
wy_1_18 = Int('wy_1_18')
wy_1_19 = Int('wy_1_19')
wy_1_20 = Int('wy_1_20')
wy_1_21 = Int('wy_1_21')
wy_1_22 = Int('wy_1_22')
wy_1_23 = Int('wy_1_23')
wy_1_24 = Int('wy_1_24')
wy_1_25 = Int('wy_1_25')
wy_1_26 = Int('wy_1_26')
wy_1_27 = Int('wy_1_27')
wy_1_28 = Int('wy_1_28')
wy_1_29 = Int('wy_1_29')
wy_1_30 = Int('wy_1_30')
wy_1_31 = Int('wy_1_31')
wy_1_32 = Int('wy_1_32')
wy_1_33 = Int('wy_1_33')
wy_1_34 = Int('wy_1_34')
wy_1_35 = Int('wy_1_35')
wy_1_36 = Int('wy_1_36')
wy_1_37 = Int('wy_1_37')
wy_1_38 = Int('wy_1_38')
wy_1_39 = Int('wy_1_39')
wy_1_40 = Int('wy_1_40')
wy_1_41 = Int('wy_1_41')
wy_1_42 = Int('wy_1_42')
wy_1_43 = Int('wy_1_43')
wy_1_44 = Int('wy_1_44')
wy_1_45 = Int('wy_1_45')
wy_1_46 = Int('wy_1_46')
wy_1_47 = Int('wy_1_47')
wy_1_48 = Int('wy_1_48')
wy_1_49 = Int('wy_1_49')

wy_2_1 = Int('wy_2_1')
wy_2_2 = Int('wy_2_2')
wy_2_3 = Int('wy_2_3')
wy_2_4 = Int('wy_2_4')
wy_2_5 = Int('wy_2_5')
wy_2_6 = Int('wy_2_6')
wy_2_7 = Int('wy_2_7')
wy_2_8 = Int('wy_2_8')
wy_2_9 = Int('wy_2_9')
wy_2_10 = Int('wy_2_10')
wy_2_11 = Int('wy_2_11')
wy_2_12 = Int('wy_2_12')
wy_2_13 = Int('wy_2_13')
wy_2_14 = Int('wy_2_14')
wy_2_15 = Int('wy_2_15')
wy_2_16 = Int('wy_2_16')
wy_2_17 = Int('wy_2_17')
wy_2_18 = Int('wy_2_18')
wy_2_19 = Int('wy_2_19')
wy_2_20 = Int('wy_2_20')
wy_2_21 = Int('wy_2_21')
wy_2_22 = Int('wy_2_22')
wy_2_23 = Int('wy_2_23')
wy_2_24 = Int('wy_2_24')
wy_2_25 = Int('wy_2_25')
wy_2_26 = Int('wy_2_26')
wy_2_27 = Int('wy_2_27')
wy_2_28 = Int('wy_2_28')
wy_2_29 = Int('wy_2_29')
wy_2_30 = Int('wy_2_30')
wy_2_31 = Int('wy_2_31')
wy_2_32 = Int('wy_2_32')
wy_2_33 = Int('wy_2_33')
wy_2_34 = Int('wy_2_34')
wy_2_35 = Int('wy_2_35')
wy_2_36 = Int('wy_2_36')
wy_2_37 = Int('wy_2_37')
wy_2_38 = Int('wy_2_38')
wy_2_39 = Int('wy_2_39')
wy_2_40 = Int('wy_2_40')
wy_2_41 = Int('wy_2_41')
wy_2_42 = Int('wy_2_42')
wy_2_43 = Int('wy_2_43')
wy_2_44 = Int('wy_2_44')
wy_2_45 = Int('wy_2_45')
wy_2_46 = Int('wy_2_46')
wy_2_47 = Int('wy_2_47')
wy_2_48 = Int('wy_2_48')
wy_2_49 = Int('wy_2_49')

wy_3_1 = Int('wy_3_1')
wy_3_2 = Int('wy_3_2')
wy_3_3 = Int('wy_3_3')
wy_3_4 = Int('wy_3_4')
wy_3_5 = Int('wy_3_5')
wy_3_6 = Int('wy_3_6')
wy_3_7 = Int('wy_3_7')
wy_3_8 = Int('wy_3_8')
wy_3_9 = Int('wy_3_9')
wy_3_10 = Int('wy_3_10')
wy_3_11 = Int('wy_3_11')
wy_3_12 = Int('wy_3_12')
wy_3_13 = Int('wy_3_13')
wy_3_14 = Int('wy_3_14')
wy_3_15 = Int('wy_3_15')
wy_3_16 = Int('wy_3_16')
wy_3_17 = Int('wy_3_17')
wy_3_18 = Int('wy_3_18')
wy_3_19 = Int('wy_3_19')
wy_3_20 = Int('wy_3_20')
wy_3_21 = Int('wy_3_21')
wy_3_22 = Int('wy_3_22')
wy_3_23 = Int('wy_3_23')
wy_3_24 = Int('wy_3_24')
wy_3_25 = Int('wy_3_25')
wy_3_26 = Int('wy_3_26')
wy_3_27 = Int('wy_3_27')
wy_3_28 = Int('wy_3_28')
wy_3_29 = Int('wy_3_29')
wy_3_30 = Int('wy_3_30')
wy_3_31 = Int('wy_3_31')
wy_3_32 = Int('wy_3_32')
wy_3_33 = Int('wy_3_33')
wy_3_34 = Int('wy_3_34')
wy_3_35 = Int('wy_3_35')
wy_3_36 = Int('wy_3_36')
wy_3_37 = Int('wy_3_37')
wy_3_38 = Int('wy_3_38')
wy_3_39 = Int('wy_3_39')
wy_3_40 = Int('wy_3_40')
wy_3_41 = Int('wy_3_41')
wy_3_42 = Int('wy_3_42')
wy_3_43 = Int('wy_3_43')
wy_3_44 = Int('wy_3_44')
wy_3_45 = Int('wy_3_45')
wy_3_46 = Int('wy_3_46')
wy_3_47 = Int('wy_3_47')
wy_3_48 = Int('wy_3_48')
wy_3_49 = Int('wy_3_49')

wy_4_1 = Int('wy_4_1')
wy_4_2 = Int('wy_4_2')
wy_4_3 = Int('wy_4_3')
wy_4_4 = Int('wy_4_4')
wy_4_5 = Int('wy_4_5')
wy_4_6 = Int('wy_4_6')
wy_4_7 = Int('wy_4_7')
wy_4_8 = Int('wy_4_8')
wy_4_9 = Int('wy_4_9')
wy_4_10 = Int('wy_4_10')
wy_4_11 = Int('wy_4_11')
wy_4_12 = Int('wy_4_12')
wy_4_13 = Int('wy_4_13')
wy_4_14 = Int('wy_4_14')
wy_4_15 = Int('wy_4_15')
wy_4_16 = Int('wy_4_16')
wy_4_17 = Int('wy_4_17')
wy_4_18 = Int('wy_4_18')
wy_4_19 = Int('wy_4_19')
wy_4_20 = Int('wy_4_20')
wy_4_21 = Int('wy_4_21')
wy_4_22 = Int('wy_4_22')
wy_4_23 = Int('wy_4_23')
wy_4_24 = Int('wy_4_24')
wy_4_25 = Int('wy_4_25')
wy_4_26 = Int('wy_4_26')
wy_4_27 = Int('wy_4_27')
wy_4_28 = Int('wy_4_28')
wy_4_29 = Int('wy_4_29')
wy_4_30 = Int('wy_4_30')
wy_4_31 = Int('wy_4_31')
wy_4_32 = Int('wy_4_32')
wy_4_33 = Int('wy_4_33')
wy_4_34 = Int('wy_4_34')
wy_4_35 = Int('wy_4_35')
wy_4_36 = Int('wy_4_36')
wy_4_37 = Int('wy_4_37')
wy_4_38 = Int('wy_4_38')
wy_4_39 = Int('wy_4_39')
wy_4_40 = Int('wy_4_40')
wy_4_41 = Int('wy_4_41')
wy_4_42 = Int('wy_4_42')
wy_4_43 = Int('wy_4_43')
wy_4_44 = Int('wy_4_44')
wy_4_45 = Int('wy_4_45')
wy_4_46 = Int('wy_4_46')
wy_4_47 = Int('wy_4_47')
wy_4_48 = Int('wy_4_48')
wy_4_49 = Int('wy_4_49')


ch_1_1 = Int('ch_1_1')
ch_1_2 = Int('ch_1_2')
ch_1_3 = Int('ch_1_3')
ch_1_4 = Int('ch_1_4')
ch_1_5 = Int('ch_1_5')
ch_1_6 = Int('ch_1_6')
ch_1_7 = Int('ch_1_7')
ch_1_8 = Int('ch_1_8')
ch_1_9 = Int('ch_1_9')
ch_1_10 = Int('ch_1_10')
ch_1_11 = Int('ch_1_11')
ch_1_12 = Int('ch_1_12')
ch_1_13 = Int('ch_1_13')
ch_1_14 = Int('ch_1_14')
ch_1_15 = Int('ch_1_15')
ch_1_16 = Int('ch_1_16')
ch_1_17 = Int('ch_1_17')
ch_1_18 = Int('ch_1_18')
ch_1_19 = Int('ch_1_19')
ch_1_20 = Int('ch_1_20')
ch_1_21 = Int('ch_1_21')
ch_1_22 = Int('ch_1_22')
ch_1_23 = Int('ch_1_23')
ch_1_24 = Int('ch_1_24')
ch_1_25 = Int('ch_1_25')
ch_1_26 = Int('ch_1_26')
ch_1_27 = Int('ch_1_27')
ch_1_28 = Int('ch_1_28')
ch_1_29 = Int('ch_1_29')
ch_1_30 = Int('ch_1_30')
ch_1_31 = Int('ch_1_31')
ch_1_32 = Int('ch_1_32')
ch_1_33 = Int('ch_1_33')
ch_1_34 = Int('ch_1_34')
ch_1_35 = Int('ch_1_35')
ch_1_36 = Int('ch_1_36')
ch_1_37 = Int('ch_1_37')
ch_1_38 = Int('ch_1_38')
ch_1_39 = Int('ch_1_39')
ch_1_40 = Int('ch_1_40')
ch_1_41 = Int('ch_1_41')
ch_1_42 = Int('ch_1_42')
ch_1_43 = Int('ch_1_43')
ch_1_44 = Int('ch_1_44')
ch_1_45 = Int('ch_1_45')
ch_1_46 = Int('ch_1_46')
ch_1_47 = Int('ch_1_47')
ch_1_48 = Int('ch_1_48')
ch_1_49 = Int('ch_1_49')

ch_2_1 = Int('ch_2_1')
ch_2_2 = Int('ch_2_2')
ch_2_3 = Int('ch_2_3')
ch_2_4 = Int('ch_2_4')
ch_2_5 = Int('ch_2_5')
ch_2_6 = Int('ch_2_6')
ch_2_7 = Int('ch_2_7')
ch_2_8 = Int('ch_2_8')
ch_2_9 = Int('ch_2_9')
ch_2_10 = Int('ch_2_10')
ch_2_11 = Int('ch_2_11')
ch_2_12 = Int('ch_2_12')
ch_2_13 = Int('ch_2_13')
ch_2_14 = Int('ch_2_14')
ch_2_15 = Int('ch_2_15')
ch_2_16 = Int('ch_2_16')
ch_2_17 = Int('ch_2_17')
ch_2_18 = Int('ch_2_18')
ch_2_19 = Int('ch_2_19')
ch_2_20 = Int('ch_2_20')
ch_2_21 = Int('ch_2_21')
ch_2_22 = Int('ch_2_22')
ch_2_23 = Int('ch_2_23')
ch_2_24 = Int('ch_2_24')
ch_2_25 = Int('ch_2_25')
ch_2_26 = Int('ch_2_26')
ch_2_27 = Int('ch_2_27')
ch_2_28 = Int('ch_2_28')
ch_2_29 = Int('ch_2_29')
ch_2_30 = Int('ch_2_30')
ch_2_31 = Int('ch_2_31')
ch_2_32 = Int('ch_2_32')
ch_2_33 = Int('ch_2_33')
ch_2_34 = Int('ch_2_34')
ch_2_35 = Int('ch_2_35')
ch_2_36 = Int('ch_2_36')
ch_2_37 = Int('ch_2_37')
ch_2_38 = Int('ch_2_38')
ch_2_39 = Int('ch_2_39')
ch_2_40 = Int('ch_2_40')
ch_2_41 = Int('ch_2_41')
ch_2_42 = Int('ch_2_42')
ch_2_43 = Int('ch_2_43')
ch_2_44 = Int('ch_2_44')
ch_2_45 = Int('ch_2_45')
ch_2_46 = Int('ch_2_46')
ch_2_47 = Int('ch_2_47')
ch_2_48 = Int('ch_2_48')
ch_2_49 = Int('ch_2_49')

ch_3_1 = Int('ch_3_1')
ch_3_2 = Int('ch_3_2')
ch_3_3 = Int('ch_3_3')
ch_3_4 = Int('ch_3_4')
ch_3_5 = Int('ch_3_5')
ch_3_6 = Int('ch_3_6')
ch_3_7 = Int('ch_3_7')
ch_3_8 = Int('ch_3_8')
ch_3_9 = Int('ch_3_9')
ch_3_10 = Int('ch_3_10')
ch_3_11 = Int('ch_3_11')
ch_3_12 = Int('ch_3_12')
ch_3_13 = Int('ch_3_13')
ch_3_14 = Int('ch_3_14')
ch_3_15 = Int('ch_3_15')
ch_3_16 = Int('ch_3_16')
ch_3_17 = Int('ch_3_17')
ch_3_18 = Int('ch_3_18')
ch_3_19 = Int('ch_3_19')
ch_3_20 = Int('ch_3_20')
ch_3_21 = Int('ch_3_21')
ch_3_22 = Int('ch_3_22')
ch_3_23 = Int('ch_3_23')
ch_3_24 = Int('ch_3_24')
ch_3_25 = Int('ch_3_25')
ch_3_26 = Int('ch_3_26')
ch_3_27 = Int('ch_3_27')
ch_3_28 = Int('ch_3_28')
ch_3_29 = Int('ch_3_29')
ch_3_30 = Int('ch_3_30')
ch_3_31 = Int('ch_3_31')
ch_3_32 = Int('ch_3_32')
ch_3_33 = Int('ch_3_33')
ch_3_34 = Int('ch_3_34')
ch_3_35 = Int('ch_3_35')
ch_3_36 = Int('ch_3_36')
ch_3_37 = Int('ch_3_37')
ch_3_38 = Int('ch_3_38')
ch_3_39 = Int('ch_3_39')
ch_3_40 = Int('ch_3_40')
ch_3_41 = Int('ch_3_41')
ch_3_42 = Int('ch_3_42')
ch_3_43 = Int('ch_3_43')
ch_3_44 = Int('ch_3_44')
ch_3_45 = Int('ch_3_45')
ch_3_46 = Int('ch_3_46')
ch_3_47 = Int('ch_3_47')
ch_3_48 = Int('ch_3_48')
ch_3_49 = Int('ch_3_49')

ch_4_1 = Int('ch_4_1')
ch_4_2 = Int('ch_4_2')
ch_4_3 = Int('ch_4_3')
ch_4_4 = Int('ch_4_4')
ch_4_5 = Int('ch_4_5')
ch_4_6 = Int('ch_4_6')
ch_4_7 = Int('ch_4_7')
ch_4_8 = Int('ch_4_8')
ch_4_9 = Int('ch_4_9')
ch_4_10 = Int('ch_4_10')
ch_4_11 = Int('ch_4_11')
ch_4_12 = Int('ch_4_12')
ch_4_13 = Int('ch_4_13')
ch_4_14 = Int('ch_4_14')
ch_4_15 = Int('ch_4_15')
ch_4_16 = Int('ch_4_16')
ch_4_17 = Int('ch_4_17')
ch_4_18 = Int('ch_4_18')
ch_4_19 = Int('ch_4_19')
ch_4_20 = Int('ch_4_20')
ch_4_21 = Int('ch_4_21')
ch_4_22 = Int('ch_4_22')
ch_4_23 = Int('ch_4_23')
ch_4_24 = Int('ch_4_24')
ch_4_25 = Int('ch_4_25')
ch_4_26 = Int('ch_4_26')
ch_4_27 = Int('ch_4_27')
ch_4_28 = Int('ch_4_28')
ch_4_29 = Int('ch_4_29')
ch_4_30 = Int('ch_4_30')
ch_4_31 = Int('ch_4_31')
ch_4_32 = Int('ch_4_32')
ch_4_33 = Int('ch_4_33')
ch_4_34 = Int('ch_4_34')
ch_4_35 = Int('ch_4_35')
ch_4_36 = Int('ch_4_36')
ch_4_37 = Int('ch_4_37')
ch_4_38 = Int('ch_4_38')
ch_4_39 = Int('ch_4_39')
ch_4_40 = Int('ch_4_40')
ch_4_41 = Int('ch_4_41')
ch_4_42 = Int('ch_4_42')
ch_4_43 = Int('ch_4_43')
ch_4_44 = Int('ch_4_44')
ch_4_45 = Int('ch_4_45')
ch_4_46 = Int('ch_4_46')
ch_4_47 = Int('ch_4_47')
ch_4_48 = Int('ch_4_48')
ch_4_49 = Int('ch_4_49')


waitcount_1_1 = Int('waitcount_1_1')
waitcount_1_2 = Int('waitcount_1_2')
waitcount_1_3 = Int('waitcount_1_3')
waitcount_1_4 = Int('waitcount_1_4')
waitcount_1_5 = Int('waitcount_1_5')
waitcount_1_6 = Int('waitcount_1_6')
waitcount_1_7 = Int('waitcount_1_7')
waitcount_1_8 = Int('waitcount_1_8')
waitcount_1_9 = Int('waitcount_1_9')
waitcount_1_10 = Int('waitcount_1_10')
waitcount_1_11 = Int('waitcount_1_11')
waitcount_1_12 = Int('waitcount_1_12')
waitcount_1_13 = Int('waitcount_1_13')
waitcount_1_14 = Int('waitcount_1_14')
waitcount_1_15 = Int('waitcount_1_15')
waitcount_1_16 = Int('waitcount_1_16')
waitcount_1_17 = Int('waitcount_1_17')
waitcount_1_18 = Int('waitcount_1_18')
waitcount_1_19 = Int('waitcount_1_19')
waitcount_1_20 = Int('waitcount_1_20')
waitcount_1_21 = Int('waitcount_1_21')
waitcount_1_22 = Int('waitcount_1_22')
waitcount_1_23 = Int('waitcount_1_23')
waitcount_1_24 = Int('waitcount_1_24')
waitcount_1_25 = Int('waitcount_1_25')
waitcount_1_26 = Int('waitcount_1_26')
waitcount_1_27 = Int('waitcount_1_27')
waitcount_1_28 = Int('waitcount_1_28')
waitcount_1_29 = Int('waitcount_1_29')
waitcount_1_30 = Int('waitcount_1_30')
waitcount_1_31 = Int('waitcount_1_31')
waitcount_1_32 = Int('waitcount_1_32')
waitcount_1_33 = Int('waitcount_1_33')
waitcount_1_34 = Int('waitcount_1_34')
waitcount_1_35 = Int('waitcount_1_35')
waitcount_1_36 = Int('waitcount_1_36')
waitcount_1_37 = Int('waitcount_1_37')
waitcount_1_38 = Int('waitcount_1_38')
waitcount_1_39 = Int('waitcount_1_39')
waitcount_1_40 = Int('waitcount_1_40')
waitcount_1_41 = Int('waitcount_1_41')
waitcount_1_42 = Int('waitcount_1_42')
waitcount_1_43 = Int('waitcount_1_43')
waitcount_1_44 = Int('waitcount_1_44')
waitcount_1_45 = Int('waitcount_1_45')
waitcount_1_46 = Int('waitcount_1_46')
waitcount_1_47 = Int('waitcount_1_47')
waitcount_1_48 = Int('waitcount_1_48')
waitcount_2_1 = Int('waitcount_2_1')
waitcount_2_2 = Int('waitcount_2_2')
waitcount_2_3 = Int('waitcount_2_3')
waitcount_2_4 = Int('waitcount_2_4')
waitcount_2_5 = Int('waitcount_2_5')
waitcount_2_6 = Int('waitcount_2_6')
waitcount_2_7 = Int('waitcount_2_7')
waitcount_2_8 = Int('waitcount_2_8')
waitcount_2_9 = Int('waitcount_2_9')
waitcount_2_10 = Int('waitcount_2_10')
waitcount_2_11 = Int('waitcount_2_11')
waitcount_2_12 = Int('waitcount_2_12')
waitcount_2_13 = Int('waitcount_2_13')
waitcount_2_14 = Int('waitcount_2_14')
waitcount_2_15 = Int('waitcount_2_15')
waitcount_2_16 = Int('waitcount_2_16')
waitcount_2_17 = Int('waitcount_2_17')
waitcount_2_18 = Int('waitcount_2_18')
waitcount_2_19 = Int('waitcount_2_19')
waitcount_2_20 = Int('waitcount_2_20')
waitcount_2_21 = Int('waitcount_2_21')
waitcount_2_22 = Int('waitcount_2_22')
waitcount_2_23 = Int('waitcount_2_23')
waitcount_2_24 = Int('waitcount_2_24')
waitcount_2_25 = Int('waitcount_2_25')
waitcount_2_26 = Int('waitcount_2_26')
waitcount_2_27 = Int('waitcount_2_27')
waitcount_2_28 = Int('waitcount_2_28')
waitcount_2_29 = Int('waitcount_2_29')
waitcount_2_30 = Int('waitcount_2_30')
waitcount_2_31 = Int('waitcount_2_31')
waitcount_2_32 = Int('waitcount_2_32')
waitcount_2_33 = Int('waitcount_2_33')
waitcount_2_34 = Int('waitcount_2_34')
waitcount_2_35 = Int('waitcount_2_35')
waitcount_2_36 = Int('waitcount_2_36')
waitcount_2_37 = Int('waitcount_2_37')
waitcount_2_38 = Int('waitcount_2_38')
waitcount_2_39 = Int('waitcount_2_39')
waitcount_2_40 = Int('waitcount_2_40')
waitcount_2_41 = Int('waitcount_2_41')
waitcount_2_42 = Int('waitcount_2_42')
waitcount_2_43 = Int('waitcount_2_43')
waitcount_2_44 = Int('waitcount_2_44')
waitcount_2_45 = Int('waitcount_2_45')
waitcount_2_46 = Int('waitcount_2_46')
waitcount_2_47 = Int('waitcount_2_47')
waitcount_2_48 = Int('waitcount_2_48')
waitcount_3_1 = Int('waitcount_3_1')
waitcount_3_2 = Int('waitcount_3_2')
waitcount_3_3 = Int('waitcount_3_3')
waitcount_3_4 = Int('waitcount_3_4')
waitcount_3_5 = Int('waitcount_3_5')
waitcount_3_6 = Int('waitcount_3_6')
waitcount_3_7 = Int('waitcount_3_7')
waitcount_3_8 = Int('waitcount_3_8')
waitcount_3_9 = Int('waitcount_3_9')
waitcount_3_10 = Int('waitcount_3_10')
waitcount_3_11 = Int('waitcount_3_11')
waitcount_3_12 = Int('waitcount_3_12')
waitcount_3_13 = Int('waitcount_3_13')
waitcount_3_14 = Int('waitcount_3_14')
waitcount_3_15 = Int('waitcount_3_15')
waitcount_3_16 = Int('waitcount_3_16')
waitcount_3_17 = Int('waitcount_3_17')
waitcount_3_18 = Int('waitcount_3_18')
waitcount_3_19 = Int('waitcount_3_19')
waitcount_3_20 = Int('waitcount_3_20')
waitcount_3_21 = Int('waitcount_3_21')
waitcount_3_22 = Int('waitcount_3_22')
waitcount_3_23 = Int('waitcount_3_23')
waitcount_3_24 = Int('waitcount_3_24')
waitcount_3_25 = Int('waitcount_3_25')
waitcount_3_26 = Int('waitcount_3_26')
waitcount_3_27 = Int('waitcount_3_27')
waitcount_3_28 = Int('waitcount_3_28')
waitcount_3_29 = Int('waitcount_3_29')
waitcount_3_30 = Int('waitcount_3_30')
waitcount_3_31 = Int('waitcount_3_31')
waitcount_3_32 = Int('waitcount_3_32')
waitcount_3_33 = Int('waitcount_3_33')
waitcount_3_34 = Int('waitcount_3_34')
waitcount_3_35 = Int('waitcount_3_35')
waitcount_3_36 = Int('waitcount_3_36')
waitcount_3_37 = Int('waitcount_3_37')
waitcount_3_38 = Int('waitcount_3_38')
waitcount_3_39 = Int('waitcount_3_39')
waitcount_3_40 = Int('waitcount_3_40')
waitcount_3_41 = Int('waitcount_3_41')
waitcount_3_42 = Int('waitcount_3_42')
waitcount_3_43 = Int('waitcount_3_43')
waitcount_3_44 = Int('waitcount_3_44')
waitcount_3_45 = Int('waitcount_3_45')
waitcount_3_46 = Int('waitcount_3_46')
waitcount_3_47 = Int('waitcount_3_47')
waitcount_3_48 = Int('waitcount_3_48')
waitcount_4_1 = Int('waitcount_4_1')
waitcount_4_2 = Int('waitcount_4_2')
waitcount_4_3 = Int('waitcount_4_3')
waitcount_4_4 = Int('waitcount_4_4')
waitcount_4_5 = Int('waitcount_4_5')
waitcount_4_6 = Int('waitcount_4_6')
waitcount_4_7 = Int('waitcount_4_7')
waitcount_4_8 = Int('waitcount_4_8')
waitcount_4_9 = Int('waitcount_4_9')
waitcount_4_10 = Int('waitcount_4_10')
waitcount_4_11 = Int('waitcount_4_11')
waitcount_4_12 = Int('waitcount_4_12')
waitcount_4_13 = Int('waitcount_4_13')
waitcount_4_14 = Int('waitcount_4_14')
waitcount_4_15 = Int('waitcount_4_15')
waitcount_4_16 = Int('waitcount_4_16')
waitcount_4_17 = Int('waitcount_4_17')
waitcount_4_18 = Int('waitcount_4_18')
waitcount_4_19 = Int('waitcount_4_19')
waitcount_4_20 = Int('waitcount_4_20')
waitcount_4_21 = Int('waitcount_4_21')
waitcount_4_22 = Int('waitcount_4_22')
waitcount_4_23 = Int('waitcount_4_23')
waitcount_4_24 = Int('waitcount_4_24')
waitcount_4_25 = Int('waitcount_4_25')
waitcount_4_26 = Int('waitcount_4_26')
waitcount_4_27 = Int('waitcount_4_27')
waitcount_4_28 = Int('waitcount_4_28')
waitcount_4_29 = Int('waitcount_4_29')
waitcount_4_30 = Int('waitcount_4_30')
waitcount_4_31 = Int('waitcount_4_31')
waitcount_4_32 = Int('waitcount_4_32')
waitcount_4_33 = Int('waitcount_4_33')
waitcount_4_34 = Int('waitcount_4_34')
waitcount_4_35 = Int('waitcount_4_35')
waitcount_4_36 = Int('waitcount_4_36')
waitcount_4_37 = Int('waitcount_4_37')
waitcount_4_38 = Int('waitcount_4_38')
waitcount_4_39 = Int('waitcount_4_39')
waitcount_4_40 = Int('waitcount_4_40')
waitcount_4_41 = Int('waitcount_4_41')
waitcount_4_42 = Int('waitcount_4_42')
waitcount_4_43 = Int('waitcount_4_43')
waitcount_4_44 = Int('waitcount_4_44')
waitcount_4_45 = Int('waitcount_4_45')
waitcount_4_46 = Int('waitcount_4_46')
waitcount_4_47 = Int('waitcount_4_47')
waitcount_4_48 = Int('waitcount_4_48')

rechcount_1_1 = Int('rechcount_1_1')
rechcount_1_2 = Int('rechcount_1_2')
rechcount_1_3 = Int('rechcount_1_3')
rechcount_1_4 = Int('rechcount_1_4')
rechcount_1_5 = Int('rechcount_1_5')
rechcount_1_6 = Int('rechcount_1_6')
rechcount_1_7 = Int('rechcount_1_7')
rechcount_1_8 = Int('rechcount_1_8')
rechcount_1_9 = Int('rechcount_1_9')
rechcount_1_10 = Int('rechcount_1_10')
rechcount_1_11 = Int('rechcount_1_11')
rechcount_1_12 = Int('rechcount_1_12')
rechcount_1_13 = Int('rechcount_1_13')
rechcount_1_14 = Int('rechcount_1_14')
rechcount_1_15 = Int('rechcount_1_15')
rechcount_1_16 = Int('rechcount_1_16')
rechcount_1_17 = Int('rechcount_1_17')
rechcount_1_18 = Int('rechcount_1_18')
rechcount_1_19 = Int('rechcount_1_19')
rechcount_1_20 = Int('rechcount_1_20')
rechcount_1_21 = Int('rechcount_1_21')
rechcount_1_22 = Int('rechcount_1_22')
rechcount_1_23 = Int('rechcount_1_23')
rechcount_1_24 = Int('rechcount_1_24')
rechcount_1_25 = Int('rechcount_1_25')
rechcount_1_26 = Int('rechcount_1_26')
rechcount_1_27 = Int('rechcount_1_27')
rechcount_1_28 = Int('rechcount_1_28')
rechcount_1_29 = Int('rechcount_1_29')
rechcount_1_30 = Int('rechcount_1_30')
rechcount_1_31 = Int('rechcount_1_31')
rechcount_1_32 = Int('rechcount_1_32')
rechcount_1_33 = Int('rechcount_1_33')
rechcount_1_34 = Int('rechcount_1_34')
rechcount_1_35 = Int('rechcount_1_35')
rechcount_1_36 = Int('rechcount_1_36')
rechcount_1_37 = Int('rechcount_1_37')
rechcount_1_38 = Int('rechcount_1_38')
rechcount_1_39 = Int('rechcount_1_39')
rechcount_1_40 = Int('rechcount_1_40')
rechcount_1_41 = Int('rechcount_1_41')
rechcount_1_42 = Int('rechcount_1_42')
rechcount_1_43 = Int('rechcount_1_43')
rechcount_1_44 = Int('rechcount_1_44')
rechcount_1_45 = Int('rechcount_1_45')
rechcount_1_46 = Int('rechcount_1_46')
rechcount_1_47 = Int('rechcount_1_47')
rechcount_1_48 = Int('rechcount_1_48')
rechcount_2_1 = Int('rechcount_2_1')
rechcount_2_2 = Int('rechcount_2_2')
rechcount_2_3 = Int('rechcount_2_3')
rechcount_2_4 = Int('rechcount_2_4')
rechcount_2_5 = Int('rechcount_2_5')
rechcount_2_6 = Int('rechcount_2_6')
rechcount_2_7 = Int('rechcount_2_7')
rechcount_2_8 = Int('rechcount_2_8')
rechcount_2_9 = Int('rechcount_2_9')
rechcount_2_10 = Int('rechcount_2_10')
rechcount_2_11 = Int('rechcount_2_11')
rechcount_2_12 = Int('rechcount_2_12')
rechcount_2_13 = Int('rechcount_2_13')
rechcount_2_14 = Int('rechcount_2_14')
rechcount_2_15 = Int('rechcount_2_15')
rechcount_2_16 = Int('rechcount_2_16')
rechcount_2_17 = Int('rechcount_2_17')
rechcount_2_18 = Int('rechcount_2_18')
rechcount_2_19 = Int('rechcount_2_19')
rechcount_2_20 = Int('rechcount_2_20')
rechcount_2_21 = Int('rechcount_2_21')
rechcount_2_22 = Int('rechcount_2_22')
rechcount_2_23 = Int('rechcount_2_23')
rechcount_2_24 = Int('rechcount_2_24')
rechcount_2_25 = Int('rechcount_2_25')
rechcount_2_26 = Int('rechcount_2_26')
rechcount_2_27 = Int('rechcount_2_27')
rechcount_2_28 = Int('rechcount_2_28')
rechcount_2_29 = Int('rechcount_2_29')
rechcount_2_30 = Int('rechcount_2_30')
rechcount_2_31 = Int('rechcount_2_31')
rechcount_2_32 = Int('rechcount_2_32')
rechcount_2_33 = Int('rechcount_2_33')
rechcount_2_34 = Int('rechcount_2_34')
rechcount_2_35 = Int('rechcount_2_35')
rechcount_2_36 = Int('rechcount_2_36')
rechcount_2_37 = Int('rechcount_2_37')
rechcount_2_38 = Int('rechcount_2_38')
rechcount_2_39 = Int('rechcount_2_39')
rechcount_2_40 = Int('rechcount_2_40')
rechcount_2_41 = Int('rechcount_2_41')
rechcount_2_42 = Int('rechcount_2_42')
rechcount_2_43 = Int('rechcount_2_43')
rechcount_2_44 = Int('rechcount_2_44')
rechcount_2_45 = Int('rechcount_2_45')
rechcount_2_46 = Int('rechcount_2_46')
rechcount_2_47 = Int('rechcount_2_47')
rechcount_2_48 = Int('rechcount_2_48')
rechcount_3_1 = Int('rechcount_3_1')
rechcount_3_2 = Int('rechcount_3_2')
rechcount_3_3 = Int('rechcount_3_3')
rechcount_3_4 = Int('rechcount_3_4')
rechcount_3_5 = Int('rechcount_3_5')
rechcount_3_6 = Int('rechcount_3_6')
rechcount_3_7 = Int('rechcount_3_7')
rechcount_3_8 = Int('rechcount_3_8')
rechcount_3_9 = Int('rechcount_3_9')
rechcount_3_10 = Int('rechcount_3_10')
rechcount_3_11 = Int('rechcount_3_11')
rechcount_3_12 = Int('rechcount_3_12')
rechcount_3_13 = Int('rechcount_3_13')
rechcount_3_14 = Int('rechcount_3_14')
rechcount_3_15 = Int('rechcount_3_15')
rechcount_3_16 = Int('rechcount_3_16')
rechcount_3_17 = Int('rechcount_3_17')
rechcount_3_18 = Int('rechcount_3_18')
rechcount_3_19 = Int('rechcount_3_19')
rechcount_3_20 = Int('rechcount_3_20')
rechcount_3_21 = Int('rechcount_3_21')
rechcount_3_22 = Int('rechcount_3_22')
rechcount_3_23 = Int('rechcount_3_23')
rechcount_3_24 = Int('rechcount_3_24')
rechcount_3_25 = Int('rechcount_3_25')
rechcount_3_26 = Int('rechcount_3_26')
rechcount_3_27 = Int('rechcount_3_27')
rechcount_3_28 = Int('rechcount_3_28')
rechcount_3_29 = Int('rechcount_3_29')
rechcount_3_30 = Int('rechcount_3_30')
rechcount_3_31 = Int('rechcount_3_31')
rechcount_3_32 = Int('rechcount_3_32')
rechcount_3_33 = Int('rechcount_3_33')
rechcount_3_34 = Int('rechcount_3_34')
rechcount_3_35 = Int('rechcount_3_35')
rechcount_3_36 = Int('rechcount_3_36')
rechcount_3_37 = Int('rechcount_3_37')
rechcount_3_38 = Int('rechcount_3_38')
rechcount_3_39 = Int('rechcount_3_39')
rechcount_3_40 = Int('rechcount_3_40')
rechcount_3_41 = Int('rechcount_3_41')
rechcount_3_42 = Int('rechcount_3_42')
rechcount_3_43 = Int('rechcount_3_43')
rechcount_3_44 = Int('rechcount_3_44')
rechcount_3_45 = Int('rechcount_3_45')
rechcount_3_46 = Int('rechcount_3_46')
rechcount_3_47 = Int('rechcount_3_47')
rechcount_3_48 = Int('rechcount_3_48')
rechcount_4_1 = Int('rechcount_4_1')
rechcount_4_2 = Int('rechcount_4_2')
rechcount_4_3 = Int('rechcount_4_3')
rechcount_4_4 = Int('rechcount_4_4')
rechcount_4_5 = Int('rechcount_4_5')
rechcount_4_6 = Int('rechcount_4_6')
rechcount_4_7 = Int('rechcount_4_7')
rechcount_4_8 = Int('rechcount_4_8')
rechcount_4_9 = Int('rechcount_4_9')
rechcount_4_10 = Int('rechcount_4_10')
rechcount_4_11 = Int('rechcount_4_11')
rechcount_4_12 = Int('rechcount_4_12')
rechcount_4_13 = Int('rechcount_4_13')
rechcount_4_14 = Int('rechcount_4_14')
rechcount_4_15 = Int('rechcount_4_15')
rechcount_4_16 = Int('rechcount_4_16')
rechcount_4_17 = Int('rechcount_4_17')
rechcount_4_18 = Int('rechcount_4_18')
rechcount_4_19 = Int('rechcount_4_19')
rechcount_4_20 = Int('rechcount_4_20')
rechcount_4_21 = Int('rechcount_4_21')
rechcount_4_22 = Int('rechcount_4_22')
rechcount_4_23 = Int('rechcount_4_23')
rechcount_4_24 = Int('rechcount_4_24')
rechcount_4_25 = Int('rechcount_4_25')
rechcount_4_26 = Int('rechcount_4_26')
rechcount_4_27 = Int('rechcount_4_27')
rechcount_4_28 = Int('rechcount_4_28')
rechcount_4_29 = Int('rechcount_4_29')
rechcount_4_30 = Int('rechcount_4_30')
rechcount_4_31 = Int('rechcount_4_31')
rechcount_4_32 = Int('rechcount_4_32')
rechcount_4_33 = Int('rechcount_4_33')
rechcount_4_34 = Int('rechcount_4_34')
rechcount_4_35 = Int('rechcount_4_35')
rechcount_4_36 = Int('rechcount_4_36')
rechcount_4_37 = Int('rechcount_4_37')
rechcount_4_38 = Int('rechcount_4_38')
rechcount_4_39 = Int('rechcount_4_39')
rechcount_4_40 = Int('rechcount_4_40')
rechcount_4_41 = Int('rechcount_4_41')
rechcount_4_42 = Int('rechcount_4_42')
rechcount_4_43 = Int('rechcount_4_43')
rechcount_4_44 = Int('rechcount_4_44')
rechcount_4_45 = Int('rechcount_4_45')
rechcount_4_46 = Int('rechcount_4_46')
rechcount_4_47 = Int('rechcount_4_47')
rechcount_4_48 = Int('rechcount_4_48')

rechassigned_1_1 = Int('rechassigned_1_1')
rechassigned_1_2 = Int('rechassigned_1_2')
rechassigned_1_3 = Int('rechassigned_1_3')
rechassigned_1_4 = Int('rechassigned_1_4')
rechassigned_1_5 = Int('rechassigned_1_5')
rechassigned_1_6 = Int('rechassigned_1_6')
rechassigned_1_7 = Int('rechassigned_1_7')
rechassigned_1_8 = Int('rechassigned_1_8')
rechassigned_1_9 = Int('rechassigned_1_9')
rechassigned_1_10 = Int('rechassigned_1_10')
rechassigned_1_11 = Int('rechassigned_1_11')
rechassigned_1_12 = Int('rechassigned_1_12')
rechassigned_1_13 = Int('rechassigned_1_13')
rechassigned_1_14 = Int('rechassigned_1_14')
rechassigned_1_15 = Int('rechassigned_1_15')
rechassigned_1_16 = Int('rechassigned_1_16')
rechassigned_1_17 = Int('rechassigned_1_17')
rechassigned_1_18 = Int('rechassigned_1_18')
rechassigned_1_19 = Int('rechassigned_1_19')
rechassigned_1_20 = Int('rechassigned_1_20')
rechassigned_1_21 = Int('rechassigned_1_21')
rechassigned_1_22 = Int('rechassigned_1_22')
rechassigned_1_23 = Int('rechassigned_1_23')
rechassigned_1_24 = Int('rechassigned_1_24')
rechassigned_1_25 = Int('rechassigned_1_25')
rechassigned_1_26 = Int('rechassigned_1_26')
rechassigned_1_27 = Int('rechassigned_1_27')
rechassigned_1_28 = Int('rechassigned_1_28')
rechassigned_1_29 = Int('rechassigned_1_29')
rechassigned_1_30 = Int('rechassigned_1_30')
rechassigned_1_31 = Int('rechassigned_1_31')
rechassigned_1_32 = Int('rechassigned_1_32')
rechassigned_1_33 = Int('rechassigned_1_33')
rechassigned_1_34 = Int('rechassigned_1_34')
rechassigned_1_35 = Int('rechassigned_1_35')
rechassigned_1_36 = Int('rechassigned_1_36')
rechassigned_1_37 = Int('rechassigned_1_37')
rechassigned_1_38 = Int('rechassigned_1_38')
rechassigned_1_39 = Int('rechassigned_1_39')
rechassigned_1_40 = Int('rechassigned_1_40')
rechassigned_1_41 = Int('rechassigned_1_41')
rechassigned_1_42 = Int('rechassigned_1_42')
rechassigned_1_43 = Int('rechassigned_1_43')
rechassigned_1_44 = Int('rechassigned_1_44')
rechassigned_1_45 = Int('rechassigned_1_45')
rechassigned_1_46 = Int('rechassigned_1_46')
rechassigned_1_47 = Int('rechassigned_1_47')
rechassigned_1_48 = Int('rechassigned_1_48')
rechassigned_2_1 = Int('rechassigned_2_1')
rechassigned_2_2 = Int('rechassigned_2_2')
rechassigned_2_3 = Int('rechassigned_2_3')
rechassigned_2_4 = Int('rechassigned_2_4')
rechassigned_2_5 = Int('rechassigned_2_5')
rechassigned_2_6 = Int('rechassigned_2_6')
rechassigned_2_7 = Int('rechassigned_2_7')
rechassigned_2_8 = Int('rechassigned_2_8')
rechassigned_2_9 = Int('rechassigned_2_9')
rechassigned_2_10 = Int('rechassigned_2_10')
rechassigned_2_11 = Int('rechassigned_2_11')
rechassigned_2_12 = Int('rechassigned_2_12')
rechassigned_2_13 = Int('rechassigned_2_13')
rechassigned_2_14 = Int('rechassigned_2_14')
rechassigned_2_15 = Int('rechassigned_2_15')
rechassigned_2_16 = Int('rechassigned_2_16')
rechassigned_2_17 = Int('rechassigned_2_17')
rechassigned_2_18 = Int('rechassigned_2_18')
rechassigned_2_19 = Int('rechassigned_2_19')
rechassigned_2_20 = Int('rechassigned_2_20')
rechassigned_2_21 = Int('rechassigned_2_21')
rechassigned_2_22 = Int('rechassigned_2_22')
rechassigned_2_23 = Int('rechassigned_2_23')
rechassigned_2_24 = Int('rechassigned_2_24')
rechassigned_2_25 = Int('rechassigned_2_25')
rechassigned_2_26 = Int('rechassigned_2_26')
rechassigned_2_27 = Int('rechassigned_2_27')
rechassigned_2_28 = Int('rechassigned_2_28')
rechassigned_2_29 = Int('rechassigned_2_29')
rechassigned_2_30 = Int('rechassigned_2_30')
rechassigned_2_31 = Int('rechassigned_2_31')
rechassigned_2_32 = Int('rechassigned_2_32')
rechassigned_2_33 = Int('rechassigned_2_33')
rechassigned_2_34 = Int('rechassigned_2_34')
rechassigned_2_35 = Int('rechassigned_2_35')
rechassigned_2_36 = Int('rechassigned_2_36')
rechassigned_2_37 = Int('rechassigned_2_37')
rechassigned_2_38 = Int('rechassigned_2_38')
rechassigned_2_39 = Int('rechassigned_2_39')
rechassigned_2_40 = Int('rechassigned_2_40')
rechassigned_2_41 = Int('rechassigned_2_41')
rechassigned_2_42 = Int('rechassigned_2_42')
rechassigned_2_43 = Int('rechassigned_2_43')
rechassigned_2_44 = Int('rechassigned_2_44')
rechassigned_2_45 = Int('rechassigned_2_45')
rechassigned_2_46 = Int('rechassigned_2_46')
rechassigned_2_47 = Int('rechassigned_2_47')
rechassigned_2_48 = Int('rechassigned_2_48')
rechassigned_3_1 = Int('rechassigned_3_1')
rechassigned_3_2 = Int('rechassigned_3_2')
rechassigned_3_3 = Int('rechassigned_3_3')
rechassigned_3_4 = Int('rechassigned_3_4')
rechassigned_3_5 = Int('rechassigned_3_5')
rechassigned_3_6 = Int('rechassigned_3_6')
rechassigned_3_7 = Int('rechassigned_3_7')
rechassigned_3_8 = Int('rechassigned_3_8')
rechassigned_3_9 = Int('rechassigned_3_9')
rechassigned_3_10 = Int('rechassigned_3_10')
rechassigned_3_11 = Int('rechassigned_3_11')
rechassigned_3_12 = Int('rechassigned_3_12')
rechassigned_3_13 = Int('rechassigned_3_13')
rechassigned_3_14 = Int('rechassigned_3_14')
rechassigned_3_15 = Int('rechassigned_3_15')
rechassigned_3_16 = Int('rechassigned_3_16')
rechassigned_3_17 = Int('rechassigned_3_17')
rechassigned_3_18 = Int('rechassigned_3_18')
rechassigned_3_19 = Int('rechassigned_3_19')
rechassigned_3_20 = Int('rechassigned_3_20')
rechassigned_3_21 = Int('rechassigned_3_21')
rechassigned_3_22 = Int('rechassigned_3_22')
rechassigned_3_23 = Int('rechassigned_3_23')
rechassigned_3_24 = Int('rechassigned_3_24')
rechassigned_3_25 = Int('rechassigned_3_25')
rechassigned_3_26 = Int('rechassigned_3_26')
rechassigned_3_27 = Int('rechassigned_3_27')
rechassigned_3_28 = Int('rechassigned_3_28')
rechassigned_3_29 = Int('rechassigned_3_29')
rechassigned_3_30 = Int('rechassigned_3_30')
rechassigned_3_31 = Int('rechassigned_3_31')
rechassigned_3_32 = Int('rechassigned_3_32')
rechassigned_3_33 = Int('rechassigned_3_33')
rechassigned_3_34 = Int('rechassigned_3_34')
rechassigned_3_35 = Int('rechassigned_3_35')
rechassigned_3_36 = Int('rechassigned_3_36')
rechassigned_3_37 = Int('rechassigned_3_37')
rechassigned_3_38 = Int('rechassigned_3_38')
rechassigned_3_39 = Int('rechassigned_3_39')
rechassigned_3_40 = Int('rechassigned_3_40')
rechassigned_3_41 = Int('rechassigned_3_41')
rechassigned_3_42 = Int('rechassigned_3_42')
rechassigned_3_43 = Int('rechassigned_3_43')
rechassigned_3_44 = Int('rechassigned_3_44')
rechassigned_3_45 = Int('rechassigned_3_45')
rechassigned_3_46 = Int('rechassigned_3_46')
rechassigned_3_47 = Int('rechassigned_3_47')
rechassigned_3_48 = Int('rechassigned_3_48')
rechassigned_4_1 = Int('rechassigned_4_1')
rechassigned_4_2 = Int('rechassigned_4_2')
rechassigned_4_3 = Int('rechassigned_4_3')
rechassigned_4_4 = Int('rechassigned_4_4')
rechassigned_4_5 = Int('rechassigned_4_5')
rechassigned_4_6 = Int('rechassigned_4_6')
rechassigned_4_7 = Int('rechassigned_4_7')
rechassigned_4_8 = Int('rechassigned_4_8')
rechassigned_4_9 = Int('rechassigned_4_9')
rechassigned_4_10 = Int('rechassigned_4_10')
rechassigned_4_11 = Int('rechassigned_4_11')
rechassigned_4_12 = Int('rechassigned_4_12')
rechassigned_4_13 = Int('rechassigned_4_13')
rechassigned_4_14 = Int('rechassigned_4_14')
rechassigned_4_15 = Int('rechassigned_4_15')
rechassigned_4_16 = Int('rechassigned_4_16')
rechassigned_4_17 = Int('rechassigned_4_17')
rechassigned_4_18 = Int('rechassigned_4_18')
rechassigned_4_19 = Int('rechassigned_4_19')
rechassigned_4_20 = Int('rechassigned_4_20')
rechassigned_4_21 = Int('rechassigned_4_21')
rechassigned_4_22 = Int('rechassigned_4_22')
rechassigned_4_23 = Int('rechassigned_4_23')
rechassigned_4_24 = Int('rechassigned_4_24')
rechassigned_4_25 = Int('rechassigned_4_25')
rechassigned_4_26 = Int('rechassigned_4_26')
rechassigned_4_27 = Int('rechassigned_4_27')
rechassigned_4_28 = Int('rechassigned_4_28')
rechassigned_4_29 = Int('rechassigned_4_29')
rechassigned_4_30 = Int('rechassigned_4_30')
rechassigned_4_31 = Int('rechassigned_4_31')
rechassigned_4_32 = Int('rechassigned_4_32')
rechassigned_4_33 = Int('rechassigned_4_33')
rechassigned_4_34 = Int('rechassigned_4_34')
rechassigned_4_35 = Int('rechassigned_4_35')
rechassigned_4_36 = Int('rechassigned_4_36')
rechassigned_4_37 = Int('rechassigned_4_37')
rechassigned_4_38 = Int('rechassigned_4_38')
rechassigned_4_39 = Int('rechassigned_4_39')
rechassigned_4_40 = Int('rechassigned_4_40')
rechassigned_4_41 = Int('rechassigned_4_41')
rechassigned_4_42 = Int('rechassigned_4_42')
rechassigned_4_43 = Int('rechassigned_4_43')
rechassigned_4_44 = Int('rechassigned_4_44')
rechassigned_4_45 = Int('rechassigned_4_45')
rechassigned_4_46 = Int('rechassigned_4_46')
rechassigned_4_47 = Int('rechassigned_4_47')
rechassigned_4_48 = Int('rechassigned_4_48')

total_wait = Int('total_wait')
total_rech = Int('total_rech')
# declaration : constants for rechargers
obstacle = Function('obstacle', IntSort(), IntSort(), BoolSort())
rprim_1_1 = Int('rprim_1_1')
rprim_1_2 = Int('rprim_1_2')
rprim_1_3 = Int('rprim_1_3')
rprim_1_4 = Int('rprim_1_4')
rprim_1_5 = Int('rprim_1_5')
rprim_1_6 = Int('rprim_1_6')
rprim_1_7 = Int('rprim_1_7')
rprim_1_8 = Int('rprim_1_8')
rprim_1_9 = Int('rprim_1_9')
rprim_1_10 = Int('rprim_1_10')
rprim_1_11 = Int('rprim_1_11')
rprim_1_12 = Int('rprim_1_12')
rprim_1_13 = Int('rprim_1_13')
rprim_1_14 = Int('rprim_1_14')
rprim_1_15 = Int('rprim_1_15')
rprim_1_16 = Int('rprim_1_16')
rprim_1_17 = Int('rprim_1_17')
rprim_1_18 = Int('rprim_1_18')
rprim_1_19 = Int('rprim_1_19')
rprim_1_20 = Int('rprim_1_20')
rprim_1_21 = Int('rprim_1_21')
rprim_1_22 = Int('rprim_1_22')
rprim_1_23 = Int('rprim_1_23')
rprim_1_24 = Int('rprim_1_24')
rprim_1_25 = Int('rprim_1_25')
rprim_1_26 = Int('rprim_1_26')
rprim_1_27 = Int('rprim_1_27')
rprim_1_28 = Int('rprim_1_28')
rprim_1_29 = Int('rprim_1_29')
rprim_1_30 = Int('rprim_1_30')
rprim_1_31 = Int('rprim_1_31')
rprim_1_32 = Int('rprim_1_32')
rprim_1_33 = Int('rprim_1_33')
rprim_1_34 = Int('rprim_1_34')
rprim_1_35 = Int('rprim_1_35')
rprim_1_36 = Int('rprim_1_36')
rprim_1_37 = Int('rprim_1_37')
rprim_1_38 = Int('rprim_1_38')
rprim_1_39 = Int('rprim_1_39')
rprim_1_40 = Int('rprim_1_40')
rprim_1_41 = Int('rprim_1_41')
rprim_1_42 = Int('rprim_1_42')
rprim_1_43 = Int('rprim_1_43')
rprim_1_44 = Int('rprim_1_44')
rprim_1_45 = Int('rprim_1_45')
rprim_1_46 = Int('rprim_1_46')
rprim_1_47 = Int('rprim_1_47')
rprim_1_48 = Int('rprim_1_48')
rcost_1_1 = Int('rcost_1_1')
rcost_1_2 = Int('rcost_1_2')
rcost_1_3 = Int('rcost_1_3')
rcost_1_4 = Int('rcost_1_4')
rcost_1_5 = Int('rcost_1_5')
rcost_1_6 = Int('rcost_1_6')
rcost_1_7 = Int('rcost_1_7')
rcost_1_8 = Int('rcost_1_8')
rcost_1_9 = Int('rcost_1_9')
rcost_1_10 = Int('rcost_1_10')
rcost_1_11 = Int('rcost_1_11')
rcost_1_12 = Int('rcost_1_12')
rcost_1_13 = Int('rcost_1_13')
rcost_1_14 = Int('rcost_1_14')
rcost_1_15 = Int('rcost_1_15')
rcost_1_16 = Int('rcost_1_16')
rcost_1_17 = Int('rcost_1_17')
rcost_1_18 = Int('rcost_1_18')
rcost_1_19 = Int('rcost_1_19')
rcost_1_20 = Int('rcost_1_20')
rcost_1_21 = Int('rcost_1_21')
rcost_1_22 = Int('rcost_1_22')
rcost_1_23 = Int('rcost_1_23')
rcost_1_24 = Int('rcost_1_24')
rcost_1_25 = Int('rcost_1_25')
rcost_1_26 = Int('rcost_1_26')
rcost_1_27 = Int('rcost_1_27')
rcost_1_28 = Int('rcost_1_28')
rcost_1_29 = Int('rcost_1_29')
rcost_1_30 = Int('rcost_1_30')
rcost_1_31 = Int('rcost_1_31')
rcost_1_32 = Int('rcost_1_32')
rcost_1_33 = Int('rcost_1_33')
rcost_1_34 = Int('rcost_1_34')
rcost_1_35 = Int('rcost_1_35')
rcost_1_36 = Int('rcost_1_36')
rcost_1_37 = Int('rcost_1_37')
rcost_1_38 = Int('rcost_1_38')
rcost_1_39 = Int('rcost_1_39')
rcost_1_40 = Int('rcost_1_40')
rcost_1_41 = Int('rcost_1_41')
rcost_1_42 = Int('rcost_1_42')
rcost_1_43 = Int('rcost_1_43')
rcost_1_44 = Int('rcost_1_44')
rcost_1_45 = Int('rcost_1_45')
rcost_1_46 = Int('rcost_1_46')
rcost_1_47 = Int('rcost_1_47')
rcost_1_48 = Int('rcost_1_48')
rx_f_1_1 = Int('rx_f_1_1')
rx_f_1_2 = Int('rx_f_1_2')
rx_f_1_3 = Int('rx_f_1_3')
rx_f_1_4 = Int('rx_f_1_4')
rx_f_1_5 = Int('rx_f_1_5')
rx_f_1_6 = Int('rx_f_1_6')
rx_f_1_7 = Int('rx_f_1_7')
rx_f_1_8 = Int('rx_f_1_8')
rx_f_1_9 = Int('rx_f_1_9')
rx_f_1_10 = Int('rx_f_1_10')
rx_f_1_11 = Int('rx_f_1_11')
rx_f_1_12 = Int('rx_f_1_12')
rx_f_1_13 = Int('rx_f_1_13')
rx_f_1_14 = Int('rx_f_1_14')
rx_f_1_15 = Int('rx_f_1_15')
rx_f_1_16 = Int('rx_f_1_16')
rx_f_1_17 = Int('rx_f_1_17')
rx_f_1_18 = Int('rx_f_1_18')
rx_f_1_19 = Int('rx_f_1_19')
rx_f_1_20 = Int('rx_f_1_20')
rx_f_1_21 = Int('rx_f_1_21')
rx_f_1_22 = Int('rx_f_1_22')
rx_f_1_23 = Int('rx_f_1_23')
rx_f_1_24 = Int('rx_f_1_24')
rx_f_1_25 = Int('rx_f_1_25')
rx_f_1_26 = Int('rx_f_1_26')
rx_f_1_27 = Int('rx_f_1_27')
rx_f_1_28 = Int('rx_f_1_28')
rx_f_1_29 = Int('rx_f_1_29')
rx_f_1_30 = Int('rx_f_1_30')
rx_f_1_31 = Int('rx_f_1_31')
rx_f_1_32 = Int('rx_f_1_32')
rx_f_1_33 = Int('rx_f_1_33')
rx_f_1_34 = Int('rx_f_1_34')
rx_f_1_35 = Int('rx_f_1_35')
rx_f_1_36 = Int('rx_f_1_36')
rx_f_1_37 = Int('rx_f_1_37')
rx_f_1_38 = Int('rx_f_1_38')
rx_f_1_39 = Int('rx_f_1_39')
rx_f_1_40 = Int('rx_f_1_40')
rx_f_1_41 = Int('rx_f_1_41')
rx_f_1_42 = Int('rx_f_1_42')
rx_f_1_43 = Int('rx_f_1_43')
rx_f_1_44 = Int('rx_f_1_44')
rx_f_1_45 = Int('rx_f_1_45')
rx_f_1_46 = Int('rx_f_1_46')
rx_f_1_47 = Int('rx_f_1_47')
rx_f_1_48 = Int('rx_f_1_48')
ry_f_1_1 = Int('ry_f_1_1')
ry_f_1_2 = Int('ry_f_1_2')
ry_f_1_3 = Int('ry_f_1_3')
ry_f_1_4 = Int('ry_f_1_4')
ry_f_1_5 = Int('ry_f_1_5')
ry_f_1_6 = Int('ry_f_1_6')
ry_f_1_7 = Int('ry_f_1_7')
ry_f_1_8 = Int('ry_f_1_8')
ry_f_1_9 = Int('ry_f_1_9')
ry_f_1_10 = Int('ry_f_1_10')
ry_f_1_11 = Int('ry_f_1_11')
ry_f_1_12 = Int('ry_f_1_12')
ry_f_1_13 = Int('ry_f_1_13')
ry_f_1_14 = Int('ry_f_1_14')
ry_f_1_15 = Int('ry_f_1_15')
ry_f_1_16 = Int('ry_f_1_16')
ry_f_1_17 = Int('ry_f_1_17')
ry_f_1_18 = Int('ry_f_1_18')
ry_f_1_19 = Int('ry_f_1_19')
ry_f_1_20 = Int('ry_f_1_20')
ry_f_1_21 = Int('ry_f_1_21')
ry_f_1_22 = Int('ry_f_1_22')
ry_f_1_23 = Int('ry_f_1_23')
ry_f_1_24 = Int('ry_f_1_24')
ry_f_1_25 = Int('ry_f_1_25')
ry_f_1_26 = Int('ry_f_1_26')
ry_f_1_27 = Int('ry_f_1_27')
ry_f_1_28 = Int('ry_f_1_28')
ry_f_1_29 = Int('ry_f_1_29')
ry_f_1_30 = Int('ry_f_1_30')
ry_f_1_31 = Int('ry_f_1_31')
ry_f_1_32 = Int('ry_f_1_32')
ry_f_1_33 = Int('ry_f_1_33')
ry_f_1_34 = Int('ry_f_1_34')
ry_f_1_35 = Int('ry_f_1_35')
ry_f_1_36 = Int('ry_f_1_36')
ry_f_1_37 = Int('ry_f_1_37')
ry_f_1_38 = Int('ry_f_1_38')
ry_f_1_39 = Int('ry_f_1_39')
ry_f_1_40 = Int('ry_f_1_40')
ry_f_1_41 = Int('ry_f_1_41')
ry_f_1_42 = Int('ry_f_1_42')
ry_f_1_43 = Int('ry_f_1_43')
ry_f_1_44 = Int('ry_f_1_44')
ry_f_1_45 = Int('ry_f_1_45')
ry_f_1_46 = Int('ry_f_1_46')
ry_f_1_47 = Int('ry_f_1_47')
ry_f_1_48 = Int('ry_f_1_48')
rx_1_1 = Int('rx_1_1')
rx_1_2 = Int('rx_1_2')
rx_1_3 = Int('rx_1_3')
rx_1_4 = Int('rx_1_4')
rx_1_5 = Int('rx_1_5')
rx_1_6 = Int('rx_1_6')
rx_1_7 = Int('rx_1_7')
rx_1_8 = Int('rx_1_8')
rx_1_9 = Int('rx_1_9')
rx_1_10 = Int('rx_1_10')
rx_1_11 = Int('rx_1_11')
rx_1_12 = Int('rx_1_12')
rx_1_13 = Int('rx_1_13')
rx_1_14 = Int('rx_1_14')
rx_1_15 = Int('rx_1_15')
rx_1_16 = Int('rx_1_16')
rx_1_17 = Int('rx_1_17')
rx_1_18 = Int('rx_1_18')
rx_1_19 = Int('rx_1_19')
rx_1_20 = Int('rx_1_20')
rx_1_21 = Int('rx_1_21')
rx_1_22 = Int('rx_1_22')
rx_1_23 = Int('rx_1_23')
rx_1_24 = Int('rx_1_24')
rx_1_25 = Int('rx_1_25')
rx_1_26 = Int('rx_1_26')
rx_1_27 = Int('rx_1_27')
rx_1_28 = Int('rx_1_28')
rx_1_29 = Int('rx_1_29')
rx_1_30 = Int('rx_1_30')
rx_1_31 = Int('rx_1_31')
rx_1_32 = Int('rx_1_32')
rx_1_33 = Int('rx_1_33')
rx_1_34 = Int('rx_1_34')
rx_1_35 = Int('rx_1_35')
rx_1_36 = Int('rx_1_36')
rx_1_37 = Int('rx_1_37')
rx_1_38 = Int('rx_1_38')
rx_1_39 = Int('rx_1_39')
rx_1_40 = Int('rx_1_40')
rx_1_41 = Int('rx_1_41')
rx_1_42 = Int('rx_1_42')
rx_1_43 = Int('rx_1_43')
rx_1_44 = Int('rx_1_44')
rx_1_45 = Int('rx_1_45')
rx_1_46 = Int('rx_1_46')
rx_1_47 = Int('rx_1_47')
rx_1_48 = Int('rx_1_48')
rx_1_49 = Int('rx_1_49')
ry_1_1 = Int('ry_1_1')
ry_1_2 = Int('ry_1_2')
ry_1_3 = Int('ry_1_3')
ry_1_4 = Int('ry_1_4')
ry_1_5 = Int('ry_1_5')
ry_1_6 = Int('ry_1_6')
ry_1_7 = Int('ry_1_7')
ry_1_8 = Int('ry_1_8')
ry_1_9 = Int('ry_1_9')
ry_1_10 = Int('ry_1_10')
ry_1_11 = Int('ry_1_11')
ry_1_12 = Int('ry_1_12')
ry_1_13 = Int('ry_1_13')
ry_1_14 = Int('ry_1_14')
ry_1_15 = Int('ry_1_15')
ry_1_16 = Int('ry_1_16')
ry_1_17 = Int('ry_1_17')
ry_1_18 = Int('ry_1_18')
ry_1_19 = Int('ry_1_19')
ry_1_20 = Int('ry_1_20')
ry_1_21 = Int('ry_1_21')
ry_1_22 = Int('ry_1_22')
ry_1_23 = Int('ry_1_23')
ry_1_24 = Int('ry_1_24')
ry_1_25 = Int('ry_1_25')
ry_1_26 = Int('ry_1_26')
ry_1_27 = Int('ry_1_27')
ry_1_28 = Int('ry_1_28')
ry_1_29 = Int('ry_1_29')
ry_1_30 = Int('ry_1_30')
ry_1_31 = Int('ry_1_31')
ry_1_32 = Int('ry_1_32')
ry_1_33 = Int('ry_1_33')
ry_1_34 = Int('ry_1_34')
ry_1_35 = Int('ry_1_35')
ry_1_36 = Int('ry_1_36')
ry_1_37 = Int('ry_1_37')
ry_1_38 = Int('ry_1_38')
ry_1_39 = Int('ry_1_39')
ry_1_40 = Int('ry_1_40')
ry_1_41 = Int('ry_1_41')
ry_1_42 = Int('ry_1_42')
ry_1_43 = Int('ry_1_43')
ry_1_44 = Int('ry_1_44')
ry_1_45 = Int('ry_1_45')
ry_1_46 = Int('ry_1_46')
ry_1_47 = Int('ry_1_47')
ry_1_48 = Int('ry_1_48')
ry_1_49 = Int('ry_1_49')
total_rcost = Int('total_rcost')

# instantiate : instantiation of constants for workers
s.add(wtraj_1_1==1)
s.add(wtraj_2_1==1)
s.add(wtraj_3_1==1)
s.add(wtraj_4_1==1)


# instantiate : trajectory point constraints for workers
s.add(wtraj_1_2>=1, wtraj_1_2<=4)
s.add(wtraj_1_3>=1, wtraj_1_3<=4)
s.add(wtraj_1_4>=1, wtraj_1_4<=4)
s.add(wtraj_1_5>=1, wtraj_1_5<=4)
s.add(wtraj_1_6>=1, wtraj_1_6<=4)
s.add(wtraj_1_7>=1, wtraj_1_7<=4)
s.add(wtraj_1_8>=1, wtraj_1_8<=4)
s.add(wtraj_1_9>=1, wtraj_1_9<=4)
s.add(wtraj_1_10>=1, wtraj_1_10<=4)
s.add(wtraj_1_11>=1, wtraj_1_11<=4)
s.add(wtraj_1_12>=1, wtraj_1_12<=4)
s.add(wtraj_1_13>=1, wtraj_1_13<=4)
s.add(wtraj_1_14>=1, wtraj_1_14<=4)
s.add(wtraj_1_15>=1, wtraj_1_15<=4)
s.add(wtraj_1_16>=1, wtraj_1_16<=4)
s.add(wtraj_1_17>=1, wtraj_1_17<=4)
s.add(wtraj_1_18>=1, wtraj_1_18<=4)
s.add(wtraj_1_19>=1, wtraj_1_19<=4)
s.add(wtraj_1_20>=1, wtraj_1_20<=4)
s.add(wtraj_1_21>=1, wtraj_1_21<=4)
s.add(wtraj_1_22>=1, wtraj_1_22<=4)
s.add(wtraj_1_23>=1, wtraj_1_23<=4)
s.add(wtraj_1_24>=1, wtraj_1_24<=4)
s.add(wtraj_1_25>=1, wtraj_1_25<=4)
s.add(wtraj_1_26>=1, wtraj_1_26<=4)
s.add(wtraj_1_27>=1, wtraj_1_27<=4)
s.add(wtraj_1_28>=1, wtraj_1_28<=4)
s.add(wtraj_1_29>=1, wtraj_1_29<=4)
s.add(wtraj_1_30>=1, wtraj_1_30<=4)
s.add(wtraj_1_31>=1, wtraj_1_31<=4)
s.add(wtraj_1_32>=1, wtraj_1_32<=4)
s.add(wtraj_1_33>=1, wtraj_1_33<=4)
s.add(wtraj_1_34>=1, wtraj_1_34<=4)
s.add(wtraj_1_35>=1, wtraj_1_35<=4)
s.add(wtraj_1_36>=1, wtraj_1_36<=4)
s.add(wtraj_1_37>=1, wtraj_1_37<=4)
s.add(wtraj_1_38>=1, wtraj_1_38<=4)
s.add(wtraj_1_39>=1, wtraj_1_39<=4)
s.add(wtraj_1_40>=1, wtraj_1_40<=4)
s.add(wtraj_1_41>=1, wtraj_1_41<=4)
s.add(wtraj_1_42>=1, wtraj_1_42<=4)
s.add(wtraj_1_43>=1, wtraj_1_43<=4)
s.add(wtraj_1_44>=1, wtraj_1_44<=4)
s.add(wtraj_1_45>=1, wtraj_1_45<=4)
s.add(wtraj_1_46>=1, wtraj_1_46<=4)
s.add(wtraj_1_47>=1, wtraj_1_47<=4)
s.add(wtraj_1_48>=1, wtraj_1_48<=4)
s.add(wtraj_1_49>=1, wtraj_1_49<=4)
s.add(wtraj_2_2>=1, wtraj_2_2<=6)
s.add(wtraj_2_3>=1, wtraj_2_3<=6)
s.add(wtraj_2_4>=1, wtraj_2_4<=6)
s.add(wtraj_2_5>=1, wtraj_2_5<=6)
s.add(wtraj_2_6>=1, wtraj_2_6<=6)
s.add(wtraj_2_7>=1, wtraj_2_7<=6)
s.add(wtraj_2_8>=1, wtraj_2_8<=6)
s.add(wtraj_2_9>=1, wtraj_2_9<=6)
s.add(wtraj_2_10>=1, wtraj_2_10<=6)
s.add(wtraj_2_11>=1, wtraj_2_11<=6)
s.add(wtraj_2_12>=1, wtraj_2_12<=6)
s.add(wtraj_2_13>=1, wtraj_2_13<=6)
s.add(wtraj_2_14>=1, wtraj_2_14<=6)
s.add(wtraj_2_15>=1, wtraj_2_15<=6)
s.add(wtraj_2_16>=1, wtraj_2_16<=6)
s.add(wtraj_2_17>=1, wtraj_2_17<=6)
s.add(wtraj_2_18>=1, wtraj_2_18<=6)
s.add(wtraj_2_19>=1, wtraj_2_19<=6)
s.add(wtraj_2_20>=1, wtraj_2_20<=6)
s.add(wtraj_2_21>=1, wtraj_2_21<=6)
s.add(wtraj_2_22>=1, wtraj_2_22<=6)
s.add(wtraj_2_23>=1, wtraj_2_23<=6)
s.add(wtraj_2_24>=1, wtraj_2_24<=6)
s.add(wtraj_2_25>=1, wtraj_2_25<=6)
s.add(wtraj_2_26>=1, wtraj_2_26<=6)
s.add(wtraj_2_27>=1, wtraj_2_27<=6)
s.add(wtraj_2_28>=1, wtraj_2_28<=6)
s.add(wtraj_2_29>=1, wtraj_2_29<=6)
s.add(wtraj_2_30>=1, wtraj_2_30<=6)
s.add(wtraj_2_31>=1, wtraj_2_31<=6)
s.add(wtraj_2_32>=1, wtraj_2_32<=6)
s.add(wtraj_2_33>=1, wtraj_2_33<=6)
s.add(wtraj_2_34>=1, wtraj_2_34<=6)
s.add(wtraj_2_35>=1, wtraj_2_35<=6)
s.add(wtraj_2_36>=1, wtraj_2_36<=6)
s.add(wtraj_2_37>=1, wtraj_2_37<=6)
s.add(wtraj_2_38>=1, wtraj_2_38<=6)
s.add(wtraj_2_39>=1, wtraj_2_39<=6)
s.add(wtraj_2_40>=1, wtraj_2_40<=6)
s.add(wtraj_2_41>=1, wtraj_2_41<=6)
s.add(wtraj_2_42>=1, wtraj_2_42<=6)
s.add(wtraj_2_43>=1, wtraj_2_43<=6)
s.add(wtraj_2_44>=1, wtraj_2_44<=6)
s.add(wtraj_2_45>=1, wtraj_2_45<=6)
s.add(wtraj_2_46>=1, wtraj_2_46<=6)
s.add(wtraj_2_47>=1, wtraj_2_47<=6)
s.add(wtraj_2_48>=1, wtraj_2_48<=6)
s.add(wtraj_2_49>=1, wtraj_2_49<=6)
s.add(wtraj_3_2>=1, wtraj_3_2<=4)
s.add(wtraj_3_3>=1, wtraj_3_3<=4)
s.add(wtraj_3_4>=1, wtraj_3_4<=4)
s.add(wtraj_3_5>=1, wtraj_3_5<=4)
s.add(wtraj_3_6>=1, wtraj_3_6<=4)
s.add(wtraj_3_7>=1, wtraj_3_7<=4)
s.add(wtraj_3_8>=1, wtraj_3_8<=4)
s.add(wtraj_3_9>=1, wtraj_3_9<=4)
s.add(wtraj_3_10>=1, wtraj_3_10<=4)
s.add(wtraj_3_11>=1, wtraj_3_11<=4)
s.add(wtraj_3_12>=1, wtraj_3_12<=4)
s.add(wtraj_3_13>=1, wtraj_3_13<=4)
s.add(wtraj_3_14>=1, wtraj_3_14<=4)
s.add(wtraj_3_15>=1, wtraj_3_15<=4)
s.add(wtraj_3_16>=1, wtraj_3_16<=4)
s.add(wtraj_3_17>=1, wtraj_3_17<=4)
s.add(wtraj_3_18>=1, wtraj_3_18<=4)
s.add(wtraj_3_19>=1, wtraj_3_19<=4)
s.add(wtraj_3_20>=1, wtraj_3_20<=4)
s.add(wtraj_3_21>=1, wtraj_3_21<=4)
s.add(wtraj_3_22>=1, wtraj_3_22<=4)
s.add(wtraj_3_23>=1, wtraj_3_23<=4)
s.add(wtraj_3_24>=1, wtraj_3_24<=4)
s.add(wtraj_3_25>=1, wtraj_3_25<=4)
s.add(wtraj_3_26>=1, wtraj_3_26<=4)
s.add(wtraj_3_27>=1, wtraj_3_27<=4)
s.add(wtraj_3_28>=1, wtraj_3_28<=4)
s.add(wtraj_3_29>=1, wtraj_3_29<=4)
s.add(wtraj_3_30>=1, wtraj_3_30<=4)
s.add(wtraj_3_31>=1, wtraj_3_31<=4)
s.add(wtraj_3_32>=1, wtraj_3_32<=4)
s.add(wtraj_3_33>=1, wtraj_3_33<=4)
s.add(wtraj_3_34>=1, wtraj_3_34<=4)
s.add(wtraj_3_35>=1, wtraj_3_35<=4)
s.add(wtraj_3_36>=1, wtraj_3_36<=4)
s.add(wtraj_3_37>=1, wtraj_3_37<=4)
s.add(wtraj_3_38>=1, wtraj_3_38<=4)
s.add(wtraj_3_39>=1, wtraj_3_39<=4)
s.add(wtraj_3_40>=1, wtraj_3_40<=4)
s.add(wtraj_3_41>=1, wtraj_3_41<=4)
s.add(wtraj_3_42>=1, wtraj_3_42<=4)
s.add(wtraj_3_43>=1, wtraj_3_43<=4)
s.add(wtraj_3_44>=1, wtraj_3_44<=4)
s.add(wtraj_3_45>=1, wtraj_3_45<=4)
s.add(wtraj_3_46>=1, wtraj_3_46<=4)
s.add(wtraj_3_47>=1, wtraj_3_47<=4)
s.add(wtraj_3_48>=1, wtraj_3_48<=4)
s.add(wtraj_3_49>=1, wtraj_3_49<=4)
s.add(wtraj_4_2>=1, wtraj_4_2<=6)
s.add(wtraj_4_3>=1, wtraj_4_3<=6)
s.add(wtraj_4_4>=1, wtraj_4_4<=6)
s.add(wtraj_4_5>=1, wtraj_4_5<=6)
s.add(wtraj_4_6>=1, wtraj_4_6<=6)
s.add(wtraj_4_7>=1, wtraj_4_7<=6)
s.add(wtraj_4_8>=1, wtraj_4_8<=6)
s.add(wtraj_4_9>=1, wtraj_4_9<=6)
s.add(wtraj_4_10>=1, wtraj_4_10<=6)
s.add(wtraj_4_11>=1, wtraj_4_11<=6)
s.add(wtraj_4_12>=1, wtraj_4_12<=6)
s.add(wtraj_4_13>=1, wtraj_4_13<=6)
s.add(wtraj_4_14>=1, wtraj_4_14<=6)
s.add(wtraj_4_15>=1, wtraj_4_15<=6)
s.add(wtraj_4_16>=1, wtraj_4_16<=6)
s.add(wtraj_4_17>=1, wtraj_4_17<=6)
s.add(wtraj_4_18>=1, wtraj_4_18<=6)
s.add(wtraj_4_19>=1, wtraj_4_19<=6)
s.add(wtraj_4_20>=1, wtraj_4_20<=6)
s.add(wtraj_4_21>=1, wtraj_4_21<=6)
s.add(wtraj_4_22>=1, wtraj_4_22<=6)
s.add(wtraj_4_23>=1, wtraj_4_23<=6)
s.add(wtraj_4_24>=1, wtraj_4_24<=6)
s.add(wtraj_4_25>=1, wtraj_4_25<=6)
s.add(wtraj_4_26>=1, wtraj_4_26<=6)
s.add(wtraj_4_27>=1, wtraj_4_27<=6)
s.add(wtraj_4_28>=1, wtraj_4_28<=6)
s.add(wtraj_4_29>=1, wtraj_4_29<=6)
s.add(wtraj_4_30>=1, wtraj_4_30<=6)
s.add(wtraj_4_31>=1, wtraj_4_31<=6)
s.add(wtraj_4_32>=1, wtraj_4_32<=6)
s.add(wtraj_4_33>=1, wtraj_4_33<=6)
s.add(wtraj_4_34>=1, wtraj_4_34<=6)
s.add(wtraj_4_35>=1, wtraj_4_35<=6)
s.add(wtraj_4_36>=1, wtraj_4_36<=6)
s.add(wtraj_4_37>=1, wtraj_4_37<=6)
s.add(wtraj_4_38>=1, wtraj_4_38<=6)
s.add(wtraj_4_39>=1, wtraj_4_39<=6)
s.add(wtraj_4_40>=1, wtraj_4_40<=6)
s.add(wtraj_4_41>=1, wtraj_4_41<=6)
s.add(wtraj_4_42>=1, wtraj_4_42<=6)
s.add(wtraj_4_43>=1, wtraj_4_43<=6)
s.add(wtraj_4_44>=1, wtraj_4_44<=6)
s.add(wtraj_4_45>=1, wtraj_4_45<=6)
s.add(wtraj_4_46>=1, wtraj_4_46<=6)
s.add(wtraj_4_47>=1, wtraj_4_47<=6)
s.add(wtraj_4_48>=1, wtraj_4_48<=6)
s.add(wtraj_4_49>=1, wtraj_4_49<=6)

# instantiate : moving/not-moving/recharging for workers
s.add(wprim_1_1>=0, wprim_1_1<=2)
s.add(wprim_1_2>=0, wprim_1_2<=2)
s.add(wprim_1_3>=0, wprim_1_3<=2)
s.add(wprim_1_4>=0, wprim_1_4<=2)
s.add(wprim_1_5>=0, wprim_1_5<=2)
s.add(wprim_1_6>=0, wprim_1_6<=2)
s.add(wprim_1_7>=0, wprim_1_7<=2)
s.add(wprim_1_8>=0, wprim_1_8<=2)
s.add(wprim_1_9>=0, wprim_1_9<=2)
s.add(wprim_1_10>=0, wprim_1_10<=2)
s.add(wprim_1_11>=0, wprim_1_11<=2)
s.add(wprim_1_12>=0, wprim_1_12<=2)
s.add(wprim_1_13>=0, wprim_1_13<=2)
s.add(wprim_1_14>=0, wprim_1_14<=2)
s.add(wprim_1_15>=0, wprim_1_15<=2)
s.add(wprim_1_16>=0, wprim_1_16<=2)
s.add(wprim_1_17>=0, wprim_1_17<=2)
s.add(wprim_1_18>=0, wprim_1_18<=2)
s.add(wprim_1_19>=0, wprim_1_19<=2)
s.add(wprim_1_20>=0, wprim_1_20<=2)
s.add(wprim_1_21>=0, wprim_1_21<=2)
s.add(wprim_1_22>=0, wprim_1_22<=2)
s.add(wprim_1_23>=0, wprim_1_23<=2)
s.add(wprim_1_24>=0, wprim_1_24<=2)
s.add(wprim_1_25>=0, wprim_1_25<=2)
s.add(wprim_1_26>=0, wprim_1_26<=2)
s.add(wprim_1_27>=0, wprim_1_27<=2)
s.add(wprim_1_28>=0, wprim_1_28<=2)
s.add(wprim_1_29>=0, wprim_1_29<=2)
s.add(wprim_1_30>=0, wprim_1_30<=2)
s.add(wprim_1_31>=0, wprim_1_31<=2)
s.add(wprim_1_32>=0, wprim_1_32<=2)
s.add(wprim_1_33>=0, wprim_1_33<=2)
s.add(wprim_1_34>=0, wprim_1_34<=2)
s.add(wprim_1_35>=0, wprim_1_35<=2)
s.add(wprim_1_36>=0, wprim_1_36<=2)
s.add(wprim_1_37>=0, wprim_1_37<=2)
s.add(wprim_1_38>=0, wprim_1_38<=2)
s.add(wprim_1_39>=0, wprim_1_39<=2)
s.add(wprim_1_40>=0, wprim_1_40<=2)
s.add(wprim_1_41>=0, wprim_1_41<=2)
s.add(wprim_1_42>=0, wprim_1_42<=2)
s.add(wprim_1_43>=0, wprim_1_43<=2)
s.add(wprim_1_44>=0, wprim_1_44<=2)
s.add(wprim_1_45>=0, wprim_1_45<=2)
s.add(wprim_1_46>=0, wprim_1_46<=2)
s.add(wprim_1_47>=0, wprim_1_47<=2)
s.add(wprim_1_48>=0, wprim_1_48<=2)
s.add(wprim_2_1>=0, wprim_2_1<=2)
s.add(wprim_2_2>=0, wprim_2_2<=2)
s.add(wprim_2_3>=0, wprim_2_3<=2)
s.add(wprim_2_4>=0, wprim_2_4<=2)
s.add(wprim_2_5>=0, wprim_2_5<=2)
s.add(wprim_2_6>=0, wprim_2_6<=2)
s.add(wprim_2_7>=0, wprim_2_7<=2)
s.add(wprim_2_8>=0, wprim_2_8<=2)
s.add(wprim_2_9>=0, wprim_2_9<=2)
s.add(wprim_2_10>=0, wprim_2_10<=2)
s.add(wprim_2_11>=0, wprim_2_11<=2)
s.add(wprim_2_12>=0, wprim_2_12<=2)
s.add(wprim_2_13>=0, wprim_2_13<=2)
s.add(wprim_2_14>=0, wprim_2_14<=2)
s.add(wprim_2_15>=0, wprim_2_15<=2)
s.add(wprim_2_16>=0, wprim_2_16<=2)
s.add(wprim_2_17>=0, wprim_2_17<=2)
s.add(wprim_2_18>=0, wprim_2_18<=2)
s.add(wprim_2_19>=0, wprim_2_19<=2)
s.add(wprim_2_20>=0, wprim_2_20<=2)
s.add(wprim_2_21>=0, wprim_2_21<=2)
s.add(wprim_2_22>=0, wprim_2_22<=2)
s.add(wprim_2_23>=0, wprim_2_23<=2)
s.add(wprim_2_24>=0, wprim_2_24<=2)
s.add(wprim_2_25>=0, wprim_2_25<=2)
s.add(wprim_2_26>=0, wprim_2_26<=2)
s.add(wprim_2_27>=0, wprim_2_27<=2)
s.add(wprim_2_28>=0, wprim_2_28<=2)
s.add(wprim_2_29>=0, wprim_2_29<=2)
s.add(wprim_2_30>=0, wprim_2_30<=2)
s.add(wprim_2_31>=0, wprim_2_31<=2)
s.add(wprim_2_32>=0, wprim_2_32<=2)
s.add(wprim_2_33>=0, wprim_2_33<=2)
s.add(wprim_2_34>=0, wprim_2_34<=2)
s.add(wprim_2_35>=0, wprim_2_35<=2)
s.add(wprim_2_36>=0, wprim_2_36<=2)
s.add(wprim_2_37>=0, wprim_2_37<=2)
s.add(wprim_2_38>=0, wprim_2_38<=2)
s.add(wprim_2_39>=0, wprim_2_39<=2)
s.add(wprim_2_40>=0, wprim_2_40<=2)
s.add(wprim_2_41>=0, wprim_2_41<=2)
s.add(wprim_2_42>=0, wprim_2_42<=2)
s.add(wprim_2_43>=0, wprim_2_43<=2)
s.add(wprim_2_44>=0, wprim_2_44<=2)
s.add(wprim_2_45>=0, wprim_2_45<=2)
s.add(wprim_2_46>=0, wprim_2_46<=2)
s.add(wprim_2_47>=0, wprim_2_47<=2)
s.add(wprim_2_48>=0, wprim_2_48<=2)
s.add(wprim_3_1>=0, wprim_3_1<=2)
s.add(wprim_3_2>=0, wprim_3_2<=2)
s.add(wprim_3_3>=0, wprim_3_3<=2)
s.add(wprim_3_4>=0, wprim_3_4<=2)
s.add(wprim_3_5>=0, wprim_3_5<=2)
s.add(wprim_3_6>=0, wprim_3_6<=2)
s.add(wprim_3_7>=0, wprim_3_7<=2)
s.add(wprim_3_8>=0, wprim_3_8<=2)
s.add(wprim_3_9>=0, wprim_3_9<=2)
s.add(wprim_3_10>=0, wprim_3_10<=2)
s.add(wprim_3_11>=0, wprim_3_11<=2)
s.add(wprim_3_12>=0, wprim_3_12<=2)
s.add(wprim_3_13>=0, wprim_3_13<=2)
s.add(wprim_3_14>=0, wprim_3_14<=2)
s.add(wprim_3_15>=0, wprim_3_15<=2)
s.add(wprim_3_16>=0, wprim_3_16<=2)
s.add(wprim_3_17>=0, wprim_3_17<=2)
s.add(wprim_3_18>=0, wprim_3_18<=2)
s.add(wprim_3_19>=0, wprim_3_19<=2)
s.add(wprim_3_20>=0, wprim_3_20<=2)
s.add(wprim_3_21>=0, wprim_3_21<=2)
s.add(wprim_3_22>=0, wprim_3_22<=2)
s.add(wprim_3_23>=0, wprim_3_23<=2)
s.add(wprim_3_24>=0, wprim_3_24<=2)
s.add(wprim_3_25>=0, wprim_3_25<=2)
s.add(wprim_3_26>=0, wprim_3_26<=2)
s.add(wprim_3_27>=0, wprim_3_27<=2)
s.add(wprim_3_28>=0, wprim_3_28<=2)
s.add(wprim_3_29>=0, wprim_3_29<=2)
s.add(wprim_3_30>=0, wprim_3_30<=2)
s.add(wprim_3_31>=0, wprim_3_31<=2)
s.add(wprim_3_32>=0, wprim_3_32<=2)
s.add(wprim_3_33>=0, wprim_3_33<=2)
s.add(wprim_3_34>=0, wprim_3_34<=2)
s.add(wprim_3_35>=0, wprim_3_35<=2)
s.add(wprim_3_36>=0, wprim_3_36<=2)
s.add(wprim_3_37>=0, wprim_3_37<=2)
s.add(wprim_3_38>=0, wprim_3_38<=2)
s.add(wprim_3_39>=0, wprim_3_39<=2)
s.add(wprim_3_40>=0, wprim_3_40<=2)
s.add(wprim_3_41>=0, wprim_3_41<=2)
s.add(wprim_3_42>=0, wprim_3_42<=2)
s.add(wprim_3_43>=0, wprim_3_43<=2)
s.add(wprim_3_44>=0, wprim_3_44<=2)
s.add(wprim_3_45>=0, wprim_3_45<=2)
s.add(wprim_3_46>=0, wprim_3_46<=2)
s.add(wprim_3_47>=0, wprim_3_47<=2)
s.add(wprim_3_48>=0, wprim_3_48<=2)
s.add(wprim_4_1>=0, wprim_4_1<=2)
s.add(wprim_4_2>=0, wprim_4_2<=2)
s.add(wprim_4_3>=0, wprim_4_3<=2)
s.add(wprim_4_4>=0, wprim_4_4<=2)
s.add(wprim_4_5>=0, wprim_4_5<=2)
s.add(wprim_4_6>=0, wprim_4_6<=2)
s.add(wprim_4_7>=0, wprim_4_7<=2)
s.add(wprim_4_8>=0, wprim_4_8<=2)
s.add(wprim_4_9>=0, wprim_4_9<=2)
s.add(wprim_4_10>=0, wprim_4_10<=2)
s.add(wprim_4_11>=0, wprim_4_11<=2)
s.add(wprim_4_12>=0, wprim_4_12<=2)
s.add(wprim_4_13>=0, wprim_4_13<=2)
s.add(wprim_4_14>=0, wprim_4_14<=2)
s.add(wprim_4_15>=0, wprim_4_15<=2)
s.add(wprim_4_16>=0, wprim_4_16<=2)
s.add(wprim_4_17>=0, wprim_4_17<=2)
s.add(wprim_4_18>=0, wprim_4_18<=2)
s.add(wprim_4_19>=0, wprim_4_19<=2)
s.add(wprim_4_20>=0, wprim_4_20<=2)
s.add(wprim_4_21>=0, wprim_4_21<=2)
s.add(wprim_4_22>=0, wprim_4_22<=2)
s.add(wprim_4_23>=0, wprim_4_23<=2)
s.add(wprim_4_24>=0, wprim_4_24<=2)
s.add(wprim_4_25>=0, wprim_4_25<=2)
s.add(wprim_4_26>=0, wprim_4_26<=2)
s.add(wprim_4_27>=0, wprim_4_27<=2)
s.add(wprim_4_28>=0, wprim_4_28<=2)
s.add(wprim_4_29>=0, wprim_4_29<=2)
s.add(wprim_4_30>=0, wprim_4_30<=2)
s.add(wprim_4_31>=0, wprim_4_31<=2)
s.add(wprim_4_32>=0, wprim_4_32<=2)
s.add(wprim_4_33>=0, wprim_4_33<=2)
s.add(wprim_4_34>=0, wprim_4_34<=2)
s.add(wprim_4_35>=0, wprim_4_35<=2)
s.add(wprim_4_36>=0, wprim_4_36<=2)
s.add(wprim_4_37>=0, wprim_4_37<=2)
s.add(wprim_4_38>=0, wprim_4_38<=2)
s.add(wprim_4_39>=0, wprim_4_39<=2)
s.add(wprim_4_40>=0, wprim_4_40<=2)
s.add(wprim_4_41>=0, wprim_4_41<=2)
s.add(wprim_4_42>=0, wprim_4_42<=2)
s.add(wprim_4_43>=0, wprim_4_43<=2)
s.add(wprim_4_44>=0, wprim_4_44<=2)
s.add(wprim_4_45>=0, wprim_4_45<=2)
s.add(wprim_4_46>=0, wprim_4_46<=2)
s.add(wprim_4_47>=0, wprim_4_47<=2)
s.add(wprim_4_48>=0, wprim_4_48<=2)

# instantiate : x-coordinate range for workers
s.add(wx_1_1>=0, wx_1_1<=18)
s.add(wx_1_2>=0, wx_1_2<=18)
s.add(wx_1_3>=0, wx_1_3<=18)
s.add(wx_1_4>=0, wx_1_4<=18)
s.add(wx_1_5>=0, wx_1_5<=18)
s.add(wx_1_6>=0, wx_1_6<=18)
s.add(wx_1_7>=0, wx_1_7<=18)
s.add(wx_1_8>=0, wx_1_8<=18)
s.add(wx_1_9>=0, wx_1_9<=18)
s.add(wx_1_10>=0, wx_1_10<=18)
s.add(wx_1_11>=0, wx_1_11<=18)
s.add(wx_1_12>=0, wx_1_12<=18)
s.add(wx_1_13>=0, wx_1_13<=18)
s.add(wx_1_14>=0, wx_1_14<=18)
s.add(wx_1_15>=0, wx_1_15<=18)
s.add(wx_1_16>=0, wx_1_16<=18)
s.add(wx_1_17>=0, wx_1_17<=18)
s.add(wx_1_18>=0, wx_1_18<=18)
s.add(wx_1_19>=0, wx_1_19<=18)
s.add(wx_1_20>=0, wx_1_20<=18)
s.add(wx_1_21>=0, wx_1_21<=18)
s.add(wx_1_22>=0, wx_1_22<=18)
s.add(wx_1_23>=0, wx_1_23<=18)
s.add(wx_1_24>=0, wx_1_24<=18)
s.add(wx_1_25>=0, wx_1_25<=18)
s.add(wx_1_26>=0, wx_1_26<=18)
s.add(wx_1_27>=0, wx_1_27<=18)
s.add(wx_1_28>=0, wx_1_28<=18)
s.add(wx_1_29>=0, wx_1_29<=18)
s.add(wx_1_30>=0, wx_1_30<=18)
s.add(wx_1_31>=0, wx_1_31<=18)
s.add(wx_1_32>=0, wx_1_32<=18)
s.add(wx_1_33>=0, wx_1_33<=18)
s.add(wx_1_34>=0, wx_1_34<=18)
s.add(wx_1_35>=0, wx_1_35<=18)
s.add(wx_1_36>=0, wx_1_36<=18)
s.add(wx_1_37>=0, wx_1_37<=18)
s.add(wx_1_38>=0, wx_1_38<=18)
s.add(wx_1_39>=0, wx_1_39<=18)
s.add(wx_1_40>=0, wx_1_40<=18)
s.add(wx_1_41>=0, wx_1_41<=18)
s.add(wx_1_42>=0, wx_1_42<=18)
s.add(wx_1_43>=0, wx_1_43<=18)
s.add(wx_1_44>=0, wx_1_44<=18)
s.add(wx_1_45>=0, wx_1_45<=18)
s.add(wx_1_46>=0, wx_1_46<=18)
s.add(wx_1_47>=0, wx_1_47<=18)
s.add(wx_1_48>=0, wx_1_48<=18)
s.add(wx_1_49>=0, wx_1_49<=18)
s.add(wx_2_1>=0, wx_2_1<=18)
s.add(wx_2_2>=0, wx_2_2<=18)
s.add(wx_2_3>=0, wx_2_3<=18)
s.add(wx_2_4>=0, wx_2_4<=18)
s.add(wx_2_5>=0, wx_2_5<=18)
s.add(wx_2_6>=0, wx_2_6<=18)
s.add(wx_2_7>=0, wx_2_7<=18)
s.add(wx_2_8>=0, wx_2_8<=18)
s.add(wx_2_9>=0, wx_2_9<=18)
s.add(wx_2_10>=0, wx_2_10<=18)
s.add(wx_2_11>=0, wx_2_11<=18)
s.add(wx_2_12>=0, wx_2_12<=18)
s.add(wx_2_13>=0, wx_2_13<=18)
s.add(wx_2_14>=0, wx_2_14<=18)
s.add(wx_2_15>=0, wx_2_15<=18)
s.add(wx_2_16>=0, wx_2_16<=18)
s.add(wx_2_17>=0, wx_2_17<=18)
s.add(wx_2_18>=0, wx_2_18<=18)
s.add(wx_2_19>=0, wx_2_19<=18)
s.add(wx_2_20>=0, wx_2_20<=18)
s.add(wx_2_21>=0, wx_2_21<=18)
s.add(wx_2_22>=0, wx_2_22<=18)
s.add(wx_2_23>=0, wx_2_23<=18)
s.add(wx_2_24>=0, wx_2_24<=18)
s.add(wx_2_25>=0, wx_2_25<=18)
s.add(wx_2_26>=0, wx_2_26<=18)
s.add(wx_2_27>=0, wx_2_27<=18)
s.add(wx_2_28>=0, wx_2_28<=18)
s.add(wx_2_29>=0, wx_2_29<=18)
s.add(wx_2_30>=0, wx_2_30<=18)
s.add(wx_2_31>=0, wx_2_31<=18)
s.add(wx_2_32>=0, wx_2_32<=18)
s.add(wx_2_33>=0, wx_2_33<=18)
s.add(wx_2_34>=0, wx_2_34<=18)
s.add(wx_2_35>=0, wx_2_35<=18)
s.add(wx_2_36>=0, wx_2_36<=18)
s.add(wx_2_37>=0, wx_2_37<=18)
s.add(wx_2_38>=0, wx_2_38<=18)
s.add(wx_2_39>=0, wx_2_39<=18)
s.add(wx_2_40>=0, wx_2_40<=18)
s.add(wx_2_41>=0, wx_2_41<=18)
s.add(wx_2_42>=0, wx_2_42<=18)
s.add(wx_2_43>=0, wx_2_43<=18)
s.add(wx_2_44>=0, wx_2_44<=18)
s.add(wx_2_45>=0, wx_2_45<=18)
s.add(wx_2_46>=0, wx_2_46<=18)
s.add(wx_2_47>=0, wx_2_47<=18)
s.add(wx_2_48>=0, wx_2_48<=18)
s.add(wx_2_49>=0, wx_2_49<=18)
s.add(wx_3_1>=0, wx_3_1<=18)
s.add(wx_3_2>=0, wx_3_2<=18)
s.add(wx_3_3>=0, wx_3_3<=18)
s.add(wx_3_4>=0, wx_3_4<=18)
s.add(wx_3_5>=0, wx_3_5<=18)
s.add(wx_3_6>=0, wx_3_6<=18)
s.add(wx_3_7>=0, wx_3_7<=18)
s.add(wx_3_8>=0, wx_3_8<=18)
s.add(wx_3_9>=0, wx_3_9<=18)
s.add(wx_3_10>=0, wx_3_10<=18)
s.add(wx_3_11>=0, wx_3_11<=18)
s.add(wx_3_12>=0, wx_3_12<=18)
s.add(wx_3_13>=0, wx_3_13<=18)
s.add(wx_3_14>=0, wx_3_14<=18)
s.add(wx_3_15>=0, wx_3_15<=18)
s.add(wx_3_16>=0, wx_3_16<=18)
s.add(wx_3_17>=0, wx_3_17<=18)
s.add(wx_3_18>=0, wx_3_18<=18)
s.add(wx_3_19>=0, wx_3_19<=18)
s.add(wx_3_20>=0, wx_3_20<=18)
s.add(wx_3_21>=0, wx_3_21<=18)
s.add(wx_3_22>=0, wx_3_22<=18)
s.add(wx_3_23>=0, wx_3_23<=18)
s.add(wx_3_24>=0, wx_3_24<=18)
s.add(wx_3_25>=0, wx_3_25<=18)
s.add(wx_3_26>=0, wx_3_26<=18)
s.add(wx_3_27>=0, wx_3_27<=18)
s.add(wx_3_28>=0, wx_3_28<=18)
s.add(wx_3_29>=0, wx_3_29<=18)
s.add(wx_3_30>=0, wx_3_30<=18)
s.add(wx_3_31>=0, wx_3_31<=18)
s.add(wx_3_32>=0, wx_3_32<=18)
s.add(wx_3_33>=0, wx_3_33<=18)
s.add(wx_3_34>=0, wx_3_34<=18)
s.add(wx_3_35>=0, wx_3_35<=18)
s.add(wx_3_36>=0, wx_3_36<=18)
s.add(wx_3_37>=0, wx_3_37<=18)
s.add(wx_3_38>=0, wx_3_38<=18)
s.add(wx_3_39>=0, wx_3_39<=18)
s.add(wx_3_40>=0, wx_3_40<=18)
s.add(wx_3_41>=0, wx_3_41<=18)
s.add(wx_3_42>=0, wx_3_42<=18)
s.add(wx_3_43>=0, wx_3_43<=18)
s.add(wx_3_44>=0, wx_3_44<=18)
s.add(wx_3_45>=0, wx_3_45<=18)
s.add(wx_3_46>=0, wx_3_46<=18)
s.add(wx_3_47>=0, wx_3_47<=18)
s.add(wx_3_48>=0, wx_3_48<=18)
s.add(wx_3_49>=0, wx_3_49<=18)
s.add(wx_4_1>=0, wx_4_1<=18)
s.add(wx_4_2>=0, wx_4_2<=18)
s.add(wx_4_3>=0, wx_4_3<=18)
s.add(wx_4_4>=0, wx_4_4<=18)
s.add(wx_4_5>=0, wx_4_5<=18)
s.add(wx_4_6>=0, wx_4_6<=18)
s.add(wx_4_7>=0, wx_4_7<=18)
s.add(wx_4_8>=0, wx_4_8<=18)
s.add(wx_4_9>=0, wx_4_9<=18)
s.add(wx_4_10>=0, wx_4_10<=18)
s.add(wx_4_11>=0, wx_4_11<=18)
s.add(wx_4_12>=0, wx_4_12<=18)
s.add(wx_4_13>=0, wx_4_13<=18)
s.add(wx_4_14>=0, wx_4_14<=18)
s.add(wx_4_15>=0, wx_4_15<=18)
s.add(wx_4_16>=0, wx_4_16<=18)
s.add(wx_4_17>=0, wx_4_17<=18)
s.add(wx_4_18>=0, wx_4_18<=18)
s.add(wx_4_19>=0, wx_4_19<=18)
s.add(wx_4_20>=0, wx_4_20<=18)
s.add(wx_4_21>=0, wx_4_21<=18)
s.add(wx_4_22>=0, wx_4_22<=18)
s.add(wx_4_23>=0, wx_4_23<=18)
s.add(wx_4_24>=0, wx_4_24<=18)
s.add(wx_4_25>=0, wx_4_25<=18)
s.add(wx_4_26>=0, wx_4_26<=18)
s.add(wx_4_27>=0, wx_4_27<=18)
s.add(wx_4_28>=0, wx_4_28<=18)
s.add(wx_4_29>=0, wx_4_29<=18)
s.add(wx_4_30>=0, wx_4_30<=18)
s.add(wx_4_31>=0, wx_4_31<=18)
s.add(wx_4_32>=0, wx_4_32<=18)
s.add(wx_4_33>=0, wx_4_33<=18)
s.add(wx_4_34>=0, wx_4_34<=18)
s.add(wx_4_35>=0, wx_4_35<=18)
s.add(wx_4_36>=0, wx_4_36<=18)
s.add(wx_4_37>=0, wx_4_37<=18)
s.add(wx_4_38>=0, wx_4_38<=18)
s.add(wx_4_39>=0, wx_4_39<=18)
s.add(wx_4_40>=0, wx_4_40<=18)
s.add(wx_4_41>=0, wx_4_41<=18)
s.add(wx_4_42>=0, wx_4_42<=18)
s.add(wx_4_43>=0, wx_4_43<=18)
s.add(wx_4_44>=0, wx_4_44<=18)
s.add(wx_4_45>=0, wx_4_45<=18)
s.add(wx_4_46>=0, wx_4_46<=18)
s.add(wx_4_47>=0, wx_4_47<=18)
s.add(wx_4_48>=0, wx_4_48<=18)
s.add(wx_4_49>=0, wx_4_49<=18)

# instantiate : y-coordinate range for workers
s.add(wy_1_1>=0, wy_1_1<=18)
s.add(wy_1_2>=0, wy_1_2<=18)
s.add(wy_1_3>=0, wy_1_3<=18)
s.add(wy_1_4>=0, wy_1_4<=18)
s.add(wy_1_5>=0, wy_1_5<=18)
s.add(wy_1_6>=0, wy_1_6<=18)
s.add(wy_1_7>=0, wy_1_7<=18)
s.add(wy_1_8>=0, wy_1_8<=18)
s.add(wy_1_9>=0, wy_1_9<=18)
s.add(wy_1_10>=0, wy_1_10<=18)
s.add(wy_1_11>=0, wy_1_11<=18)
s.add(wy_1_12>=0, wy_1_12<=18)
s.add(wy_1_13>=0, wy_1_13<=18)
s.add(wy_1_14>=0, wy_1_14<=18)
s.add(wy_1_15>=0, wy_1_15<=18)
s.add(wy_1_16>=0, wy_1_16<=18)
s.add(wy_1_17>=0, wy_1_17<=18)
s.add(wy_1_18>=0, wy_1_18<=18)
s.add(wy_1_19>=0, wy_1_19<=18)
s.add(wy_1_20>=0, wy_1_20<=18)
s.add(wy_1_21>=0, wy_1_21<=18)
s.add(wy_1_22>=0, wy_1_22<=18)
s.add(wy_1_23>=0, wy_1_23<=18)
s.add(wy_1_24>=0, wy_1_24<=18)
s.add(wy_1_25>=0, wy_1_25<=18)
s.add(wy_1_26>=0, wy_1_26<=18)
s.add(wy_1_27>=0, wy_1_27<=18)
s.add(wy_1_28>=0, wy_1_28<=18)
s.add(wy_1_29>=0, wy_1_29<=18)
s.add(wy_1_30>=0, wy_1_30<=18)
s.add(wy_1_31>=0, wy_1_31<=18)
s.add(wy_1_32>=0, wy_1_32<=18)
s.add(wy_1_33>=0, wy_1_33<=18)
s.add(wy_1_34>=0, wy_1_34<=18)
s.add(wy_1_35>=0, wy_1_35<=18)
s.add(wy_1_36>=0, wy_1_36<=18)
s.add(wy_1_37>=0, wy_1_37<=18)
s.add(wy_1_38>=0, wy_1_38<=18)
s.add(wy_1_39>=0, wy_1_39<=18)
s.add(wy_1_40>=0, wy_1_40<=18)
s.add(wy_1_41>=0, wy_1_41<=18)
s.add(wy_1_42>=0, wy_1_42<=18)
s.add(wy_1_43>=0, wy_1_43<=18)
s.add(wy_1_44>=0, wy_1_44<=18)
s.add(wy_1_45>=0, wy_1_45<=18)
s.add(wy_1_46>=0, wy_1_46<=18)
s.add(wy_1_47>=0, wy_1_47<=18)
s.add(wy_1_48>=0, wy_1_48<=18)
s.add(wy_1_49>=0, wy_1_49<=18)
s.add(wy_2_1>=0, wy_2_1<=18)
s.add(wy_2_2>=0, wy_2_2<=18)
s.add(wy_2_3>=0, wy_2_3<=18)
s.add(wy_2_4>=0, wy_2_4<=18)
s.add(wy_2_5>=0, wy_2_5<=18)
s.add(wy_2_6>=0, wy_2_6<=18)
s.add(wy_2_7>=0, wy_2_7<=18)
s.add(wy_2_8>=0, wy_2_8<=18)
s.add(wy_2_9>=0, wy_2_9<=18)
s.add(wy_2_10>=0, wy_2_10<=18)
s.add(wy_2_11>=0, wy_2_11<=18)
s.add(wy_2_12>=0, wy_2_12<=18)
s.add(wy_2_13>=0, wy_2_13<=18)
s.add(wy_2_14>=0, wy_2_14<=18)
s.add(wy_2_15>=0, wy_2_15<=18)
s.add(wy_2_16>=0, wy_2_16<=18)
s.add(wy_2_17>=0, wy_2_17<=18)
s.add(wy_2_18>=0, wy_2_18<=18)
s.add(wy_2_19>=0, wy_2_19<=18)
s.add(wy_2_20>=0, wy_2_20<=18)
s.add(wy_2_21>=0, wy_2_21<=18)
s.add(wy_2_22>=0, wy_2_22<=18)
s.add(wy_2_23>=0, wy_2_23<=18)
s.add(wy_2_24>=0, wy_2_24<=18)
s.add(wy_2_25>=0, wy_2_25<=18)
s.add(wy_2_26>=0, wy_2_26<=18)
s.add(wy_2_27>=0, wy_2_27<=18)
s.add(wy_2_28>=0, wy_2_28<=18)
s.add(wy_2_29>=0, wy_2_29<=18)
s.add(wy_2_30>=0, wy_2_30<=18)
s.add(wy_2_31>=0, wy_2_31<=18)
s.add(wy_2_32>=0, wy_2_32<=18)
s.add(wy_2_33>=0, wy_2_33<=18)
s.add(wy_2_34>=0, wy_2_34<=18)
s.add(wy_2_35>=0, wy_2_35<=18)
s.add(wy_2_36>=0, wy_2_36<=18)
s.add(wy_2_37>=0, wy_2_37<=18)
s.add(wy_2_38>=0, wy_2_38<=18)
s.add(wy_2_39>=0, wy_2_39<=18)
s.add(wy_2_40>=0, wy_2_40<=18)
s.add(wy_2_41>=0, wy_2_41<=18)
s.add(wy_2_42>=0, wy_2_42<=18)
s.add(wy_2_43>=0, wy_2_43<=18)
s.add(wy_2_44>=0, wy_2_44<=18)
s.add(wy_2_45>=0, wy_2_45<=18)
s.add(wy_2_46>=0, wy_2_46<=18)
s.add(wy_2_47>=0, wy_2_47<=18)
s.add(wy_2_48>=0, wy_2_48<=18)
s.add(wy_2_49>=0, wy_2_49<=18)
s.add(wy_3_1>=0, wy_3_1<=18)
s.add(wy_3_2>=0, wy_3_2<=18)
s.add(wy_3_3>=0, wy_3_3<=18)
s.add(wy_3_4>=0, wy_3_4<=18)
s.add(wy_3_5>=0, wy_3_5<=18)
s.add(wy_3_6>=0, wy_3_6<=18)
s.add(wy_3_7>=0, wy_3_7<=18)
s.add(wy_3_8>=0, wy_3_8<=18)
s.add(wy_3_9>=0, wy_3_9<=18)
s.add(wy_3_10>=0, wy_3_10<=18)
s.add(wy_3_11>=0, wy_3_11<=18)
s.add(wy_3_12>=0, wy_3_12<=18)
s.add(wy_3_13>=0, wy_3_13<=18)
s.add(wy_3_14>=0, wy_3_14<=18)
s.add(wy_3_15>=0, wy_3_15<=18)
s.add(wy_3_16>=0, wy_3_16<=18)
s.add(wy_3_17>=0, wy_3_17<=18)
s.add(wy_3_18>=0, wy_3_18<=18)
s.add(wy_3_19>=0, wy_3_19<=18)
s.add(wy_3_20>=0, wy_3_20<=18)
s.add(wy_3_21>=0, wy_3_21<=18)
s.add(wy_3_22>=0, wy_3_22<=18)
s.add(wy_3_23>=0, wy_3_23<=18)
s.add(wy_3_24>=0, wy_3_24<=18)
s.add(wy_3_25>=0, wy_3_25<=18)
s.add(wy_3_26>=0, wy_3_26<=18)
s.add(wy_3_27>=0, wy_3_27<=18)
s.add(wy_3_28>=0, wy_3_28<=18)
s.add(wy_3_29>=0, wy_3_29<=18)
s.add(wy_3_30>=0, wy_3_30<=18)
s.add(wy_3_31>=0, wy_3_31<=18)
s.add(wy_3_32>=0, wy_3_32<=18)
s.add(wy_3_33>=0, wy_3_33<=18)
s.add(wy_3_34>=0, wy_3_34<=18)
s.add(wy_3_35>=0, wy_3_35<=18)
s.add(wy_3_36>=0, wy_3_36<=18)
s.add(wy_3_37>=0, wy_3_37<=18)
s.add(wy_3_38>=0, wy_3_38<=18)
s.add(wy_3_39>=0, wy_3_39<=18)
s.add(wy_3_40>=0, wy_3_40<=18)
s.add(wy_3_41>=0, wy_3_41<=18)
s.add(wy_3_42>=0, wy_3_42<=18)
s.add(wy_3_43>=0, wy_3_43<=18)
s.add(wy_3_44>=0, wy_3_44<=18)
s.add(wy_3_45>=0, wy_3_45<=18)
s.add(wy_3_46>=0, wy_3_46<=18)
s.add(wy_3_47>=0, wy_3_47<=18)
s.add(wy_3_48>=0, wy_3_48<=18)
s.add(wy_3_49>=0, wy_3_49<=18)
s.add(wy_4_1>=0, wy_4_1<=18)
s.add(wy_4_2>=0, wy_4_2<=18)
s.add(wy_4_3>=0, wy_4_3<=18)
s.add(wy_4_4>=0, wy_4_4<=18)
s.add(wy_4_5>=0, wy_4_5<=18)
s.add(wy_4_6>=0, wy_4_6<=18)
s.add(wy_4_7>=0, wy_4_7<=18)
s.add(wy_4_8>=0, wy_4_8<=18)
s.add(wy_4_9>=0, wy_4_9<=18)
s.add(wy_4_10>=0, wy_4_10<=18)
s.add(wy_4_11>=0, wy_4_11<=18)
s.add(wy_4_12>=0, wy_4_12<=18)
s.add(wy_4_13>=0, wy_4_13<=18)
s.add(wy_4_14>=0, wy_4_14<=18)
s.add(wy_4_15>=0, wy_4_15<=18)
s.add(wy_4_16>=0, wy_4_16<=18)
s.add(wy_4_17>=0, wy_4_17<=18)
s.add(wy_4_18>=0, wy_4_18<=18)
s.add(wy_4_19>=0, wy_4_19<=18)
s.add(wy_4_20>=0, wy_4_20<=18)
s.add(wy_4_21>=0, wy_4_21<=18)
s.add(wy_4_22>=0, wy_4_22<=18)
s.add(wy_4_23>=0, wy_4_23<=18)
s.add(wy_4_24>=0, wy_4_24<=18)
s.add(wy_4_25>=0, wy_4_25<=18)
s.add(wy_4_26>=0, wy_4_26<=18)
s.add(wy_4_27>=0, wy_4_27<=18)
s.add(wy_4_28>=0, wy_4_28<=18)
s.add(wy_4_29>=0, wy_4_29<=18)
s.add(wy_4_30>=0, wy_4_30<=18)
s.add(wy_4_31>=0, wy_4_31<=18)
s.add(wy_4_32>=0, wy_4_32<=18)
s.add(wy_4_33>=0, wy_4_33<=18)
s.add(wy_4_34>=0, wy_4_34<=18)
s.add(wy_4_35>=0, wy_4_35<=18)
s.add(wy_4_36>=0, wy_4_36<=18)
s.add(wy_4_37>=0, wy_4_37<=18)
s.add(wy_4_38>=0, wy_4_38<=18)
s.add(wy_4_39>=0, wy_4_39<=18)
s.add(wy_4_40>=0, wy_4_40<=18)
s.add(wy_4_41>=0, wy_4_41<=18)
s.add(wy_4_42>=0, wy_4_42<=18)
s.add(wy_4_43>=0, wy_4_43<=18)
s.add(wy_4_44>=0, wy_4_44<=18)
s.add(wy_4_45>=0, wy_4_45<=18)
s.add(wy_4_46>=0, wy_4_46<=18)
s.add(wy_4_47>=0, wy_4_47<=18)
s.add(wy_4_48>=0, wy_4_48<=18)
s.add(wy_4_49>=0, wy_4_49<=18)

# instantiate : full charge at the beginning, for workers
s.add(ch_1_1==20)
s.add(ch_2_1==20)
s.add(ch_3_1==20)
s.add(ch_4_1==20)

# instantiate : range of charge, for workers
s.add(ch_1_1>=0, ch_1_1<=20)
s.add(ch_1_2>=0, ch_1_2<=20)
s.add(ch_1_3>=0, ch_1_3<=20)
s.add(ch_1_4>=0, ch_1_4<=20)
s.add(ch_1_5>=0, ch_1_5<=20)
s.add(ch_1_6>=0, ch_1_6<=20)
s.add(ch_1_7>=0, ch_1_7<=20)
s.add(ch_1_8>=0, ch_1_8<=20)
s.add(ch_1_9>=0, ch_1_9<=20)
s.add(ch_1_10>=0, ch_1_10<=20)
s.add(ch_1_11>=0, ch_1_11<=20)
s.add(ch_1_12>=0, ch_1_12<=20)
s.add(ch_1_13>=0, ch_1_13<=20)
s.add(ch_1_14>=0, ch_1_14<=20)
s.add(ch_1_15>=0, ch_1_15<=20)
s.add(ch_1_16>=0, ch_1_16<=20)
s.add(ch_1_17>=0, ch_1_17<=20)
s.add(ch_1_18>=0, ch_1_18<=20)
s.add(ch_1_19>=0, ch_1_19<=20)
s.add(ch_1_20>=0, ch_1_20<=20)
s.add(ch_1_21>=0, ch_1_21<=20)
s.add(ch_1_22>=0, ch_1_22<=20)
s.add(ch_1_23>=0, ch_1_23<=20)
s.add(ch_1_24>=0, ch_1_24<=20)
s.add(ch_1_25>=0, ch_1_25<=20)
s.add(ch_1_26>=0, ch_1_26<=20)
s.add(ch_1_27>=0, ch_1_27<=20)
s.add(ch_1_28>=0, ch_1_28<=20)
s.add(ch_1_29>=0, ch_1_29<=20)
s.add(ch_1_30>=0, ch_1_30<=20)
s.add(ch_1_31>=0, ch_1_31<=20)
s.add(ch_1_32>=0, ch_1_32<=20)
s.add(ch_1_33>=0, ch_1_33<=20)
s.add(ch_1_34>=0, ch_1_34<=20)
s.add(ch_1_35>=0, ch_1_35<=20)
s.add(ch_1_36>=0, ch_1_36<=20)
s.add(ch_1_37>=0, ch_1_37<=20)
s.add(ch_1_38>=0, ch_1_38<=20)
s.add(ch_1_39>=0, ch_1_39<=20)
s.add(ch_1_40>=0, ch_1_40<=20)
s.add(ch_1_41>=0, ch_1_41<=20)
s.add(ch_1_42>=0, ch_1_42<=20)
s.add(ch_1_43>=0, ch_1_43<=20)
s.add(ch_1_44>=0, ch_1_44<=20)
s.add(ch_1_45>=0, ch_1_45<=20)
s.add(ch_1_46>=0, ch_1_46<=20)
s.add(ch_1_47>=0, ch_1_47<=20)
s.add(ch_1_48>=0, ch_1_48<=20)
s.add(ch_1_49>=0, ch_1_49<=20)
s.add(ch_2_1>=0, ch_2_1<=20)
s.add(ch_2_2>=0, ch_2_2<=20)
s.add(ch_2_3>=0, ch_2_3<=20)
s.add(ch_2_4>=0, ch_2_4<=20)
s.add(ch_2_5>=0, ch_2_5<=20)
s.add(ch_2_6>=0, ch_2_6<=20)
s.add(ch_2_7>=0, ch_2_7<=20)
s.add(ch_2_8>=0, ch_2_8<=20)
s.add(ch_2_9>=0, ch_2_9<=20)
s.add(ch_2_10>=0, ch_2_10<=20)
s.add(ch_2_11>=0, ch_2_11<=20)
s.add(ch_2_12>=0, ch_2_12<=20)
s.add(ch_2_13>=0, ch_2_13<=20)
s.add(ch_2_14>=0, ch_2_14<=20)
s.add(ch_2_15>=0, ch_2_15<=20)
s.add(ch_2_16>=0, ch_2_16<=20)
s.add(ch_2_17>=0, ch_2_17<=20)
s.add(ch_2_18>=0, ch_2_18<=20)
s.add(ch_2_19>=0, ch_2_19<=20)
s.add(ch_2_20>=0, ch_2_20<=20)
s.add(ch_2_21>=0, ch_2_21<=20)
s.add(ch_2_22>=0, ch_2_22<=20)
s.add(ch_2_23>=0, ch_2_23<=20)
s.add(ch_2_24>=0, ch_2_24<=20)
s.add(ch_2_25>=0, ch_2_25<=20)
s.add(ch_2_26>=0, ch_2_26<=20)
s.add(ch_2_27>=0, ch_2_27<=20)
s.add(ch_2_28>=0, ch_2_28<=20)
s.add(ch_2_29>=0, ch_2_29<=20)
s.add(ch_2_30>=0, ch_2_30<=20)
s.add(ch_2_31>=0, ch_2_31<=20)
s.add(ch_2_32>=0, ch_2_32<=20)
s.add(ch_2_33>=0, ch_2_33<=20)
s.add(ch_2_34>=0, ch_2_34<=20)
s.add(ch_2_35>=0, ch_2_35<=20)
s.add(ch_2_36>=0, ch_2_36<=20)
s.add(ch_2_37>=0, ch_2_37<=20)
s.add(ch_2_38>=0, ch_2_38<=20)
s.add(ch_2_39>=0, ch_2_39<=20)
s.add(ch_2_40>=0, ch_2_40<=20)
s.add(ch_2_41>=0, ch_2_41<=20)
s.add(ch_2_42>=0, ch_2_42<=20)
s.add(ch_2_43>=0, ch_2_43<=20)
s.add(ch_2_44>=0, ch_2_44<=20)
s.add(ch_2_45>=0, ch_2_45<=20)
s.add(ch_2_46>=0, ch_2_46<=20)
s.add(ch_2_47>=0, ch_2_47<=20)
s.add(ch_2_48>=0, ch_2_48<=20)
s.add(ch_2_49>=0, ch_2_49<=20)
s.add(ch_3_1>=0, ch_3_1<=20)
s.add(ch_3_2>=0, ch_3_2<=20)
s.add(ch_3_3>=0, ch_3_3<=20)
s.add(ch_3_4>=0, ch_3_4<=20)
s.add(ch_3_5>=0, ch_3_5<=20)
s.add(ch_3_6>=0, ch_3_6<=20)
s.add(ch_3_7>=0, ch_3_7<=20)
s.add(ch_3_8>=0, ch_3_8<=20)
s.add(ch_3_9>=0, ch_3_9<=20)
s.add(ch_3_10>=0, ch_3_10<=20)
s.add(ch_3_11>=0, ch_3_11<=20)
s.add(ch_3_12>=0, ch_3_12<=20)
s.add(ch_3_13>=0, ch_3_13<=20)
s.add(ch_3_14>=0, ch_3_14<=20)
s.add(ch_3_15>=0, ch_3_15<=20)
s.add(ch_3_16>=0, ch_3_16<=20)
s.add(ch_3_17>=0, ch_3_17<=20)
s.add(ch_3_18>=0, ch_3_18<=20)
s.add(ch_3_19>=0, ch_3_19<=20)
s.add(ch_3_20>=0, ch_3_20<=20)
s.add(ch_3_21>=0, ch_3_21<=20)
s.add(ch_3_22>=0, ch_3_22<=20)
s.add(ch_3_23>=0, ch_3_23<=20)
s.add(ch_3_24>=0, ch_3_24<=20)
s.add(ch_3_25>=0, ch_3_25<=20)
s.add(ch_3_26>=0, ch_3_26<=20)
s.add(ch_3_27>=0, ch_3_27<=20)
s.add(ch_3_28>=0, ch_3_28<=20)
s.add(ch_3_29>=0, ch_3_29<=20)
s.add(ch_3_30>=0, ch_3_30<=20)
s.add(ch_3_31>=0, ch_3_31<=20)
s.add(ch_3_32>=0, ch_3_32<=20)
s.add(ch_3_33>=0, ch_3_33<=20)
s.add(ch_3_34>=0, ch_3_34<=20)
s.add(ch_3_35>=0, ch_3_35<=20)
s.add(ch_3_36>=0, ch_3_36<=20)
s.add(ch_3_37>=0, ch_3_37<=20)
s.add(ch_3_38>=0, ch_3_38<=20)
s.add(ch_3_39>=0, ch_3_39<=20)
s.add(ch_3_40>=0, ch_3_40<=20)
s.add(ch_3_41>=0, ch_3_41<=20)
s.add(ch_3_42>=0, ch_3_42<=20)
s.add(ch_3_43>=0, ch_3_43<=20)
s.add(ch_3_44>=0, ch_3_44<=20)
s.add(ch_3_45>=0, ch_3_45<=20)
s.add(ch_3_46>=0, ch_3_46<=20)
s.add(ch_3_47>=0, ch_3_47<=20)
s.add(ch_3_48>=0, ch_3_48<=20)
s.add(ch_3_49>=0, ch_3_49<=20)
s.add(ch_4_1>=0, ch_4_1<=20)
s.add(ch_4_2>=0, ch_4_2<=20)
s.add(ch_4_3>=0, ch_4_3<=20)
s.add(ch_4_4>=0, ch_4_4<=20)
s.add(ch_4_5>=0, ch_4_5<=20)
s.add(ch_4_6>=0, ch_4_6<=20)
s.add(ch_4_7>=0, ch_4_7<=20)
s.add(ch_4_8>=0, ch_4_8<=20)
s.add(ch_4_9>=0, ch_4_9<=20)
s.add(ch_4_10>=0, ch_4_10<=20)
s.add(ch_4_11>=0, ch_4_11<=20)
s.add(ch_4_12>=0, ch_4_12<=20)
s.add(ch_4_13>=0, ch_4_13<=20)
s.add(ch_4_14>=0, ch_4_14<=20)
s.add(ch_4_15>=0, ch_4_15<=20)
s.add(ch_4_16>=0, ch_4_16<=20)
s.add(ch_4_17>=0, ch_4_17<=20)
s.add(ch_4_18>=0, ch_4_18<=20)
s.add(ch_4_19>=0, ch_4_19<=20)
s.add(ch_4_20>=0, ch_4_20<=20)
s.add(ch_4_21>=0, ch_4_21<=20)
s.add(ch_4_22>=0, ch_4_22<=20)
s.add(ch_4_23>=0, ch_4_23<=20)
s.add(ch_4_24>=0, ch_4_24<=20)
s.add(ch_4_25>=0, ch_4_25<=20)
s.add(ch_4_26>=0, ch_4_26<=20)
s.add(ch_4_27>=0, ch_4_27<=20)
s.add(ch_4_28>=0, ch_4_28<=20)
s.add(ch_4_29>=0, ch_4_29<=20)
s.add(ch_4_30>=0, ch_4_30<=20)
s.add(ch_4_31>=0, ch_4_31<=20)
s.add(ch_4_32>=0, ch_4_32<=20)
s.add(ch_4_33>=0, ch_4_33<=20)
s.add(ch_4_34>=0, ch_4_34<=20)
s.add(ch_4_35>=0, ch_4_35<=20)
s.add(ch_4_36>=0, ch_4_36<=20)
s.add(ch_4_37>=0, ch_4_37<=20)
s.add(ch_4_38>=0, ch_4_38<=20)
s.add(ch_4_39>=0, ch_4_39<=20)
s.add(ch_4_40>=0, ch_4_40<=20)
s.add(ch_4_41>=0, ch_4_41<=20)
s.add(ch_4_42>=0, ch_4_42<=20)
s.add(ch_4_43>=0, ch_4_43<=20)
s.add(ch_4_44>=0, ch_4_44<=20)
s.add(ch_4_45>=0, ch_4_45<=20)
s.add(ch_4_46>=0, ch_4_46<=20)
s.add(ch_4_47>=0, ch_4_47<=20)
s.add(ch_4_48>=0, ch_4_48<=20)
s.add(ch_4_49>=0, ch_4_49<=20)

# instantiate : waitcount for workers
s.add(waitcount_1_1>=0, waitcount_1_1<=1)
s.add(waitcount_1_2>=0, waitcount_1_2<=1)
s.add(waitcount_1_3>=0, waitcount_1_3<=1)
s.add(waitcount_1_4>=0, waitcount_1_4<=1)
s.add(waitcount_1_5>=0, waitcount_1_5<=1)
s.add(waitcount_1_6>=0, waitcount_1_6<=1)
s.add(waitcount_1_7>=0, waitcount_1_7<=1)
s.add(waitcount_1_8>=0, waitcount_1_8<=1)
s.add(waitcount_1_9>=0, waitcount_1_9<=1)
s.add(waitcount_1_10>=0, waitcount_1_10<=1)
s.add(waitcount_1_11>=0, waitcount_1_11<=1)
s.add(waitcount_1_12>=0, waitcount_1_12<=1)
s.add(waitcount_1_13>=0, waitcount_1_13<=1)
s.add(waitcount_1_14>=0, waitcount_1_14<=1)
s.add(waitcount_1_15>=0, waitcount_1_15<=1)
s.add(waitcount_1_16>=0, waitcount_1_16<=1)
s.add(waitcount_1_17>=0, waitcount_1_17<=1)
s.add(waitcount_1_18>=0, waitcount_1_18<=1)
s.add(waitcount_1_19>=0, waitcount_1_19<=1)
s.add(waitcount_1_20>=0, waitcount_1_20<=1)
s.add(waitcount_1_21>=0, waitcount_1_21<=1)
s.add(waitcount_1_22>=0, waitcount_1_22<=1)
s.add(waitcount_1_23>=0, waitcount_1_23<=1)
s.add(waitcount_1_24>=0, waitcount_1_24<=1)
s.add(waitcount_1_25>=0, waitcount_1_25<=1)
s.add(waitcount_1_26>=0, waitcount_1_26<=1)
s.add(waitcount_1_27>=0, waitcount_1_27<=1)
s.add(waitcount_1_28>=0, waitcount_1_28<=1)
s.add(waitcount_1_29>=0, waitcount_1_29<=1)
s.add(waitcount_1_30>=0, waitcount_1_30<=1)
s.add(waitcount_1_31>=0, waitcount_1_31<=1)
s.add(waitcount_1_32>=0, waitcount_1_32<=1)
s.add(waitcount_1_33>=0, waitcount_1_33<=1)
s.add(waitcount_1_34>=0, waitcount_1_34<=1)
s.add(waitcount_1_35>=0, waitcount_1_35<=1)
s.add(waitcount_1_36>=0, waitcount_1_36<=1)
s.add(waitcount_1_37>=0, waitcount_1_37<=1)
s.add(waitcount_1_38>=0, waitcount_1_38<=1)
s.add(waitcount_1_39>=0, waitcount_1_39<=1)
s.add(waitcount_1_40>=0, waitcount_1_40<=1)
s.add(waitcount_1_41>=0, waitcount_1_41<=1)
s.add(waitcount_1_42>=0, waitcount_1_42<=1)
s.add(waitcount_1_43>=0, waitcount_1_43<=1)
s.add(waitcount_1_44>=0, waitcount_1_44<=1)
s.add(waitcount_1_45>=0, waitcount_1_45<=1)
s.add(waitcount_1_46>=0, waitcount_1_46<=1)
s.add(waitcount_1_47>=0, waitcount_1_47<=1)
s.add(waitcount_1_48>=0, waitcount_1_48<=1)
s.add(waitcount_2_1>=0, waitcount_2_1<=1)
s.add(waitcount_2_2>=0, waitcount_2_2<=1)
s.add(waitcount_2_3>=0, waitcount_2_3<=1)
s.add(waitcount_2_4>=0, waitcount_2_4<=1)
s.add(waitcount_2_5>=0, waitcount_2_5<=1)
s.add(waitcount_2_6>=0, waitcount_2_6<=1)
s.add(waitcount_2_7>=0, waitcount_2_7<=1)
s.add(waitcount_2_8>=0, waitcount_2_8<=1)
s.add(waitcount_2_9>=0, waitcount_2_9<=1)
s.add(waitcount_2_10>=0, waitcount_2_10<=1)
s.add(waitcount_2_11>=0, waitcount_2_11<=1)
s.add(waitcount_2_12>=0, waitcount_2_12<=1)
s.add(waitcount_2_13>=0, waitcount_2_13<=1)
s.add(waitcount_2_14>=0, waitcount_2_14<=1)
s.add(waitcount_2_15>=0, waitcount_2_15<=1)
s.add(waitcount_2_16>=0, waitcount_2_16<=1)
s.add(waitcount_2_17>=0, waitcount_2_17<=1)
s.add(waitcount_2_18>=0, waitcount_2_18<=1)
s.add(waitcount_2_19>=0, waitcount_2_19<=1)
s.add(waitcount_2_20>=0, waitcount_2_20<=1)
s.add(waitcount_2_21>=0, waitcount_2_21<=1)
s.add(waitcount_2_22>=0, waitcount_2_22<=1)
s.add(waitcount_2_23>=0, waitcount_2_23<=1)
s.add(waitcount_2_24>=0, waitcount_2_24<=1)
s.add(waitcount_2_25>=0, waitcount_2_25<=1)
s.add(waitcount_2_26>=0, waitcount_2_26<=1)
s.add(waitcount_2_27>=0, waitcount_2_27<=1)
s.add(waitcount_2_28>=0, waitcount_2_28<=1)
s.add(waitcount_2_29>=0, waitcount_2_29<=1)
s.add(waitcount_2_30>=0, waitcount_2_30<=1)
s.add(waitcount_2_31>=0, waitcount_2_31<=1)
s.add(waitcount_2_32>=0, waitcount_2_32<=1)
s.add(waitcount_2_33>=0, waitcount_2_33<=1)
s.add(waitcount_2_34>=0, waitcount_2_34<=1)
s.add(waitcount_2_35>=0, waitcount_2_35<=1)
s.add(waitcount_2_36>=0, waitcount_2_36<=1)
s.add(waitcount_2_37>=0, waitcount_2_37<=1)
s.add(waitcount_2_38>=0, waitcount_2_38<=1)
s.add(waitcount_2_39>=0, waitcount_2_39<=1)
s.add(waitcount_2_40>=0, waitcount_2_40<=1)
s.add(waitcount_2_41>=0, waitcount_2_41<=1)
s.add(waitcount_2_42>=0, waitcount_2_42<=1)
s.add(waitcount_2_43>=0, waitcount_2_43<=1)
s.add(waitcount_2_44>=0, waitcount_2_44<=1)
s.add(waitcount_2_45>=0, waitcount_2_45<=1)
s.add(waitcount_2_46>=0, waitcount_2_46<=1)
s.add(waitcount_2_47>=0, waitcount_2_47<=1)
s.add(waitcount_2_48>=0, waitcount_2_48<=1)
s.add(waitcount_3_1>=0, waitcount_3_1<=1)
s.add(waitcount_3_2>=0, waitcount_3_2<=1)
s.add(waitcount_3_3>=0, waitcount_3_3<=1)
s.add(waitcount_3_4>=0, waitcount_3_4<=1)
s.add(waitcount_3_5>=0, waitcount_3_5<=1)
s.add(waitcount_3_6>=0, waitcount_3_6<=1)
s.add(waitcount_3_7>=0, waitcount_3_7<=1)
s.add(waitcount_3_8>=0, waitcount_3_8<=1)
s.add(waitcount_3_9>=0, waitcount_3_9<=1)
s.add(waitcount_3_10>=0, waitcount_3_10<=1)
s.add(waitcount_3_11>=0, waitcount_3_11<=1)
s.add(waitcount_3_12>=0, waitcount_3_12<=1)
s.add(waitcount_3_13>=0, waitcount_3_13<=1)
s.add(waitcount_3_14>=0, waitcount_3_14<=1)
s.add(waitcount_3_15>=0, waitcount_3_15<=1)
s.add(waitcount_3_16>=0, waitcount_3_16<=1)
s.add(waitcount_3_17>=0, waitcount_3_17<=1)
s.add(waitcount_3_18>=0, waitcount_3_18<=1)
s.add(waitcount_3_19>=0, waitcount_3_19<=1)
s.add(waitcount_3_20>=0, waitcount_3_20<=1)
s.add(waitcount_3_21>=0, waitcount_3_21<=1)
s.add(waitcount_3_22>=0, waitcount_3_22<=1)
s.add(waitcount_3_23>=0, waitcount_3_23<=1)
s.add(waitcount_3_24>=0, waitcount_3_24<=1)
s.add(waitcount_3_25>=0, waitcount_3_25<=1)
s.add(waitcount_3_26>=0, waitcount_3_26<=1)
s.add(waitcount_3_27>=0, waitcount_3_27<=1)
s.add(waitcount_3_28>=0, waitcount_3_28<=1)
s.add(waitcount_3_29>=0, waitcount_3_29<=1)
s.add(waitcount_3_30>=0, waitcount_3_30<=1)
s.add(waitcount_3_31>=0, waitcount_3_31<=1)
s.add(waitcount_3_32>=0, waitcount_3_32<=1)
s.add(waitcount_3_33>=0, waitcount_3_33<=1)
s.add(waitcount_3_34>=0, waitcount_3_34<=1)
s.add(waitcount_3_35>=0, waitcount_3_35<=1)
s.add(waitcount_3_36>=0, waitcount_3_36<=1)
s.add(waitcount_3_37>=0, waitcount_3_37<=1)
s.add(waitcount_3_38>=0, waitcount_3_38<=1)
s.add(waitcount_3_39>=0, waitcount_3_39<=1)
s.add(waitcount_3_40>=0, waitcount_3_40<=1)
s.add(waitcount_3_41>=0, waitcount_3_41<=1)
s.add(waitcount_3_42>=0, waitcount_3_42<=1)
s.add(waitcount_3_43>=0, waitcount_3_43<=1)
s.add(waitcount_3_44>=0, waitcount_3_44<=1)
s.add(waitcount_3_45>=0, waitcount_3_45<=1)
s.add(waitcount_3_46>=0, waitcount_3_46<=1)
s.add(waitcount_3_47>=0, waitcount_3_47<=1)
s.add(waitcount_3_48>=0, waitcount_3_48<=1)
s.add(waitcount_4_1>=0, waitcount_4_1<=1)
s.add(waitcount_4_2>=0, waitcount_4_2<=1)
s.add(waitcount_4_3>=0, waitcount_4_3<=1)
s.add(waitcount_4_4>=0, waitcount_4_4<=1)
s.add(waitcount_4_5>=0, waitcount_4_5<=1)
s.add(waitcount_4_6>=0, waitcount_4_6<=1)
s.add(waitcount_4_7>=0, waitcount_4_7<=1)
s.add(waitcount_4_8>=0, waitcount_4_8<=1)
s.add(waitcount_4_9>=0, waitcount_4_9<=1)
s.add(waitcount_4_10>=0, waitcount_4_10<=1)
s.add(waitcount_4_11>=0, waitcount_4_11<=1)
s.add(waitcount_4_12>=0, waitcount_4_12<=1)
s.add(waitcount_4_13>=0, waitcount_4_13<=1)
s.add(waitcount_4_14>=0, waitcount_4_14<=1)
s.add(waitcount_4_15>=0, waitcount_4_15<=1)
s.add(waitcount_4_16>=0, waitcount_4_16<=1)
s.add(waitcount_4_17>=0, waitcount_4_17<=1)
s.add(waitcount_4_18>=0, waitcount_4_18<=1)
s.add(waitcount_4_19>=0, waitcount_4_19<=1)
s.add(waitcount_4_20>=0, waitcount_4_20<=1)
s.add(waitcount_4_21>=0, waitcount_4_21<=1)
s.add(waitcount_4_22>=0, waitcount_4_22<=1)
s.add(waitcount_4_23>=0, waitcount_4_23<=1)
s.add(waitcount_4_24>=0, waitcount_4_24<=1)
s.add(waitcount_4_25>=0, waitcount_4_25<=1)
s.add(waitcount_4_26>=0, waitcount_4_26<=1)
s.add(waitcount_4_27>=0, waitcount_4_27<=1)
s.add(waitcount_4_28>=0, waitcount_4_28<=1)
s.add(waitcount_4_29>=0, waitcount_4_29<=1)
s.add(waitcount_4_30>=0, waitcount_4_30<=1)
s.add(waitcount_4_31>=0, waitcount_4_31<=1)
s.add(waitcount_4_32>=0, waitcount_4_32<=1)
s.add(waitcount_4_33>=0, waitcount_4_33<=1)
s.add(waitcount_4_34>=0, waitcount_4_34<=1)
s.add(waitcount_4_35>=0, waitcount_4_35<=1)
s.add(waitcount_4_36>=0, waitcount_4_36<=1)
s.add(waitcount_4_37>=0, waitcount_4_37<=1)
s.add(waitcount_4_38>=0, waitcount_4_38<=1)
s.add(waitcount_4_39>=0, waitcount_4_39<=1)
s.add(waitcount_4_40>=0, waitcount_4_40<=1)
s.add(waitcount_4_41>=0, waitcount_4_41<=1)
s.add(waitcount_4_42>=0, waitcount_4_42<=1)
s.add(waitcount_4_43>=0, waitcount_4_43<=1)
s.add(waitcount_4_44>=0, waitcount_4_44<=1)
s.add(waitcount_4_45>=0, waitcount_4_45<=1)
s.add(waitcount_4_46>=0, waitcount_4_46<=1)
s.add(waitcount_4_47>=0, waitcount_4_47<=1)
s.add(waitcount_4_48>=0, waitcount_4_48<=1)

# instantiate : rechcount for workers
s.add(rechcount_1_1>=0, rechcount_1_1<=1)
s.add(rechcount_1_2>=0, rechcount_1_2<=1)
s.add(rechcount_1_3>=0, rechcount_1_3<=1)
s.add(rechcount_1_4>=0, rechcount_1_4<=1)
s.add(rechcount_1_5>=0, rechcount_1_5<=1)
s.add(rechcount_1_6>=0, rechcount_1_6<=1)
s.add(rechcount_1_7>=0, rechcount_1_7<=1)
s.add(rechcount_1_8>=0, rechcount_1_8<=1)
s.add(rechcount_1_9>=0, rechcount_1_9<=1)
s.add(rechcount_1_10>=0, rechcount_1_10<=1)
s.add(rechcount_1_11>=0, rechcount_1_11<=1)
s.add(rechcount_1_12>=0, rechcount_1_12<=1)
s.add(rechcount_1_13>=0, rechcount_1_13<=1)
s.add(rechcount_1_14>=0, rechcount_1_14<=1)
s.add(rechcount_1_15>=0, rechcount_1_15<=1)
s.add(rechcount_1_16>=0, rechcount_1_16<=1)
s.add(rechcount_1_17>=0, rechcount_1_17<=1)
s.add(rechcount_1_18>=0, rechcount_1_18<=1)
s.add(rechcount_1_19>=0, rechcount_1_19<=1)
s.add(rechcount_1_20>=0, rechcount_1_20<=1)
s.add(rechcount_1_21>=0, rechcount_1_21<=1)
s.add(rechcount_1_22>=0, rechcount_1_22<=1)
s.add(rechcount_1_23>=0, rechcount_1_23<=1)
s.add(rechcount_1_24>=0, rechcount_1_24<=1)
s.add(rechcount_1_25>=0, rechcount_1_25<=1)
s.add(rechcount_1_26>=0, rechcount_1_26<=1)
s.add(rechcount_1_27>=0, rechcount_1_27<=1)
s.add(rechcount_1_28>=0, rechcount_1_28<=1)
s.add(rechcount_1_29>=0, rechcount_1_29<=1)
s.add(rechcount_1_30>=0, rechcount_1_30<=1)
s.add(rechcount_1_31>=0, rechcount_1_31<=1)
s.add(rechcount_1_32>=0, rechcount_1_32<=1)
s.add(rechcount_1_33>=0, rechcount_1_33<=1)
s.add(rechcount_1_34>=0, rechcount_1_34<=1)
s.add(rechcount_1_35>=0, rechcount_1_35<=1)
s.add(rechcount_1_36>=0, rechcount_1_36<=1)
s.add(rechcount_1_37>=0, rechcount_1_37<=1)
s.add(rechcount_1_38>=0, rechcount_1_38<=1)
s.add(rechcount_1_39>=0, rechcount_1_39<=1)
s.add(rechcount_1_40>=0, rechcount_1_40<=1)
s.add(rechcount_1_41>=0, rechcount_1_41<=1)
s.add(rechcount_1_42>=0, rechcount_1_42<=1)
s.add(rechcount_1_43>=0, rechcount_1_43<=1)
s.add(rechcount_1_44>=0, rechcount_1_44<=1)
s.add(rechcount_1_45>=0, rechcount_1_45<=1)
s.add(rechcount_1_46>=0, rechcount_1_46<=1)
s.add(rechcount_1_47>=0, rechcount_1_47<=1)
s.add(rechcount_1_48>=0, rechcount_1_48<=1)
s.add(rechcount_2_1>=0, rechcount_2_1<=1)
s.add(rechcount_2_2>=0, rechcount_2_2<=1)
s.add(rechcount_2_3>=0, rechcount_2_3<=1)
s.add(rechcount_2_4>=0, rechcount_2_4<=1)
s.add(rechcount_2_5>=0, rechcount_2_5<=1)
s.add(rechcount_2_6>=0, rechcount_2_6<=1)
s.add(rechcount_2_7>=0, rechcount_2_7<=1)
s.add(rechcount_2_8>=0, rechcount_2_8<=1)
s.add(rechcount_2_9>=0, rechcount_2_9<=1)
s.add(rechcount_2_10>=0, rechcount_2_10<=1)
s.add(rechcount_2_11>=0, rechcount_2_11<=1)
s.add(rechcount_2_12>=0, rechcount_2_12<=1)
s.add(rechcount_2_13>=0, rechcount_2_13<=1)
s.add(rechcount_2_14>=0, rechcount_2_14<=1)
s.add(rechcount_2_15>=0, rechcount_2_15<=1)
s.add(rechcount_2_16>=0, rechcount_2_16<=1)
s.add(rechcount_2_17>=0, rechcount_2_17<=1)
s.add(rechcount_2_18>=0, rechcount_2_18<=1)
s.add(rechcount_2_19>=0, rechcount_2_19<=1)
s.add(rechcount_2_20>=0, rechcount_2_20<=1)
s.add(rechcount_2_21>=0, rechcount_2_21<=1)
s.add(rechcount_2_22>=0, rechcount_2_22<=1)
s.add(rechcount_2_23>=0, rechcount_2_23<=1)
s.add(rechcount_2_24>=0, rechcount_2_24<=1)
s.add(rechcount_2_25>=0, rechcount_2_25<=1)
s.add(rechcount_2_26>=0, rechcount_2_26<=1)
s.add(rechcount_2_27>=0, rechcount_2_27<=1)
s.add(rechcount_2_28>=0, rechcount_2_28<=1)
s.add(rechcount_2_29>=0, rechcount_2_29<=1)
s.add(rechcount_2_30>=0, rechcount_2_30<=1)
s.add(rechcount_2_31>=0, rechcount_2_31<=1)
s.add(rechcount_2_32>=0, rechcount_2_32<=1)
s.add(rechcount_2_33>=0, rechcount_2_33<=1)
s.add(rechcount_2_34>=0, rechcount_2_34<=1)
s.add(rechcount_2_35>=0, rechcount_2_35<=1)
s.add(rechcount_2_36>=0, rechcount_2_36<=1)
s.add(rechcount_2_37>=0, rechcount_2_37<=1)
s.add(rechcount_2_38>=0, rechcount_2_38<=1)
s.add(rechcount_2_39>=0, rechcount_2_39<=1)
s.add(rechcount_2_40>=0, rechcount_2_40<=1)
s.add(rechcount_2_41>=0, rechcount_2_41<=1)
s.add(rechcount_2_42>=0, rechcount_2_42<=1)
s.add(rechcount_2_43>=0, rechcount_2_43<=1)
s.add(rechcount_2_44>=0, rechcount_2_44<=1)
s.add(rechcount_2_45>=0, rechcount_2_45<=1)
s.add(rechcount_2_46>=0, rechcount_2_46<=1)
s.add(rechcount_2_47>=0, rechcount_2_47<=1)
s.add(rechcount_2_48>=0, rechcount_2_48<=1)
s.add(rechcount_3_1>=0, rechcount_3_1<=1)
s.add(rechcount_3_2>=0, rechcount_3_2<=1)
s.add(rechcount_3_3>=0, rechcount_3_3<=1)
s.add(rechcount_3_4>=0, rechcount_3_4<=1)
s.add(rechcount_3_5>=0, rechcount_3_5<=1)
s.add(rechcount_3_6>=0, rechcount_3_6<=1)
s.add(rechcount_3_7>=0, rechcount_3_7<=1)
s.add(rechcount_3_8>=0, rechcount_3_8<=1)
s.add(rechcount_3_9>=0, rechcount_3_9<=1)
s.add(rechcount_3_10>=0, rechcount_3_10<=1)
s.add(rechcount_3_11>=0, rechcount_3_11<=1)
s.add(rechcount_3_12>=0, rechcount_3_12<=1)
s.add(rechcount_3_13>=0, rechcount_3_13<=1)
s.add(rechcount_3_14>=0, rechcount_3_14<=1)
s.add(rechcount_3_15>=0, rechcount_3_15<=1)
s.add(rechcount_3_16>=0, rechcount_3_16<=1)
s.add(rechcount_3_17>=0, rechcount_3_17<=1)
s.add(rechcount_3_18>=0, rechcount_3_18<=1)
s.add(rechcount_3_19>=0, rechcount_3_19<=1)
s.add(rechcount_3_20>=0, rechcount_3_20<=1)
s.add(rechcount_3_21>=0, rechcount_3_21<=1)
s.add(rechcount_3_22>=0, rechcount_3_22<=1)
s.add(rechcount_3_23>=0, rechcount_3_23<=1)
s.add(rechcount_3_24>=0, rechcount_3_24<=1)
s.add(rechcount_3_25>=0, rechcount_3_25<=1)
s.add(rechcount_3_26>=0, rechcount_3_26<=1)
s.add(rechcount_3_27>=0, rechcount_3_27<=1)
s.add(rechcount_3_28>=0, rechcount_3_28<=1)
s.add(rechcount_3_29>=0, rechcount_3_29<=1)
s.add(rechcount_3_30>=0, rechcount_3_30<=1)
s.add(rechcount_3_31>=0, rechcount_3_31<=1)
s.add(rechcount_3_32>=0, rechcount_3_32<=1)
s.add(rechcount_3_33>=0, rechcount_3_33<=1)
s.add(rechcount_3_34>=0, rechcount_3_34<=1)
s.add(rechcount_3_35>=0, rechcount_3_35<=1)
s.add(rechcount_3_36>=0, rechcount_3_36<=1)
s.add(rechcount_3_37>=0, rechcount_3_37<=1)
s.add(rechcount_3_38>=0, rechcount_3_38<=1)
s.add(rechcount_3_39>=0, rechcount_3_39<=1)
s.add(rechcount_3_40>=0, rechcount_3_40<=1)
s.add(rechcount_3_41>=0, rechcount_3_41<=1)
s.add(rechcount_3_42>=0, rechcount_3_42<=1)
s.add(rechcount_3_43>=0, rechcount_3_43<=1)
s.add(rechcount_3_44>=0, rechcount_3_44<=1)
s.add(rechcount_3_45>=0, rechcount_3_45<=1)
s.add(rechcount_3_46>=0, rechcount_3_46<=1)
s.add(rechcount_3_47>=0, rechcount_3_47<=1)
s.add(rechcount_3_48>=0, rechcount_3_48<=1)
s.add(rechcount_4_1>=0, rechcount_4_1<=1)
s.add(rechcount_4_2>=0, rechcount_4_2<=1)
s.add(rechcount_4_3>=0, rechcount_4_3<=1)
s.add(rechcount_4_4>=0, rechcount_4_4<=1)
s.add(rechcount_4_5>=0, rechcount_4_5<=1)
s.add(rechcount_4_6>=0, rechcount_4_6<=1)
s.add(rechcount_4_7>=0, rechcount_4_7<=1)
s.add(rechcount_4_8>=0, rechcount_4_8<=1)
s.add(rechcount_4_9>=0, rechcount_4_9<=1)
s.add(rechcount_4_10>=0, rechcount_4_10<=1)
s.add(rechcount_4_11>=0, rechcount_4_11<=1)
s.add(rechcount_4_12>=0, rechcount_4_12<=1)
s.add(rechcount_4_13>=0, rechcount_4_13<=1)
s.add(rechcount_4_14>=0, rechcount_4_14<=1)
s.add(rechcount_4_15>=0, rechcount_4_15<=1)
s.add(rechcount_4_16>=0, rechcount_4_16<=1)
s.add(rechcount_4_17>=0, rechcount_4_17<=1)
s.add(rechcount_4_18>=0, rechcount_4_18<=1)
s.add(rechcount_4_19>=0, rechcount_4_19<=1)
s.add(rechcount_4_20>=0, rechcount_4_20<=1)
s.add(rechcount_4_21>=0, rechcount_4_21<=1)
s.add(rechcount_4_22>=0, rechcount_4_22<=1)
s.add(rechcount_4_23>=0, rechcount_4_23<=1)
s.add(rechcount_4_24>=0, rechcount_4_24<=1)
s.add(rechcount_4_25>=0, rechcount_4_25<=1)
s.add(rechcount_4_26>=0, rechcount_4_26<=1)
s.add(rechcount_4_27>=0, rechcount_4_27<=1)
s.add(rechcount_4_28>=0, rechcount_4_28<=1)
s.add(rechcount_4_29>=0, rechcount_4_29<=1)
s.add(rechcount_4_30>=0, rechcount_4_30<=1)
s.add(rechcount_4_31>=0, rechcount_4_31<=1)
s.add(rechcount_4_32>=0, rechcount_4_32<=1)
s.add(rechcount_4_33>=0, rechcount_4_33<=1)
s.add(rechcount_4_34>=0, rechcount_4_34<=1)
s.add(rechcount_4_35>=0, rechcount_4_35<=1)
s.add(rechcount_4_36>=0, rechcount_4_36<=1)
s.add(rechcount_4_37>=0, rechcount_4_37<=1)
s.add(rechcount_4_38>=0, rechcount_4_38<=1)
s.add(rechcount_4_39>=0, rechcount_4_39<=1)
s.add(rechcount_4_40>=0, rechcount_4_40<=1)
s.add(rechcount_4_41>=0, rechcount_4_41<=1)
s.add(rechcount_4_42>=0, rechcount_4_42<=1)
s.add(rechcount_4_43>=0, rechcount_4_43<=1)
s.add(rechcount_4_44>=0, rechcount_4_44<=1)
s.add(rechcount_4_45>=0, rechcount_4_45<=1)
s.add(rechcount_4_46>=0, rechcount_4_46<=1)
s.add(rechcount_4_47>=0, rechcount_4_47<=1)
s.add(rechcount_4_48>=0, rechcount_4_48<=1)

# instantiate : rechassigned for workers
s.add(rechassigned_1_1>=1, rechassigned_1_1<=2)
s.add(rechassigned_1_2>=1, rechassigned_1_2<=2)
s.add(rechassigned_1_3>=1, rechassigned_1_3<=2)
s.add(rechassigned_1_4>=1, rechassigned_1_4<=2)
s.add(rechassigned_1_5>=1, rechassigned_1_5<=2)
s.add(rechassigned_1_6>=1, rechassigned_1_6<=2)
s.add(rechassigned_1_7>=1, rechassigned_1_7<=2)
s.add(rechassigned_1_8>=1, rechassigned_1_8<=2)
s.add(rechassigned_1_9>=1, rechassigned_1_9<=2)
s.add(rechassigned_1_10>=1, rechassigned_1_10<=2)
s.add(rechassigned_1_11>=1, rechassigned_1_11<=2)
s.add(rechassigned_1_12>=1, rechassigned_1_12<=2)
s.add(rechassigned_1_13>=1, rechassigned_1_13<=2)
s.add(rechassigned_1_14>=1, rechassigned_1_14<=2)
s.add(rechassigned_1_15>=1, rechassigned_1_15<=2)
s.add(rechassigned_1_16>=1, rechassigned_1_16<=2)
s.add(rechassigned_1_17>=1, rechassigned_1_17<=2)
s.add(rechassigned_1_18>=1, rechassigned_1_18<=2)
s.add(rechassigned_1_19>=1, rechassigned_1_19<=2)
s.add(rechassigned_1_20>=1, rechassigned_1_20<=2)
s.add(rechassigned_1_21>=1, rechassigned_1_21<=2)
s.add(rechassigned_1_22>=1, rechassigned_1_22<=2)
s.add(rechassigned_1_23>=1, rechassigned_1_23<=2)
s.add(rechassigned_1_24>=1, rechassigned_1_24<=2)
s.add(rechassigned_1_25>=1, rechassigned_1_25<=2)
s.add(rechassigned_1_26>=1, rechassigned_1_26<=2)
s.add(rechassigned_1_27>=1, rechassigned_1_27<=2)
s.add(rechassigned_1_28>=1, rechassigned_1_28<=2)
s.add(rechassigned_1_29>=1, rechassigned_1_29<=2)
s.add(rechassigned_1_30>=1, rechassigned_1_30<=2)
s.add(rechassigned_1_31>=1, rechassigned_1_31<=2)
s.add(rechassigned_1_32>=1, rechassigned_1_32<=2)
s.add(rechassigned_1_33>=1, rechassigned_1_33<=2)
s.add(rechassigned_1_34>=1, rechassigned_1_34<=2)
s.add(rechassigned_1_35>=1, rechassigned_1_35<=2)
s.add(rechassigned_1_36>=1, rechassigned_1_36<=2)
s.add(rechassigned_1_37>=1, rechassigned_1_37<=2)
s.add(rechassigned_1_38>=1, rechassigned_1_38<=2)
s.add(rechassigned_1_39>=1, rechassigned_1_39<=2)
s.add(rechassigned_1_40>=1, rechassigned_1_40<=2)
s.add(rechassigned_1_41>=1, rechassigned_1_41<=2)
s.add(rechassigned_1_42>=1, rechassigned_1_42<=2)
s.add(rechassigned_1_43>=1, rechassigned_1_43<=2)
s.add(rechassigned_1_44>=1, rechassigned_1_44<=2)
s.add(rechassigned_1_45>=1, rechassigned_1_45<=2)
s.add(rechassigned_1_46>=1, rechassigned_1_46<=2)
s.add(rechassigned_1_47>=1, rechassigned_1_47<=2)
s.add(rechassigned_1_48>=1, rechassigned_1_48<=2)
s.add(rechassigned_2_1>=1, rechassigned_2_1<=2)
s.add(rechassigned_2_2>=1, rechassigned_2_2<=2)
s.add(rechassigned_2_3>=1, rechassigned_2_3<=2)
s.add(rechassigned_2_4>=1, rechassigned_2_4<=2)
s.add(rechassigned_2_5>=1, rechassigned_2_5<=2)
s.add(rechassigned_2_6>=1, rechassigned_2_6<=2)
s.add(rechassigned_2_7>=1, rechassigned_2_7<=2)
s.add(rechassigned_2_8>=1, rechassigned_2_8<=2)
s.add(rechassigned_2_9>=1, rechassigned_2_9<=2)
s.add(rechassigned_2_10>=1, rechassigned_2_10<=2)
s.add(rechassigned_2_11>=1, rechassigned_2_11<=2)
s.add(rechassigned_2_12>=1, rechassigned_2_12<=2)
s.add(rechassigned_2_13>=1, rechassigned_2_13<=2)
s.add(rechassigned_2_14>=1, rechassigned_2_14<=2)
s.add(rechassigned_2_15>=1, rechassigned_2_15<=2)
s.add(rechassigned_2_16>=1, rechassigned_2_16<=2)
s.add(rechassigned_2_17>=1, rechassigned_2_17<=2)
s.add(rechassigned_2_18>=1, rechassigned_2_18<=2)
s.add(rechassigned_2_19>=1, rechassigned_2_19<=2)
s.add(rechassigned_2_20>=1, rechassigned_2_20<=2)
s.add(rechassigned_2_21>=1, rechassigned_2_21<=2)
s.add(rechassigned_2_22>=1, rechassigned_2_22<=2)
s.add(rechassigned_2_23>=1, rechassigned_2_23<=2)
s.add(rechassigned_2_24>=1, rechassigned_2_24<=2)
s.add(rechassigned_2_25>=1, rechassigned_2_25<=2)
s.add(rechassigned_2_26>=1, rechassigned_2_26<=2)
s.add(rechassigned_2_27>=1, rechassigned_2_27<=2)
s.add(rechassigned_2_28>=1, rechassigned_2_28<=2)
s.add(rechassigned_2_29>=1, rechassigned_2_29<=2)
s.add(rechassigned_2_30>=1, rechassigned_2_30<=2)
s.add(rechassigned_2_31>=1, rechassigned_2_31<=2)
s.add(rechassigned_2_32>=1, rechassigned_2_32<=2)
s.add(rechassigned_2_33>=1, rechassigned_2_33<=2)
s.add(rechassigned_2_34>=1, rechassigned_2_34<=2)
s.add(rechassigned_2_35>=1, rechassigned_2_35<=2)
s.add(rechassigned_2_36>=1, rechassigned_2_36<=2)
s.add(rechassigned_2_37>=1, rechassigned_2_37<=2)
s.add(rechassigned_2_38>=1, rechassigned_2_38<=2)
s.add(rechassigned_2_39>=1, rechassigned_2_39<=2)
s.add(rechassigned_2_40>=1, rechassigned_2_40<=2)
s.add(rechassigned_2_41>=1, rechassigned_2_41<=2)
s.add(rechassigned_2_42>=1, rechassigned_2_42<=2)
s.add(rechassigned_2_43>=1, rechassigned_2_43<=2)
s.add(rechassigned_2_44>=1, rechassigned_2_44<=2)
s.add(rechassigned_2_45>=1, rechassigned_2_45<=2)
s.add(rechassigned_2_46>=1, rechassigned_2_46<=2)
s.add(rechassigned_2_47>=1, rechassigned_2_47<=2)
s.add(rechassigned_2_48>=1, rechassigned_2_48<=2)
s.add(rechassigned_3_1>=1, rechassigned_3_1<=2)
s.add(rechassigned_3_2>=1, rechassigned_3_2<=2)
s.add(rechassigned_3_3>=1, rechassigned_3_3<=2)
s.add(rechassigned_3_4>=1, rechassigned_3_4<=2)
s.add(rechassigned_3_5>=1, rechassigned_3_5<=2)
s.add(rechassigned_3_6>=1, rechassigned_3_6<=2)
s.add(rechassigned_3_7>=1, rechassigned_3_7<=2)
s.add(rechassigned_3_8>=1, rechassigned_3_8<=2)
s.add(rechassigned_3_9>=1, rechassigned_3_9<=2)
s.add(rechassigned_3_10>=1, rechassigned_3_10<=2)
s.add(rechassigned_3_11>=1, rechassigned_3_11<=2)
s.add(rechassigned_3_12>=1, rechassigned_3_12<=2)
s.add(rechassigned_3_13>=1, rechassigned_3_13<=2)
s.add(rechassigned_3_14>=1, rechassigned_3_14<=2)
s.add(rechassigned_3_15>=1, rechassigned_3_15<=2)
s.add(rechassigned_3_16>=1, rechassigned_3_16<=2)
s.add(rechassigned_3_17>=1, rechassigned_3_17<=2)
s.add(rechassigned_3_18>=1, rechassigned_3_18<=2)
s.add(rechassigned_3_19>=1, rechassigned_3_19<=2)
s.add(rechassigned_3_20>=1, rechassigned_3_20<=2)
s.add(rechassigned_3_21>=1, rechassigned_3_21<=2)
s.add(rechassigned_3_22>=1, rechassigned_3_22<=2)
s.add(rechassigned_3_23>=1, rechassigned_3_23<=2)
s.add(rechassigned_3_24>=1, rechassigned_3_24<=2)
s.add(rechassigned_3_25>=1, rechassigned_3_25<=2)
s.add(rechassigned_3_26>=1, rechassigned_3_26<=2)
s.add(rechassigned_3_27>=1, rechassigned_3_27<=2)
s.add(rechassigned_3_28>=1, rechassigned_3_28<=2)
s.add(rechassigned_3_29>=1, rechassigned_3_29<=2)
s.add(rechassigned_3_30>=1, rechassigned_3_30<=2)
s.add(rechassigned_3_31>=1, rechassigned_3_31<=2)
s.add(rechassigned_3_32>=1, rechassigned_3_32<=2)
s.add(rechassigned_3_33>=1, rechassigned_3_33<=2)
s.add(rechassigned_3_34>=1, rechassigned_3_34<=2)
s.add(rechassigned_3_35>=1, rechassigned_3_35<=2)
s.add(rechassigned_3_36>=1, rechassigned_3_36<=2)
s.add(rechassigned_3_37>=1, rechassigned_3_37<=2)
s.add(rechassigned_3_38>=1, rechassigned_3_38<=2)
s.add(rechassigned_3_39>=1, rechassigned_3_39<=2)
s.add(rechassigned_3_40>=1, rechassigned_3_40<=2)
s.add(rechassigned_3_41>=1, rechassigned_3_41<=2)
s.add(rechassigned_3_42>=1, rechassigned_3_42<=2)
s.add(rechassigned_3_43>=1, rechassigned_3_43<=2)
s.add(rechassigned_3_44>=1, rechassigned_3_44<=2)
s.add(rechassigned_3_45>=1, rechassigned_3_45<=2)
s.add(rechassigned_3_46>=1, rechassigned_3_46<=2)
s.add(rechassigned_3_47>=1, rechassigned_3_47<=2)
s.add(rechassigned_3_48>=1, rechassigned_3_48<=2)
s.add(rechassigned_4_1>=1, rechassigned_4_1<=2)
s.add(rechassigned_4_2>=1, rechassigned_4_2<=2)
s.add(rechassigned_4_3>=1, rechassigned_4_3<=2)
s.add(rechassigned_4_4>=1, rechassigned_4_4<=2)
s.add(rechassigned_4_5>=1, rechassigned_4_5<=2)
s.add(rechassigned_4_6>=1, rechassigned_4_6<=2)
s.add(rechassigned_4_7>=1, rechassigned_4_7<=2)
s.add(rechassigned_4_8>=1, rechassigned_4_8<=2)
s.add(rechassigned_4_9>=1, rechassigned_4_9<=2)
s.add(rechassigned_4_10>=1, rechassigned_4_10<=2)
s.add(rechassigned_4_11>=1, rechassigned_4_11<=2)
s.add(rechassigned_4_12>=1, rechassigned_4_12<=2)
s.add(rechassigned_4_13>=1, rechassigned_4_13<=2)
s.add(rechassigned_4_14>=1, rechassigned_4_14<=2)
s.add(rechassigned_4_15>=1, rechassigned_4_15<=2)
s.add(rechassigned_4_16>=1, rechassigned_4_16<=2)
s.add(rechassigned_4_17>=1, rechassigned_4_17<=2)
s.add(rechassigned_4_18>=1, rechassigned_4_18<=2)
s.add(rechassigned_4_19>=1, rechassigned_4_19<=2)
s.add(rechassigned_4_20>=1, rechassigned_4_20<=2)
s.add(rechassigned_4_21>=1, rechassigned_4_21<=2)
s.add(rechassigned_4_22>=1, rechassigned_4_22<=2)
s.add(rechassigned_4_23>=1, rechassigned_4_23<=2)
s.add(rechassigned_4_24>=1, rechassigned_4_24<=2)
s.add(rechassigned_4_25>=1, rechassigned_4_25<=2)
s.add(rechassigned_4_26>=1, rechassigned_4_26<=2)
s.add(rechassigned_4_27>=1, rechassigned_4_27<=2)
s.add(rechassigned_4_28>=1, rechassigned_4_28<=2)
s.add(rechassigned_4_29>=1, rechassigned_4_29<=2)
s.add(rechassigned_4_30>=1, rechassigned_4_30<=2)
s.add(rechassigned_4_31>=1, rechassigned_4_31<=2)
s.add(rechassigned_4_32>=1, rechassigned_4_32<=2)
s.add(rechassigned_4_33>=1, rechassigned_4_33<=2)
s.add(rechassigned_4_34>=1, rechassigned_4_34<=2)
s.add(rechassigned_4_35>=1, rechassigned_4_35<=2)
s.add(rechassigned_4_36>=1, rechassigned_4_36<=2)
s.add(rechassigned_4_37>=1, rechassigned_4_37<=2)
s.add(rechassigned_4_38>=1, rechassigned_4_38<=2)
s.add(rechassigned_4_39>=1, rechassigned_4_39<=2)
s.add(rechassigned_4_40>=1, rechassigned_4_40<=2)
s.add(rechassigned_4_41>=1, rechassigned_4_41<=2)
s.add(rechassigned_4_42>=1, rechassigned_4_42<=2)
s.add(rechassigned_4_43>=1, rechassigned_4_43<=2)
s.add(rechassigned_4_44>=1, rechassigned_4_44<=2)
s.add(rechassigned_4_45>=1, rechassigned_4_45<=2)
s.add(rechassigned_4_46>=1, rechassigned_4_46<=2)
s.add(rechassigned_4_47>=1, rechassigned_4_47<=2)
s.add(rechassigned_4_48>=1, rechassigned_4_48<=2)

# mapping : Worker trajectory to loop point
s.add(Implies(wtraj_1_1==1, And(wx_1_1==7, wy_1_1==3)))
s.add(Implies(wtraj_1_1==2, And(wx_1_1==4, wy_1_1==5)))
s.add(Implies(wtraj_1_1==3, And(wx_1_1==1, wy_1_1==3)))
s.add(Implies(wtraj_1_1==4, And(wx_1_1==4, wy_1_1==1)))
s.add(Implies(wtraj_1_2==1, And(wx_1_2==7, wy_1_2==3)))
s.add(Implies(wtraj_1_2==2, And(wx_1_2==4, wy_1_2==5)))
s.add(Implies(wtraj_1_2==3, And(wx_1_2==1, wy_1_2==3)))
s.add(Implies(wtraj_1_2==4, And(wx_1_2==4, wy_1_2==1)))
s.add(Implies(wtraj_1_3==1, And(wx_1_3==7, wy_1_3==3)))
s.add(Implies(wtraj_1_3==2, And(wx_1_3==4, wy_1_3==5)))
s.add(Implies(wtraj_1_3==3, And(wx_1_3==1, wy_1_3==3)))
s.add(Implies(wtraj_1_3==4, And(wx_1_3==4, wy_1_3==1)))
s.add(Implies(wtraj_1_4==1, And(wx_1_4==7, wy_1_4==3)))
s.add(Implies(wtraj_1_4==2, And(wx_1_4==4, wy_1_4==5)))
s.add(Implies(wtraj_1_4==3, And(wx_1_4==1, wy_1_4==3)))
s.add(Implies(wtraj_1_4==4, And(wx_1_4==4, wy_1_4==1)))
s.add(Implies(wtraj_1_5==1, And(wx_1_5==7, wy_1_5==3)))
s.add(Implies(wtraj_1_5==2, And(wx_1_5==4, wy_1_5==5)))
s.add(Implies(wtraj_1_5==3, And(wx_1_5==1, wy_1_5==3)))
s.add(Implies(wtraj_1_5==4, And(wx_1_5==4, wy_1_5==1)))
s.add(Implies(wtraj_1_6==1, And(wx_1_6==7, wy_1_6==3)))
s.add(Implies(wtraj_1_6==2, And(wx_1_6==4, wy_1_6==5)))
s.add(Implies(wtraj_1_6==3, And(wx_1_6==1, wy_1_6==3)))
s.add(Implies(wtraj_1_6==4, And(wx_1_6==4, wy_1_6==1)))
s.add(Implies(wtraj_1_7==1, And(wx_1_7==7, wy_1_7==3)))
s.add(Implies(wtraj_1_7==2, And(wx_1_7==4, wy_1_7==5)))
s.add(Implies(wtraj_1_7==3, And(wx_1_7==1, wy_1_7==3)))
s.add(Implies(wtraj_1_7==4, And(wx_1_7==4, wy_1_7==1)))
s.add(Implies(wtraj_1_8==1, And(wx_1_8==7, wy_1_8==3)))
s.add(Implies(wtraj_1_8==2, And(wx_1_8==4, wy_1_8==5)))
s.add(Implies(wtraj_1_8==3, And(wx_1_8==1, wy_1_8==3)))
s.add(Implies(wtraj_1_8==4, And(wx_1_8==4, wy_1_8==1)))
s.add(Implies(wtraj_1_9==1, And(wx_1_9==7, wy_1_9==3)))
s.add(Implies(wtraj_1_9==2, And(wx_1_9==4, wy_1_9==5)))
s.add(Implies(wtraj_1_9==3, And(wx_1_9==1, wy_1_9==3)))
s.add(Implies(wtraj_1_9==4, And(wx_1_9==4, wy_1_9==1)))
s.add(Implies(wtraj_1_10==1, And(wx_1_10==7, wy_1_10==3)))
s.add(Implies(wtraj_1_10==2, And(wx_1_10==4, wy_1_10==5)))
s.add(Implies(wtraj_1_10==3, And(wx_1_10==1, wy_1_10==3)))
s.add(Implies(wtraj_1_10==4, And(wx_1_10==4, wy_1_10==1)))
s.add(Implies(wtraj_1_11==1, And(wx_1_11==7, wy_1_11==3)))
s.add(Implies(wtraj_1_11==2, And(wx_1_11==4, wy_1_11==5)))
s.add(Implies(wtraj_1_11==3, And(wx_1_11==1, wy_1_11==3)))
s.add(Implies(wtraj_1_11==4, And(wx_1_11==4, wy_1_11==1)))
s.add(Implies(wtraj_1_12==1, And(wx_1_12==7, wy_1_12==3)))
s.add(Implies(wtraj_1_12==2, And(wx_1_12==4, wy_1_12==5)))
s.add(Implies(wtraj_1_12==3, And(wx_1_12==1, wy_1_12==3)))
s.add(Implies(wtraj_1_12==4, And(wx_1_12==4, wy_1_12==1)))
s.add(Implies(wtraj_1_13==1, And(wx_1_13==7, wy_1_13==3)))
s.add(Implies(wtraj_1_13==2, And(wx_1_13==4, wy_1_13==5)))
s.add(Implies(wtraj_1_13==3, And(wx_1_13==1, wy_1_13==3)))
s.add(Implies(wtraj_1_13==4, And(wx_1_13==4, wy_1_13==1)))
s.add(Implies(wtraj_1_14==1, And(wx_1_14==7, wy_1_14==3)))
s.add(Implies(wtraj_1_14==2, And(wx_1_14==4, wy_1_14==5)))
s.add(Implies(wtraj_1_14==3, And(wx_1_14==1, wy_1_14==3)))
s.add(Implies(wtraj_1_14==4, And(wx_1_14==4, wy_1_14==1)))
s.add(Implies(wtraj_1_15==1, And(wx_1_15==7, wy_1_15==3)))
s.add(Implies(wtraj_1_15==2, And(wx_1_15==4, wy_1_15==5)))
s.add(Implies(wtraj_1_15==3, And(wx_1_15==1, wy_1_15==3)))
s.add(Implies(wtraj_1_15==4, And(wx_1_15==4, wy_1_15==1)))
s.add(Implies(wtraj_1_16==1, And(wx_1_16==7, wy_1_16==3)))
s.add(Implies(wtraj_1_16==2, And(wx_1_16==4, wy_1_16==5)))
s.add(Implies(wtraj_1_16==3, And(wx_1_16==1, wy_1_16==3)))
s.add(Implies(wtraj_1_16==4, And(wx_1_16==4, wy_1_16==1)))
s.add(Implies(wtraj_1_17==1, And(wx_1_17==7, wy_1_17==3)))
s.add(Implies(wtraj_1_17==2, And(wx_1_17==4, wy_1_17==5)))
s.add(Implies(wtraj_1_17==3, And(wx_1_17==1, wy_1_17==3)))
s.add(Implies(wtraj_1_17==4, And(wx_1_17==4, wy_1_17==1)))
s.add(Implies(wtraj_1_18==1, And(wx_1_18==7, wy_1_18==3)))
s.add(Implies(wtraj_1_18==2, And(wx_1_18==4, wy_1_18==5)))
s.add(Implies(wtraj_1_18==3, And(wx_1_18==1, wy_1_18==3)))
s.add(Implies(wtraj_1_18==4, And(wx_1_18==4, wy_1_18==1)))
s.add(Implies(wtraj_1_19==1, And(wx_1_19==7, wy_1_19==3)))
s.add(Implies(wtraj_1_19==2, And(wx_1_19==4, wy_1_19==5)))
s.add(Implies(wtraj_1_19==3, And(wx_1_19==1, wy_1_19==3)))
s.add(Implies(wtraj_1_19==4, And(wx_1_19==4, wy_1_19==1)))
s.add(Implies(wtraj_1_20==1, And(wx_1_20==7, wy_1_20==3)))
s.add(Implies(wtraj_1_20==2, And(wx_1_20==4, wy_1_20==5)))
s.add(Implies(wtraj_1_20==3, And(wx_1_20==1, wy_1_20==3)))
s.add(Implies(wtraj_1_20==4, And(wx_1_20==4, wy_1_20==1)))
s.add(Implies(wtraj_1_21==1, And(wx_1_21==7, wy_1_21==3)))
s.add(Implies(wtraj_1_21==2, And(wx_1_21==4, wy_1_21==5)))
s.add(Implies(wtraj_1_21==3, And(wx_1_21==1, wy_1_21==3)))
s.add(Implies(wtraj_1_21==4, And(wx_1_21==4, wy_1_21==1)))
s.add(Implies(wtraj_1_22==1, And(wx_1_22==7, wy_1_22==3)))
s.add(Implies(wtraj_1_22==2, And(wx_1_22==4, wy_1_22==5)))
s.add(Implies(wtraj_1_22==3, And(wx_1_22==1, wy_1_22==3)))
s.add(Implies(wtraj_1_22==4, And(wx_1_22==4, wy_1_22==1)))
s.add(Implies(wtraj_1_23==1, And(wx_1_23==7, wy_1_23==3)))
s.add(Implies(wtraj_1_23==2, And(wx_1_23==4, wy_1_23==5)))
s.add(Implies(wtraj_1_23==3, And(wx_1_23==1, wy_1_23==3)))
s.add(Implies(wtraj_1_23==4, And(wx_1_23==4, wy_1_23==1)))
s.add(Implies(wtraj_1_24==1, And(wx_1_24==7, wy_1_24==3)))
s.add(Implies(wtraj_1_24==2, And(wx_1_24==4, wy_1_24==5)))
s.add(Implies(wtraj_1_24==3, And(wx_1_24==1, wy_1_24==3)))
s.add(Implies(wtraj_1_24==4, And(wx_1_24==4, wy_1_24==1)))
s.add(Implies(wtraj_1_25==1, And(wx_1_25==7, wy_1_25==3)))
s.add(Implies(wtraj_1_25==2, And(wx_1_25==4, wy_1_25==5)))
s.add(Implies(wtraj_1_25==3, And(wx_1_25==1, wy_1_25==3)))
s.add(Implies(wtraj_1_25==4, And(wx_1_25==4, wy_1_25==1)))
s.add(Implies(wtraj_1_26==1, And(wx_1_26==7, wy_1_26==3)))
s.add(Implies(wtraj_1_26==2, And(wx_1_26==4, wy_1_26==5)))
s.add(Implies(wtraj_1_26==3, And(wx_1_26==1, wy_1_26==3)))
s.add(Implies(wtraj_1_26==4, And(wx_1_26==4, wy_1_26==1)))
s.add(Implies(wtraj_1_27==1, And(wx_1_27==7, wy_1_27==3)))
s.add(Implies(wtraj_1_27==2, And(wx_1_27==4, wy_1_27==5)))
s.add(Implies(wtraj_1_27==3, And(wx_1_27==1, wy_1_27==3)))
s.add(Implies(wtraj_1_27==4, And(wx_1_27==4, wy_1_27==1)))
s.add(Implies(wtraj_1_28==1, And(wx_1_28==7, wy_1_28==3)))
s.add(Implies(wtraj_1_28==2, And(wx_1_28==4, wy_1_28==5)))
s.add(Implies(wtraj_1_28==3, And(wx_1_28==1, wy_1_28==3)))
s.add(Implies(wtraj_1_28==4, And(wx_1_28==4, wy_1_28==1)))
s.add(Implies(wtraj_1_29==1, And(wx_1_29==7, wy_1_29==3)))
s.add(Implies(wtraj_1_29==2, And(wx_1_29==4, wy_1_29==5)))
s.add(Implies(wtraj_1_29==3, And(wx_1_29==1, wy_1_29==3)))
s.add(Implies(wtraj_1_29==4, And(wx_1_29==4, wy_1_29==1)))
s.add(Implies(wtraj_1_30==1, And(wx_1_30==7, wy_1_30==3)))
s.add(Implies(wtraj_1_30==2, And(wx_1_30==4, wy_1_30==5)))
s.add(Implies(wtraj_1_30==3, And(wx_1_30==1, wy_1_30==3)))
s.add(Implies(wtraj_1_30==4, And(wx_1_30==4, wy_1_30==1)))
s.add(Implies(wtraj_1_31==1, And(wx_1_31==7, wy_1_31==3)))
s.add(Implies(wtraj_1_31==2, And(wx_1_31==4, wy_1_31==5)))
s.add(Implies(wtraj_1_31==3, And(wx_1_31==1, wy_1_31==3)))
s.add(Implies(wtraj_1_31==4, And(wx_1_31==4, wy_1_31==1)))
s.add(Implies(wtraj_1_32==1, And(wx_1_32==7, wy_1_32==3)))
s.add(Implies(wtraj_1_32==2, And(wx_1_32==4, wy_1_32==5)))
s.add(Implies(wtraj_1_32==3, And(wx_1_32==1, wy_1_32==3)))
s.add(Implies(wtraj_1_32==4, And(wx_1_32==4, wy_1_32==1)))
s.add(Implies(wtraj_1_33==1, And(wx_1_33==7, wy_1_33==3)))
s.add(Implies(wtraj_1_33==2, And(wx_1_33==4, wy_1_33==5)))
s.add(Implies(wtraj_1_33==3, And(wx_1_33==1, wy_1_33==3)))
s.add(Implies(wtraj_1_33==4, And(wx_1_33==4, wy_1_33==1)))
s.add(Implies(wtraj_1_34==1, And(wx_1_34==7, wy_1_34==3)))
s.add(Implies(wtraj_1_34==2, And(wx_1_34==4, wy_1_34==5)))
s.add(Implies(wtraj_1_34==3, And(wx_1_34==1, wy_1_34==3)))
s.add(Implies(wtraj_1_34==4, And(wx_1_34==4, wy_1_34==1)))
s.add(Implies(wtraj_1_35==1, And(wx_1_35==7, wy_1_35==3)))
s.add(Implies(wtraj_1_35==2, And(wx_1_35==4, wy_1_35==5)))
s.add(Implies(wtraj_1_35==3, And(wx_1_35==1, wy_1_35==3)))
s.add(Implies(wtraj_1_35==4, And(wx_1_35==4, wy_1_35==1)))
s.add(Implies(wtraj_1_36==1, And(wx_1_36==7, wy_1_36==3)))
s.add(Implies(wtraj_1_36==2, And(wx_1_36==4, wy_1_36==5)))
s.add(Implies(wtraj_1_36==3, And(wx_1_36==1, wy_1_36==3)))
s.add(Implies(wtraj_1_36==4, And(wx_1_36==4, wy_1_36==1)))
s.add(Implies(wtraj_1_37==1, And(wx_1_37==7, wy_1_37==3)))
s.add(Implies(wtraj_1_37==2, And(wx_1_37==4, wy_1_37==5)))
s.add(Implies(wtraj_1_37==3, And(wx_1_37==1, wy_1_37==3)))
s.add(Implies(wtraj_1_37==4, And(wx_1_37==4, wy_1_37==1)))
s.add(Implies(wtraj_1_38==1, And(wx_1_38==7, wy_1_38==3)))
s.add(Implies(wtraj_1_38==2, And(wx_1_38==4, wy_1_38==5)))
s.add(Implies(wtraj_1_38==3, And(wx_1_38==1, wy_1_38==3)))
s.add(Implies(wtraj_1_38==4, And(wx_1_38==4, wy_1_38==1)))
s.add(Implies(wtraj_1_39==1, And(wx_1_39==7, wy_1_39==3)))
s.add(Implies(wtraj_1_39==2, And(wx_1_39==4, wy_1_39==5)))
s.add(Implies(wtraj_1_39==3, And(wx_1_39==1, wy_1_39==3)))
s.add(Implies(wtraj_1_39==4, And(wx_1_39==4, wy_1_39==1)))
s.add(Implies(wtraj_1_40==1, And(wx_1_40==7, wy_1_40==3)))
s.add(Implies(wtraj_1_40==2, And(wx_1_40==4, wy_1_40==5)))
s.add(Implies(wtraj_1_40==3, And(wx_1_40==1, wy_1_40==3)))
s.add(Implies(wtraj_1_40==4, And(wx_1_40==4, wy_1_40==1)))
s.add(Implies(wtraj_1_41==1, And(wx_1_41==7, wy_1_41==3)))
s.add(Implies(wtraj_1_41==2, And(wx_1_41==4, wy_1_41==5)))
s.add(Implies(wtraj_1_41==3, And(wx_1_41==1, wy_1_41==3)))
s.add(Implies(wtraj_1_41==4, And(wx_1_41==4, wy_1_41==1)))
s.add(Implies(wtraj_1_42==1, And(wx_1_42==7, wy_1_42==3)))
s.add(Implies(wtraj_1_42==2, And(wx_1_42==4, wy_1_42==5)))
s.add(Implies(wtraj_1_42==3, And(wx_1_42==1, wy_1_42==3)))
s.add(Implies(wtraj_1_42==4, And(wx_1_42==4, wy_1_42==1)))
s.add(Implies(wtraj_1_43==1, And(wx_1_43==7, wy_1_43==3)))
s.add(Implies(wtraj_1_43==2, And(wx_1_43==4, wy_1_43==5)))
s.add(Implies(wtraj_1_43==3, And(wx_1_43==1, wy_1_43==3)))
s.add(Implies(wtraj_1_43==4, And(wx_1_43==4, wy_1_43==1)))
s.add(Implies(wtraj_1_44==1, And(wx_1_44==7, wy_1_44==3)))
s.add(Implies(wtraj_1_44==2, And(wx_1_44==4, wy_1_44==5)))
s.add(Implies(wtraj_1_44==3, And(wx_1_44==1, wy_1_44==3)))
s.add(Implies(wtraj_1_44==4, And(wx_1_44==4, wy_1_44==1)))
s.add(Implies(wtraj_1_45==1, And(wx_1_45==7, wy_1_45==3)))
s.add(Implies(wtraj_1_45==2, And(wx_1_45==4, wy_1_45==5)))
s.add(Implies(wtraj_1_45==3, And(wx_1_45==1, wy_1_45==3)))
s.add(Implies(wtraj_1_45==4, And(wx_1_45==4, wy_1_45==1)))
s.add(Implies(wtraj_1_46==1, And(wx_1_46==7, wy_1_46==3)))
s.add(Implies(wtraj_1_46==2, And(wx_1_46==4, wy_1_46==5)))
s.add(Implies(wtraj_1_46==3, And(wx_1_46==1, wy_1_46==3)))
s.add(Implies(wtraj_1_46==4, And(wx_1_46==4, wy_1_46==1)))
s.add(Implies(wtraj_1_47==1, And(wx_1_47==7, wy_1_47==3)))
s.add(Implies(wtraj_1_47==2, And(wx_1_47==4, wy_1_47==5)))
s.add(Implies(wtraj_1_47==3, And(wx_1_47==1, wy_1_47==3)))
s.add(Implies(wtraj_1_47==4, And(wx_1_47==4, wy_1_47==1)))
s.add(Implies(wtraj_1_48==1, And(wx_1_48==7, wy_1_48==3)))
s.add(Implies(wtraj_1_48==2, And(wx_1_48==4, wy_1_48==5)))
s.add(Implies(wtraj_1_48==3, And(wx_1_48==1, wy_1_48==3)))
s.add(Implies(wtraj_1_48==4, And(wx_1_48==4, wy_1_48==1)))
s.add(Implies(wtraj_1_49==1, And(wx_1_49==7, wy_1_49==3)))
s.add(Implies(wtraj_1_49==2, And(wx_1_49==4, wy_1_49==5)))
s.add(Implies(wtraj_1_49==3, And(wx_1_49==1, wy_1_49==3)))
s.add(Implies(wtraj_1_49==4, And(wx_1_49==4, wy_1_49==1)))
s.add(Implies(wtraj_2_1==1, And(wx_2_1==11, wy_2_1==3)))
s.add(Implies(wtraj_2_1==2, And(wx_2_1==13, wy_2_1==1)))
s.add(Implies(wtraj_2_1==3, And(wx_2_1==15, wy_2_1==1)))
s.add(Implies(wtraj_2_1==4, And(wx_2_1==17, wy_2_1==3)))
s.add(Implies(wtraj_2_1==5, And(wx_2_1==15, wy_2_1==5)))
s.add(Implies(wtraj_2_1==6, And(wx_2_1==13, wy_2_1==5)))
s.add(Implies(wtraj_2_2==1, And(wx_2_2==11, wy_2_2==3)))
s.add(Implies(wtraj_2_2==2, And(wx_2_2==13, wy_2_2==1)))
s.add(Implies(wtraj_2_2==3, And(wx_2_2==15, wy_2_2==1)))
s.add(Implies(wtraj_2_2==4, And(wx_2_2==17, wy_2_2==3)))
s.add(Implies(wtraj_2_2==5, And(wx_2_2==15, wy_2_2==5)))
s.add(Implies(wtraj_2_2==6, And(wx_2_2==13, wy_2_2==5)))
s.add(Implies(wtraj_2_3==1, And(wx_2_3==11, wy_2_3==3)))
s.add(Implies(wtraj_2_3==2, And(wx_2_3==13, wy_2_3==1)))
s.add(Implies(wtraj_2_3==3, And(wx_2_3==15, wy_2_3==1)))
s.add(Implies(wtraj_2_3==4, And(wx_2_3==17, wy_2_3==3)))
s.add(Implies(wtraj_2_3==5, And(wx_2_3==15, wy_2_3==5)))
s.add(Implies(wtraj_2_3==6, And(wx_2_3==13, wy_2_3==5)))
s.add(Implies(wtraj_2_4==1, And(wx_2_4==11, wy_2_4==3)))
s.add(Implies(wtraj_2_4==2, And(wx_2_4==13, wy_2_4==1)))
s.add(Implies(wtraj_2_4==3, And(wx_2_4==15, wy_2_4==1)))
s.add(Implies(wtraj_2_4==4, And(wx_2_4==17, wy_2_4==3)))
s.add(Implies(wtraj_2_4==5, And(wx_2_4==15, wy_2_4==5)))
s.add(Implies(wtraj_2_4==6, And(wx_2_4==13, wy_2_4==5)))
s.add(Implies(wtraj_2_5==1, And(wx_2_5==11, wy_2_5==3)))
s.add(Implies(wtraj_2_5==2, And(wx_2_5==13, wy_2_5==1)))
s.add(Implies(wtraj_2_5==3, And(wx_2_5==15, wy_2_5==1)))
s.add(Implies(wtraj_2_5==4, And(wx_2_5==17, wy_2_5==3)))
s.add(Implies(wtraj_2_5==5, And(wx_2_5==15, wy_2_5==5)))
s.add(Implies(wtraj_2_5==6, And(wx_2_5==13, wy_2_5==5)))
s.add(Implies(wtraj_2_6==1, And(wx_2_6==11, wy_2_6==3)))
s.add(Implies(wtraj_2_6==2, And(wx_2_6==13, wy_2_6==1)))
s.add(Implies(wtraj_2_6==3, And(wx_2_6==15, wy_2_6==1)))
s.add(Implies(wtraj_2_6==4, And(wx_2_6==17, wy_2_6==3)))
s.add(Implies(wtraj_2_6==5, And(wx_2_6==15, wy_2_6==5)))
s.add(Implies(wtraj_2_6==6, And(wx_2_6==13, wy_2_6==5)))
s.add(Implies(wtraj_2_7==1, And(wx_2_7==11, wy_2_7==3)))
s.add(Implies(wtraj_2_7==2, And(wx_2_7==13, wy_2_7==1)))
s.add(Implies(wtraj_2_7==3, And(wx_2_7==15, wy_2_7==1)))
s.add(Implies(wtraj_2_7==4, And(wx_2_7==17, wy_2_7==3)))
s.add(Implies(wtraj_2_7==5, And(wx_2_7==15, wy_2_7==5)))
s.add(Implies(wtraj_2_7==6, And(wx_2_7==13, wy_2_7==5)))
s.add(Implies(wtraj_2_8==1, And(wx_2_8==11, wy_2_8==3)))
s.add(Implies(wtraj_2_8==2, And(wx_2_8==13, wy_2_8==1)))
s.add(Implies(wtraj_2_8==3, And(wx_2_8==15, wy_2_8==1)))
s.add(Implies(wtraj_2_8==4, And(wx_2_8==17, wy_2_8==3)))
s.add(Implies(wtraj_2_8==5, And(wx_2_8==15, wy_2_8==5)))
s.add(Implies(wtraj_2_8==6, And(wx_2_8==13, wy_2_8==5)))
s.add(Implies(wtraj_2_9==1, And(wx_2_9==11, wy_2_9==3)))
s.add(Implies(wtraj_2_9==2, And(wx_2_9==13, wy_2_9==1)))
s.add(Implies(wtraj_2_9==3, And(wx_2_9==15, wy_2_9==1)))
s.add(Implies(wtraj_2_9==4, And(wx_2_9==17, wy_2_9==3)))
s.add(Implies(wtraj_2_9==5, And(wx_2_9==15, wy_2_9==5)))
s.add(Implies(wtraj_2_9==6, And(wx_2_9==13, wy_2_9==5)))
s.add(Implies(wtraj_2_10==1, And(wx_2_10==11, wy_2_10==3)))
s.add(Implies(wtraj_2_10==2, And(wx_2_10==13, wy_2_10==1)))
s.add(Implies(wtraj_2_10==3, And(wx_2_10==15, wy_2_10==1)))
s.add(Implies(wtraj_2_10==4, And(wx_2_10==17, wy_2_10==3)))
s.add(Implies(wtraj_2_10==5, And(wx_2_10==15, wy_2_10==5)))
s.add(Implies(wtraj_2_10==6, And(wx_2_10==13, wy_2_10==5)))
s.add(Implies(wtraj_2_11==1, And(wx_2_11==11, wy_2_11==3)))
s.add(Implies(wtraj_2_11==2, And(wx_2_11==13, wy_2_11==1)))
s.add(Implies(wtraj_2_11==3, And(wx_2_11==15, wy_2_11==1)))
s.add(Implies(wtraj_2_11==4, And(wx_2_11==17, wy_2_11==3)))
s.add(Implies(wtraj_2_11==5, And(wx_2_11==15, wy_2_11==5)))
s.add(Implies(wtraj_2_11==6, And(wx_2_11==13, wy_2_11==5)))
s.add(Implies(wtraj_2_12==1, And(wx_2_12==11, wy_2_12==3)))
s.add(Implies(wtraj_2_12==2, And(wx_2_12==13, wy_2_12==1)))
s.add(Implies(wtraj_2_12==3, And(wx_2_12==15, wy_2_12==1)))
s.add(Implies(wtraj_2_12==4, And(wx_2_12==17, wy_2_12==3)))
s.add(Implies(wtraj_2_12==5, And(wx_2_12==15, wy_2_12==5)))
s.add(Implies(wtraj_2_12==6, And(wx_2_12==13, wy_2_12==5)))
s.add(Implies(wtraj_2_13==1, And(wx_2_13==11, wy_2_13==3)))
s.add(Implies(wtraj_2_13==2, And(wx_2_13==13, wy_2_13==1)))
s.add(Implies(wtraj_2_13==3, And(wx_2_13==15, wy_2_13==1)))
s.add(Implies(wtraj_2_13==4, And(wx_2_13==17, wy_2_13==3)))
s.add(Implies(wtraj_2_13==5, And(wx_2_13==15, wy_2_13==5)))
s.add(Implies(wtraj_2_13==6, And(wx_2_13==13, wy_2_13==5)))
s.add(Implies(wtraj_2_14==1, And(wx_2_14==11, wy_2_14==3)))
s.add(Implies(wtraj_2_14==2, And(wx_2_14==13, wy_2_14==1)))
s.add(Implies(wtraj_2_14==3, And(wx_2_14==15, wy_2_14==1)))
s.add(Implies(wtraj_2_14==4, And(wx_2_14==17, wy_2_14==3)))
s.add(Implies(wtraj_2_14==5, And(wx_2_14==15, wy_2_14==5)))
s.add(Implies(wtraj_2_14==6, And(wx_2_14==13, wy_2_14==5)))
s.add(Implies(wtraj_2_15==1, And(wx_2_15==11, wy_2_15==3)))
s.add(Implies(wtraj_2_15==2, And(wx_2_15==13, wy_2_15==1)))
s.add(Implies(wtraj_2_15==3, And(wx_2_15==15, wy_2_15==1)))
s.add(Implies(wtraj_2_15==4, And(wx_2_15==17, wy_2_15==3)))
s.add(Implies(wtraj_2_15==5, And(wx_2_15==15, wy_2_15==5)))
s.add(Implies(wtraj_2_15==6, And(wx_2_15==13, wy_2_15==5)))
s.add(Implies(wtraj_2_16==1, And(wx_2_16==11, wy_2_16==3)))
s.add(Implies(wtraj_2_16==2, And(wx_2_16==13, wy_2_16==1)))
s.add(Implies(wtraj_2_16==3, And(wx_2_16==15, wy_2_16==1)))
s.add(Implies(wtraj_2_16==4, And(wx_2_16==17, wy_2_16==3)))
s.add(Implies(wtraj_2_16==5, And(wx_2_16==15, wy_2_16==5)))
s.add(Implies(wtraj_2_16==6, And(wx_2_16==13, wy_2_16==5)))
s.add(Implies(wtraj_2_17==1, And(wx_2_17==11, wy_2_17==3)))
s.add(Implies(wtraj_2_17==2, And(wx_2_17==13, wy_2_17==1)))
s.add(Implies(wtraj_2_17==3, And(wx_2_17==15, wy_2_17==1)))
s.add(Implies(wtraj_2_17==4, And(wx_2_17==17, wy_2_17==3)))
s.add(Implies(wtraj_2_17==5, And(wx_2_17==15, wy_2_17==5)))
s.add(Implies(wtraj_2_17==6, And(wx_2_17==13, wy_2_17==5)))
s.add(Implies(wtraj_2_18==1, And(wx_2_18==11, wy_2_18==3)))
s.add(Implies(wtraj_2_18==2, And(wx_2_18==13, wy_2_18==1)))
s.add(Implies(wtraj_2_18==3, And(wx_2_18==15, wy_2_18==1)))
s.add(Implies(wtraj_2_18==4, And(wx_2_18==17, wy_2_18==3)))
s.add(Implies(wtraj_2_18==5, And(wx_2_18==15, wy_2_18==5)))
s.add(Implies(wtraj_2_18==6, And(wx_2_18==13, wy_2_18==5)))
s.add(Implies(wtraj_2_19==1, And(wx_2_19==11, wy_2_19==3)))
s.add(Implies(wtraj_2_19==2, And(wx_2_19==13, wy_2_19==1)))
s.add(Implies(wtraj_2_19==3, And(wx_2_19==15, wy_2_19==1)))
s.add(Implies(wtraj_2_19==4, And(wx_2_19==17, wy_2_19==3)))
s.add(Implies(wtraj_2_19==5, And(wx_2_19==15, wy_2_19==5)))
s.add(Implies(wtraj_2_19==6, And(wx_2_19==13, wy_2_19==5)))
s.add(Implies(wtraj_2_20==1, And(wx_2_20==11, wy_2_20==3)))
s.add(Implies(wtraj_2_20==2, And(wx_2_20==13, wy_2_20==1)))
s.add(Implies(wtraj_2_20==3, And(wx_2_20==15, wy_2_20==1)))
s.add(Implies(wtraj_2_20==4, And(wx_2_20==17, wy_2_20==3)))
s.add(Implies(wtraj_2_20==5, And(wx_2_20==15, wy_2_20==5)))
s.add(Implies(wtraj_2_20==6, And(wx_2_20==13, wy_2_20==5)))
s.add(Implies(wtraj_2_21==1, And(wx_2_21==11, wy_2_21==3)))
s.add(Implies(wtraj_2_21==2, And(wx_2_21==13, wy_2_21==1)))
s.add(Implies(wtraj_2_21==3, And(wx_2_21==15, wy_2_21==1)))
s.add(Implies(wtraj_2_21==4, And(wx_2_21==17, wy_2_21==3)))
s.add(Implies(wtraj_2_21==5, And(wx_2_21==15, wy_2_21==5)))
s.add(Implies(wtraj_2_21==6, And(wx_2_21==13, wy_2_21==5)))
s.add(Implies(wtraj_2_22==1, And(wx_2_22==11, wy_2_22==3)))
s.add(Implies(wtraj_2_22==2, And(wx_2_22==13, wy_2_22==1)))
s.add(Implies(wtraj_2_22==3, And(wx_2_22==15, wy_2_22==1)))
s.add(Implies(wtraj_2_22==4, And(wx_2_22==17, wy_2_22==3)))
s.add(Implies(wtraj_2_22==5, And(wx_2_22==15, wy_2_22==5)))
s.add(Implies(wtraj_2_22==6, And(wx_2_22==13, wy_2_22==5)))
s.add(Implies(wtraj_2_23==1, And(wx_2_23==11, wy_2_23==3)))
s.add(Implies(wtraj_2_23==2, And(wx_2_23==13, wy_2_23==1)))
s.add(Implies(wtraj_2_23==3, And(wx_2_23==15, wy_2_23==1)))
s.add(Implies(wtraj_2_23==4, And(wx_2_23==17, wy_2_23==3)))
s.add(Implies(wtraj_2_23==5, And(wx_2_23==15, wy_2_23==5)))
s.add(Implies(wtraj_2_23==6, And(wx_2_23==13, wy_2_23==5)))
s.add(Implies(wtraj_2_24==1, And(wx_2_24==11, wy_2_24==3)))
s.add(Implies(wtraj_2_24==2, And(wx_2_24==13, wy_2_24==1)))
s.add(Implies(wtraj_2_24==3, And(wx_2_24==15, wy_2_24==1)))
s.add(Implies(wtraj_2_24==4, And(wx_2_24==17, wy_2_24==3)))
s.add(Implies(wtraj_2_24==5, And(wx_2_24==15, wy_2_24==5)))
s.add(Implies(wtraj_2_24==6, And(wx_2_24==13, wy_2_24==5)))
s.add(Implies(wtraj_2_25==1, And(wx_2_25==11, wy_2_25==3)))
s.add(Implies(wtraj_2_25==2, And(wx_2_25==13, wy_2_25==1)))
s.add(Implies(wtraj_2_25==3, And(wx_2_25==15, wy_2_25==1)))
s.add(Implies(wtraj_2_25==4, And(wx_2_25==17, wy_2_25==3)))
s.add(Implies(wtraj_2_25==5, And(wx_2_25==15, wy_2_25==5)))
s.add(Implies(wtraj_2_25==6, And(wx_2_25==13, wy_2_25==5)))
s.add(Implies(wtraj_2_26==1, And(wx_2_26==11, wy_2_26==3)))
s.add(Implies(wtraj_2_26==2, And(wx_2_26==13, wy_2_26==1)))
s.add(Implies(wtraj_2_26==3, And(wx_2_26==15, wy_2_26==1)))
s.add(Implies(wtraj_2_26==4, And(wx_2_26==17, wy_2_26==3)))
s.add(Implies(wtraj_2_26==5, And(wx_2_26==15, wy_2_26==5)))
s.add(Implies(wtraj_2_26==6, And(wx_2_26==13, wy_2_26==5)))
s.add(Implies(wtraj_2_27==1, And(wx_2_27==11, wy_2_27==3)))
s.add(Implies(wtraj_2_27==2, And(wx_2_27==13, wy_2_27==1)))
s.add(Implies(wtraj_2_27==3, And(wx_2_27==15, wy_2_27==1)))
s.add(Implies(wtraj_2_27==4, And(wx_2_27==17, wy_2_27==3)))
s.add(Implies(wtraj_2_27==5, And(wx_2_27==15, wy_2_27==5)))
s.add(Implies(wtraj_2_27==6, And(wx_2_27==13, wy_2_27==5)))
s.add(Implies(wtraj_2_28==1, And(wx_2_28==11, wy_2_28==3)))
s.add(Implies(wtraj_2_28==2, And(wx_2_28==13, wy_2_28==1)))
s.add(Implies(wtraj_2_28==3, And(wx_2_28==15, wy_2_28==1)))
s.add(Implies(wtraj_2_28==4, And(wx_2_28==17, wy_2_28==3)))
s.add(Implies(wtraj_2_28==5, And(wx_2_28==15, wy_2_28==5)))
s.add(Implies(wtraj_2_28==6, And(wx_2_28==13, wy_2_28==5)))
s.add(Implies(wtraj_2_29==1, And(wx_2_29==11, wy_2_29==3)))
s.add(Implies(wtraj_2_29==2, And(wx_2_29==13, wy_2_29==1)))
s.add(Implies(wtraj_2_29==3, And(wx_2_29==15, wy_2_29==1)))
s.add(Implies(wtraj_2_29==4, And(wx_2_29==17, wy_2_29==3)))
s.add(Implies(wtraj_2_29==5, And(wx_2_29==15, wy_2_29==5)))
s.add(Implies(wtraj_2_29==6, And(wx_2_29==13, wy_2_29==5)))
s.add(Implies(wtraj_2_30==1, And(wx_2_30==11, wy_2_30==3)))
s.add(Implies(wtraj_2_30==2, And(wx_2_30==13, wy_2_30==1)))
s.add(Implies(wtraj_2_30==3, And(wx_2_30==15, wy_2_30==1)))
s.add(Implies(wtraj_2_30==4, And(wx_2_30==17, wy_2_30==3)))
s.add(Implies(wtraj_2_30==5, And(wx_2_30==15, wy_2_30==5)))
s.add(Implies(wtraj_2_30==6, And(wx_2_30==13, wy_2_30==5)))
s.add(Implies(wtraj_2_31==1, And(wx_2_31==11, wy_2_31==3)))
s.add(Implies(wtraj_2_31==2, And(wx_2_31==13, wy_2_31==1)))
s.add(Implies(wtraj_2_31==3, And(wx_2_31==15, wy_2_31==1)))
s.add(Implies(wtraj_2_31==4, And(wx_2_31==17, wy_2_31==3)))
s.add(Implies(wtraj_2_31==5, And(wx_2_31==15, wy_2_31==5)))
s.add(Implies(wtraj_2_31==6, And(wx_2_31==13, wy_2_31==5)))
s.add(Implies(wtraj_2_32==1, And(wx_2_32==11, wy_2_32==3)))
s.add(Implies(wtraj_2_32==2, And(wx_2_32==13, wy_2_32==1)))
s.add(Implies(wtraj_2_32==3, And(wx_2_32==15, wy_2_32==1)))
s.add(Implies(wtraj_2_32==4, And(wx_2_32==17, wy_2_32==3)))
s.add(Implies(wtraj_2_32==5, And(wx_2_32==15, wy_2_32==5)))
s.add(Implies(wtraj_2_32==6, And(wx_2_32==13, wy_2_32==5)))
s.add(Implies(wtraj_2_33==1, And(wx_2_33==11, wy_2_33==3)))
s.add(Implies(wtraj_2_33==2, And(wx_2_33==13, wy_2_33==1)))
s.add(Implies(wtraj_2_33==3, And(wx_2_33==15, wy_2_33==1)))
s.add(Implies(wtraj_2_33==4, And(wx_2_33==17, wy_2_33==3)))
s.add(Implies(wtraj_2_33==5, And(wx_2_33==15, wy_2_33==5)))
s.add(Implies(wtraj_2_33==6, And(wx_2_33==13, wy_2_33==5)))
s.add(Implies(wtraj_2_34==1, And(wx_2_34==11, wy_2_34==3)))
s.add(Implies(wtraj_2_34==2, And(wx_2_34==13, wy_2_34==1)))
s.add(Implies(wtraj_2_34==3, And(wx_2_34==15, wy_2_34==1)))
s.add(Implies(wtraj_2_34==4, And(wx_2_34==17, wy_2_34==3)))
s.add(Implies(wtraj_2_34==5, And(wx_2_34==15, wy_2_34==5)))
s.add(Implies(wtraj_2_34==6, And(wx_2_34==13, wy_2_34==5)))
s.add(Implies(wtraj_2_35==1, And(wx_2_35==11, wy_2_35==3)))
s.add(Implies(wtraj_2_35==2, And(wx_2_35==13, wy_2_35==1)))
s.add(Implies(wtraj_2_35==3, And(wx_2_35==15, wy_2_35==1)))
s.add(Implies(wtraj_2_35==4, And(wx_2_35==17, wy_2_35==3)))
s.add(Implies(wtraj_2_35==5, And(wx_2_35==15, wy_2_35==5)))
s.add(Implies(wtraj_2_35==6, And(wx_2_35==13, wy_2_35==5)))
s.add(Implies(wtraj_2_36==1, And(wx_2_36==11, wy_2_36==3)))
s.add(Implies(wtraj_2_36==2, And(wx_2_36==13, wy_2_36==1)))
s.add(Implies(wtraj_2_36==3, And(wx_2_36==15, wy_2_36==1)))
s.add(Implies(wtraj_2_36==4, And(wx_2_36==17, wy_2_36==3)))
s.add(Implies(wtraj_2_36==5, And(wx_2_36==15, wy_2_36==5)))
s.add(Implies(wtraj_2_36==6, And(wx_2_36==13, wy_2_36==5)))
s.add(Implies(wtraj_2_37==1, And(wx_2_37==11, wy_2_37==3)))
s.add(Implies(wtraj_2_37==2, And(wx_2_37==13, wy_2_37==1)))
s.add(Implies(wtraj_2_37==3, And(wx_2_37==15, wy_2_37==1)))
s.add(Implies(wtraj_2_37==4, And(wx_2_37==17, wy_2_37==3)))
s.add(Implies(wtraj_2_37==5, And(wx_2_37==15, wy_2_37==5)))
s.add(Implies(wtraj_2_37==6, And(wx_2_37==13, wy_2_37==5)))
s.add(Implies(wtraj_2_38==1, And(wx_2_38==11, wy_2_38==3)))
s.add(Implies(wtraj_2_38==2, And(wx_2_38==13, wy_2_38==1)))
s.add(Implies(wtraj_2_38==3, And(wx_2_38==15, wy_2_38==1)))
s.add(Implies(wtraj_2_38==4, And(wx_2_38==17, wy_2_38==3)))
s.add(Implies(wtraj_2_38==5, And(wx_2_38==15, wy_2_38==5)))
s.add(Implies(wtraj_2_38==6, And(wx_2_38==13, wy_2_38==5)))
s.add(Implies(wtraj_2_39==1, And(wx_2_39==11, wy_2_39==3)))
s.add(Implies(wtraj_2_39==2, And(wx_2_39==13, wy_2_39==1)))
s.add(Implies(wtraj_2_39==3, And(wx_2_39==15, wy_2_39==1)))
s.add(Implies(wtraj_2_39==4, And(wx_2_39==17, wy_2_39==3)))
s.add(Implies(wtraj_2_39==5, And(wx_2_39==15, wy_2_39==5)))
s.add(Implies(wtraj_2_39==6, And(wx_2_39==13, wy_2_39==5)))
s.add(Implies(wtraj_2_40==1, And(wx_2_40==11, wy_2_40==3)))
s.add(Implies(wtraj_2_40==2, And(wx_2_40==13, wy_2_40==1)))
s.add(Implies(wtraj_2_40==3, And(wx_2_40==15, wy_2_40==1)))
s.add(Implies(wtraj_2_40==4, And(wx_2_40==17, wy_2_40==3)))
s.add(Implies(wtraj_2_40==5, And(wx_2_40==15, wy_2_40==5)))
s.add(Implies(wtraj_2_40==6, And(wx_2_40==13, wy_2_40==5)))
s.add(Implies(wtraj_2_41==1, And(wx_2_41==11, wy_2_41==3)))
s.add(Implies(wtraj_2_41==2, And(wx_2_41==13, wy_2_41==1)))
s.add(Implies(wtraj_2_41==3, And(wx_2_41==15, wy_2_41==1)))
s.add(Implies(wtraj_2_41==4, And(wx_2_41==17, wy_2_41==3)))
s.add(Implies(wtraj_2_41==5, And(wx_2_41==15, wy_2_41==5)))
s.add(Implies(wtraj_2_41==6, And(wx_2_41==13, wy_2_41==5)))
s.add(Implies(wtraj_2_42==1, And(wx_2_42==11, wy_2_42==3)))
s.add(Implies(wtraj_2_42==2, And(wx_2_42==13, wy_2_42==1)))
s.add(Implies(wtraj_2_42==3, And(wx_2_42==15, wy_2_42==1)))
s.add(Implies(wtraj_2_42==4, And(wx_2_42==17, wy_2_42==3)))
s.add(Implies(wtraj_2_42==5, And(wx_2_42==15, wy_2_42==5)))
s.add(Implies(wtraj_2_42==6, And(wx_2_42==13, wy_2_42==5)))
s.add(Implies(wtraj_2_43==1, And(wx_2_43==11, wy_2_43==3)))
s.add(Implies(wtraj_2_43==2, And(wx_2_43==13, wy_2_43==1)))
s.add(Implies(wtraj_2_43==3, And(wx_2_43==15, wy_2_43==1)))
s.add(Implies(wtraj_2_43==4, And(wx_2_43==17, wy_2_43==3)))
s.add(Implies(wtraj_2_43==5, And(wx_2_43==15, wy_2_43==5)))
s.add(Implies(wtraj_2_43==6, And(wx_2_43==13, wy_2_43==5)))
s.add(Implies(wtraj_2_44==1, And(wx_2_44==11, wy_2_44==3)))
s.add(Implies(wtraj_2_44==2, And(wx_2_44==13, wy_2_44==1)))
s.add(Implies(wtraj_2_44==3, And(wx_2_44==15, wy_2_44==1)))
s.add(Implies(wtraj_2_44==4, And(wx_2_44==17, wy_2_44==3)))
s.add(Implies(wtraj_2_44==5, And(wx_2_44==15, wy_2_44==5)))
s.add(Implies(wtraj_2_44==6, And(wx_2_44==13, wy_2_44==5)))
s.add(Implies(wtraj_2_45==1, And(wx_2_45==11, wy_2_45==3)))
s.add(Implies(wtraj_2_45==2, And(wx_2_45==13, wy_2_45==1)))
s.add(Implies(wtraj_2_45==3, And(wx_2_45==15, wy_2_45==1)))
s.add(Implies(wtraj_2_45==4, And(wx_2_45==17, wy_2_45==3)))
s.add(Implies(wtraj_2_45==5, And(wx_2_45==15, wy_2_45==5)))
s.add(Implies(wtraj_2_45==6, And(wx_2_45==13, wy_2_45==5)))
s.add(Implies(wtraj_2_46==1, And(wx_2_46==11, wy_2_46==3)))
s.add(Implies(wtraj_2_46==2, And(wx_2_46==13, wy_2_46==1)))
s.add(Implies(wtraj_2_46==3, And(wx_2_46==15, wy_2_46==1)))
s.add(Implies(wtraj_2_46==4, And(wx_2_46==17, wy_2_46==3)))
s.add(Implies(wtraj_2_46==5, And(wx_2_46==15, wy_2_46==5)))
s.add(Implies(wtraj_2_46==6, And(wx_2_46==13, wy_2_46==5)))
s.add(Implies(wtraj_2_47==1, And(wx_2_47==11, wy_2_47==3)))
s.add(Implies(wtraj_2_47==2, And(wx_2_47==13, wy_2_47==1)))
s.add(Implies(wtraj_2_47==3, And(wx_2_47==15, wy_2_47==1)))
s.add(Implies(wtraj_2_47==4, And(wx_2_47==17, wy_2_47==3)))
s.add(Implies(wtraj_2_47==5, And(wx_2_47==15, wy_2_47==5)))
s.add(Implies(wtraj_2_47==6, And(wx_2_47==13, wy_2_47==5)))
s.add(Implies(wtraj_2_48==1, And(wx_2_48==11, wy_2_48==3)))
s.add(Implies(wtraj_2_48==2, And(wx_2_48==13, wy_2_48==1)))
s.add(Implies(wtraj_2_48==3, And(wx_2_48==15, wy_2_48==1)))
s.add(Implies(wtraj_2_48==4, And(wx_2_48==17, wy_2_48==3)))
s.add(Implies(wtraj_2_48==5, And(wx_2_48==15, wy_2_48==5)))
s.add(Implies(wtraj_2_48==6, And(wx_2_48==13, wy_2_48==5)))
s.add(Implies(wtraj_2_49==1, And(wx_2_49==11, wy_2_49==3)))
s.add(Implies(wtraj_2_49==2, And(wx_2_49==13, wy_2_49==1)))
s.add(Implies(wtraj_2_49==3, And(wx_2_49==15, wy_2_49==1)))
s.add(Implies(wtraj_2_49==4, And(wx_2_49==17, wy_2_49==3)))
s.add(Implies(wtraj_2_49==5, And(wx_2_49==15, wy_2_49==5)))
s.add(Implies(wtraj_2_49==6, And(wx_2_49==13, wy_2_49==5)))
s.add(Implies(wtraj_3_1==1, And(wx_3_1==17, wy_3_1==9)))
s.add(Implies(wtraj_3_1==2, And(wx_3_1==14, wy_3_1==11)))
s.add(Implies(wtraj_3_1==3, And(wx_3_1==11, wy_3_1==9)))
s.add(Implies(wtraj_3_1==4, And(wx_3_1==14, wy_3_1==7)))
s.add(Implies(wtraj_3_2==1, And(wx_3_2==17, wy_3_2==9)))
s.add(Implies(wtraj_3_2==2, And(wx_3_2==14, wy_3_2==11)))
s.add(Implies(wtraj_3_2==3, And(wx_3_2==11, wy_3_2==9)))
s.add(Implies(wtraj_3_2==4, And(wx_3_2==14, wy_3_2==7)))
s.add(Implies(wtraj_3_3==1, And(wx_3_3==17, wy_3_3==9)))
s.add(Implies(wtraj_3_3==2, And(wx_3_3==14, wy_3_3==11)))
s.add(Implies(wtraj_3_3==3, And(wx_3_3==11, wy_3_3==9)))
s.add(Implies(wtraj_3_3==4, And(wx_3_3==14, wy_3_3==7)))
s.add(Implies(wtraj_3_4==1, And(wx_3_4==17, wy_3_4==9)))
s.add(Implies(wtraj_3_4==2, And(wx_3_4==14, wy_3_4==11)))
s.add(Implies(wtraj_3_4==3, And(wx_3_4==11, wy_3_4==9)))
s.add(Implies(wtraj_3_4==4, And(wx_3_4==14, wy_3_4==7)))
s.add(Implies(wtraj_3_5==1, And(wx_3_5==17, wy_3_5==9)))
s.add(Implies(wtraj_3_5==2, And(wx_3_5==14, wy_3_5==11)))
s.add(Implies(wtraj_3_5==3, And(wx_3_5==11, wy_3_5==9)))
s.add(Implies(wtraj_3_5==4, And(wx_3_5==14, wy_3_5==7)))
s.add(Implies(wtraj_3_6==1, And(wx_3_6==17, wy_3_6==9)))
s.add(Implies(wtraj_3_6==2, And(wx_3_6==14, wy_3_6==11)))
s.add(Implies(wtraj_3_6==3, And(wx_3_6==11, wy_3_6==9)))
s.add(Implies(wtraj_3_6==4, And(wx_3_6==14, wy_3_6==7)))
s.add(Implies(wtraj_3_7==1, And(wx_3_7==17, wy_3_7==9)))
s.add(Implies(wtraj_3_7==2, And(wx_3_7==14, wy_3_7==11)))
s.add(Implies(wtraj_3_7==3, And(wx_3_7==11, wy_3_7==9)))
s.add(Implies(wtraj_3_7==4, And(wx_3_7==14, wy_3_7==7)))
s.add(Implies(wtraj_3_8==1, And(wx_3_8==17, wy_3_8==9)))
s.add(Implies(wtraj_3_8==2, And(wx_3_8==14, wy_3_8==11)))
s.add(Implies(wtraj_3_8==3, And(wx_3_8==11, wy_3_8==9)))
s.add(Implies(wtraj_3_8==4, And(wx_3_8==14, wy_3_8==7)))
s.add(Implies(wtraj_3_9==1, And(wx_3_9==17, wy_3_9==9)))
s.add(Implies(wtraj_3_9==2, And(wx_3_9==14, wy_3_9==11)))
s.add(Implies(wtraj_3_9==3, And(wx_3_9==11, wy_3_9==9)))
s.add(Implies(wtraj_3_9==4, And(wx_3_9==14, wy_3_9==7)))
s.add(Implies(wtraj_3_10==1, And(wx_3_10==17, wy_3_10==9)))
s.add(Implies(wtraj_3_10==2, And(wx_3_10==14, wy_3_10==11)))
s.add(Implies(wtraj_3_10==3, And(wx_3_10==11, wy_3_10==9)))
s.add(Implies(wtraj_3_10==4, And(wx_3_10==14, wy_3_10==7)))
s.add(Implies(wtraj_3_11==1, And(wx_3_11==17, wy_3_11==9)))
s.add(Implies(wtraj_3_11==2, And(wx_3_11==14, wy_3_11==11)))
s.add(Implies(wtraj_3_11==3, And(wx_3_11==11, wy_3_11==9)))
s.add(Implies(wtraj_3_11==4, And(wx_3_11==14, wy_3_11==7)))
s.add(Implies(wtraj_3_12==1, And(wx_3_12==17, wy_3_12==9)))
s.add(Implies(wtraj_3_12==2, And(wx_3_12==14, wy_3_12==11)))
s.add(Implies(wtraj_3_12==3, And(wx_3_12==11, wy_3_12==9)))
s.add(Implies(wtraj_3_12==4, And(wx_3_12==14, wy_3_12==7)))
s.add(Implies(wtraj_3_13==1, And(wx_3_13==17, wy_3_13==9)))
s.add(Implies(wtraj_3_13==2, And(wx_3_13==14, wy_3_13==11)))
s.add(Implies(wtraj_3_13==3, And(wx_3_13==11, wy_3_13==9)))
s.add(Implies(wtraj_3_13==4, And(wx_3_13==14, wy_3_13==7)))
s.add(Implies(wtraj_3_14==1, And(wx_3_14==17, wy_3_14==9)))
s.add(Implies(wtraj_3_14==2, And(wx_3_14==14, wy_3_14==11)))
s.add(Implies(wtraj_3_14==3, And(wx_3_14==11, wy_3_14==9)))
s.add(Implies(wtraj_3_14==4, And(wx_3_14==14, wy_3_14==7)))
s.add(Implies(wtraj_3_15==1, And(wx_3_15==17, wy_3_15==9)))
s.add(Implies(wtraj_3_15==2, And(wx_3_15==14, wy_3_15==11)))
s.add(Implies(wtraj_3_15==3, And(wx_3_15==11, wy_3_15==9)))
s.add(Implies(wtraj_3_15==4, And(wx_3_15==14, wy_3_15==7)))
s.add(Implies(wtraj_3_16==1, And(wx_3_16==17, wy_3_16==9)))
s.add(Implies(wtraj_3_16==2, And(wx_3_16==14, wy_3_16==11)))
s.add(Implies(wtraj_3_16==3, And(wx_3_16==11, wy_3_16==9)))
s.add(Implies(wtraj_3_16==4, And(wx_3_16==14, wy_3_16==7)))
s.add(Implies(wtraj_3_17==1, And(wx_3_17==17, wy_3_17==9)))
s.add(Implies(wtraj_3_17==2, And(wx_3_17==14, wy_3_17==11)))
s.add(Implies(wtraj_3_17==3, And(wx_3_17==11, wy_3_17==9)))
s.add(Implies(wtraj_3_17==4, And(wx_3_17==14, wy_3_17==7)))
s.add(Implies(wtraj_3_18==1, And(wx_3_18==17, wy_3_18==9)))
s.add(Implies(wtraj_3_18==2, And(wx_3_18==14, wy_3_18==11)))
s.add(Implies(wtraj_3_18==3, And(wx_3_18==11, wy_3_18==9)))
s.add(Implies(wtraj_3_18==4, And(wx_3_18==14, wy_3_18==7)))
s.add(Implies(wtraj_3_19==1, And(wx_3_19==17, wy_3_19==9)))
s.add(Implies(wtraj_3_19==2, And(wx_3_19==14, wy_3_19==11)))
s.add(Implies(wtraj_3_19==3, And(wx_3_19==11, wy_3_19==9)))
s.add(Implies(wtraj_3_19==4, And(wx_3_19==14, wy_3_19==7)))
s.add(Implies(wtraj_3_20==1, And(wx_3_20==17, wy_3_20==9)))
s.add(Implies(wtraj_3_20==2, And(wx_3_20==14, wy_3_20==11)))
s.add(Implies(wtraj_3_20==3, And(wx_3_20==11, wy_3_20==9)))
s.add(Implies(wtraj_3_20==4, And(wx_3_20==14, wy_3_20==7)))
s.add(Implies(wtraj_3_21==1, And(wx_3_21==17, wy_3_21==9)))
s.add(Implies(wtraj_3_21==2, And(wx_3_21==14, wy_3_21==11)))
s.add(Implies(wtraj_3_21==3, And(wx_3_21==11, wy_3_21==9)))
s.add(Implies(wtraj_3_21==4, And(wx_3_21==14, wy_3_21==7)))
s.add(Implies(wtraj_3_22==1, And(wx_3_22==17, wy_3_22==9)))
s.add(Implies(wtraj_3_22==2, And(wx_3_22==14, wy_3_22==11)))
s.add(Implies(wtraj_3_22==3, And(wx_3_22==11, wy_3_22==9)))
s.add(Implies(wtraj_3_22==4, And(wx_3_22==14, wy_3_22==7)))
s.add(Implies(wtraj_3_23==1, And(wx_3_23==17, wy_3_23==9)))
s.add(Implies(wtraj_3_23==2, And(wx_3_23==14, wy_3_23==11)))
s.add(Implies(wtraj_3_23==3, And(wx_3_23==11, wy_3_23==9)))
s.add(Implies(wtraj_3_23==4, And(wx_3_23==14, wy_3_23==7)))
s.add(Implies(wtraj_3_24==1, And(wx_3_24==17, wy_3_24==9)))
s.add(Implies(wtraj_3_24==2, And(wx_3_24==14, wy_3_24==11)))
s.add(Implies(wtraj_3_24==3, And(wx_3_24==11, wy_3_24==9)))
s.add(Implies(wtraj_3_24==4, And(wx_3_24==14, wy_3_24==7)))
s.add(Implies(wtraj_3_25==1, And(wx_3_25==17, wy_3_25==9)))
s.add(Implies(wtraj_3_25==2, And(wx_3_25==14, wy_3_25==11)))
s.add(Implies(wtraj_3_25==3, And(wx_3_25==11, wy_3_25==9)))
s.add(Implies(wtraj_3_25==4, And(wx_3_25==14, wy_3_25==7)))
s.add(Implies(wtraj_3_26==1, And(wx_3_26==17, wy_3_26==9)))
s.add(Implies(wtraj_3_26==2, And(wx_3_26==14, wy_3_26==11)))
s.add(Implies(wtraj_3_26==3, And(wx_3_26==11, wy_3_26==9)))
s.add(Implies(wtraj_3_26==4, And(wx_3_26==14, wy_3_26==7)))
s.add(Implies(wtraj_3_27==1, And(wx_3_27==17, wy_3_27==9)))
s.add(Implies(wtraj_3_27==2, And(wx_3_27==14, wy_3_27==11)))
s.add(Implies(wtraj_3_27==3, And(wx_3_27==11, wy_3_27==9)))
s.add(Implies(wtraj_3_27==4, And(wx_3_27==14, wy_3_27==7)))
s.add(Implies(wtraj_3_28==1, And(wx_3_28==17, wy_3_28==9)))
s.add(Implies(wtraj_3_28==2, And(wx_3_28==14, wy_3_28==11)))
s.add(Implies(wtraj_3_28==3, And(wx_3_28==11, wy_3_28==9)))
s.add(Implies(wtraj_3_28==4, And(wx_3_28==14, wy_3_28==7)))
s.add(Implies(wtraj_3_29==1, And(wx_3_29==17, wy_3_29==9)))
s.add(Implies(wtraj_3_29==2, And(wx_3_29==14, wy_3_29==11)))
s.add(Implies(wtraj_3_29==3, And(wx_3_29==11, wy_3_29==9)))
s.add(Implies(wtraj_3_29==4, And(wx_3_29==14, wy_3_29==7)))
s.add(Implies(wtraj_3_30==1, And(wx_3_30==17, wy_3_30==9)))
s.add(Implies(wtraj_3_30==2, And(wx_3_30==14, wy_3_30==11)))
s.add(Implies(wtraj_3_30==3, And(wx_3_30==11, wy_3_30==9)))
s.add(Implies(wtraj_3_30==4, And(wx_3_30==14, wy_3_30==7)))
s.add(Implies(wtraj_3_31==1, And(wx_3_31==17, wy_3_31==9)))
s.add(Implies(wtraj_3_31==2, And(wx_3_31==14, wy_3_31==11)))
s.add(Implies(wtraj_3_31==3, And(wx_3_31==11, wy_3_31==9)))
s.add(Implies(wtraj_3_31==4, And(wx_3_31==14, wy_3_31==7)))
s.add(Implies(wtraj_3_32==1, And(wx_3_32==17, wy_3_32==9)))
s.add(Implies(wtraj_3_32==2, And(wx_3_32==14, wy_3_32==11)))
s.add(Implies(wtraj_3_32==3, And(wx_3_32==11, wy_3_32==9)))
s.add(Implies(wtraj_3_32==4, And(wx_3_32==14, wy_3_32==7)))
s.add(Implies(wtraj_3_33==1, And(wx_3_33==17, wy_3_33==9)))
s.add(Implies(wtraj_3_33==2, And(wx_3_33==14, wy_3_33==11)))
s.add(Implies(wtraj_3_33==3, And(wx_3_33==11, wy_3_33==9)))
s.add(Implies(wtraj_3_33==4, And(wx_3_33==14, wy_3_33==7)))
s.add(Implies(wtraj_3_34==1, And(wx_3_34==17, wy_3_34==9)))
s.add(Implies(wtraj_3_34==2, And(wx_3_34==14, wy_3_34==11)))
s.add(Implies(wtraj_3_34==3, And(wx_3_34==11, wy_3_34==9)))
s.add(Implies(wtraj_3_34==4, And(wx_3_34==14, wy_3_34==7)))
s.add(Implies(wtraj_3_35==1, And(wx_3_35==17, wy_3_35==9)))
s.add(Implies(wtraj_3_35==2, And(wx_3_35==14, wy_3_35==11)))
s.add(Implies(wtraj_3_35==3, And(wx_3_35==11, wy_3_35==9)))
s.add(Implies(wtraj_3_35==4, And(wx_3_35==14, wy_3_35==7)))
s.add(Implies(wtraj_3_36==1, And(wx_3_36==17, wy_3_36==9)))
s.add(Implies(wtraj_3_36==2, And(wx_3_36==14, wy_3_36==11)))
s.add(Implies(wtraj_3_36==3, And(wx_3_36==11, wy_3_36==9)))
s.add(Implies(wtraj_3_36==4, And(wx_3_36==14, wy_3_36==7)))
s.add(Implies(wtraj_3_37==1, And(wx_3_37==17, wy_3_37==9)))
s.add(Implies(wtraj_3_37==2, And(wx_3_37==14, wy_3_37==11)))
s.add(Implies(wtraj_3_37==3, And(wx_3_37==11, wy_3_37==9)))
s.add(Implies(wtraj_3_37==4, And(wx_3_37==14, wy_3_37==7)))
s.add(Implies(wtraj_3_38==1, And(wx_3_38==17, wy_3_38==9)))
s.add(Implies(wtraj_3_38==2, And(wx_3_38==14, wy_3_38==11)))
s.add(Implies(wtraj_3_38==3, And(wx_3_38==11, wy_3_38==9)))
s.add(Implies(wtraj_3_38==4, And(wx_3_38==14, wy_3_38==7)))
s.add(Implies(wtraj_3_39==1, And(wx_3_39==17, wy_3_39==9)))
s.add(Implies(wtraj_3_39==2, And(wx_3_39==14, wy_3_39==11)))
s.add(Implies(wtraj_3_39==3, And(wx_3_39==11, wy_3_39==9)))
s.add(Implies(wtraj_3_39==4, And(wx_3_39==14, wy_3_39==7)))
s.add(Implies(wtraj_3_40==1, And(wx_3_40==17, wy_3_40==9)))
s.add(Implies(wtraj_3_40==2, And(wx_3_40==14, wy_3_40==11)))
s.add(Implies(wtraj_3_40==3, And(wx_3_40==11, wy_3_40==9)))
s.add(Implies(wtraj_3_40==4, And(wx_3_40==14, wy_3_40==7)))
s.add(Implies(wtraj_3_41==1, And(wx_3_41==17, wy_3_41==9)))
s.add(Implies(wtraj_3_41==2, And(wx_3_41==14, wy_3_41==11)))
s.add(Implies(wtraj_3_41==3, And(wx_3_41==11, wy_3_41==9)))
s.add(Implies(wtraj_3_41==4, And(wx_3_41==14, wy_3_41==7)))
s.add(Implies(wtraj_3_42==1, And(wx_3_42==17, wy_3_42==9)))
s.add(Implies(wtraj_3_42==2, And(wx_3_42==14, wy_3_42==11)))
s.add(Implies(wtraj_3_42==3, And(wx_3_42==11, wy_3_42==9)))
s.add(Implies(wtraj_3_42==4, And(wx_3_42==14, wy_3_42==7)))
s.add(Implies(wtraj_3_43==1, And(wx_3_43==17, wy_3_43==9)))
s.add(Implies(wtraj_3_43==2, And(wx_3_43==14, wy_3_43==11)))
s.add(Implies(wtraj_3_43==3, And(wx_3_43==11, wy_3_43==9)))
s.add(Implies(wtraj_3_43==4, And(wx_3_43==14, wy_3_43==7)))
s.add(Implies(wtraj_3_44==1, And(wx_3_44==17, wy_3_44==9)))
s.add(Implies(wtraj_3_44==2, And(wx_3_44==14, wy_3_44==11)))
s.add(Implies(wtraj_3_44==3, And(wx_3_44==11, wy_3_44==9)))
s.add(Implies(wtraj_3_44==4, And(wx_3_44==14, wy_3_44==7)))
s.add(Implies(wtraj_3_45==1, And(wx_3_45==17, wy_3_45==9)))
s.add(Implies(wtraj_3_45==2, And(wx_3_45==14, wy_3_45==11)))
s.add(Implies(wtraj_3_45==3, And(wx_3_45==11, wy_3_45==9)))
s.add(Implies(wtraj_3_45==4, And(wx_3_45==14, wy_3_45==7)))
s.add(Implies(wtraj_3_46==1, And(wx_3_46==17, wy_3_46==9)))
s.add(Implies(wtraj_3_46==2, And(wx_3_46==14, wy_3_46==11)))
s.add(Implies(wtraj_3_46==3, And(wx_3_46==11, wy_3_46==9)))
s.add(Implies(wtraj_3_46==4, And(wx_3_46==14, wy_3_46==7)))
s.add(Implies(wtraj_3_47==1, And(wx_3_47==17, wy_3_47==9)))
s.add(Implies(wtraj_3_47==2, And(wx_3_47==14, wy_3_47==11)))
s.add(Implies(wtraj_3_47==3, And(wx_3_47==11, wy_3_47==9)))
s.add(Implies(wtraj_3_47==4, And(wx_3_47==14, wy_3_47==7)))
s.add(Implies(wtraj_3_48==1, And(wx_3_48==17, wy_3_48==9)))
s.add(Implies(wtraj_3_48==2, And(wx_3_48==14, wy_3_48==11)))
s.add(Implies(wtraj_3_48==3, And(wx_3_48==11, wy_3_48==9)))
s.add(Implies(wtraj_3_48==4, And(wx_3_48==14, wy_3_48==7)))
s.add(Implies(wtraj_3_49==1, And(wx_3_49==17, wy_3_49==9)))
s.add(Implies(wtraj_3_49==2, And(wx_3_49==14, wy_3_49==11)))
s.add(Implies(wtraj_3_49==3, And(wx_3_49==11, wy_3_49==9)))
s.add(Implies(wtraj_3_49==4, And(wx_3_49==14, wy_3_49==7)))
s.add(Implies(wtraj_4_1==1, And(wx_4_1==7, wy_4_1==9)))
s.add(Implies(wtraj_4_1==2, And(wx_4_1==5, wy_4_1==11)))
s.add(Implies(wtraj_4_1==3, And(wx_4_1==3, wy_4_1==11)))
s.add(Implies(wtraj_4_1==4, And(wx_4_1==1, wy_4_1==9)))
s.add(Implies(wtraj_4_1==5, And(wx_4_1==3, wy_4_1==7)))
s.add(Implies(wtraj_4_1==6, And(wx_4_1==5, wy_4_1==7)))
s.add(Implies(wtraj_4_2==1, And(wx_4_2==7, wy_4_2==9)))
s.add(Implies(wtraj_4_2==2, And(wx_4_2==5, wy_4_2==11)))
s.add(Implies(wtraj_4_2==3, And(wx_4_2==3, wy_4_2==11)))
s.add(Implies(wtraj_4_2==4, And(wx_4_2==1, wy_4_2==9)))
s.add(Implies(wtraj_4_2==5, And(wx_4_2==3, wy_4_2==7)))
s.add(Implies(wtraj_4_2==6, And(wx_4_2==5, wy_4_2==7)))
s.add(Implies(wtraj_4_3==1, And(wx_4_3==7, wy_4_3==9)))
s.add(Implies(wtraj_4_3==2, And(wx_4_3==5, wy_4_3==11)))
s.add(Implies(wtraj_4_3==3, And(wx_4_3==3, wy_4_3==11)))
s.add(Implies(wtraj_4_3==4, And(wx_4_3==1, wy_4_3==9)))
s.add(Implies(wtraj_4_3==5, And(wx_4_3==3, wy_4_3==7)))
s.add(Implies(wtraj_4_3==6, And(wx_4_3==5, wy_4_3==7)))
s.add(Implies(wtraj_4_4==1, And(wx_4_4==7, wy_4_4==9)))
s.add(Implies(wtraj_4_4==2, And(wx_4_4==5, wy_4_4==11)))
s.add(Implies(wtraj_4_4==3, And(wx_4_4==3, wy_4_4==11)))
s.add(Implies(wtraj_4_4==4, And(wx_4_4==1, wy_4_4==9)))
s.add(Implies(wtraj_4_4==5, And(wx_4_4==3, wy_4_4==7)))
s.add(Implies(wtraj_4_4==6, And(wx_4_4==5, wy_4_4==7)))
s.add(Implies(wtraj_4_5==1, And(wx_4_5==7, wy_4_5==9)))
s.add(Implies(wtraj_4_5==2, And(wx_4_5==5, wy_4_5==11)))
s.add(Implies(wtraj_4_5==3, And(wx_4_5==3, wy_4_5==11)))
s.add(Implies(wtraj_4_5==4, And(wx_4_5==1, wy_4_5==9)))
s.add(Implies(wtraj_4_5==5, And(wx_4_5==3, wy_4_5==7)))
s.add(Implies(wtraj_4_5==6, And(wx_4_5==5, wy_4_5==7)))
s.add(Implies(wtraj_4_6==1, And(wx_4_6==7, wy_4_6==9)))
s.add(Implies(wtraj_4_6==2, And(wx_4_6==5, wy_4_6==11)))
s.add(Implies(wtraj_4_6==3, And(wx_4_6==3, wy_4_6==11)))
s.add(Implies(wtraj_4_6==4, And(wx_4_6==1, wy_4_6==9)))
s.add(Implies(wtraj_4_6==5, And(wx_4_6==3, wy_4_6==7)))
s.add(Implies(wtraj_4_6==6, And(wx_4_6==5, wy_4_6==7)))
s.add(Implies(wtraj_4_7==1, And(wx_4_7==7, wy_4_7==9)))
s.add(Implies(wtraj_4_7==2, And(wx_4_7==5, wy_4_7==11)))
s.add(Implies(wtraj_4_7==3, And(wx_4_7==3, wy_4_7==11)))
s.add(Implies(wtraj_4_7==4, And(wx_4_7==1, wy_4_7==9)))
s.add(Implies(wtraj_4_7==5, And(wx_4_7==3, wy_4_7==7)))
s.add(Implies(wtraj_4_7==6, And(wx_4_7==5, wy_4_7==7)))
s.add(Implies(wtraj_4_8==1, And(wx_4_8==7, wy_4_8==9)))
s.add(Implies(wtraj_4_8==2, And(wx_4_8==5, wy_4_8==11)))
s.add(Implies(wtraj_4_8==3, And(wx_4_8==3, wy_4_8==11)))
s.add(Implies(wtraj_4_8==4, And(wx_4_8==1, wy_4_8==9)))
s.add(Implies(wtraj_4_8==5, And(wx_4_8==3, wy_4_8==7)))
s.add(Implies(wtraj_4_8==6, And(wx_4_8==5, wy_4_8==7)))
s.add(Implies(wtraj_4_9==1, And(wx_4_9==7, wy_4_9==9)))
s.add(Implies(wtraj_4_9==2, And(wx_4_9==5, wy_4_9==11)))
s.add(Implies(wtraj_4_9==3, And(wx_4_9==3, wy_4_9==11)))
s.add(Implies(wtraj_4_9==4, And(wx_4_9==1, wy_4_9==9)))
s.add(Implies(wtraj_4_9==5, And(wx_4_9==3, wy_4_9==7)))
s.add(Implies(wtraj_4_9==6, And(wx_4_9==5, wy_4_9==7)))
s.add(Implies(wtraj_4_10==1, And(wx_4_10==7, wy_4_10==9)))
s.add(Implies(wtraj_4_10==2, And(wx_4_10==5, wy_4_10==11)))
s.add(Implies(wtraj_4_10==3, And(wx_4_10==3, wy_4_10==11)))
s.add(Implies(wtraj_4_10==4, And(wx_4_10==1, wy_4_10==9)))
s.add(Implies(wtraj_4_10==5, And(wx_4_10==3, wy_4_10==7)))
s.add(Implies(wtraj_4_10==6, And(wx_4_10==5, wy_4_10==7)))
s.add(Implies(wtraj_4_11==1, And(wx_4_11==7, wy_4_11==9)))
s.add(Implies(wtraj_4_11==2, And(wx_4_11==5, wy_4_11==11)))
s.add(Implies(wtraj_4_11==3, And(wx_4_11==3, wy_4_11==11)))
s.add(Implies(wtraj_4_11==4, And(wx_4_11==1, wy_4_11==9)))
s.add(Implies(wtraj_4_11==5, And(wx_4_11==3, wy_4_11==7)))
s.add(Implies(wtraj_4_11==6, And(wx_4_11==5, wy_4_11==7)))
s.add(Implies(wtraj_4_12==1, And(wx_4_12==7, wy_4_12==9)))
s.add(Implies(wtraj_4_12==2, And(wx_4_12==5, wy_4_12==11)))
s.add(Implies(wtraj_4_12==3, And(wx_4_12==3, wy_4_12==11)))
s.add(Implies(wtraj_4_12==4, And(wx_4_12==1, wy_4_12==9)))
s.add(Implies(wtraj_4_12==5, And(wx_4_12==3, wy_4_12==7)))
s.add(Implies(wtraj_4_12==6, And(wx_4_12==5, wy_4_12==7)))
s.add(Implies(wtraj_4_13==1, And(wx_4_13==7, wy_4_13==9)))
s.add(Implies(wtraj_4_13==2, And(wx_4_13==5, wy_4_13==11)))
s.add(Implies(wtraj_4_13==3, And(wx_4_13==3, wy_4_13==11)))
s.add(Implies(wtraj_4_13==4, And(wx_4_13==1, wy_4_13==9)))
s.add(Implies(wtraj_4_13==5, And(wx_4_13==3, wy_4_13==7)))
s.add(Implies(wtraj_4_13==6, And(wx_4_13==5, wy_4_13==7)))
s.add(Implies(wtraj_4_14==1, And(wx_4_14==7, wy_4_14==9)))
s.add(Implies(wtraj_4_14==2, And(wx_4_14==5, wy_4_14==11)))
s.add(Implies(wtraj_4_14==3, And(wx_4_14==3, wy_4_14==11)))
s.add(Implies(wtraj_4_14==4, And(wx_4_14==1, wy_4_14==9)))
s.add(Implies(wtraj_4_14==5, And(wx_4_14==3, wy_4_14==7)))
s.add(Implies(wtraj_4_14==6, And(wx_4_14==5, wy_4_14==7)))
s.add(Implies(wtraj_4_15==1, And(wx_4_15==7, wy_4_15==9)))
s.add(Implies(wtraj_4_15==2, And(wx_4_15==5, wy_4_15==11)))
s.add(Implies(wtraj_4_15==3, And(wx_4_15==3, wy_4_15==11)))
s.add(Implies(wtraj_4_15==4, And(wx_4_15==1, wy_4_15==9)))
s.add(Implies(wtraj_4_15==5, And(wx_4_15==3, wy_4_15==7)))
s.add(Implies(wtraj_4_15==6, And(wx_4_15==5, wy_4_15==7)))
s.add(Implies(wtraj_4_16==1, And(wx_4_16==7, wy_4_16==9)))
s.add(Implies(wtraj_4_16==2, And(wx_4_16==5, wy_4_16==11)))
s.add(Implies(wtraj_4_16==3, And(wx_4_16==3, wy_4_16==11)))
s.add(Implies(wtraj_4_16==4, And(wx_4_16==1, wy_4_16==9)))
s.add(Implies(wtraj_4_16==5, And(wx_4_16==3, wy_4_16==7)))
s.add(Implies(wtraj_4_16==6, And(wx_4_16==5, wy_4_16==7)))
s.add(Implies(wtraj_4_17==1, And(wx_4_17==7, wy_4_17==9)))
s.add(Implies(wtraj_4_17==2, And(wx_4_17==5, wy_4_17==11)))
s.add(Implies(wtraj_4_17==3, And(wx_4_17==3, wy_4_17==11)))
s.add(Implies(wtraj_4_17==4, And(wx_4_17==1, wy_4_17==9)))
s.add(Implies(wtraj_4_17==5, And(wx_4_17==3, wy_4_17==7)))
s.add(Implies(wtraj_4_17==6, And(wx_4_17==5, wy_4_17==7)))
s.add(Implies(wtraj_4_18==1, And(wx_4_18==7, wy_4_18==9)))
s.add(Implies(wtraj_4_18==2, And(wx_4_18==5, wy_4_18==11)))
s.add(Implies(wtraj_4_18==3, And(wx_4_18==3, wy_4_18==11)))
s.add(Implies(wtraj_4_18==4, And(wx_4_18==1, wy_4_18==9)))
s.add(Implies(wtraj_4_18==5, And(wx_4_18==3, wy_4_18==7)))
s.add(Implies(wtraj_4_18==6, And(wx_4_18==5, wy_4_18==7)))
s.add(Implies(wtraj_4_19==1, And(wx_4_19==7, wy_4_19==9)))
s.add(Implies(wtraj_4_19==2, And(wx_4_19==5, wy_4_19==11)))
s.add(Implies(wtraj_4_19==3, And(wx_4_19==3, wy_4_19==11)))
s.add(Implies(wtraj_4_19==4, And(wx_4_19==1, wy_4_19==9)))
s.add(Implies(wtraj_4_19==5, And(wx_4_19==3, wy_4_19==7)))
s.add(Implies(wtraj_4_19==6, And(wx_4_19==5, wy_4_19==7)))
s.add(Implies(wtraj_4_20==1, And(wx_4_20==7, wy_4_20==9)))
s.add(Implies(wtraj_4_20==2, And(wx_4_20==5, wy_4_20==11)))
s.add(Implies(wtraj_4_20==3, And(wx_4_20==3, wy_4_20==11)))
s.add(Implies(wtraj_4_20==4, And(wx_4_20==1, wy_4_20==9)))
s.add(Implies(wtraj_4_20==5, And(wx_4_20==3, wy_4_20==7)))
s.add(Implies(wtraj_4_20==6, And(wx_4_20==5, wy_4_20==7)))
s.add(Implies(wtraj_4_21==1, And(wx_4_21==7, wy_4_21==9)))
s.add(Implies(wtraj_4_21==2, And(wx_4_21==5, wy_4_21==11)))
s.add(Implies(wtraj_4_21==3, And(wx_4_21==3, wy_4_21==11)))
s.add(Implies(wtraj_4_21==4, And(wx_4_21==1, wy_4_21==9)))
s.add(Implies(wtraj_4_21==5, And(wx_4_21==3, wy_4_21==7)))
s.add(Implies(wtraj_4_21==6, And(wx_4_21==5, wy_4_21==7)))
s.add(Implies(wtraj_4_22==1, And(wx_4_22==7, wy_4_22==9)))
s.add(Implies(wtraj_4_22==2, And(wx_4_22==5, wy_4_22==11)))
s.add(Implies(wtraj_4_22==3, And(wx_4_22==3, wy_4_22==11)))
s.add(Implies(wtraj_4_22==4, And(wx_4_22==1, wy_4_22==9)))
s.add(Implies(wtraj_4_22==5, And(wx_4_22==3, wy_4_22==7)))
s.add(Implies(wtraj_4_22==6, And(wx_4_22==5, wy_4_22==7)))
s.add(Implies(wtraj_4_23==1, And(wx_4_23==7, wy_4_23==9)))
s.add(Implies(wtraj_4_23==2, And(wx_4_23==5, wy_4_23==11)))
s.add(Implies(wtraj_4_23==3, And(wx_4_23==3, wy_4_23==11)))
s.add(Implies(wtraj_4_23==4, And(wx_4_23==1, wy_4_23==9)))
s.add(Implies(wtraj_4_23==5, And(wx_4_23==3, wy_4_23==7)))
s.add(Implies(wtraj_4_23==6, And(wx_4_23==5, wy_4_23==7)))
s.add(Implies(wtraj_4_24==1, And(wx_4_24==7, wy_4_24==9)))
s.add(Implies(wtraj_4_24==2, And(wx_4_24==5, wy_4_24==11)))
s.add(Implies(wtraj_4_24==3, And(wx_4_24==3, wy_4_24==11)))
s.add(Implies(wtraj_4_24==4, And(wx_4_24==1, wy_4_24==9)))
s.add(Implies(wtraj_4_24==5, And(wx_4_24==3, wy_4_24==7)))
s.add(Implies(wtraj_4_24==6, And(wx_4_24==5, wy_4_24==7)))
s.add(Implies(wtraj_4_25==1, And(wx_4_25==7, wy_4_25==9)))
s.add(Implies(wtraj_4_25==2, And(wx_4_25==5, wy_4_25==11)))
s.add(Implies(wtraj_4_25==3, And(wx_4_25==3, wy_4_25==11)))
s.add(Implies(wtraj_4_25==4, And(wx_4_25==1, wy_4_25==9)))
s.add(Implies(wtraj_4_25==5, And(wx_4_25==3, wy_4_25==7)))
s.add(Implies(wtraj_4_25==6, And(wx_4_25==5, wy_4_25==7)))
s.add(Implies(wtraj_4_26==1, And(wx_4_26==7, wy_4_26==9)))
s.add(Implies(wtraj_4_26==2, And(wx_4_26==5, wy_4_26==11)))
s.add(Implies(wtraj_4_26==3, And(wx_4_26==3, wy_4_26==11)))
s.add(Implies(wtraj_4_26==4, And(wx_4_26==1, wy_4_26==9)))
s.add(Implies(wtraj_4_26==5, And(wx_4_26==3, wy_4_26==7)))
s.add(Implies(wtraj_4_26==6, And(wx_4_26==5, wy_4_26==7)))
s.add(Implies(wtraj_4_27==1, And(wx_4_27==7, wy_4_27==9)))
s.add(Implies(wtraj_4_27==2, And(wx_4_27==5, wy_4_27==11)))
s.add(Implies(wtraj_4_27==3, And(wx_4_27==3, wy_4_27==11)))
s.add(Implies(wtraj_4_27==4, And(wx_4_27==1, wy_4_27==9)))
s.add(Implies(wtraj_4_27==5, And(wx_4_27==3, wy_4_27==7)))
s.add(Implies(wtraj_4_27==6, And(wx_4_27==5, wy_4_27==7)))
s.add(Implies(wtraj_4_28==1, And(wx_4_28==7, wy_4_28==9)))
s.add(Implies(wtraj_4_28==2, And(wx_4_28==5, wy_4_28==11)))
s.add(Implies(wtraj_4_28==3, And(wx_4_28==3, wy_4_28==11)))
s.add(Implies(wtraj_4_28==4, And(wx_4_28==1, wy_4_28==9)))
s.add(Implies(wtraj_4_28==5, And(wx_4_28==3, wy_4_28==7)))
s.add(Implies(wtraj_4_28==6, And(wx_4_28==5, wy_4_28==7)))
s.add(Implies(wtraj_4_29==1, And(wx_4_29==7, wy_4_29==9)))
s.add(Implies(wtraj_4_29==2, And(wx_4_29==5, wy_4_29==11)))
s.add(Implies(wtraj_4_29==3, And(wx_4_29==3, wy_4_29==11)))
s.add(Implies(wtraj_4_29==4, And(wx_4_29==1, wy_4_29==9)))
s.add(Implies(wtraj_4_29==5, And(wx_4_29==3, wy_4_29==7)))
s.add(Implies(wtraj_4_29==6, And(wx_4_29==5, wy_4_29==7)))
s.add(Implies(wtraj_4_30==1, And(wx_4_30==7, wy_4_30==9)))
s.add(Implies(wtraj_4_30==2, And(wx_4_30==5, wy_4_30==11)))
s.add(Implies(wtraj_4_30==3, And(wx_4_30==3, wy_4_30==11)))
s.add(Implies(wtraj_4_30==4, And(wx_4_30==1, wy_4_30==9)))
s.add(Implies(wtraj_4_30==5, And(wx_4_30==3, wy_4_30==7)))
s.add(Implies(wtraj_4_30==6, And(wx_4_30==5, wy_4_30==7)))
s.add(Implies(wtraj_4_31==1, And(wx_4_31==7, wy_4_31==9)))
s.add(Implies(wtraj_4_31==2, And(wx_4_31==5, wy_4_31==11)))
s.add(Implies(wtraj_4_31==3, And(wx_4_31==3, wy_4_31==11)))
s.add(Implies(wtraj_4_31==4, And(wx_4_31==1, wy_4_31==9)))
s.add(Implies(wtraj_4_31==5, And(wx_4_31==3, wy_4_31==7)))
s.add(Implies(wtraj_4_31==6, And(wx_4_31==5, wy_4_31==7)))
s.add(Implies(wtraj_4_32==1, And(wx_4_32==7, wy_4_32==9)))
s.add(Implies(wtraj_4_32==2, And(wx_4_32==5, wy_4_32==11)))
s.add(Implies(wtraj_4_32==3, And(wx_4_32==3, wy_4_32==11)))
s.add(Implies(wtraj_4_32==4, And(wx_4_32==1, wy_4_32==9)))
s.add(Implies(wtraj_4_32==5, And(wx_4_32==3, wy_4_32==7)))
s.add(Implies(wtraj_4_32==6, And(wx_4_32==5, wy_4_32==7)))
s.add(Implies(wtraj_4_33==1, And(wx_4_33==7, wy_4_33==9)))
s.add(Implies(wtraj_4_33==2, And(wx_4_33==5, wy_4_33==11)))
s.add(Implies(wtraj_4_33==3, And(wx_4_33==3, wy_4_33==11)))
s.add(Implies(wtraj_4_33==4, And(wx_4_33==1, wy_4_33==9)))
s.add(Implies(wtraj_4_33==5, And(wx_4_33==3, wy_4_33==7)))
s.add(Implies(wtraj_4_33==6, And(wx_4_33==5, wy_4_33==7)))
s.add(Implies(wtraj_4_34==1, And(wx_4_34==7, wy_4_34==9)))
s.add(Implies(wtraj_4_34==2, And(wx_4_34==5, wy_4_34==11)))
s.add(Implies(wtraj_4_34==3, And(wx_4_34==3, wy_4_34==11)))
s.add(Implies(wtraj_4_34==4, And(wx_4_34==1, wy_4_34==9)))
s.add(Implies(wtraj_4_34==5, And(wx_4_34==3, wy_4_34==7)))
s.add(Implies(wtraj_4_34==6, And(wx_4_34==5, wy_4_34==7)))
s.add(Implies(wtraj_4_35==1, And(wx_4_35==7, wy_4_35==9)))
s.add(Implies(wtraj_4_35==2, And(wx_4_35==5, wy_4_35==11)))
s.add(Implies(wtraj_4_35==3, And(wx_4_35==3, wy_4_35==11)))
s.add(Implies(wtraj_4_35==4, And(wx_4_35==1, wy_4_35==9)))
s.add(Implies(wtraj_4_35==5, And(wx_4_35==3, wy_4_35==7)))
s.add(Implies(wtraj_4_35==6, And(wx_4_35==5, wy_4_35==7)))
s.add(Implies(wtraj_4_36==1, And(wx_4_36==7, wy_4_36==9)))
s.add(Implies(wtraj_4_36==2, And(wx_4_36==5, wy_4_36==11)))
s.add(Implies(wtraj_4_36==3, And(wx_4_36==3, wy_4_36==11)))
s.add(Implies(wtraj_4_36==4, And(wx_4_36==1, wy_4_36==9)))
s.add(Implies(wtraj_4_36==5, And(wx_4_36==3, wy_4_36==7)))
s.add(Implies(wtraj_4_36==6, And(wx_4_36==5, wy_4_36==7)))
s.add(Implies(wtraj_4_37==1, And(wx_4_37==7, wy_4_37==9)))
s.add(Implies(wtraj_4_37==2, And(wx_4_37==5, wy_4_37==11)))
s.add(Implies(wtraj_4_37==3, And(wx_4_37==3, wy_4_37==11)))
s.add(Implies(wtraj_4_37==4, And(wx_4_37==1, wy_4_37==9)))
s.add(Implies(wtraj_4_37==5, And(wx_4_37==3, wy_4_37==7)))
s.add(Implies(wtraj_4_37==6, And(wx_4_37==5, wy_4_37==7)))
s.add(Implies(wtraj_4_38==1, And(wx_4_38==7, wy_4_38==9)))
s.add(Implies(wtraj_4_38==2, And(wx_4_38==5, wy_4_38==11)))
s.add(Implies(wtraj_4_38==3, And(wx_4_38==3, wy_4_38==11)))
s.add(Implies(wtraj_4_38==4, And(wx_4_38==1, wy_4_38==9)))
s.add(Implies(wtraj_4_38==5, And(wx_4_38==3, wy_4_38==7)))
s.add(Implies(wtraj_4_38==6, And(wx_4_38==5, wy_4_38==7)))
s.add(Implies(wtraj_4_39==1, And(wx_4_39==7, wy_4_39==9)))
s.add(Implies(wtraj_4_39==2, And(wx_4_39==5, wy_4_39==11)))
s.add(Implies(wtraj_4_39==3, And(wx_4_39==3, wy_4_39==11)))
s.add(Implies(wtraj_4_39==4, And(wx_4_39==1, wy_4_39==9)))
s.add(Implies(wtraj_4_39==5, And(wx_4_39==3, wy_4_39==7)))
s.add(Implies(wtraj_4_39==6, And(wx_4_39==5, wy_4_39==7)))
s.add(Implies(wtraj_4_40==1, And(wx_4_40==7, wy_4_40==9)))
s.add(Implies(wtraj_4_40==2, And(wx_4_40==5, wy_4_40==11)))
s.add(Implies(wtraj_4_40==3, And(wx_4_40==3, wy_4_40==11)))
s.add(Implies(wtraj_4_40==4, And(wx_4_40==1, wy_4_40==9)))
s.add(Implies(wtraj_4_40==5, And(wx_4_40==3, wy_4_40==7)))
s.add(Implies(wtraj_4_40==6, And(wx_4_40==5, wy_4_40==7)))
s.add(Implies(wtraj_4_41==1, And(wx_4_41==7, wy_4_41==9)))
s.add(Implies(wtraj_4_41==2, And(wx_4_41==5, wy_4_41==11)))
s.add(Implies(wtraj_4_41==3, And(wx_4_41==3, wy_4_41==11)))
s.add(Implies(wtraj_4_41==4, And(wx_4_41==1, wy_4_41==9)))
s.add(Implies(wtraj_4_41==5, And(wx_4_41==3, wy_4_41==7)))
s.add(Implies(wtraj_4_41==6, And(wx_4_41==5, wy_4_41==7)))
s.add(Implies(wtraj_4_42==1, And(wx_4_42==7, wy_4_42==9)))
s.add(Implies(wtraj_4_42==2, And(wx_4_42==5, wy_4_42==11)))
s.add(Implies(wtraj_4_42==3, And(wx_4_42==3, wy_4_42==11)))
s.add(Implies(wtraj_4_42==4, And(wx_4_42==1, wy_4_42==9)))
s.add(Implies(wtraj_4_42==5, And(wx_4_42==3, wy_4_42==7)))
s.add(Implies(wtraj_4_42==6, And(wx_4_42==5, wy_4_42==7)))
s.add(Implies(wtraj_4_43==1, And(wx_4_43==7, wy_4_43==9)))
s.add(Implies(wtraj_4_43==2, And(wx_4_43==5, wy_4_43==11)))
s.add(Implies(wtraj_4_43==3, And(wx_4_43==3, wy_4_43==11)))
s.add(Implies(wtraj_4_43==4, And(wx_4_43==1, wy_4_43==9)))
s.add(Implies(wtraj_4_43==5, And(wx_4_43==3, wy_4_43==7)))
s.add(Implies(wtraj_4_43==6, And(wx_4_43==5, wy_4_43==7)))
s.add(Implies(wtraj_4_44==1, And(wx_4_44==7, wy_4_44==9)))
s.add(Implies(wtraj_4_44==2, And(wx_4_44==5, wy_4_44==11)))
s.add(Implies(wtraj_4_44==3, And(wx_4_44==3, wy_4_44==11)))
s.add(Implies(wtraj_4_44==4, And(wx_4_44==1, wy_4_44==9)))
s.add(Implies(wtraj_4_44==5, And(wx_4_44==3, wy_4_44==7)))
s.add(Implies(wtraj_4_44==6, And(wx_4_44==5, wy_4_44==7)))
s.add(Implies(wtraj_4_45==1, And(wx_4_45==7, wy_4_45==9)))
s.add(Implies(wtraj_4_45==2, And(wx_4_45==5, wy_4_45==11)))
s.add(Implies(wtraj_4_45==3, And(wx_4_45==3, wy_4_45==11)))
s.add(Implies(wtraj_4_45==4, And(wx_4_45==1, wy_4_45==9)))
s.add(Implies(wtraj_4_45==5, And(wx_4_45==3, wy_4_45==7)))
s.add(Implies(wtraj_4_45==6, And(wx_4_45==5, wy_4_45==7)))
s.add(Implies(wtraj_4_46==1, And(wx_4_46==7, wy_4_46==9)))
s.add(Implies(wtraj_4_46==2, And(wx_4_46==5, wy_4_46==11)))
s.add(Implies(wtraj_4_46==3, And(wx_4_46==3, wy_4_46==11)))
s.add(Implies(wtraj_4_46==4, And(wx_4_46==1, wy_4_46==9)))
s.add(Implies(wtraj_4_46==5, And(wx_4_46==3, wy_4_46==7)))
s.add(Implies(wtraj_4_46==6, And(wx_4_46==5, wy_4_46==7)))
s.add(Implies(wtraj_4_47==1, And(wx_4_47==7, wy_4_47==9)))
s.add(Implies(wtraj_4_47==2, And(wx_4_47==5, wy_4_47==11)))
s.add(Implies(wtraj_4_47==3, And(wx_4_47==3, wy_4_47==11)))
s.add(Implies(wtraj_4_47==4, And(wx_4_47==1, wy_4_47==9)))
s.add(Implies(wtraj_4_47==5, And(wx_4_47==3, wy_4_47==7)))
s.add(Implies(wtraj_4_47==6, And(wx_4_47==5, wy_4_47==7)))
s.add(Implies(wtraj_4_48==1, And(wx_4_48==7, wy_4_48==9)))
s.add(Implies(wtraj_4_48==2, And(wx_4_48==5, wy_4_48==11)))
s.add(Implies(wtraj_4_48==3, And(wx_4_48==3, wy_4_48==11)))
s.add(Implies(wtraj_4_48==4, And(wx_4_48==1, wy_4_48==9)))
s.add(Implies(wtraj_4_48==5, And(wx_4_48==3, wy_4_48==7)))
s.add(Implies(wtraj_4_48==6, And(wx_4_48==5, wy_4_48==7)))
s.add(Implies(wtraj_4_49==1, And(wx_4_49==7, wy_4_49==9)))
s.add(Implies(wtraj_4_49==2, And(wx_4_49==5, wy_4_49==11)))
s.add(Implies(wtraj_4_49==3, And(wx_4_49==3, wy_4_49==11)))
s.add(Implies(wtraj_4_49==4, And(wx_4_49==1, wy_4_49==9)))
s.add(Implies(wtraj_4_49==5, And(wx_4_49==3, wy_4_49==7)))
s.add(Implies(wtraj_4_49==6, And(wx_4_49==5, wy_4_49==7)))

# matching : same location for workers
s.add(And(wx_1_1==wx_1_49, wy_1_1==wy_1_49))
s.add(And(wx_2_1==wx_2_49, wy_2_1==wy_2_49))
s.add(And(wx_3_1==wx_3_49, wy_3_1==wy_3_49))
s.add(And(wx_4_1==wx_4_49, wy_4_1==wy_4_49))

# matching : same charge-level for workers
s.add(ch_1_1==ch_1_49)
s.add(ch_2_1==ch_2_49)
s.add(ch_3_1==ch_3_49)
s.add(ch_4_1==ch_4_49)

# matching : same location for rechargers
s.add(And(rx_1_1==rx_1_49, ry_1_1==ry_1_49))

# transition : for workers
rech_amt_1_1 = Int('rech_amt_1_1')
rech_amt_1_2 = Int('rech_amt_1_2')
rech_amt_1_3 = Int('rech_amt_1_3')
rech_amt_1_4 = Int('rech_amt_1_4')
rech_amt_1_5 = Int('rech_amt_1_5')
rech_amt_1_6 = Int('rech_amt_1_6')
rech_amt_1_7 = Int('rech_amt_1_7')
rech_amt_1_8 = Int('rech_amt_1_8')
rech_amt_1_9 = Int('rech_amt_1_9')
rech_amt_1_10 = Int('rech_amt_1_10')
rech_amt_1_11 = Int('rech_amt_1_11')
rech_amt_1_12 = Int('rech_amt_1_12')
rech_amt_1_13 = Int('rech_amt_1_13')
rech_amt_1_14 = Int('rech_amt_1_14')
rech_amt_1_15 = Int('rech_amt_1_15')
rech_amt_1_16 = Int('rech_amt_1_16')
rech_amt_1_17 = Int('rech_amt_1_17')
rech_amt_1_18 = Int('rech_amt_1_18')
rech_amt_1_19 = Int('rech_amt_1_19')
rech_amt_1_20 = Int('rech_amt_1_20')
rech_amt_1_21 = Int('rech_amt_1_21')
rech_amt_1_22 = Int('rech_amt_1_22')
rech_amt_1_23 = Int('rech_amt_1_23')
rech_amt_1_24 = Int('rech_amt_1_24')
rech_amt_1_25 = Int('rech_amt_1_25')
rech_amt_1_26 = Int('rech_amt_1_26')
rech_amt_1_27 = Int('rech_amt_1_27')
rech_amt_1_28 = Int('rech_amt_1_28')
rech_amt_1_29 = Int('rech_amt_1_29')
rech_amt_1_30 = Int('rech_amt_1_30')
rech_amt_1_31 = Int('rech_amt_1_31')
rech_amt_1_32 = Int('rech_amt_1_32')
rech_amt_1_33 = Int('rech_amt_1_33')
rech_amt_1_34 = Int('rech_amt_1_34')
rech_amt_1_35 = Int('rech_amt_1_35')
rech_amt_1_36 = Int('rech_amt_1_36')
rech_amt_1_37 = Int('rech_amt_1_37')
rech_amt_1_38 = Int('rech_amt_1_38')
rech_amt_1_39 = Int('rech_amt_1_39')
rech_amt_1_40 = Int('rech_amt_1_40')
rech_amt_1_41 = Int('rech_amt_1_41')
rech_amt_1_42 = Int('rech_amt_1_42')
rech_amt_1_43 = Int('rech_amt_1_43')
rech_amt_1_44 = Int('rech_amt_1_44')
rech_amt_1_45 = Int('rech_amt_1_45')
rech_amt_1_46 = Int('rech_amt_1_46')
rech_amt_1_47 = Int('rech_amt_1_47')
rech_amt_1_48 = Int('rech_amt_1_48')
rech_amt_2_1 = Int('rech_amt_2_1')
rech_amt_2_2 = Int('rech_amt_2_2')
rech_amt_2_3 = Int('rech_amt_2_3')
rech_amt_2_4 = Int('rech_amt_2_4')
rech_amt_2_5 = Int('rech_amt_2_5')
rech_amt_2_6 = Int('rech_amt_2_6')
rech_amt_2_7 = Int('rech_amt_2_7')
rech_amt_2_8 = Int('rech_amt_2_8')
rech_amt_2_9 = Int('rech_amt_2_9')
rech_amt_2_10 = Int('rech_amt_2_10')
rech_amt_2_11 = Int('rech_amt_2_11')
rech_amt_2_12 = Int('rech_amt_2_12')
rech_amt_2_13 = Int('rech_amt_2_13')
rech_amt_2_14 = Int('rech_amt_2_14')
rech_amt_2_15 = Int('rech_amt_2_15')
rech_amt_2_16 = Int('rech_amt_2_16')
rech_amt_2_17 = Int('rech_amt_2_17')
rech_amt_2_18 = Int('rech_amt_2_18')
rech_amt_2_19 = Int('rech_amt_2_19')
rech_amt_2_20 = Int('rech_amt_2_20')
rech_amt_2_21 = Int('rech_amt_2_21')
rech_amt_2_22 = Int('rech_amt_2_22')
rech_amt_2_23 = Int('rech_amt_2_23')
rech_amt_2_24 = Int('rech_amt_2_24')
rech_amt_2_25 = Int('rech_amt_2_25')
rech_amt_2_26 = Int('rech_amt_2_26')
rech_amt_2_27 = Int('rech_amt_2_27')
rech_amt_2_28 = Int('rech_amt_2_28')
rech_amt_2_29 = Int('rech_amt_2_29')
rech_amt_2_30 = Int('rech_amt_2_30')
rech_amt_2_31 = Int('rech_amt_2_31')
rech_amt_2_32 = Int('rech_amt_2_32')
rech_amt_2_33 = Int('rech_amt_2_33')
rech_amt_2_34 = Int('rech_amt_2_34')
rech_amt_2_35 = Int('rech_amt_2_35')
rech_amt_2_36 = Int('rech_amt_2_36')
rech_amt_2_37 = Int('rech_amt_2_37')
rech_amt_2_38 = Int('rech_amt_2_38')
rech_amt_2_39 = Int('rech_amt_2_39')
rech_amt_2_40 = Int('rech_amt_2_40')
rech_amt_2_41 = Int('rech_amt_2_41')
rech_amt_2_42 = Int('rech_amt_2_42')
rech_amt_2_43 = Int('rech_amt_2_43')
rech_amt_2_44 = Int('rech_amt_2_44')
rech_amt_2_45 = Int('rech_amt_2_45')
rech_amt_2_46 = Int('rech_amt_2_46')
rech_amt_2_47 = Int('rech_amt_2_47')
rech_amt_2_48 = Int('rech_amt_2_48')
rech_amt_3_1 = Int('rech_amt_3_1')
rech_amt_3_2 = Int('rech_amt_3_2')
rech_amt_3_3 = Int('rech_amt_3_3')
rech_amt_3_4 = Int('rech_amt_3_4')
rech_amt_3_5 = Int('rech_amt_3_5')
rech_amt_3_6 = Int('rech_amt_3_6')
rech_amt_3_7 = Int('rech_amt_3_7')
rech_amt_3_8 = Int('rech_amt_3_8')
rech_amt_3_9 = Int('rech_amt_3_9')
rech_amt_3_10 = Int('rech_amt_3_10')
rech_amt_3_11 = Int('rech_amt_3_11')
rech_amt_3_12 = Int('rech_amt_3_12')
rech_amt_3_13 = Int('rech_amt_3_13')
rech_amt_3_14 = Int('rech_amt_3_14')
rech_amt_3_15 = Int('rech_amt_3_15')
rech_amt_3_16 = Int('rech_amt_3_16')
rech_amt_3_17 = Int('rech_amt_3_17')
rech_amt_3_18 = Int('rech_amt_3_18')
rech_amt_3_19 = Int('rech_amt_3_19')
rech_amt_3_20 = Int('rech_amt_3_20')
rech_amt_3_21 = Int('rech_amt_3_21')
rech_amt_3_22 = Int('rech_amt_3_22')
rech_amt_3_23 = Int('rech_amt_3_23')
rech_amt_3_24 = Int('rech_amt_3_24')
rech_amt_3_25 = Int('rech_amt_3_25')
rech_amt_3_26 = Int('rech_amt_3_26')
rech_amt_3_27 = Int('rech_amt_3_27')
rech_amt_3_28 = Int('rech_amt_3_28')
rech_amt_3_29 = Int('rech_amt_3_29')
rech_amt_3_30 = Int('rech_amt_3_30')
rech_amt_3_31 = Int('rech_amt_3_31')
rech_amt_3_32 = Int('rech_amt_3_32')
rech_amt_3_33 = Int('rech_amt_3_33')
rech_amt_3_34 = Int('rech_amt_3_34')
rech_amt_3_35 = Int('rech_amt_3_35')
rech_amt_3_36 = Int('rech_amt_3_36')
rech_amt_3_37 = Int('rech_amt_3_37')
rech_amt_3_38 = Int('rech_amt_3_38')
rech_amt_3_39 = Int('rech_amt_3_39')
rech_amt_3_40 = Int('rech_amt_3_40')
rech_amt_3_41 = Int('rech_amt_3_41')
rech_amt_3_42 = Int('rech_amt_3_42')
rech_amt_3_43 = Int('rech_amt_3_43')
rech_amt_3_44 = Int('rech_amt_3_44')
rech_amt_3_45 = Int('rech_amt_3_45')
rech_amt_3_46 = Int('rech_amt_3_46')
rech_amt_3_47 = Int('rech_amt_3_47')
rech_amt_3_48 = Int('rech_amt_3_48')
rech_amt_4_1 = Int('rech_amt_4_1')
rech_amt_4_2 = Int('rech_amt_4_2')
rech_amt_4_3 = Int('rech_amt_4_3')
rech_amt_4_4 = Int('rech_amt_4_4')
rech_amt_4_5 = Int('rech_amt_4_5')
rech_amt_4_6 = Int('rech_amt_4_6')
rech_amt_4_7 = Int('rech_amt_4_7')
rech_amt_4_8 = Int('rech_amt_4_8')
rech_amt_4_9 = Int('rech_amt_4_9')
rech_amt_4_10 = Int('rech_amt_4_10')
rech_amt_4_11 = Int('rech_amt_4_11')
rech_amt_4_12 = Int('rech_amt_4_12')
rech_amt_4_13 = Int('rech_amt_4_13')
rech_amt_4_14 = Int('rech_amt_4_14')
rech_amt_4_15 = Int('rech_amt_4_15')
rech_amt_4_16 = Int('rech_amt_4_16')
rech_amt_4_17 = Int('rech_amt_4_17')
rech_amt_4_18 = Int('rech_amt_4_18')
rech_amt_4_19 = Int('rech_amt_4_19')
rech_amt_4_20 = Int('rech_amt_4_20')
rech_amt_4_21 = Int('rech_amt_4_21')
rech_amt_4_22 = Int('rech_amt_4_22')
rech_amt_4_23 = Int('rech_amt_4_23')
rech_amt_4_24 = Int('rech_amt_4_24')
rech_amt_4_25 = Int('rech_amt_4_25')
rech_amt_4_26 = Int('rech_amt_4_26')
rech_amt_4_27 = Int('rech_amt_4_27')
rech_amt_4_28 = Int('rech_amt_4_28')
rech_amt_4_29 = Int('rech_amt_4_29')
rech_amt_4_30 = Int('rech_amt_4_30')
rech_amt_4_31 = Int('rech_amt_4_31')
rech_amt_4_32 = Int('rech_amt_4_32')
rech_amt_4_33 = Int('rech_amt_4_33')
rech_amt_4_34 = Int('rech_amt_4_34')
rech_amt_4_35 = Int('rech_amt_4_35')
rech_amt_4_36 = Int('rech_amt_4_36')
rech_amt_4_37 = Int('rech_amt_4_37')
rech_amt_4_38 = Int('rech_amt_4_38')
rech_amt_4_39 = Int('rech_amt_4_39')
rech_amt_4_40 = Int('rech_amt_4_40')
rech_amt_4_41 = Int('rech_amt_4_41')
rech_amt_4_42 = Int('rech_amt_4_42')
rech_amt_4_43 = Int('rech_amt_4_43')
rech_amt_4_44 = Int('rech_amt_4_44')
rech_amt_4_45 = Int('rech_amt_4_45')
rech_amt_4_46 = Int('rech_amt_4_46')
rech_amt_4_47 = Int('rech_amt_4_47')
rech_amt_4_48 = Int('rech_amt_4_48')

s.add(And(rech_amt_1_1<=10, rech_amt_1_1>0))
s.add(And(rech_amt_1_2<=10, rech_amt_1_2>0))
s.add(And(rech_amt_1_3<=10, rech_amt_1_3>0))
s.add(And(rech_amt_1_4<=10, rech_amt_1_4>0))
s.add(And(rech_amt_1_5<=10, rech_amt_1_5>0))
s.add(And(rech_amt_1_6<=10, rech_amt_1_6>0))
s.add(And(rech_amt_1_7<=10, rech_amt_1_7>0))
s.add(And(rech_amt_1_8<=10, rech_amt_1_8>0))
s.add(And(rech_amt_1_9<=10, rech_amt_1_9>0))
s.add(And(rech_amt_1_10<=10, rech_amt_1_10>0))
s.add(And(rech_amt_1_11<=10, rech_amt_1_11>0))
s.add(And(rech_amt_1_12<=10, rech_amt_1_12>0))
s.add(And(rech_amt_1_13<=10, rech_amt_1_13>0))
s.add(And(rech_amt_1_14<=10, rech_amt_1_14>0))
s.add(And(rech_amt_1_15<=10, rech_amt_1_15>0))
s.add(And(rech_amt_1_16<=10, rech_amt_1_16>0))
s.add(And(rech_amt_1_17<=10, rech_amt_1_17>0))
s.add(And(rech_amt_1_18<=10, rech_amt_1_18>0))
s.add(And(rech_amt_1_19<=10, rech_amt_1_19>0))
s.add(And(rech_amt_1_20<=10, rech_amt_1_20>0))
s.add(And(rech_amt_1_21<=10, rech_amt_1_21>0))
s.add(And(rech_amt_1_22<=10, rech_amt_1_22>0))
s.add(And(rech_amt_1_23<=10, rech_amt_1_23>0))
s.add(And(rech_amt_1_24<=10, rech_amt_1_24>0))
s.add(And(rech_amt_1_25<=10, rech_amt_1_25>0))
s.add(And(rech_amt_1_26<=10, rech_amt_1_26>0))
s.add(And(rech_amt_1_27<=10, rech_amt_1_27>0))
s.add(And(rech_amt_1_28<=10, rech_amt_1_28>0))
s.add(And(rech_amt_1_29<=10, rech_amt_1_29>0))
s.add(And(rech_amt_1_30<=10, rech_amt_1_30>0))
s.add(And(rech_amt_1_31<=10, rech_amt_1_31>0))
s.add(And(rech_amt_1_32<=10, rech_amt_1_32>0))
s.add(And(rech_amt_1_33<=10, rech_amt_1_33>0))
s.add(And(rech_amt_1_34<=10, rech_amt_1_34>0))
s.add(And(rech_amt_1_35<=10, rech_amt_1_35>0))
s.add(And(rech_amt_1_36<=10, rech_amt_1_36>0))
s.add(And(rech_amt_1_37<=10, rech_amt_1_37>0))
s.add(And(rech_amt_1_38<=10, rech_amt_1_38>0))
s.add(And(rech_amt_1_39<=10, rech_amt_1_39>0))
s.add(And(rech_amt_1_40<=10, rech_amt_1_40>0))
s.add(And(rech_amt_1_41<=10, rech_amt_1_41>0))
s.add(And(rech_amt_1_42<=10, rech_amt_1_42>0))
s.add(And(rech_amt_1_43<=10, rech_amt_1_43>0))
s.add(And(rech_amt_1_44<=10, rech_amt_1_44>0))
s.add(And(rech_amt_1_45<=10, rech_amt_1_45>0))
s.add(And(rech_amt_1_46<=10, rech_amt_1_46>0))
s.add(And(rech_amt_1_47<=10, rech_amt_1_47>0))
s.add(And(rech_amt_1_48<=10, rech_amt_1_48>0))
s.add(And(rech_amt_2_1<=10, rech_amt_2_1>0))
s.add(And(rech_amt_2_2<=10, rech_amt_2_2>0))
s.add(And(rech_amt_2_3<=10, rech_amt_2_3>0))
s.add(And(rech_amt_2_4<=10, rech_amt_2_4>0))
s.add(And(rech_amt_2_5<=10, rech_amt_2_5>0))
s.add(And(rech_amt_2_6<=10, rech_amt_2_6>0))
s.add(And(rech_amt_2_7<=10, rech_amt_2_7>0))
s.add(And(rech_amt_2_8<=10, rech_amt_2_8>0))
s.add(And(rech_amt_2_9<=10, rech_amt_2_9>0))
s.add(And(rech_amt_2_10<=10, rech_amt_2_10>0))
s.add(And(rech_amt_2_11<=10, rech_amt_2_11>0))
s.add(And(rech_amt_2_12<=10, rech_amt_2_12>0))
s.add(And(rech_amt_2_13<=10, rech_amt_2_13>0))
s.add(And(rech_amt_2_14<=10, rech_amt_2_14>0))
s.add(And(rech_amt_2_15<=10, rech_amt_2_15>0))
s.add(And(rech_amt_2_16<=10, rech_amt_2_16>0))
s.add(And(rech_amt_2_17<=10, rech_amt_2_17>0))
s.add(And(rech_amt_2_18<=10, rech_amt_2_18>0))
s.add(And(rech_amt_2_19<=10, rech_amt_2_19>0))
s.add(And(rech_amt_2_20<=10, rech_amt_2_20>0))
s.add(And(rech_amt_2_21<=10, rech_amt_2_21>0))
s.add(And(rech_amt_2_22<=10, rech_amt_2_22>0))
s.add(And(rech_amt_2_23<=10, rech_amt_2_23>0))
s.add(And(rech_amt_2_24<=10, rech_amt_2_24>0))
s.add(And(rech_amt_2_25<=10, rech_amt_2_25>0))
s.add(And(rech_amt_2_26<=10, rech_amt_2_26>0))
s.add(And(rech_amt_2_27<=10, rech_amt_2_27>0))
s.add(And(rech_amt_2_28<=10, rech_amt_2_28>0))
s.add(And(rech_amt_2_29<=10, rech_amt_2_29>0))
s.add(And(rech_amt_2_30<=10, rech_amt_2_30>0))
s.add(And(rech_amt_2_31<=10, rech_amt_2_31>0))
s.add(And(rech_amt_2_32<=10, rech_amt_2_32>0))
s.add(And(rech_amt_2_33<=10, rech_amt_2_33>0))
s.add(And(rech_amt_2_34<=10, rech_amt_2_34>0))
s.add(And(rech_amt_2_35<=10, rech_amt_2_35>0))
s.add(And(rech_amt_2_36<=10, rech_amt_2_36>0))
s.add(And(rech_amt_2_37<=10, rech_amt_2_37>0))
s.add(And(rech_amt_2_38<=10, rech_amt_2_38>0))
s.add(And(rech_amt_2_39<=10, rech_amt_2_39>0))
s.add(And(rech_amt_2_40<=10, rech_amt_2_40>0))
s.add(And(rech_amt_2_41<=10, rech_amt_2_41>0))
s.add(And(rech_amt_2_42<=10, rech_amt_2_42>0))
s.add(And(rech_amt_2_43<=10, rech_amt_2_43>0))
s.add(And(rech_amt_2_44<=10, rech_amt_2_44>0))
s.add(And(rech_amt_2_45<=10, rech_amt_2_45>0))
s.add(And(rech_amt_2_46<=10, rech_amt_2_46>0))
s.add(And(rech_amt_2_47<=10, rech_amt_2_47>0))
s.add(And(rech_amt_2_48<=10, rech_amt_2_48>0))
s.add(And(rech_amt_3_1<=10, rech_amt_3_1>0))
s.add(And(rech_amt_3_2<=10, rech_amt_3_2>0))
s.add(And(rech_amt_3_3<=10, rech_amt_3_3>0))
s.add(And(rech_amt_3_4<=10, rech_amt_3_4>0))
s.add(And(rech_amt_3_5<=10, rech_amt_3_5>0))
s.add(And(rech_amt_3_6<=10, rech_amt_3_6>0))
s.add(And(rech_amt_3_7<=10, rech_amt_3_7>0))
s.add(And(rech_amt_3_8<=10, rech_amt_3_8>0))
s.add(And(rech_amt_3_9<=10, rech_amt_3_9>0))
s.add(And(rech_amt_3_10<=10, rech_amt_3_10>0))
s.add(And(rech_amt_3_11<=10, rech_amt_3_11>0))
s.add(And(rech_amt_3_12<=10, rech_amt_3_12>0))
s.add(And(rech_amt_3_13<=10, rech_amt_3_13>0))
s.add(And(rech_amt_3_14<=10, rech_amt_3_14>0))
s.add(And(rech_amt_3_15<=10, rech_amt_3_15>0))
s.add(And(rech_amt_3_16<=10, rech_amt_3_16>0))
s.add(And(rech_amt_3_17<=10, rech_amt_3_17>0))
s.add(And(rech_amt_3_18<=10, rech_amt_3_18>0))
s.add(And(rech_amt_3_19<=10, rech_amt_3_19>0))
s.add(And(rech_amt_3_20<=10, rech_amt_3_20>0))
s.add(And(rech_amt_3_21<=10, rech_amt_3_21>0))
s.add(And(rech_amt_3_22<=10, rech_amt_3_22>0))
s.add(And(rech_amt_3_23<=10, rech_amt_3_23>0))
s.add(And(rech_amt_3_24<=10, rech_amt_3_24>0))
s.add(And(rech_amt_3_25<=10, rech_amt_3_25>0))
s.add(And(rech_amt_3_26<=10, rech_amt_3_26>0))
s.add(And(rech_amt_3_27<=10, rech_amt_3_27>0))
s.add(And(rech_amt_3_28<=10, rech_amt_3_28>0))
s.add(And(rech_amt_3_29<=10, rech_amt_3_29>0))
s.add(And(rech_amt_3_30<=10, rech_amt_3_30>0))
s.add(And(rech_amt_3_31<=10, rech_amt_3_31>0))
s.add(And(rech_amt_3_32<=10, rech_amt_3_32>0))
s.add(And(rech_amt_3_33<=10, rech_amt_3_33>0))
s.add(And(rech_amt_3_34<=10, rech_amt_3_34>0))
s.add(And(rech_amt_3_35<=10, rech_amt_3_35>0))
s.add(And(rech_amt_3_36<=10, rech_amt_3_36>0))
s.add(And(rech_amt_3_37<=10, rech_amt_3_37>0))
s.add(And(rech_amt_3_38<=10, rech_amt_3_38>0))
s.add(And(rech_amt_3_39<=10, rech_amt_3_39>0))
s.add(And(rech_amt_3_40<=10, rech_amt_3_40>0))
s.add(And(rech_amt_3_41<=10, rech_amt_3_41>0))
s.add(And(rech_amt_3_42<=10, rech_amt_3_42>0))
s.add(And(rech_amt_3_43<=10, rech_amt_3_43>0))
s.add(And(rech_amt_3_44<=10, rech_amt_3_44>0))
s.add(And(rech_amt_3_45<=10, rech_amt_3_45>0))
s.add(And(rech_amt_3_46<=10, rech_amt_3_46>0))
s.add(And(rech_amt_3_47<=10, rech_amt_3_47>0))
s.add(And(rech_amt_3_48<=10, rech_amt_3_48>0))
s.add(And(rech_amt_4_1<=10, rech_amt_4_1>0))
s.add(And(rech_amt_4_2<=10, rech_amt_4_2>0))
s.add(And(rech_amt_4_3<=10, rech_amt_4_3>0))
s.add(And(rech_amt_4_4<=10, rech_amt_4_4>0))
s.add(And(rech_amt_4_5<=10, rech_amt_4_5>0))
s.add(And(rech_amt_4_6<=10, rech_amt_4_6>0))
s.add(And(rech_amt_4_7<=10, rech_amt_4_7>0))
s.add(And(rech_amt_4_8<=10, rech_amt_4_8>0))
s.add(And(rech_amt_4_9<=10, rech_amt_4_9>0))
s.add(And(rech_amt_4_10<=10, rech_amt_4_10>0))
s.add(And(rech_amt_4_11<=10, rech_amt_4_11>0))
s.add(And(rech_amt_4_12<=10, rech_amt_4_12>0))
s.add(And(rech_amt_4_13<=10, rech_amt_4_13>0))
s.add(And(rech_amt_4_14<=10, rech_amt_4_14>0))
s.add(And(rech_amt_4_15<=10, rech_amt_4_15>0))
s.add(And(rech_amt_4_16<=10, rech_amt_4_16>0))
s.add(And(rech_amt_4_17<=10, rech_amt_4_17>0))
s.add(And(rech_amt_4_18<=10, rech_amt_4_18>0))
s.add(And(rech_amt_4_19<=10, rech_amt_4_19>0))
s.add(And(rech_amt_4_20<=10, rech_amt_4_20>0))
s.add(And(rech_amt_4_21<=10, rech_amt_4_21>0))
s.add(And(rech_amt_4_22<=10, rech_amt_4_22>0))
s.add(And(rech_amt_4_23<=10, rech_amt_4_23>0))
s.add(And(rech_amt_4_24<=10, rech_amt_4_24>0))
s.add(And(rech_amt_4_25<=10, rech_amt_4_25>0))
s.add(And(rech_amt_4_26<=10, rech_amt_4_26>0))
s.add(And(rech_amt_4_27<=10, rech_amt_4_27>0))
s.add(And(rech_amt_4_28<=10, rech_amt_4_28>0))
s.add(And(rech_amt_4_29<=10, rech_amt_4_29>0))
s.add(And(rech_amt_4_30<=10, rech_amt_4_30>0))
s.add(And(rech_amt_4_31<=10, rech_amt_4_31>0))
s.add(And(rech_amt_4_32<=10, rech_amt_4_32>0))
s.add(And(rech_amt_4_33<=10, rech_amt_4_33>0))
s.add(And(rech_amt_4_34<=10, rech_amt_4_34>0))
s.add(And(rech_amt_4_35<=10, rech_amt_4_35>0))
s.add(And(rech_amt_4_36<=10, rech_amt_4_36>0))
s.add(And(rech_amt_4_37<=10, rech_amt_4_37>0))
s.add(And(rech_amt_4_38<=10, rech_amt_4_38>0))
s.add(And(rech_amt_4_39<=10, rech_amt_4_39>0))
s.add(And(rech_amt_4_40<=10, rech_amt_4_40>0))
s.add(And(rech_amt_4_41<=10, rech_amt_4_41>0))
s.add(And(rech_amt_4_42<=10, rech_amt_4_42>0))
s.add(And(rech_amt_4_43<=10, rech_amt_4_43>0))
s.add(And(rech_amt_4_44<=10, rech_amt_4_44>0))
s.add(And(rech_amt_4_45<=10, rech_amt_4_45>0))
s.add(And(rech_amt_4_46<=10, rech_amt_4_46>0))
s.add(And(rech_amt_4_47<=10, rech_amt_4_47>0))
s.add(And(rech_amt_4_48<=10, rech_amt_4_48>0))

# recharging : intermediate
fch_1 = Int('fch_1')
s.add(fch_1==20)

# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_1_1<4,wprim_1_1==1), 
And(wtraj_1_2==wtraj_1_1+1, ch_1_2==ch_1_1 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_1_1==4,wprim_1_1==1), 
And(wtraj_1_2==1, ch_1_2==ch_1_1 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_1_1==0), 
And(wtraj_1_2==wtraj_1_1, ch_1_2==ch_1_1)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_1_2<4,wprim_1_2==1), 
And(wtraj_1_3==wtraj_1_2+1, ch_1_3==ch_1_2 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_1_2==4,wprim_1_2==1), 
And(wtraj_1_3==1, ch_1_3==ch_1_2 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_1_2==0), 
And(wtraj_1_3==wtraj_1_2, ch_1_3==ch_1_2)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_1_3<4,wprim_1_3==1), 
And(wtraj_1_4==wtraj_1_3+1, ch_1_4==ch_1_3 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_1_3==4,wprim_1_3==1), 
And(wtraj_1_4==1, ch_1_4==ch_1_3 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_1_3==0), 
And(wtraj_1_4==wtraj_1_3, ch_1_4==ch_1_3)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_1_4<4,wprim_1_4==1), 
And(wtraj_1_5==wtraj_1_4+1, ch_1_5==ch_1_4 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_1_4==4,wprim_1_4==1), 
And(wtraj_1_5==1, ch_1_5==ch_1_4 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_1_4==0), 
And(wtraj_1_5==wtraj_1_4, ch_1_5==ch_1_4)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_1_5<4,wprim_1_5==1), 
And(wtraj_1_6==wtraj_1_5+1, ch_1_6==ch_1_5 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_1_5==4,wprim_1_5==1), 
And(wtraj_1_6==1, ch_1_6==ch_1_5 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_1_5==0), 
And(wtraj_1_6==wtraj_1_5, ch_1_6==ch_1_5)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_1_6<4,wprim_1_6==1), 
And(wtraj_1_7==wtraj_1_6+1, ch_1_7==ch_1_6 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_1_6==4,wprim_1_6==1), 
And(wtraj_1_7==1, ch_1_7==ch_1_6 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_1_6==0), 
And(wtraj_1_7==wtraj_1_6, ch_1_7==ch_1_6)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_1_7<4,wprim_1_7==1), 
And(wtraj_1_8==wtraj_1_7+1, ch_1_8==ch_1_7 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_1_7==4,wprim_1_7==1), 
And(wtraj_1_8==1, ch_1_8==ch_1_7 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_1_7==0), 
And(wtraj_1_8==wtraj_1_7, ch_1_8==ch_1_7)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_1_8<4,wprim_1_8==1), 
And(wtraj_1_9==wtraj_1_8+1, ch_1_9==ch_1_8 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_1_8==4,wprim_1_8==1), 
And(wtraj_1_9==1, ch_1_9==ch_1_8 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_1_8==0), 
And(wtraj_1_9==wtraj_1_8, ch_1_9==ch_1_8)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_1_9<4,wprim_1_9==1), 
And(wtraj_1_10==wtraj_1_9+1, ch_1_10==ch_1_9 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_1_9==4,wprim_1_9==1), 
And(wtraj_1_10==1, ch_1_10==ch_1_9 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_1_9==0), 
And(wtraj_1_10==wtraj_1_9, ch_1_10==ch_1_9)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_1_10<4,wprim_1_10==1), 
And(wtraj_1_11==wtraj_1_10+1, ch_1_11==ch_1_10 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_1_10==4,wprim_1_10==1), 
And(wtraj_1_11==1, ch_1_11==ch_1_10 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_1_10==0), 
And(wtraj_1_11==wtraj_1_10, ch_1_11==ch_1_10)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_1_11<4,wprim_1_11==1), 
And(wtraj_1_12==wtraj_1_11+1, ch_1_12==ch_1_11 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_1_11==4,wprim_1_11==1), 
And(wtraj_1_12==1, ch_1_12==ch_1_11 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_1_11==0), 
And(wtraj_1_12==wtraj_1_11, ch_1_12==ch_1_11)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_1_12<4,wprim_1_12==1), 
And(wtraj_1_13==wtraj_1_12+1, ch_1_13==ch_1_12 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_1_12==4,wprim_1_12==1), 
And(wtraj_1_13==1, ch_1_13==ch_1_12 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_1_12==0), 
And(wtraj_1_13==wtraj_1_12, ch_1_13==ch_1_12)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_1_13<4,wprim_1_13==1), 
And(wtraj_1_14==wtraj_1_13+1, ch_1_14==ch_1_13 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_1_13==4,wprim_1_13==1), 
And(wtraj_1_14==1, ch_1_14==ch_1_13 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_1_13==0), 
And(wtraj_1_14==wtraj_1_13, ch_1_14==ch_1_13)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_1_14<4,wprim_1_14==1), 
And(wtraj_1_15==wtraj_1_14+1, ch_1_15==ch_1_14 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_1_14==4,wprim_1_14==1), 
And(wtraj_1_15==1, ch_1_15==ch_1_14 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_1_14==0), 
And(wtraj_1_15==wtraj_1_14, ch_1_15==ch_1_14)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_1_15<4,wprim_1_15==1), 
And(wtraj_1_16==wtraj_1_15+1, ch_1_16==ch_1_15 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_1_15==4,wprim_1_15==1), 
And(wtraj_1_16==1, ch_1_16==ch_1_15 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_1_15==0), 
And(wtraj_1_16==wtraj_1_15, ch_1_16==ch_1_15)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_1_16<4,wprim_1_16==1), 
And(wtraj_1_17==wtraj_1_16+1, ch_1_17==ch_1_16 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_1_16==4,wprim_1_16==1), 
And(wtraj_1_17==1, ch_1_17==ch_1_16 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_1_16==0), 
And(wtraj_1_17==wtraj_1_16, ch_1_17==ch_1_16)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_1_17<4,wprim_1_17==1), 
And(wtraj_1_18==wtraj_1_17+1, ch_1_18==ch_1_17 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_1_17==4,wprim_1_17==1), 
And(wtraj_1_18==1, ch_1_18==ch_1_17 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_1_17==0), 
And(wtraj_1_18==wtraj_1_17, ch_1_18==ch_1_17)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_1_18<4,wprim_1_18==1), 
And(wtraj_1_19==wtraj_1_18+1, ch_1_19==ch_1_18 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_1_18==4,wprim_1_18==1), 
And(wtraj_1_19==1, ch_1_19==ch_1_18 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_1_18==0), 
And(wtraj_1_19==wtraj_1_18, ch_1_19==ch_1_18)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_1_19<4,wprim_1_19==1), 
And(wtraj_1_20==wtraj_1_19+1, ch_1_20==ch_1_19 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_1_19==4,wprim_1_19==1), 
And(wtraj_1_20==1, ch_1_20==ch_1_19 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_1_19==0), 
And(wtraj_1_20==wtraj_1_19, ch_1_20==ch_1_19)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_1_20<4,wprim_1_20==1), 
And(wtraj_1_21==wtraj_1_20+1, ch_1_21==ch_1_20 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_1_20==4,wprim_1_20==1), 
And(wtraj_1_21==1, ch_1_21==ch_1_20 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_1_20==0), 
And(wtraj_1_21==wtraj_1_20, ch_1_21==ch_1_20)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_1_21<4,wprim_1_21==1), 
And(wtraj_1_22==wtraj_1_21+1, ch_1_22==ch_1_21 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_1_21==4,wprim_1_21==1), 
And(wtraj_1_22==1, ch_1_22==ch_1_21 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_1_21==0), 
And(wtraj_1_22==wtraj_1_21, ch_1_22==ch_1_21)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_1_22<4,wprim_1_22==1), 
And(wtraj_1_23==wtraj_1_22+1, ch_1_23==ch_1_22 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_1_22==4,wprim_1_22==1), 
And(wtraj_1_23==1, ch_1_23==ch_1_22 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_1_22==0), 
And(wtraj_1_23==wtraj_1_22, ch_1_23==ch_1_22)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_1_23<4,wprim_1_23==1), 
And(wtraj_1_24==wtraj_1_23+1, ch_1_24==ch_1_23 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_1_23==4,wprim_1_23==1), 
And(wtraj_1_24==1, ch_1_24==ch_1_23 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_1_23==0), 
And(wtraj_1_24==wtraj_1_23, ch_1_24==ch_1_23)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_1_24<4,wprim_1_24==1), 
And(wtraj_1_25==wtraj_1_24+1, ch_1_25==ch_1_24 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_1_24==4,wprim_1_24==1), 
And(wtraj_1_25==1, ch_1_25==ch_1_24 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_1_24==0), 
And(wtraj_1_25==wtraj_1_24, ch_1_25==ch_1_24)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_1_25<4,wprim_1_25==1), 
And(wtraj_1_26==wtraj_1_25+1, ch_1_26==ch_1_25 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_1_25==4,wprim_1_25==1), 
And(wtraj_1_26==1, ch_1_26==ch_1_25 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_1_25==0), 
And(wtraj_1_26==wtraj_1_25, ch_1_26==ch_1_25)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_1_26<4,wprim_1_26==1), 
And(wtraj_1_27==wtraj_1_26+1, ch_1_27==ch_1_26 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_1_26==4,wprim_1_26==1), 
And(wtraj_1_27==1, ch_1_27==ch_1_26 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_1_26==0), 
And(wtraj_1_27==wtraj_1_26, ch_1_27==ch_1_26)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_1_27<4,wprim_1_27==1), 
And(wtraj_1_28==wtraj_1_27+1, ch_1_28==ch_1_27 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_1_27==4,wprim_1_27==1), 
And(wtraj_1_28==1, ch_1_28==ch_1_27 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_1_27==0), 
And(wtraj_1_28==wtraj_1_27, ch_1_28==ch_1_27)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_1_28<4,wprim_1_28==1), 
And(wtraj_1_29==wtraj_1_28+1, ch_1_29==ch_1_28 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_1_28==4,wprim_1_28==1), 
And(wtraj_1_29==1, ch_1_29==ch_1_28 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_1_28==0), 
And(wtraj_1_29==wtraj_1_28, ch_1_29==ch_1_28)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_1_29<4,wprim_1_29==1), 
And(wtraj_1_30==wtraj_1_29+1, ch_1_30==ch_1_29 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_1_29==4,wprim_1_29==1), 
And(wtraj_1_30==1, ch_1_30==ch_1_29 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_1_29==0), 
And(wtraj_1_30==wtraj_1_29, ch_1_30==ch_1_29)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_1_30<4,wprim_1_30==1), 
And(wtraj_1_31==wtraj_1_30+1, ch_1_31==ch_1_30 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_1_30==4,wprim_1_30==1), 
And(wtraj_1_31==1, ch_1_31==ch_1_30 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_1_30==0), 
And(wtraj_1_31==wtraj_1_30, ch_1_31==ch_1_30)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_1_31<4,wprim_1_31==1), 
And(wtraj_1_32==wtraj_1_31+1, ch_1_32==ch_1_31 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_1_31==4,wprim_1_31==1), 
And(wtraj_1_32==1, ch_1_32==ch_1_31 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_1_31==0), 
And(wtraj_1_32==wtraj_1_31, ch_1_32==ch_1_31)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_1_32<4,wprim_1_32==1), 
And(wtraj_1_33==wtraj_1_32+1, ch_1_33==ch_1_32 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_1_32==4,wprim_1_32==1), 
And(wtraj_1_33==1, ch_1_33==ch_1_32 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_1_32==0), 
And(wtraj_1_33==wtraj_1_32, ch_1_33==ch_1_32)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_1_33<4,wprim_1_33==1), 
And(wtraj_1_34==wtraj_1_33+1, ch_1_34==ch_1_33 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_1_33==4,wprim_1_33==1), 
And(wtraj_1_34==1, ch_1_34==ch_1_33 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_1_33==0), 
And(wtraj_1_34==wtraj_1_33, ch_1_34==ch_1_33)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_1_34<4,wprim_1_34==1), 
And(wtraj_1_35==wtraj_1_34+1, ch_1_35==ch_1_34 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_1_34==4,wprim_1_34==1), 
And(wtraj_1_35==1, ch_1_35==ch_1_34 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_1_34==0), 
And(wtraj_1_35==wtraj_1_34, ch_1_35==ch_1_34)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_1_35<4,wprim_1_35==1), 
And(wtraj_1_36==wtraj_1_35+1, ch_1_36==ch_1_35 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_1_35==4,wprim_1_35==1), 
And(wtraj_1_36==1, ch_1_36==ch_1_35 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_1_35==0), 
And(wtraj_1_36==wtraj_1_35, ch_1_36==ch_1_35)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_1_36<4,wprim_1_36==1), 
And(wtraj_1_37==wtraj_1_36+1, ch_1_37==ch_1_36 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_1_36==4,wprim_1_36==1), 
And(wtraj_1_37==1, ch_1_37==ch_1_36 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_1_36==0), 
And(wtraj_1_37==wtraj_1_36, ch_1_37==ch_1_36)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_1_37<4,wprim_1_37==1), 
And(wtraj_1_38==wtraj_1_37+1, ch_1_38==ch_1_37 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_1_37==4,wprim_1_37==1), 
And(wtraj_1_38==1, ch_1_38==ch_1_37 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_1_37==0), 
And(wtraj_1_38==wtraj_1_37, ch_1_38==ch_1_37)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_1_38<4,wprim_1_38==1), 
And(wtraj_1_39==wtraj_1_38+1, ch_1_39==ch_1_38 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_1_38==4,wprim_1_38==1), 
And(wtraj_1_39==1, ch_1_39==ch_1_38 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_1_38==0), 
And(wtraj_1_39==wtraj_1_38, ch_1_39==ch_1_38)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_1_39<4,wprim_1_39==1), 
And(wtraj_1_40==wtraj_1_39+1, ch_1_40==ch_1_39 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_1_39==4,wprim_1_39==1), 
And(wtraj_1_40==1, ch_1_40==ch_1_39 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_1_39==0), 
And(wtraj_1_40==wtraj_1_39, ch_1_40==ch_1_39)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_1_40<4,wprim_1_40==1), 
And(wtraj_1_41==wtraj_1_40+1, ch_1_41==ch_1_40 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_1_40==4,wprim_1_40==1), 
And(wtraj_1_41==1, ch_1_41==ch_1_40 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_1_40==0), 
And(wtraj_1_41==wtraj_1_40, ch_1_41==ch_1_40)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_1_41<4,wprim_1_41==1), 
And(wtraj_1_42==wtraj_1_41+1, ch_1_42==ch_1_41 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_1_41==4,wprim_1_41==1), 
And(wtraj_1_42==1, ch_1_42==ch_1_41 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_1_41==0), 
And(wtraj_1_42==wtraj_1_41, ch_1_42==ch_1_41)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_1_42<4,wprim_1_42==1), 
And(wtraj_1_43==wtraj_1_42+1, ch_1_43==ch_1_42 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_1_42==4,wprim_1_42==1), 
And(wtraj_1_43==1, ch_1_43==ch_1_42 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_1_42==0), 
And(wtraj_1_43==wtraj_1_42, ch_1_43==ch_1_42)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_1_43<4,wprim_1_43==1), 
And(wtraj_1_44==wtraj_1_43+1, ch_1_44==ch_1_43 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_1_43==4,wprim_1_43==1), 
And(wtraj_1_44==1, ch_1_44==ch_1_43 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_1_43==0), 
And(wtraj_1_44==wtraj_1_43, ch_1_44==ch_1_43)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_1_44<4,wprim_1_44==1), 
And(wtraj_1_45==wtraj_1_44+1, ch_1_45==ch_1_44 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_1_44==4,wprim_1_44==1), 
And(wtraj_1_45==1, ch_1_45==ch_1_44 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_1_44==0), 
And(wtraj_1_45==wtraj_1_44, ch_1_45==ch_1_44)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_1_45<4,wprim_1_45==1), 
And(wtraj_1_46==wtraj_1_45+1, ch_1_46==ch_1_45 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_1_45==4,wprim_1_45==1), 
And(wtraj_1_46==1, ch_1_46==ch_1_45 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_1_45==0), 
And(wtraj_1_46==wtraj_1_45, ch_1_46==ch_1_45)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_1_46<4,wprim_1_46==1), 
And(wtraj_1_47==wtraj_1_46+1, ch_1_47==ch_1_46 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_1_46==4,wprim_1_46==1), 
And(wtraj_1_47==1, ch_1_47==ch_1_46 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_1_46==0), 
And(wtraj_1_47==wtraj_1_46, ch_1_47==ch_1_46)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_1_47<4,wprim_1_47==1), 
And(wtraj_1_48==wtraj_1_47+1, ch_1_48==ch_1_47 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_1_47==4,wprim_1_47==1), 
And(wtraj_1_48==1, ch_1_48==ch_1_47 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_1_47==0), 
And(wtraj_1_48==wtraj_1_47, ch_1_48==ch_1_47)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_1_48<4,wprim_1_48==1), 
And(wtraj_1_49==wtraj_1_48+1, ch_1_49==ch_1_48 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_1_48==4,wprim_1_48==1), 
And(wtraj_1_49==1, ch_1_49==ch_1_48 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_1_48==0), 
And(wtraj_1_49==wtraj_1_48, ch_1_49==ch_1_48)))

fch_2 = Int('fch_2')
s.add(fch_2==20)

# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_2_1<6,wprim_2_1==1), 
And(wtraj_2_2==wtraj_2_1+1, ch_2_2==ch_2_1 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_2_1==6,wprim_2_1==1), 
And(wtraj_2_2==1, ch_2_2==ch_2_1 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_2_1==0), 
And(wtraj_2_2==wtraj_2_1, ch_2_2==ch_2_1)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_2_2<6,wprim_2_2==1), 
And(wtraj_2_3==wtraj_2_2+1, ch_2_3==ch_2_2 -1)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_2_2==6,wprim_2_2==1), 
And(wtraj_2_3==1, ch_2_3==ch_2_2 -1)), 
# wprim = 0 : robot is static
Implies(And(wprim_2_2==0), 
And(wtraj_2_3==wtraj_2_2, ch_2_3==ch_2_2)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_2_3<6,wprim_2_3==1), 
And(wtraj_2_4==wtraj_2_3+1, ch_2_4==ch_2_3 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_2_3==6,wprim_2_3==1), 
And(wtraj_2_4==1, ch_2_4==ch_2_3 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_2_3==0), 
And(wtraj_2_4==wtraj_2_3, ch_2_4==ch_2_3)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_2_4<6,wprim_2_4==1), 
And(wtraj_2_5==wtraj_2_4+1, ch_2_5==ch_2_4 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_2_4==6,wprim_2_4==1), 
And(wtraj_2_5==1, ch_2_5==ch_2_4 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_2_4==0), 
And(wtraj_2_5==wtraj_2_4, ch_2_5==ch_2_4)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_2_5<6,wprim_2_5==1), 
And(wtraj_2_6==wtraj_2_5+1, ch_2_6==ch_2_5 -1)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_2_5==6,wprim_2_5==1), 
And(wtraj_2_6==1, ch_2_6==ch_2_5 -1)), 
# wprim = 0 : robot is static
Implies(And(wprim_2_5==0), 
And(wtraj_2_6==wtraj_2_5, ch_2_6==ch_2_5)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_2_6<6,wprim_2_6==1), 
And(wtraj_2_7==wtraj_2_6+1, ch_2_7==ch_2_6 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_2_6==6,wprim_2_6==1), 
And(wtraj_2_7==1, ch_2_7==ch_2_6 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_2_6==0), 
And(wtraj_2_7==wtraj_2_6, ch_2_7==ch_2_6)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_2_7<6,wprim_2_7==1), 
And(wtraj_2_8==wtraj_2_7+1, ch_2_8==ch_2_7 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_2_7==6,wprim_2_7==1), 
And(wtraj_2_8==1, ch_2_8==ch_2_7 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_2_7==0), 
And(wtraj_2_8==wtraj_2_7, ch_2_8==ch_2_7)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_2_8<6,wprim_2_8==1), 
And(wtraj_2_9==wtraj_2_8+1, ch_2_9==ch_2_8 -1)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_2_8==6,wprim_2_8==1), 
And(wtraj_2_9==1, ch_2_9==ch_2_8 -1)), 
# wprim = 0 : robot is static
Implies(And(wprim_2_8==0), 
And(wtraj_2_9==wtraj_2_8, ch_2_9==ch_2_8)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_2_9<6,wprim_2_9==1), 
And(wtraj_2_10==wtraj_2_9+1, ch_2_10==ch_2_9 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_2_9==6,wprim_2_9==1), 
And(wtraj_2_10==1, ch_2_10==ch_2_9 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_2_9==0), 
And(wtraj_2_10==wtraj_2_9, ch_2_10==ch_2_9)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_2_10<6,wprim_2_10==1), 
And(wtraj_2_11==wtraj_2_10+1, ch_2_11==ch_2_10 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_2_10==6,wprim_2_10==1), 
And(wtraj_2_11==1, ch_2_11==ch_2_10 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_2_10==0), 
And(wtraj_2_11==wtraj_2_10, ch_2_11==ch_2_10)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_2_11<6,wprim_2_11==1), 
And(wtraj_2_12==wtraj_2_11+1, ch_2_12==ch_2_11 -1)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_2_11==6,wprim_2_11==1), 
And(wtraj_2_12==1, ch_2_12==ch_2_11 -1)), 
# wprim = 0 : robot is static
Implies(And(wprim_2_11==0), 
And(wtraj_2_12==wtraj_2_11, ch_2_12==ch_2_11)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_2_12<6,wprim_2_12==1), 
And(wtraj_2_13==wtraj_2_12+1, ch_2_13==ch_2_12 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_2_12==6,wprim_2_12==1), 
And(wtraj_2_13==1, ch_2_13==ch_2_12 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_2_12==0), 
And(wtraj_2_13==wtraj_2_12, ch_2_13==ch_2_12)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_2_13<6,wprim_2_13==1), 
And(wtraj_2_14==wtraj_2_13+1, ch_2_14==ch_2_13 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_2_13==6,wprim_2_13==1), 
And(wtraj_2_14==1, ch_2_14==ch_2_13 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_2_13==0), 
And(wtraj_2_14==wtraj_2_13, ch_2_14==ch_2_13)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_2_14<6,wprim_2_14==1), 
And(wtraj_2_15==wtraj_2_14+1, ch_2_15==ch_2_14 -1)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_2_14==6,wprim_2_14==1), 
And(wtraj_2_15==1, ch_2_15==ch_2_14 -1)), 
# wprim = 0 : robot is static
Implies(And(wprim_2_14==0), 
And(wtraj_2_15==wtraj_2_14, ch_2_15==ch_2_14)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_2_15<6,wprim_2_15==1), 
And(wtraj_2_16==wtraj_2_15+1, ch_2_16==ch_2_15 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_2_15==6,wprim_2_15==1), 
And(wtraj_2_16==1, ch_2_16==ch_2_15 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_2_15==0), 
And(wtraj_2_16==wtraj_2_15, ch_2_16==ch_2_15)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_2_16<6,wprim_2_16==1), 
And(wtraj_2_17==wtraj_2_16+1, ch_2_17==ch_2_16 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_2_16==6,wprim_2_16==1), 
And(wtraj_2_17==1, ch_2_17==ch_2_16 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_2_16==0), 
And(wtraj_2_17==wtraj_2_16, ch_2_17==ch_2_16)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_2_17<6,wprim_2_17==1), 
And(wtraj_2_18==wtraj_2_17+1, ch_2_18==ch_2_17 -1)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_2_17==6,wprim_2_17==1), 
And(wtraj_2_18==1, ch_2_18==ch_2_17 -1)), 
# wprim = 0 : robot is static
Implies(And(wprim_2_17==0), 
And(wtraj_2_18==wtraj_2_17, ch_2_18==ch_2_17)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_2_18<6,wprim_2_18==1), 
And(wtraj_2_19==wtraj_2_18+1, ch_2_19==ch_2_18 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_2_18==6,wprim_2_18==1), 
And(wtraj_2_19==1, ch_2_19==ch_2_18 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_2_18==0), 
And(wtraj_2_19==wtraj_2_18, ch_2_19==ch_2_18)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_2_19<6,wprim_2_19==1), 
And(wtraj_2_20==wtraj_2_19+1, ch_2_20==ch_2_19 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_2_19==6,wprim_2_19==1), 
And(wtraj_2_20==1, ch_2_20==ch_2_19 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_2_19==0), 
And(wtraj_2_20==wtraj_2_19, ch_2_20==ch_2_19)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_2_20<6,wprim_2_20==1), 
And(wtraj_2_21==wtraj_2_20+1, ch_2_21==ch_2_20 -1)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_2_20==6,wprim_2_20==1), 
And(wtraj_2_21==1, ch_2_21==ch_2_20 -1)), 
# wprim = 0 : robot is static
Implies(And(wprim_2_20==0), 
And(wtraj_2_21==wtraj_2_20, ch_2_21==ch_2_20)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_2_21<6,wprim_2_21==1), 
And(wtraj_2_22==wtraj_2_21+1, ch_2_22==ch_2_21 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_2_21==6,wprim_2_21==1), 
And(wtraj_2_22==1, ch_2_22==ch_2_21 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_2_21==0), 
And(wtraj_2_22==wtraj_2_21, ch_2_22==ch_2_21)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_2_22<6,wprim_2_22==1), 
And(wtraj_2_23==wtraj_2_22+1, ch_2_23==ch_2_22 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_2_22==6,wprim_2_22==1), 
And(wtraj_2_23==1, ch_2_23==ch_2_22 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_2_22==0), 
And(wtraj_2_23==wtraj_2_22, ch_2_23==ch_2_22)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_2_23<6,wprim_2_23==1), 
And(wtraj_2_24==wtraj_2_23+1, ch_2_24==ch_2_23 -1)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_2_23==6,wprim_2_23==1), 
And(wtraj_2_24==1, ch_2_24==ch_2_23 -1)), 
# wprim = 0 : robot is static
Implies(And(wprim_2_23==0), 
And(wtraj_2_24==wtraj_2_23, ch_2_24==ch_2_23)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_2_24<6,wprim_2_24==1), 
And(wtraj_2_25==wtraj_2_24+1, ch_2_25==ch_2_24 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_2_24==6,wprim_2_24==1), 
And(wtraj_2_25==1, ch_2_25==ch_2_24 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_2_24==0), 
And(wtraj_2_25==wtraj_2_24, ch_2_25==ch_2_24)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_2_25<6,wprim_2_25==1), 
And(wtraj_2_26==wtraj_2_25+1, ch_2_26==ch_2_25 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_2_25==6,wprim_2_25==1), 
And(wtraj_2_26==1, ch_2_26==ch_2_25 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_2_25==0), 
And(wtraj_2_26==wtraj_2_25, ch_2_26==ch_2_25)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_2_26<6,wprim_2_26==1), 
And(wtraj_2_27==wtraj_2_26+1, ch_2_27==ch_2_26 -1)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_2_26==6,wprim_2_26==1), 
And(wtraj_2_27==1, ch_2_27==ch_2_26 -1)), 
# wprim = 0 : robot is static
Implies(And(wprim_2_26==0), 
And(wtraj_2_27==wtraj_2_26, ch_2_27==ch_2_26)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_2_27<6,wprim_2_27==1), 
And(wtraj_2_28==wtraj_2_27+1, ch_2_28==ch_2_27 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_2_27==6,wprim_2_27==1), 
And(wtraj_2_28==1, ch_2_28==ch_2_27 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_2_27==0), 
And(wtraj_2_28==wtraj_2_27, ch_2_28==ch_2_27)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_2_28<6,wprim_2_28==1), 
And(wtraj_2_29==wtraj_2_28+1, ch_2_29==ch_2_28 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_2_28==6,wprim_2_28==1), 
And(wtraj_2_29==1, ch_2_29==ch_2_28 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_2_28==0), 
And(wtraj_2_29==wtraj_2_28, ch_2_29==ch_2_28)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_2_29<6,wprim_2_29==1), 
And(wtraj_2_30==wtraj_2_29+1, ch_2_30==ch_2_29 -1)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_2_29==6,wprim_2_29==1), 
And(wtraj_2_30==1, ch_2_30==ch_2_29 -1)), 
# wprim = 0 : robot is static
Implies(And(wprim_2_29==0), 
And(wtraj_2_30==wtraj_2_29, ch_2_30==ch_2_29)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_2_30<6,wprim_2_30==1), 
And(wtraj_2_31==wtraj_2_30+1, ch_2_31==ch_2_30 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_2_30==6,wprim_2_30==1), 
And(wtraj_2_31==1, ch_2_31==ch_2_30 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_2_30==0), 
And(wtraj_2_31==wtraj_2_30, ch_2_31==ch_2_30)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_2_31<6,wprim_2_31==1), 
And(wtraj_2_32==wtraj_2_31+1, ch_2_32==ch_2_31 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_2_31==6,wprim_2_31==1), 
And(wtraj_2_32==1, ch_2_32==ch_2_31 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_2_31==0), 
And(wtraj_2_32==wtraj_2_31, ch_2_32==ch_2_31)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_2_32<6,wprim_2_32==1), 
And(wtraj_2_33==wtraj_2_32+1, ch_2_33==ch_2_32 -1)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_2_32==6,wprim_2_32==1), 
And(wtraj_2_33==1, ch_2_33==ch_2_32 -1)), 
# wprim = 0 : robot is static
Implies(And(wprim_2_32==0), 
And(wtraj_2_33==wtraj_2_32, ch_2_33==ch_2_32)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_2_33<6,wprim_2_33==1), 
And(wtraj_2_34==wtraj_2_33+1, ch_2_34==ch_2_33 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_2_33==6,wprim_2_33==1), 
And(wtraj_2_34==1, ch_2_34==ch_2_33 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_2_33==0), 
And(wtraj_2_34==wtraj_2_33, ch_2_34==ch_2_33)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_2_34<6,wprim_2_34==1), 
And(wtraj_2_35==wtraj_2_34+1, ch_2_35==ch_2_34 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_2_34==6,wprim_2_34==1), 
And(wtraj_2_35==1, ch_2_35==ch_2_34 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_2_34==0), 
And(wtraj_2_35==wtraj_2_34, ch_2_35==ch_2_34)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_2_35<6,wprim_2_35==1), 
And(wtraj_2_36==wtraj_2_35+1, ch_2_36==ch_2_35 -1)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_2_35==6,wprim_2_35==1), 
And(wtraj_2_36==1, ch_2_36==ch_2_35 -1)), 
# wprim = 0 : robot is static
Implies(And(wprim_2_35==0), 
And(wtraj_2_36==wtraj_2_35, ch_2_36==ch_2_35)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_2_36<6,wprim_2_36==1), 
And(wtraj_2_37==wtraj_2_36+1, ch_2_37==ch_2_36 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_2_36==6,wprim_2_36==1), 
And(wtraj_2_37==1, ch_2_37==ch_2_36 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_2_36==0), 
And(wtraj_2_37==wtraj_2_36, ch_2_37==ch_2_36)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_2_37<6,wprim_2_37==1), 
And(wtraj_2_38==wtraj_2_37+1, ch_2_38==ch_2_37 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_2_37==6,wprim_2_37==1), 
And(wtraj_2_38==1, ch_2_38==ch_2_37 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_2_37==0), 
And(wtraj_2_38==wtraj_2_37, ch_2_38==ch_2_37)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_2_38<6,wprim_2_38==1), 
And(wtraj_2_39==wtraj_2_38+1, ch_2_39==ch_2_38 -1)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_2_38==6,wprim_2_38==1), 
And(wtraj_2_39==1, ch_2_39==ch_2_38 -1)), 
# wprim = 0 : robot is static
Implies(And(wprim_2_38==0), 
And(wtraj_2_39==wtraj_2_38, ch_2_39==ch_2_38)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_2_39<6,wprim_2_39==1), 
And(wtraj_2_40==wtraj_2_39+1, ch_2_40==ch_2_39 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_2_39==6,wprim_2_39==1), 
And(wtraj_2_40==1, ch_2_40==ch_2_39 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_2_39==0), 
And(wtraj_2_40==wtraj_2_39, ch_2_40==ch_2_39)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_2_40<6,wprim_2_40==1), 
And(wtraj_2_41==wtraj_2_40+1, ch_2_41==ch_2_40 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_2_40==6,wprim_2_40==1), 
And(wtraj_2_41==1, ch_2_41==ch_2_40 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_2_40==0), 
And(wtraj_2_41==wtraj_2_40, ch_2_41==ch_2_40)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_2_41<6,wprim_2_41==1), 
And(wtraj_2_42==wtraj_2_41+1, ch_2_42==ch_2_41 -1)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_2_41==6,wprim_2_41==1), 
And(wtraj_2_42==1, ch_2_42==ch_2_41 -1)), 
# wprim = 0 : robot is static
Implies(And(wprim_2_41==0), 
And(wtraj_2_42==wtraj_2_41, ch_2_42==ch_2_41)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_2_42<6,wprim_2_42==1), 
And(wtraj_2_43==wtraj_2_42+1, ch_2_43==ch_2_42 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_2_42==6,wprim_2_42==1), 
And(wtraj_2_43==1, ch_2_43==ch_2_42 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_2_42==0), 
And(wtraj_2_43==wtraj_2_42, ch_2_43==ch_2_42)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_2_43<6,wprim_2_43==1), 
And(wtraj_2_44==wtraj_2_43+1, ch_2_44==ch_2_43 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_2_43==6,wprim_2_43==1), 
And(wtraj_2_44==1, ch_2_44==ch_2_43 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_2_43==0), 
And(wtraj_2_44==wtraj_2_43, ch_2_44==ch_2_43)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_2_44<6,wprim_2_44==1), 
And(wtraj_2_45==wtraj_2_44+1, ch_2_45==ch_2_44 -1)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_2_44==6,wprim_2_44==1), 
And(wtraj_2_45==1, ch_2_45==ch_2_44 -1)), 
# wprim = 0 : robot is static
Implies(And(wprim_2_44==0), 
And(wtraj_2_45==wtraj_2_44, ch_2_45==ch_2_44)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_2_45<6,wprim_2_45==1), 
And(wtraj_2_46==wtraj_2_45+1, ch_2_46==ch_2_45 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_2_45==6,wprim_2_45==1), 
And(wtraj_2_46==1, ch_2_46==ch_2_45 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_2_45==0), 
And(wtraj_2_46==wtraj_2_45, ch_2_46==ch_2_45)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_2_46<6,wprim_2_46==1), 
And(wtraj_2_47==wtraj_2_46+1, ch_2_47==ch_2_46 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_2_46==6,wprim_2_46==1), 
And(wtraj_2_47==1, ch_2_47==ch_2_46 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_2_46==0), 
And(wtraj_2_47==wtraj_2_46, ch_2_47==ch_2_46)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_2_47<6,wprim_2_47==1), 
And(wtraj_2_48==wtraj_2_47+1, ch_2_48==ch_2_47 -1)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_2_47==6,wprim_2_47==1), 
And(wtraj_2_48==1, ch_2_48==ch_2_47 -1)), 
# wprim = 0 : robot is static
Implies(And(wprim_2_47==0), 
And(wtraj_2_48==wtraj_2_47, ch_2_48==ch_2_47)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_2_48<6,wprim_2_48==1), 
And(wtraj_2_49==wtraj_2_48+1, ch_2_49==ch_2_48 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_2_48==6,wprim_2_48==1), 
And(wtraj_2_49==1, ch_2_49==ch_2_48 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_2_48==0), 
And(wtraj_2_49==wtraj_2_48, ch_2_49==ch_2_48)))

fch_3 = Int('fch_3')
s.add(fch_3==20)

# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_3_1<4,wprim_3_1==1), 
And(wtraj_3_2==wtraj_3_1+1, ch_3_2==ch_3_1 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_3_1==4,wprim_3_1==1), 
And(wtraj_3_2==1, ch_3_2==ch_3_1 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_3_1==0), 
And(wtraj_3_2==wtraj_3_1, ch_3_2==ch_3_1)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_3_2<4,wprim_3_2==1), 
And(wtraj_3_3==wtraj_3_2+1, ch_3_3==ch_3_2 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_3_2==4,wprim_3_2==1), 
And(wtraj_3_3==1, ch_3_3==ch_3_2 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_3_2==0), 
And(wtraj_3_3==wtraj_3_2, ch_3_3==ch_3_2)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_3_3<4,wprim_3_3==1), 
And(wtraj_3_4==wtraj_3_3+1, ch_3_4==ch_3_3 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_3_3==4,wprim_3_3==1), 
And(wtraj_3_4==1, ch_3_4==ch_3_3 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_3_3==0), 
And(wtraj_3_4==wtraj_3_3, ch_3_4==ch_3_3)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_3_4<4,wprim_3_4==1), 
And(wtraj_3_5==wtraj_3_4+1, ch_3_5==ch_3_4 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_3_4==4,wprim_3_4==1), 
And(wtraj_3_5==1, ch_3_5==ch_3_4 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_3_4==0), 
And(wtraj_3_5==wtraj_3_4, ch_3_5==ch_3_4)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_3_5<4,wprim_3_5==1), 
And(wtraj_3_6==wtraj_3_5+1, ch_3_6==ch_3_5 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_3_5==4,wprim_3_5==1), 
And(wtraj_3_6==1, ch_3_6==ch_3_5 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_3_5==0), 
And(wtraj_3_6==wtraj_3_5, ch_3_6==ch_3_5)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_3_6<4,wprim_3_6==1), 
And(wtraj_3_7==wtraj_3_6+1, ch_3_7==ch_3_6 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_3_6==4,wprim_3_6==1), 
And(wtraj_3_7==1, ch_3_7==ch_3_6 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_3_6==0), 
And(wtraj_3_7==wtraj_3_6, ch_3_7==ch_3_6)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_3_7<4,wprim_3_7==1), 
And(wtraj_3_8==wtraj_3_7+1, ch_3_8==ch_3_7 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_3_7==4,wprim_3_7==1), 
And(wtraj_3_8==1, ch_3_8==ch_3_7 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_3_7==0), 
And(wtraj_3_8==wtraj_3_7, ch_3_8==ch_3_7)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_3_8<4,wprim_3_8==1), 
And(wtraj_3_9==wtraj_3_8+1, ch_3_9==ch_3_8 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_3_8==4,wprim_3_8==1), 
And(wtraj_3_9==1, ch_3_9==ch_3_8 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_3_8==0), 
And(wtraj_3_9==wtraj_3_8, ch_3_9==ch_3_8)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_3_9<4,wprim_3_9==1), 
And(wtraj_3_10==wtraj_3_9+1, ch_3_10==ch_3_9 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_3_9==4,wprim_3_9==1), 
And(wtraj_3_10==1, ch_3_10==ch_3_9 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_3_9==0), 
And(wtraj_3_10==wtraj_3_9, ch_3_10==ch_3_9)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_3_10<4,wprim_3_10==1), 
And(wtraj_3_11==wtraj_3_10+1, ch_3_11==ch_3_10 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_3_10==4,wprim_3_10==1), 
And(wtraj_3_11==1, ch_3_11==ch_3_10 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_3_10==0), 
And(wtraj_3_11==wtraj_3_10, ch_3_11==ch_3_10)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_3_11<4,wprim_3_11==1), 
And(wtraj_3_12==wtraj_3_11+1, ch_3_12==ch_3_11 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_3_11==4,wprim_3_11==1), 
And(wtraj_3_12==1, ch_3_12==ch_3_11 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_3_11==0), 
And(wtraj_3_12==wtraj_3_11, ch_3_12==ch_3_11)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_3_12<4,wprim_3_12==1), 
And(wtraj_3_13==wtraj_3_12+1, ch_3_13==ch_3_12 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_3_12==4,wprim_3_12==1), 
And(wtraj_3_13==1, ch_3_13==ch_3_12 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_3_12==0), 
And(wtraj_3_13==wtraj_3_12, ch_3_13==ch_3_12)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_3_13<4,wprim_3_13==1), 
And(wtraj_3_14==wtraj_3_13+1, ch_3_14==ch_3_13 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_3_13==4,wprim_3_13==1), 
And(wtraj_3_14==1, ch_3_14==ch_3_13 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_3_13==0), 
And(wtraj_3_14==wtraj_3_13, ch_3_14==ch_3_13)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_3_14<4,wprim_3_14==1), 
And(wtraj_3_15==wtraj_3_14+1, ch_3_15==ch_3_14 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_3_14==4,wprim_3_14==1), 
And(wtraj_3_15==1, ch_3_15==ch_3_14 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_3_14==0), 
And(wtraj_3_15==wtraj_3_14, ch_3_15==ch_3_14)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_3_15<4,wprim_3_15==1), 
And(wtraj_3_16==wtraj_3_15+1, ch_3_16==ch_3_15 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_3_15==4,wprim_3_15==1), 
And(wtraj_3_16==1, ch_3_16==ch_3_15 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_3_15==0), 
And(wtraj_3_16==wtraj_3_15, ch_3_16==ch_3_15)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_3_16<4,wprim_3_16==1), 
And(wtraj_3_17==wtraj_3_16+1, ch_3_17==ch_3_16 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_3_16==4,wprim_3_16==1), 
And(wtraj_3_17==1, ch_3_17==ch_3_16 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_3_16==0), 
And(wtraj_3_17==wtraj_3_16, ch_3_17==ch_3_16)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_3_17<4,wprim_3_17==1), 
And(wtraj_3_18==wtraj_3_17+1, ch_3_18==ch_3_17 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_3_17==4,wprim_3_17==1), 
And(wtraj_3_18==1, ch_3_18==ch_3_17 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_3_17==0), 
And(wtraj_3_18==wtraj_3_17, ch_3_18==ch_3_17)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_3_18<4,wprim_3_18==1), 
And(wtraj_3_19==wtraj_3_18+1, ch_3_19==ch_3_18 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_3_18==4,wprim_3_18==1), 
And(wtraj_3_19==1, ch_3_19==ch_3_18 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_3_18==0), 
And(wtraj_3_19==wtraj_3_18, ch_3_19==ch_3_18)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_3_19<4,wprim_3_19==1), 
And(wtraj_3_20==wtraj_3_19+1, ch_3_20==ch_3_19 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_3_19==4,wprim_3_19==1), 
And(wtraj_3_20==1, ch_3_20==ch_3_19 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_3_19==0), 
And(wtraj_3_20==wtraj_3_19, ch_3_20==ch_3_19)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_3_20<4,wprim_3_20==1), 
And(wtraj_3_21==wtraj_3_20+1, ch_3_21==ch_3_20 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_3_20==4,wprim_3_20==1), 
And(wtraj_3_21==1, ch_3_21==ch_3_20 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_3_20==0), 
And(wtraj_3_21==wtraj_3_20, ch_3_21==ch_3_20)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_3_21<4,wprim_3_21==1), 
And(wtraj_3_22==wtraj_3_21+1, ch_3_22==ch_3_21 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_3_21==4,wprim_3_21==1), 
And(wtraj_3_22==1, ch_3_22==ch_3_21 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_3_21==0), 
And(wtraj_3_22==wtraj_3_21, ch_3_22==ch_3_21)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_3_22<4,wprim_3_22==1), 
And(wtraj_3_23==wtraj_3_22+1, ch_3_23==ch_3_22 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_3_22==4,wprim_3_22==1), 
And(wtraj_3_23==1, ch_3_23==ch_3_22 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_3_22==0), 
And(wtraj_3_23==wtraj_3_22, ch_3_23==ch_3_22)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_3_23<4,wprim_3_23==1), 
And(wtraj_3_24==wtraj_3_23+1, ch_3_24==ch_3_23 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_3_23==4,wprim_3_23==1), 
And(wtraj_3_24==1, ch_3_24==ch_3_23 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_3_23==0), 
And(wtraj_3_24==wtraj_3_23, ch_3_24==ch_3_23)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_3_24<4,wprim_3_24==1), 
And(wtraj_3_25==wtraj_3_24+1, ch_3_25==ch_3_24 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_3_24==4,wprim_3_24==1), 
And(wtraj_3_25==1, ch_3_25==ch_3_24 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_3_24==0), 
And(wtraj_3_25==wtraj_3_24, ch_3_25==ch_3_24)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_3_25<4,wprim_3_25==1), 
And(wtraj_3_26==wtraj_3_25+1, ch_3_26==ch_3_25 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_3_25==4,wprim_3_25==1), 
And(wtraj_3_26==1, ch_3_26==ch_3_25 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_3_25==0), 
And(wtraj_3_26==wtraj_3_25, ch_3_26==ch_3_25)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_3_26<4,wprim_3_26==1), 
And(wtraj_3_27==wtraj_3_26+1, ch_3_27==ch_3_26 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_3_26==4,wprim_3_26==1), 
And(wtraj_3_27==1, ch_3_27==ch_3_26 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_3_26==0), 
And(wtraj_3_27==wtraj_3_26, ch_3_27==ch_3_26)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_3_27<4,wprim_3_27==1), 
And(wtraj_3_28==wtraj_3_27+1, ch_3_28==ch_3_27 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_3_27==4,wprim_3_27==1), 
And(wtraj_3_28==1, ch_3_28==ch_3_27 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_3_27==0), 
And(wtraj_3_28==wtraj_3_27, ch_3_28==ch_3_27)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_3_28<4,wprim_3_28==1), 
And(wtraj_3_29==wtraj_3_28+1, ch_3_29==ch_3_28 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_3_28==4,wprim_3_28==1), 
And(wtraj_3_29==1, ch_3_29==ch_3_28 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_3_28==0), 
And(wtraj_3_29==wtraj_3_28, ch_3_29==ch_3_28)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_3_29<4,wprim_3_29==1), 
And(wtraj_3_30==wtraj_3_29+1, ch_3_30==ch_3_29 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_3_29==4,wprim_3_29==1), 
And(wtraj_3_30==1, ch_3_30==ch_3_29 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_3_29==0), 
And(wtraj_3_30==wtraj_3_29, ch_3_30==ch_3_29)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_3_30<4,wprim_3_30==1), 
And(wtraj_3_31==wtraj_3_30+1, ch_3_31==ch_3_30 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_3_30==4,wprim_3_30==1), 
And(wtraj_3_31==1, ch_3_31==ch_3_30 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_3_30==0), 
And(wtraj_3_31==wtraj_3_30, ch_3_31==ch_3_30)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_3_31<4,wprim_3_31==1), 
And(wtraj_3_32==wtraj_3_31+1, ch_3_32==ch_3_31 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_3_31==4,wprim_3_31==1), 
And(wtraj_3_32==1, ch_3_32==ch_3_31 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_3_31==0), 
And(wtraj_3_32==wtraj_3_31, ch_3_32==ch_3_31)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_3_32<4,wprim_3_32==1), 
And(wtraj_3_33==wtraj_3_32+1, ch_3_33==ch_3_32 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_3_32==4,wprim_3_32==1), 
And(wtraj_3_33==1, ch_3_33==ch_3_32 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_3_32==0), 
And(wtraj_3_33==wtraj_3_32, ch_3_33==ch_3_32)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_3_33<4,wprim_3_33==1), 
And(wtraj_3_34==wtraj_3_33+1, ch_3_34==ch_3_33 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_3_33==4,wprim_3_33==1), 
And(wtraj_3_34==1, ch_3_34==ch_3_33 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_3_33==0), 
And(wtraj_3_34==wtraj_3_33, ch_3_34==ch_3_33)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_3_34<4,wprim_3_34==1), 
And(wtraj_3_35==wtraj_3_34+1, ch_3_35==ch_3_34 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_3_34==4,wprim_3_34==1), 
And(wtraj_3_35==1, ch_3_35==ch_3_34 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_3_34==0), 
And(wtraj_3_35==wtraj_3_34, ch_3_35==ch_3_34)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_3_35<4,wprim_3_35==1), 
And(wtraj_3_36==wtraj_3_35+1, ch_3_36==ch_3_35 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_3_35==4,wprim_3_35==1), 
And(wtraj_3_36==1, ch_3_36==ch_3_35 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_3_35==0), 
And(wtraj_3_36==wtraj_3_35, ch_3_36==ch_3_35)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_3_36<4,wprim_3_36==1), 
And(wtraj_3_37==wtraj_3_36+1, ch_3_37==ch_3_36 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_3_36==4,wprim_3_36==1), 
And(wtraj_3_37==1, ch_3_37==ch_3_36 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_3_36==0), 
And(wtraj_3_37==wtraj_3_36, ch_3_37==ch_3_36)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_3_37<4,wprim_3_37==1), 
And(wtraj_3_38==wtraj_3_37+1, ch_3_38==ch_3_37 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_3_37==4,wprim_3_37==1), 
And(wtraj_3_38==1, ch_3_38==ch_3_37 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_3_37==0), 
And(wtraj_3_38==wtraj_3_37, ch_3_38==ch_3_37)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_3_38<4,wprim_3_38==1), 
And(wtraj_3_39==wtraj_3_38+1, ch_3_39==ch_3_38 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_3_38==4,wprim_3_38==1), 
And(wtraj_3_39==1, ch_3_39==ch_3_38 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_3_38==0), 
And(wtraj_3_39==wtraj_3_38, ch_3_39==ch_3_38)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_3_39<4,wprim_3_39==1), 
And(wtraj_3_40==wtraj_3_39+1, ch_3_40==ch_3_39 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_3_39==4,wprim_3_39==1), 
And(wtraj_3_40==1, ch_3_40==ch_3_39 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_3_39==0), 
And(wtraj_3_40==wtraj_3_39, ch_3_40==ch_3_39)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_3_40<4,wprim_3_40==1), 
And(wtraj_3_41==wtraj_3_40+1, ch_3_41==ch_3_40 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_3_40==4,wprim_3_40==1), 
And(wtraj_3_41==1, ch_3_41==ch_3_40 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_3_40==0), 
And(wtraj_3_41==wtraj_3_40, ch_3_41==ch_3_40)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_3_41<4,wprim_3_41==1), 
And(wtraj_3_42==wtraj_3_41+1, ch_3_42==ch_3_41 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_3_41==4,wprim_3_41==1), 
And(wtraj_3_42==1, ch_3_42==ch_3_41 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_3_41==0), 
And(wtraj_3_42==wtraj_3_41, ch_3_42==ch_3_41)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_3_42<4,wprim_3_42==1), 
And(wtraj_3_43==wtraj_3_42+1, ch_3_43==ch_3_42 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_3_42==4,wprim_3_42==1), 
And(wtraj_3_43==1, ch_3_43==ch_3_42 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_3_42==0), 
And(wtraj_3_43==wtraj_3_42, ch_3_43==ch_3_42)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_3_43<4,wprim_3_43==1), 
And(wtraj_3_44==wtraj_3_43+1, ch_3_44==ch_3_43 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_3_43==4,wprim_3_43==1), 
And(wtraj_3_44==1, ch_3_44==ch_3_43 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_3_43==0), 
And(wtraj_3_44==wtraj_3_43, ch_3_44==ch_3_43)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_3_44<4,wprim_3_44==1), 
And(wtraj_3_45==wtraj_3_44+1, ch_3_45==ch_3_44 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_3_44==4,wprim_3_44==1), 
And(wtraj_3_45==1, ch_3_45==ch_3_44 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_3_44==0), 
And(wtraj_3_45==wtraj_3_44, ch_3_45==ch_3_44)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_3_45<4,wprim_3_45==1), 
And(wtraj_3_46==wtraj_3_45+1, ch_3_46==ch_3_45 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_3_45==4,wprim_3_45==1), 
And(wtraj_3_46==1, ch_3_46==ch_3_45 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_3_45==0), 
And(wtraj_3_46==wtraj_3_45, ch_3_46==ch_3_45)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_3_46<4,wprim_3_46==1), 
And(wtraj_3_47==wtraj_3_46+1, ch_3_47==ch_3_46 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_3_46==4,wprim_3_46==1), 
And(wtraj_3_47==1, ch_3_47==ch_3_46 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_3_46==0), 
And(wtraj_3_47==wtraj_3_46, ch_3_47==ch_3_46)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_3_47<4,wprim_3_47==1), 
And(wtraj_3_48==wtraj_3_47+1, ch_3_48==ch_3_47 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_3_47==4,wprim_3_47==1), 
And(wtraj_3_48==1, ch_3_48==ch_3_47 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_3_47==0), 
And(wtraj_3_48==wtraj_3_47, ch_3_48==ch_3_47)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_3_48<4,wprim_3_48==1), 
And(wtraj_3_49==wtraj_3_48+1, ch_3_49==ch_3_48 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_3_48==4,wprim_3_48==1), 
And(wtraj_3_49==1, ch_3_49==ch_3_48 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_3_48==0), 
And(wtraj_3_49==wtraj_3_48, ch_3_49==ch_3_48)))

fch_4 = Int('fch_4')
s.add(fch_4==20)

# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_4_1<6,wprim_4_1==1), 
And(wtraj_4_2==wtraj_4_1+1, ch_4_2==ch_4_1 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_4_1==6,wprim_4_1==1), 
And(wtraj_4_2==1, ch_4_2==ch_4_1 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_4_1==0), 
And(wtraj_4_2==wtraj_4_1, ch_4_2==ch_4_1)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_4_2<6,wprim_4_2==1), 
And(wtraj_4_3==wtraj_4_2+1, ch_4_3==ch_4_2 -1)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_4_2==6,wprim_4_2==1), 
And(wtraj_4_3==1, ch_4_3==ch_4_2 -1)), 
# wprim = 0 : robot is static
Implies(And(wprim_4_2==0), 
And(wtraj_4_3==wtraj_4_2, ch_4_3==ch_4_2)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_4_3<6,wprim_4_3==1), 
And(wtraj_4_4==wtraj_4_3+1, ch_4_4==ch_4_3 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_4_3==6,wprim_4_3==1), 
And(wtraj_4_4==1, ch_4_4==ch_4_3 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_4_3==0), 
And(wtraj_4_4==wtraj_4_3, ch_4_4==ch_4_3)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_4_4<6,wprim_4_4==1), 
And(wtraj_4_5==wtraj_4_4+1, ch_4_5==ch_4_4 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_4_4==6,wprim_4_4==1), 
And(wtraj_4_5==1, ch_4_5==ch_4_4 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_4_4==0), 
And(wtraj_4_5==wtraj_4_4, ch_4_5==ch_4_4)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_4_5<6,wprim_4_5==1), 
And(wtraj_4_6==wtraj_4_5+1, ch_4_6==ch_4_5 -1)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_4_5==6,wprim_4_5==1), 
And(wtraj_4_6==1, ch_4_6==ch_4_5 -1)), 
# wprim = 0 : robot is static
Implies(And(wprim_4_5==0), 
And(wtraj_4_6==wtraj_4_5, ch_4_6==ch_4_5)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_4_6<6,wprim_4_6==1), 
And(wtraj_4_7==wtraj_4_6+1, ch_4_7==ch_4_6 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_4_6==6,wprim_4_6==1), 
And(wtraj_4_7==1, ch_4_7==ch_4_6 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_4_6==0), 
And(wtraj_4_7==wtraj_4_6, ch_4_7==ch_4_6)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_4_7<6,wprim_4_7==1), 
And(wtraj_4_8==wtraj_4_7+1, ch_4_8==ch_4_7 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_4_7==6,wprim_4_7==1), 
And(wtraj_4_8==1, ch_4_8==ch_4_7 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_4_7==0), 
And(wtraj_4_8==wtraj_4_7, ch_4_8==ch_4_7)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_4_8<6,wprim_4_8==1), 
And(wtraj_4_9==wtraj_4_8+1, ch_4_9==ch_4_8 -1)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_4_8==6,wprim_4_8==1), 
And(wtraj_4_9==1, ch_4_9==ch_4_8 -1)), 
# wprim = 0 : robot is static
Implies(And(wprim_4_8==0), 
And(wtraj_4_9==wtraj_4_8, ch_4_9==ch_4_8)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_4_9<6,wprim_4_9==1), 
And(wtraj_4_10==wtraj_4_9+1, ch_4_10==ch_4_9 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_4_9==6,wprim_4_9==1), 
And(wtraj_4_10==1, ch_4_10==ch_4_9 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_4_9==0), 
And(wtraj_4_10==wtraj_4_9, ch_4_10==ch_4_9)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_4_10<6,wprim_4_10==1), 
And(wtraj_4_11==wtraj_4_10+1, ch_4_11==ch_4_10 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_4_10==6,wprim_4_10==1), 
And(wtraj_4_11==1, ch_4_11==ch_4_10 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_4_10==0), 
And(wtraj_4_11==wtraj_4_10, ch_4_11==ch_4_10)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_4_11<6,wprim_4_11==1), 
And(wtraj_4_12==wtraj_4_11+1, ch_4_12==ch_4_11 -1)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_4_11==6,wprim_4_11==1), 
And(wtraj_4_12==1, ch_4_12==ch_4_11 -1)), 
# wprim = 0 : robot is static
Implies(And(wprim_4_11==0), 
And(wtraj_4_12==wtraj_4_11, ch_4_12==ch_4_11)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_4_12<6,wprim_4_12==1), 
And(wtraj_4_13==wtraj_4_12+1, ch_4_13==ch_4_12 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_4_12==6,wprim_4_12==1), 
And(wtraj_4_13==1, ch_4_13==ch_4_12 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_4_12==0), 
And(wtraj_4_13==wtraj_4_12, ch_4_13==ch_4_12)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_4_13<6,wprim_4_13==1), 
And(wtraj_4_14==wtraj_4_13+1, ch_4_14==ch_4_13 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_4_13==6,wprim_4_13==1), 
And(wtraj_4_14==1, ch_4_14==ch_4_13 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_4_13==0), 
And(wtraj_4_14==wtraj_4_13, ch_4_14==ch_4_13)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_4_14<6,wprim_4_14==1), 
And(wtraj_4_15==wtraj_4_14+1, ch_4_15==ch_4_14 -1)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_4_14==6,wprim_4_14==1), 
And(wtraj_4_15==1, ch_4_15==ch_4_14 -1)), 
# wprim = 0 : robot is static
Implies(And(wprim_4_14==0), 
And(wtraj_4_15==wtraj_4_14, ch_4_15==ch_4_14)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_4_15<6,wprim_4_15==1), 
And(wtraj_4_16==wtraj_4_15+1, ch_4_16==ch_4_15 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_4_15==6,wprim_4_15==1), 
And(wtraj_4_16==1, ch_4_16==ch_4_15 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_4_15==0), 
And(wtraj_4_16==wtraj_4_15, ch_4_16==ch_4_15)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_4_16<6,wprim_4_16==1), 
And(wtraj_4_17==wtraj_4_16+1, ch_4_17==ch_4_16 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_4_16==6,wprim_4_16==1), 
And(wtraj_4_17==1, ch_4_17==ch_4_16 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_4_16==0), 
And(wtraj_4_17==wtraj_4_16, ch_4_17==ch_4_16)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_4_17<6,wprim_4_17==1), 
And(wtraj_4_18==wtraj_4_17+1, ch_4_18==ch_4_17 -1)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_4_17==6,wprim_4_17==1), 
And(wtraj_4_18==1, ch_4_18==ch_4_17 -1)), 
# wprim = 0 : robot is static
Implies(And(wprim_4_17==0), 
And(wtraj_4_18==wtraj_4_17, ch_4_18==ch_4_17)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_4_18<6,wprim_4_18==1), 
And(wtraj_4_19==wtraj_4_18+1, ch_4_19==ch_4_18 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_4_18==6,wprim_4_18==1), 
And(wtraj_4_19==1, ch_4_19==ch_4_18 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_4_18==0), 
And(wtraj_4_19==wtraj_4_18, ch_4_19==ch_4_18)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_4_19<6,wprim_4_19==1), 
And(wtraj_4_20==wtraj_4_19+1, ch_4_20==ch_4_19 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_4_19==6,wprim_4_19==1), 
And(wtraj_4_20==1, ch_4_20==ch_4_19 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_4_19==0), 
And(wtraj_4_20==wtraj_4_19, ch_4_20==ch_4_19)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_4_20<6,wprim_4_20==1), 
And(wtraj_4_21==wtraj_4_20+1, ch_4_21==ch_4_20 -1)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_4_20==6,wprim_4_20==1), 
And(wtraj_4_21==1, ch_4_21==ch_4_20 -1)), 
# wprim = 0 : robot is static
Implies(And(wprim_4_20==0), 
And(wtraj_4_21==wtraj_4_20, ch_4_21==ch_4_20)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_4_21<6,wprim_4_21==1), 
And(wtraj_4_22==wtraj_4_21+1, ch_4_22==ch_4_21 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_4_21==6,wprim_4_21==1), 
And(wtraj_4_22==1, ch_4_22==ch_4_21 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_4_21==0), 
And(wtraj_4_22==wtraj_4_21, ch_4_22==ch_4_21)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_4_22<6,wprim_4_22==1), 
And(wtraj_4_23==wtraj_4_22+1, ch_4_23==ch_4_22 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_4_22==6,wprim_4_22==1), 
And(wtraj_4_23==1, ch_4_23==ch_4_22 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_4_22==0), 
And(wtraj_4_23==wtraj_4_22, ch_4_23==ch_4_22)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_4_23<6,wprim_4_23==1), 
And(wtraj_4_24==wtraj_4_23+1, ch_4_24==ch_4_23 -1)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_4_23==6,wprim_4_23==1), 
And(wtraj_4_24==1, ch_4_24==ch_4_23 -1)), 
# wprim = 0 : robot is static
Implies(And(wprim_4_23==0), 
And(wtraj_4_24==wtraj_4_23, ch_4_24==ch_4_23)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_4_24<6,wprim_4_24==1), 
And(wtraj_4_25==wtraj_4_24+1, ch_4_25==ch_4_24 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_4_24==6,wprim_4_24==1), 
And(wtraj_4_25==1, ch_4_25==ch_4_24 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_4_24==0), 
And(wtraj_4_25==wtraj_4_24, ch_4_25==ch_4_24)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_4_25<6,wprim_4_25==1), 
And(wtraj_4_26==wtraj_4_25+1, ch_4_26==ch_4_25 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_4_25==6,wprim_4_25==1), 
And(wtraj_4_26==1, ch_4_26==ch_4_25 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_4_25==0), 
And(wtraj_4_26==wtraj_4_25, ch_4_26==ch_4_25)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_4_26<6,wprim_4_26==1), 
And(wtraj_4_27==wtraj_4_26+1, ch_4_27==ch_4_26 -1)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_4_26==6,wprim_4_26==1), 
And(wtraj_4_27==1, ch_4_27==ch_4_26 -1)), 
# wprim = 0 : robot is static
Implies(And(wprim_4_26==0), 
And(wtraj_4_27==wtraj_4_26, ch_4_27==ch_4_26)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_4_27<6,wprim_4_27==1), 
And(wtraj_4_28==wtraj_4_27+1, ch_4_28==ch_4_27 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_4_27==6,wprim_4_27==1), 
And(wtraj_4_28==1, ch_4_28==ch_4_27 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_4_27==0), 
And(wtraj_4_28==wtraj_4_27, ch_4_28==ch_4_27)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_4_28<6,wprim_4_28==1), 
And(wtraj_4_29==wtraj_4_28+1, ch_4_29==ch_4_28 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_4_28==6,wprim_4_28==1), 
And(wtraj_4_29==1, ch_4_29==ch_4_28 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_4_28==0), 
And(wtraj_4_29==wtraj_4_28, ch_4_29==ch_4_28)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_4_29<6,wprim_4_29==1), 
And(wtraj_4_30==wtraj_4_29+1, ch_4_30==ch_4_29 -1)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_4_29==6,wprim_4_29==1), 
And(wtraj_4_30==1, ch_4_30==ch_4_29 -1)), 
# wprim = 0 : robot is static
Implies(And(wprim_4_29==0), 
And(wtraj_4_30==wtraj_4_29, ch_4_30==ch_4_29)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_4_30<6,wprim_4_30==1), 
And(wtraj_4_31==wtraj_4_30+1, ch_4_31==ch_4_30 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_4_30==6,wprim_4_30==1), 
And(wtraj_4_31==1, ch_4_31==ch_4_30 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_4_30==0), 
And(wtraj_4_31==wtraj_4_30, ch_4_31==ch_4_30)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_4_31<6,wprim_4_31==1), 
And(wtraj_4_32==wtraj_4_31+1, ch_4_32==ch_4_31 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_4_31==6,wprim_4_31==1), 
And(wtraj_4_32==1, ch_4_32==ch_4_31 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_4_31==0), 
And(wtraj_4_32==wtraj_4_31, ch_4_32==ch_4_31)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_4_32<6,wprim_4_32==1), 
And(wtraj_4_33==wtraj_4_32+1, ch_4_33==ch_4_32 -1)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_4_32==6,wprim_4_32==1), 
And(wtraj_4_33==1, ch_4_33==ch_4_32 -1)), 
# wprim = 0 : robot is static
Implies(And(wprim_4_32==0), 
And(wtraj_4_33==wtraj_4_32, ch_4_33==ch_4_32)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_4_33<6,wprim_4_33==1), 
And(wtraj_4_34==wtraj_4_33+1, ch_4_34==ch_4_33 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_4_33==6,wprim_4_33==1), 
And(wtraj_4_34==1, ch_4_34==ch_4_33 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_4_33==0), 
And(wtraj_4_34==wtraj_4_33, ch_4_34==ch_4_33)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_4_34<6,wprim_4_34==1), 
And(wtraj_4_35==wtraj_4_34+1, ch_4_35==ch_4_34 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_4_34==6,wprim_4_34==1), 
And(wtraj_4_35==1, ch_4_35==ch_4_34 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_4_34==0), 
And(wtraj_4_35==wtraj_4_34, ch_4_35==ch_4_34)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_4_35<6,wprim_4_35==1), 
And(wtraj_4_36==wtraj_4_35+1, ch_4_36==ch_4_35 -1)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_4_35==6,wprim_4_35==1), 
And(wtraj_4_36==1, ch_4_36==ch_4_35 -1)), 
# wprim = 0 : robot is static
Implies(And(wprim_4_35==0), 
And(wtraj_4_36==wtraj_4_35, ch_4_36==ch_4_35)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_4_36<6,wprim_4_36==1), 
And(wtraj_4_37==wtraj_4_36+1, ch_4_37==ch_4_36 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_4_36==6,wprim_4_36==1), 
And(wtraj_4_37==1, ch_4_37==ch_4_36 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_4_36==0), 
And(wtraj_4_37==wtraj_4_36, ch_4_37==ch_4_36)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_4_37<6,wprim_4_37==1), 
And(wtraj_4_38==wtraj_4_37+1, ch_4_38==ch_4_37 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_4_37==6,wprim_4_37==1), 
And(wtraj_4_38==1, ch_4_38==ch_4_37 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_4_37==0), 
And(wtraj_4_38==wtraj_4_37, ch_4_38==ch_4_37)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_4_38<6,wprim_4_38==1), 
And(wtraj_4_39==wtraj_4_38+1, ch_4_39==ch_4_38 -1)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_4_38==6,wprim_4_38==1), 
And(wtraj_4_39==1, ch_4_39==ch_4_38 -1)), 
# wprim = 0 : robot is static
Implies(And(wprim_4_38==0), 
And(wtraj_4_39==wtraj_4_38, ch_4_39==ch_4_38)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_4_39<6,wprim_4_39==1), 
And(wtraj_4_40==wtraj_4_39+1, ch_4_40==ch_4_39 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_4_39==6,wprim_4_39==1), 
And(wtraj_4_40==1, ch_4_40==ch_4_39 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_4_39==0), 
And(wtraj_4_40==wtraj_4_39, ch_4_40==ch_4_39)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_4_40<6,wprim_4_40==1), 
And(wtraj_4_41==wtraj_4_40+1, ch_4_41==ch_4_40 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_4_40==6,wprim_4_40==1), 
And(wtraj_4_41==1, ch_4_41==ch_4_40 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_4_40==0), 
And(wtraj_4_41==wtraj_4_40, ch_4_41==ch_4_40)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_4_41<6,wprim_4_41==1), 
And(wtraj_4_42==wtraj_4_41+1, ch_4_42==ch_4_41 -1)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_4_41==6,wprim_4_41==1), 
And(wtraj_4_42==1, ch_4_42==ch_4_41 -1)), 
# wprim = 0 : robot is static
Implies(And(wprim_4_41==0), 
And(wtraj_4_42==wtraj_4_41, ch_4_42==ch_4_41)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_4_42<6,wprim_4_42==1), 
And(wtraj_4_43==wtraj_4_42+1, ch_4_43==ch_4_42 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_4_42==6,wprim_4_42==1), 
And(wtraj_4_43==1, ch_4_43==ch_4_42 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_4_42==0), 
And(wtraj_4_43==wtraj_4_42, ch_4_43==ch_4_42)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_4_43<6,wprim_4_43==1), 
And(wtraj_4_44==wtraj_4_43+1, ch_4_44==ch_4_43 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_4_43==6,wprim_4_43==1), 
And(wtraj_4_44==1, ch_4_44==ch_4_43 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_4_43==0), 
And(wtraj_4_44==wtraj_4_43, ch_4_44==ch_4_43)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_4_44<6,wprim_4_44==1), 
And(wtraj_4_45==wtraj_4_44+1, ch_4_45==ch_4_44 -1)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_4_44==6,wprim_4_44==1), 
And(wtraj_4_45==1, ch_4_45==ch_4_44 -1)), 
# wprim = 0 : robot is static
Implies(And(wprim_4_44==0), 
And(wtraj_4_45==wtraj_4_44, ch_4_45==ch_4_44)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_4_45<6,wprim_4_45==1), 
And(wtraj_4_46==wtraj_4_45+1, ch_4_46==ch_4_45 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_4_45==6,wprim_4_45==1), 
And(wtraj_4_46==1, ch_4_46==ch_4_45 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_4_45==0), 
And(wtraj_4_46==wtraj_4_45, ch_4_46==ch_4_45)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_4_46<6,wprim_4_46==1), 
And(wtraj_4_47==wtraj_4_46+1, ch_4_47==ch_4_46 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_4_46==6,wprim_4_46==1), 
And(wtraj_4_47==1, ch_4_47==ch_4_46 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_4_46==0), 
And(wtraj_4_47==wtraj_4_46, ch_4_47==ch_4_46)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_4_47<6,wprim_4_47==1), 
And(wtraj_4_48==wtraj_4_47+1, ch_4_48==ch_4_47 -1)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_4_47==6,wprim_4_47==1), 
And(wtraj_4_48==1, ch_4_48==ch_4_47 -1)), 
# wprim = 0 : robot is static
Implies(And(wprim_4_47==0), 
And(wtraj_4_48==wtraj_4_47, ch_4_48==ch_4_47)))
# wprim = 1 : robot is on move
s.add(Implies(And(wtraj_4_48<6,wprim_4_48==1), 
And(wtraj_4_49==wtraj_4_48+1, ch_4_49==ch_4_48 -2)), 
# wprim = 1 : robot is on move, circular return to first pos
Implies(And(wtraj_4_48==6,wprim_4_48==1), 
And(wtraj_4_49==1, ch_4_49==ch_4_48 -2)), 
# wprim = 0 : robot is static
Implies(And(wprim_4_48==0), 
And(wtraj_4_49==wtraj_4_48, ch_4_49==ch_4_48)))

# wprim = 2
s.add(Implies(wprim_1_1==2, 
And(wtraj_1_2==wtraj_1_1, ch_1_1<20, ch_1_2==ch_1_1+rech_amt_1_1, 
Or(
And(rprim_1_1==1, rechassigned_1_1==1, rx_1_1==wx_1_1+1, ry_1_1==wy_1_1+0), 
And(rprim_1_1==1, rechassigned_1_1==1, rx_1_1==wx_1_1+1, ry_1_1==wy_1_1+1), 
And(rprim_1_1==1, rechassigned_1_1==1, rx_1_1==wx_1_1+0, ry_1_1==wy_1_1+1), 
And(rprim_1_1==1, rechassigned_1_1==1, rx_1_1==wx_1_1+-1, ry_1_1==wy_1_1+1), 
And(rprim_1_1==1, rechassigned_1_1==1, rx_1_1==wx_1_1+-1, ry_1_1==wy_1_1+0), 
And(rprim_1_1==1, rechassigned_1_1==1, rx_1_1==wx_1_1+-1, ry_1_1==wy_1_1+-1), 
And(rprim_1_1==1, rechassigned_1_1==1, rx_1_1==wx_1_1+0, ry_1_1==wy_1_1+-1), 
And(rprim_1_1==1, rechassigned_1_1==1, rx_1_1==wx_1_1+1, ry_1_1==wy_1_1+-1), 
))))
# wprim = 2
s.add(Implies(wprim_1_2==2, 
And(wtraj_1_3==wtraj_1_2, ch_1_2<20, ch_1_3==ch_1_2+rech_amt_1_2, 
Or(
And(rprim_1_2==1, rechassigned_1_2==1, rx_1_2==wx_1_2+1, ry_1_2==wy_1_2+0), 
And(rprim_1_2==1, rechassigned_1_2==1, rx_1_2==wx_1_2+1, ry_1_2==wy_1_2+1), 
And(rprim_1_2==1, rechassigned_1_2==1, rx_1_2==wx_1_2+0, ry_1_2==wy_1_2+1), 
And(rprim_1_2==1, rechassigned_1_2==1, rx_1_2==wx_1_2+-1, ry_1_2==wy_1_2+1), 
And(rprim_1_2==1, rechassigned_1_2==1, rx_1_2==wx_1_2+-1, ry_1_2==wy_1_2+0), 
And(rprim_1_2==1, rechassigned_1_2==1, rx_1_2==wx_1_2+-1, ry_1_2==wy_1_2+-1), 
And(rprim_1_2==1, rechassigned_1_2==1, rx_1_2==wx_1_2+0, ry_1_2==wy_1_2+-1), 
And(rprim_1_2==1, rechassigned_1_2==1, rx_1_2==wx_1_2+1, ry_1_2==wy_1_2+-1), 
))))
# wprim = 2
s.add(Implies(wprim_1_3==2, 
And(wtraj_1_4==wtraj_1_3, ch_1_3<20, ch_1_4==ch_1_3+rech_amt_1_3, 
Or(
And(rprim_1_3==1, rechassigned_1_3==1, rx_1_3==wx_1_3+1, ry_1_3==wy_1_3+0), 
And(rprim_1_3==1, rechassigned_1_3==1, rx_1_3==wx_1_3+1, ry_1_3==wy_1_3+1), 
And(rprim_1_3==1, rechassigned_1_3==1, rx_1_3==wx_1_3+0, ry_1_3==wy_1_3+1), 
And(rprim_1_3==1, rechassigned_1_3==1, rx_1_3==wx_1_3+-1, ry_1_3==wy_1_3+1), 
And(rprim_1_3==1, rechassigned_1_3==1, rx_1_3==wx_1_3+-1, ry_1_3==wy_1_3+0), 
And(rprim_1_3==1, rechassigned_1_3==1, rx_1_3==wx_1_3+-1, ry_1_3==wy_1_3+-1), 
And(rprim_1_3==1, rechassigned_1_3==1, rx_1_3==wx_1_3+0, ry_1_3==wy_1_3+-1), 
And(rprim_1_3==1, rechassigned_1_3==1, rx_1_3==wx_1_3+1, ry_1_3==wy_1_3+-1), 
))))
# wprim = 2
s.add(Implies(wprim_1_4==2, 
And(wtraj_1_5==wtraj_1_4, ch_1_4<20, ch_1_5==ch_1_4+rech_amt_1_4, 
Or(
And(rprim_1_4==1, rechassigned_1_4==1, rx_1_4==wx_1_4+1, ry_1_4==wy_1_4+0), 
And(rprim_1_4==1, rechassigned_1_4==1, rx_1_4==wx_1_4+1, ry_1_4==wy_1_4+1), 
And(rprim_1_4==1, rechassigned_1_4==1, rx_1_4==wx_1_4+0, ry_1_4==wy_1_4+1), 
And(rprim_1_4==1, rechassigned_1_4==1, rx_1_4==wx_1_4+-1, ry_1_4==wy_1_4+1), 
And(rprim_1_4==1, rechassigned_1_4==1, rx_1_4==wx_1_4+-1, ry_1_4==wy_1_4+0), 
And(rprim_1_4==1, rechassigned_1_4==1, rx_1_4==wx_1_4+-1, ry_1_4==wy_1_4+-1), 
And(rprim_1_4==1, rechassigned_1_4==1, rx_1_4==wx_1_4+0, ry_1_4==wy_1_4+-1), 
And(rprim_1_4==1, rechassigned_1_4==1, rx_1_4==wx_1_4+1, ry_1_4==wy_1_4+-1), 
))))
# wprim = 2
s.add(Implies(wprim_1_5==2, 
And(wtraj_1_6==wtraj_1_5, ch_1_5<20, ch_1_6==ch_1_5+rech_amt_1_5, 
Or(
And(rprim_1_5==1, rechassigned_1_5==1, rx_1_5==wx_1_5+1, ry_1_5==wy_1_5+0), 
And(rprim_1_5==1, rechassigned_1_5==1, rx_1_5==wx_1_5+1, ry_1_5==wy_1_5+1), 
And(rprim_1_5==1, rechassigned_1_5==1, rx_1_5==wx_1_5+0, ry_1_5==wy_1_5+1), 
And(rprim_1_5==1, rechassigned_1_5==1, rx_1_5==wx_1_5+-1, ry_1_5==wy_1_5+1), 
And(rprim_1_5==1, rechassigned_1_5==1, rx_1_5==wx_1_5+-1, ry_1_5==wy_1_5+0), 
And(rprim_1_5==1, rechassigned_1_5==1, rx_1_5==wx_1_5+-1, ry_1_5==wy_1_5+-1), 
And(rprim_1_5==1, rechassigned_1_5==1, rx_1_5==wx_1_5+0, ry_1_5==wy_1_5+-1), 
And(rprim_1_5==1, rechassigned_1_5==1, rx_1_5==wx_1_5+1, ry_1_5==wy_1_5+-1), 
))))
# wprim = 2
s.add(Implies(wprim_1_6==2, 
And(wtraj_1_7==wtraj_1_6, ch_1_6<20, ch_1_7==ch_1_6+rech_amt_1_6, 
Or(
And(rprim_1_6==1, rechassigned_1_6==1, rx_1_6==wx_1_6+1, ry_1_6==wy_1_6+0), 
And(rprim_1_6==1, rechassigned_1_6==1, rx_1_6==wx_1_6+1, ry_1_6==wy_1_6+1), 
And(rprim_1_6==1, rechassigned_1_6==1, rx_1_6==wx_1_6+0, ry_1_6==wy_1_6+1), 
And(rprim_1_6==1, rechassigned_1_6==1, rx_1_6==wx_1_6+-1, ry_1_6==wy_1_6+1), 
And(rprim_1_6==1, rechassigned_1_6==1, rx_1_6==wx_1_6+-1, ry_1_6==wy_1_6+0), 
And(rprim_1_6==1, rechassigned_1_6==1, rx_1_6==wx_1_6+-1, ry_1_6==wy_1_6+-1), 
And(rprim_1_6==1, rechassigned_1_6==1, rx_1_6==wx_1_6+0, ry_1_6==wy_1_6+-1), 
And(rprim_1_6==1, rechassigned_1_6==1, rx_1_6==wx_1_6+1, ry_1_6==wy_1_6+-1), 
))))
# wprim = 2
s.add(Implies(wprim_1_7==2, 
And(wtraj_1_8==wtraj_1_7, ch_1_7<20, ch_1_8==ch_1_7+rech_amt_1_7, 
Or(
And(rprim_1_7==1, rechassigned_1_7==1, rx_1_7==wx_1_7+1, ry_1_7==wy_1_7+0), 
And(rprim_1_7==1, rechassigned_1_7==1, rx_1_7==wx_1_7+1, ry_1_7==wy_1_7+1), 
And(rprim_1_7==1, rechassigned_1_7==1, rx_1_7==wx_1_7+0, ry_1_7==wy_1_7+1), 
And(rprim_1_7==1, rechassigned_1_7==1, rx_1_7==wx_1_7+-1, ry_1_7==wy_1_7+1), 
And(rprim_1_7==1, rechassigned_1_7==1, rx_1_7==wx_1_7+-1, ry_1_7==wy_1_7+0), 
And(rprim_1_7==1, rechassigned_1_7==1, rx_1_7==wx_1_7+-1, ry_1_7==wy_1_7+-1), 
And(rprim_1_7==1, rechassigned_1_7==1, rx_1_7==wx_1_7+0, ry_1_7==wy_1_7+-1), 
And(rprim_1_7==1, rechassigned_1_7==1, rx_1_7==wx_1_7+1, ry_1_7==wy_1_7+-1), 
))))
# wprim = 2
s.add(Implies(wprim_1_8==2, 
And(wtraj_1_9==wtraj_1_8, ch_1_8<20, ch_1_9==ch_1_8+rech_amt_1_8, 
Or(
And(rprim_1_8==1, rechassigned_1_8==1, rx_1_8==wx_1_8+1, ry_1_8==wy_1_8+0), 
And(rprim_1_8==1, rechassigned_1_8==1, rx_1_8==wx_1_8+1, ry_1_8==wy_1_8+1), 
And(rprim_1_8==1, rechassigned_1_8==1, rx_1_8==wx_1_8+0, ry_1_8==wy_1_8+1), 
And(rprim_1_8==1, rechassigned_1_8==1, rx_1_8==wx_1_8+-1, ry_1_8==wy_1_8+1), 
And(rprim_1_8==1, rechassigned_1_8==1, rx_1_8==wx_1_8+-1, ry_1_8==wy_1_8+0), 
And(rprim_1_8==1, rechassigned_1_8==1, rx_1_8==wx_1_8+-1, ry_1_8==wy_1_8+-1), 
And(rprim_1_8==1, rechassigned_1_8==1, rx_1_8==wx_1_8+0, ry_1_8==wy_1_8+-1), 
And(rprim_1_8==1, rechassigned_1_8==1, rx_1_8==wx_1_8+1, ry_1_8==wy_1_8+-1), 
))))
# wprim = 2
s.add(Implies(wprim_1_9==2, 
And(wtraj_1_10==wtraj_1_9, ch_1_9<20, ch_1_10==ch_1_9+rech_amt_1_9, 
Or(
And(rprim_1_9==1, rechassigned_1_9==1, rx_1_9==wx_1_9+1, ry_1_9==wy_1_9+0), 
And(rprim_1_9==1, rechassigned_1_9==1, rx_1_9==wx_1_9+1, ry_1_9==wy_1_9+1), 
And(rprim_1_9==1, rechassigned_1_9==1, rx_1_9==wx_1_9+0, ry_1_9==wy_1_9+1), 
And(rprim_1_9==1, rechassigned_1_9==1, rx_1_9==wx_1_9+-1, ry_1_9==wy_1_9+1), 
And(rprim_1_9==1, rechassigned_1_9==1, rx_1_9==wx_1_9+-1, ry_1_9==wy_1_9+0), 
And(rprim_1_9==1, rechassigned_1_9==1, rx_1_9==wx_1_9+-1, ry_1_9==wy_1_9+-1), 
And(rprim_1_9==1, rechassigned_1_9==1, rx_1_9==wx_1_9+0, ry_1_9==wy_1_9+-1), 
And(rprim_1_9==1, rechassigned_1_9==1, rx_1_9==wx_1_9+1, ry_1_9==wy_1_9+-1), 
))))
# wprim = 2
s.add(Implies(wprim_1_10==2, 
And(wtraj_1_11==wtraj_1_10, ch_1_10<20, ch_1_11==ch_1_10+rech_amt_1_10, 
Or(
And(rprim_1_10==1, rechassigned_1_10==1, rx_1_10==wx_1_10+1, ry_1_10==wy_1_10+0), 
And(rprim_1_10==1, rechassigned_1_10==1, rx_1_10==wx_1_10+1, ry_1_10==wy_1_10+1), 
And(rprim_1_10==1, rechassigned_1_10==1, rx_1_10==wx_1_10+0, ry_1_10==wy_1_10+1), 
And(rprim_1_10==1, rechassigned_1_10==1, rx_1_10==wx_1_10+-1, ry_1_10==wy_1_10+1), 
And(rprim_1_10==1, rechassigned_1_10==1, rx_1_10==wx_1_10+-1, ry_1_10==wy_1_10+0), 
And(rprim_1_10==1, rechassigned_1_10==1, rx_1_10==wx_1_10+-1, ry_1_10==wy_1_10+-1), 
And(rprim_1_10==1, rechassigned_1_10==1, rx_1_10==wx_1_10+0, ry_1_10==wy_1_10+-1), 
And(rprim_1_10==1, rechassigned_1_10==1, rx_1_10==wx_1_10+1, ry_1_10==wy_1_10+-1), 
))))
# wprim = 2
s.add(Implies(wprim_1_11==2, 
And(wtraj_1_12==wtraj_1_11, ch_1_11<20, ch_1_12==ch_1_11+rech_amt_1_11, 
Or(
And(rprim_1_11==1, rechassigned_1_11==1, rx_1_11==wx_1_11+1, ry_1_11==wy_1_11+0), 
And(rprim_1_11==1, rechassigned_1_11==1, rx_1_11==wx_1_11+1, ry_1_11==wy_1_11+1), 
And(rprim_1_11==1, rechassigned_1_11==1, rx_1_11==wx_1_11+0, ry_1_11==wy_1_11+1), 
And(rprim_1_11==1, rechassigned_1_11==1, rx_1_11==wx_1_11+-1, ry_1_11==wy_1_11+1), 
And(rprim_1_11==1, rechassigned_1_11==1, rx_1_11==wx_1_11+-1, ry_1_11==wy_1_11+0), 
And(rprim_1_11==1, rechassigned_1_11==1, rx_1_11==wx_1_11+-1, ry_1_11==wy_1_11+-1), 
And(rprim_1_11==1, rechassigned_1_11==1, rx_1_11==wx_1_11+0, ry_1_11==wy_1_11+-1), 
And(rprim_1_11==1, rechassigned_1_11==1, rx_1_11==wx_1_11+1, ry_1_11==wy_1_11+-1), 
))))
# wprim = 2
s.add(Implies(wprim_1_12==2, 
And(wtraj_1_13==wtraj_1_12, ch_1_12<20, ch_1_13==ch_1_12+rech_amt_1_12, 
Or(
And(rprim_1_12==1, rechassigned_1_12==1, rx_1_12==wx_1_12+1, ry_1_12==wy_1_12+0), 
And(rprim_1_12==1, rechassigned_1_12==1, rx_1_12==wx_1_12+1, ry_1_12==wy_1_12+1), 
And(rprim_1_12==1, rechassigned_1_12==1, rx_1_12==wx_1_12+0, ry_1_12==wy_1_12+1), 
And(rprim_1_12==1, rechassigned_1_12==1, rx_1_12==wx_1_12+-1, ry_1_12==wy_1_12+1), 
And(rprim_1_12==1, rechassigned_1_12==1, rx_1_12==wx_1_12+-1, ry_1_12==wy_1_12+0), 
And(rprim_1_12==1, rechassigned_1_12==1, rx_1_12==wx_1_12+-1, ry_1_12==wy_1_12+-1), 
And(rprim_1_12==1, rechassigned_1_12==1, rx_1_12==wx_1_12+0, ry_1_12==wy_1_12+-1), 
And(rprim_1_12==1, rechassigned_1_12==1, rx_1_12==wx_1_12+1, ry_1_12==wy_1_12+-1), 
))))
# wprim = 2
s.add(Implies(wprim_1_13==2, 
And(wtraj_1_14==wtraj_1_13, ch_1_13<20, ch_1_14==ch_1_13+rech_amt_1_13, 
Or(
And(rprim_1_13==1, rechassigned_1_13==1, rx_1_13==wx_1_13+1, ry_1_13==wy_1_13+0), 
And(rprim_1_13==1, rechassigned_1_13==1, rx_1_13==wx_1_13+1, ry_1_13==wy_1_13+1), 
And(rprim_1_13==1, rechassigned_1_13==1, rx_1_13==wx_1_13+0, ry_1_13==wy_1_13+1), 
And(rprim_1_13==1, rechassigned_1_13==1, rx_1_13==wx_1_13+-1, ry_1_13==wy_1_13+1), 
And(rprim_1_13==1, rechassigned_1_13==1, rx_1_13==wx_1_13+-1, ry_1_13==wy_1_13+0), 
And(rprim_1_13==1, rechassigned_1_13==1, rx_1_13==wx_1_13+-1, ry_1_13==wy_1_13+-1), 
And(rprim_1_13==1, rechassigned_1_13==1, rx_1_13==wx_1_13+0, ry_1_13==wy_1_13+-1), 
And(rprim_1_13==1, rechassigned_1_13==1, rx_1_13==wx_1_13+1, ry_1_13==wy_1_13+-1), 
))))
# wprim = 2
s.add(Implies(wprim_1_14==2, 
And(wtraj_1_15==wtraj_1_14, ch_1_14<20, ch_1_15==ch_1_14+rech_amt_1_14, 
Or(
And(rprim_1_14==1, rechassigned_1_14==1, rx_1_14==wx_1_14+1, ry_1_14==wy_1_14+0), 
And(rprim_1_14==1, rechassigned_1_14==1, rx_1_14==wx_1_14+1, ry_1_14==wy_1_14+1), 
And(rprim_1_14==1, rechassigned_1_14==1, rx_1_14==wx_1_14+0, ry_1_14==wy_1_14+1), 
And(rprim_1_14==1, rechassigned_1_14==1, rx_1_14==wx_1_14+-1, ry_1_14==wy_1_14+1), 
And(rprim_1_14==1, rechassigned_1_14==1, rx_1_14==wx_1_14+-1, ry_1_14==wy_1_14+0), 
And(rprim_1_14==1, rechassigned_1_14==1, rx_1_14==wx_1_14+-1, ry_1_14==wy_1_14+-1), 
And(rprim_1_14==1, rechassigned_1_14==1, rx_1_14==wx_1_14+0, ry_1_14==wy_1_14+-1), 
And(rprim_1_14==1, rechassigned_1_14==1, rx_1_14==wx_1_14+1, ry_1_14==wy_1_14+-1), 
))))
# wprim = 2
s.add(Implies(wprim_1_15==2, 
And(wtraj_1_16==wtraj_1_15, ch_1_15<20, ch_1_16==ch_1_15+rech_amt_1_15, 
Or(
And(rprim_1_15==1, rechassigned_1_15==1, rx_1_15==wx_1_15+1, ry_1_15==wy_1_15+0), 
And(rprim_1_15==1, rechassigned_1_15==1, rx_1_15==wx_1_15+1, ry_1_15==wy_1_15+1), 
And(rprim_1_15==1, rechassigned_1_15==1, rx_1_15==wx_1_15+0, ry_1_15==wy_1_15+1), 
And(rprim_1_15==1, rechassigned_1_15==1, rx_1_15==wx_1_15+-1, ry_1_15==wy_1_15+1), 
And(rprim_1_15==1, rechassigned_1_15==1, rx_1_15==wx_1_15+-1, ry_1_15==wy_1_15+0), 
And(rprim_1_15==1, rechassigned_1_15==1, rx_1_15==wx_1_15+-1, ry_1_15==wy_1_15+-1), 
And(rprim_1_15==1, rechassigned_1_15==1, rx_1_15==wx_1_15+0, ry_1_15==wy_1_15+-1), 
And(rprim_1_15==1, rechassigned_1_15==1, rx_1_15==wx_1_15+1, ry_1_15==wy_1_15+-1), 
))))
# wprim = 2
s.add(Implies(wprim_1_16==2, 
And(wtraj_1_17==wtraj_1_16, ch_1_16<20, ch_1_17==ch_1_16+rech_amt_1_16, 
Or(
And(rprim_1_16==1, rechassigned_1_16==1, rx_1_16==wx_1_16+1, ry_1_16==wy_1_16+0), 
And(rprim_1_16==1, rechassigned_1_16==1, rx_1_16==wx_1_16+1, ry_1_16==wy_1_16+1), 
And(rprim_1_16==1, rechassigned_1_16==1, rx_1_16==wx_1_16+0, ry_1_16==wy_1_16+1), 
And(rprim_1_16==1, rechassigned_1_16==1, rx_1_16==wx_1_16+-1, ry_1_16==wy_1_16+1), 
And(rprim_1_16==1, rechassigned_1_16==1, rx_1_16==wx_1_16+-1, ry_1_16==wy_1_16+0), 
And(rprim_1_16==1, rechassigned_1_16==1, rx_1_16==wx_1_16+-1, ry_1_16==wy_1_16+-1), 
And(rprim_1_16==1, rechassigned_1_16==1, rx_1_16==wx_1_16+0, ry_1_16==wy_1_16+-1), 
And(rprim_1_16==1, rechassigned_1_16==1, rx_1_16==wx_1_16+1, ry_1_16==wy_1_16+-1), 
))))
# wprim = 2
s.add(Implies(wprim_1_17==2, 
And(wtraj_1_18==wtraj_1_17, ch_1_17<20, ch_1_18==ch_1_17+rech_amt_1_17, 
Or(
And(rprim_1_17==1, rechassigned_1_17==1, rx_1_17==wx_1_17+1, ry_1_17==wy_1_17+0), 
And(rprim_1_17==1, rechassigned_1_17==1, rx_1_17==wx_1_17+1, ry_1_17==wy_1_17+1), 
And(rprim_1_17==1, rechassigned_1_17==1, rx_1_17==wx_1_17+0, ry_1_17==wy_1_17+1), 
And(rprim_1_17==1, rechassigned_1_17==1, rx_1_17==wx_1_17+-1, ry_1_17==wy_1_17+1), 
And(rprim_1_17==1, rechassigned_1_17==1, rx_1_17==wx_1_17+-1, ry_1_17==wy_1_17+0), 
And(rprim_1_17==1, rechassigned_1_17==1, rx_1_17==wx_1_17+-1, ry_1_17==wy_1_17+-1), 
And(rprim_1_17==1, rechassigned_1_17==1, rx_1_17==wx_1_17+0, ry_1_17==wy_1_17+-1), 
And(rprim_1_17==1, rechassigned_1_17==1, rx_1_17==wx_1_17+1, ry_1_17==wy_1_17+-1), 
))))
# wprim = 2
s.add(Implies(wprim_1_18==2, 
And(wtraj_1_19==wtraj_1_18, ch_1_18<20, ch_1_19==ch_1_18+rech_amt_1_18, 
Or(
And(rprim_1_18==1, rechassigned_1_18==1, rx_1_18==wx_1_18+1, ry_1_18==wy_1_18+0), 
And(rprim_1_18==1, rechassigned_1_18==1, rx_1_18==wx_1_18+1, ry_1_18==wy_1_18+1), 
And(rprim_1_18==1, rechassigned_1_18==1, rx_1_18==wx_1_18+0, ry_1_18==wy_1_18+1), 
And(rprim_1_18==1, rechassigned_1_18==1, rx_1_18==wx_1_18+-1, ry_1_18==wy_1_18+1), 
And(rprim_1_18==1, rechassigned_1_18==1, rx_1_18==wx_1_18+-1, ry_1_18==wy_1_18+0), 
And(rprim_1_18==1, rechassigned_1_18==1, rx_1_18==wx_1_18+-1, ry_1_18==wy_1_18+-1), 
And(rprim_1_18==1, rechassigned_1_18==1, rx_1_18==wx_1_18+0, ry_1_18==wy_1_18+-1), 
And(rprim_1_18==1, rechassigned_1_18==1, rx_1_18==wx_1_18+1, ry_1_18==wy_1_18+-1), 
))))
# wprim = 2
s.add(Implies(wprim_1_19==2, 
And(wtraj_1_20==wtraj_1_19, ch_1_19<20, ch_1_20==ch_1_19+rech_amt_1_19, 
Or(
And(rprim_1_19==1, rechassigned_1_19==1, rx_1_19==wx_1_19+1, ry_1_19==wy_1_19+0), 
And(rprim_1_19==1, rechassigned_1_19==1, rx_1_19==wx_1_19+1, ry_1_19==wy_1_19+1), 
And(rprim_1_19==1, rechassigned_1_19==1, rx_1_19==wx_1_19+0, ry_1_19==wy_1_19+1), 
And(rprim_1_19==1, rechassigned_1_19==1, rx_1_19==wx_1_19+-1, ry_1_19==wy_1_19+1), 
And(rprim_1_19==1, rechassigned_1_19==1, rx_1_19==wx_1_19+-1, ry_1_19==wy_1_19+0), 
And(rprim_1_19==1, rechassigned_1_19==1, rx_1_19==wx_1_19+-1, ry_1_19==wy_1_19+-1), 
And(rprim_1_19==1, rechassigned_1_19==1, rx_1_19==wx_1_19+0, ry_1_19==wy_1_19+-1), 
And(rprim_1_19==1, rechassigned_1_19==1, rx_1_19==wx_1_19+1, ry_1_19==wy_1_19+-1), 
))))
# wprim = 2
s.add(Implies(wprim_1_20==2, 
And(wtraj_1_21==wtraj_1_20, ch_1_20<20, ch_1_21==ch_1_20+rech_amt_1_20, 
Or(
And(rprim_1_20==1, rechassigned_1_20==1, rx_1_20==wx_1_20+1, ry_1_20==wy_1_20+0), 
And(rprim_1_20==1, rechassigned_1_20==1, rx_1_20==wx_1_20+1, ry_1_20==wy_1_20+1), 
And(rprim_1_20==1, rechassigned_1_20==1, rx_1_20==wx_1_20+0, ry_1_20==wy_1_20+1), 
And(rprim_1_20==1, rechassigned_1_20==1, rx_1_20==wx_1_20+-1, ry_1_20==wy_1_20+1), 
And(rprim_1_20==1, rechassigned_1_20==1, rx_1_20==wx_1_20+-1, ry_1_20==wy_1_20+0), 
And(rprim_1_20==1, rechassigned_1_20==1, rx_1_20==wx_1_20+-1, ry_1_20==wy_1_20+-1), 
And(rprim_1_20==1, rechassigned_1_20==1, rx_1_20==wx_1_20+0, ry_1_20==wy_1_20+-1), 
And(rprim_1_20==1, rechassigned_1_20==1, rx_1_20==wx_1_20+1, ry_1_20==wy_1_20+-1), 
))))
# wprim = 2
s.add(Implies(wprim_1_21==2, 
And(wtraj_1_22==wtraj_1_21, ch_1_21<20, ch_1_22==ch_1_21+rech_amt_1_21, 
Or(
And(rprim_1_21==1, rechassigned_1_21==1, rx_1_21==wx_1_21+1, ry_1_21==wy_1_21+0), 
And(rprim_1_21==1, rechassigned_1_21==1, rx_1_21==wx_1_21+1, ry_1_21==wy_1_21+1), 
And(rprim_1_21==1, rechassigned_1_21==1, rx_1_21==wx_1_21+0, ry_1_21==wy_1_21+1), 
And(rprim_1_21==1, rechassigned_1_21==1, rx_1_21==wx_1_21+-1, ry_1_21==wy_1_21+1), 
And(rprim_1_21==1, rechassigned_1_21==1, rx_1_21==wx_1_21+-1, ry_1_21==wy_1_21+0), 
And(rprim_1_21==1, rechassigned_1_21==1, rx_1_21==wx_1_21+-1, ry_1_21==wy_1_21+-1), 
And(rprim_1_21==1, rechassigned_1_21==1, rx_1_21==wx_1_21+0, ry_1_21==wy_1_21+-1), 
And(rprim_1_21==1, rechassigned_1_21==1, rx_1_21==wx_1_21+1, ry_1_21==wy_1_21+-1), 
))))
# wprim = 2
s.add(Implies(wprim_1_22==2, 
And(wtraj_1_23==wtraj_1_22, ch_1_22<20, ch_1_23==ch_1_22+rech_amt_1_22, 
Or(
And(rprim_1_22==1, rechassigned_1_22==1, rx_1_22==wx_1_22+1, ry_1_22==wy_1_22+0), 
And(rprim_1_22==1, rechassigned_1_22==1, rx_1_22==wx_1_22+1, ry_1_22==wy_1_22+1), 
And(rprim_1_22==1, rechassigned_1_22==1, rx_1_22==wx_1_22+0, ry_1_22==wy_1_22+1), 
And(rprim_1_22==1, rechassigned_1_22==1, rx_1_22==wx_1_22+-1, ry_1_22==wy_1_22+1), 
And(rprim_1_22==1, rechassigned_1_22==1, rx_1_22==wx_1_22+-1, ry_1_22==wy_1_22+0), 
And(rprim_1_22==1, rechassigned_1_22==1, rx_1_22==wx_1_22+-1, ry_1_22==wy_1_22+-1), 
And(rprim_1_22==1, rechassigned_1_22==1, rx_1_22==wx_1_22+0, ry_1_22==wy_1_22+-1), 
And(rprim_1_22==1, rechassigned_1_22==1, rx_1_22==wx_1_22+1, ry_1_22==wy_1_22+-1), 
))))
# wprim = 2
s.add(Implies(wprim_1_23==2, 
And(wtraj_1_24==wtraj_1_23, ch_1_23<20, ch_1_24==ch_1_23+rech_amt_1_23, 
Or(
And(rprim_1_23==1, rechassigned_1_23==1, rx_1_23==wx_1_23+1, ry_1_23==wy_1_23+0), 
And(rprim_1_23==1, rechassigned_1_23==1, rx_1_23==wx_1_23+1, ry_1_23==wy_1_23+1), 
And(rprim_1_23==1, rechassigned_1_23==1, rx_1_23==wx_1_23+0, ry_1_23==wy_1_23+1), 
And(rprim_1_23==1, rechassigned_1_23==1, rx_1_23==wx_1_23+-1, ry_1_23==wy_1_23+1), 
And(rprim_1_23==1, rechassigned_1_23==1, rx_1_23==wx_1_23+-1, ry_1_23==wy_1_23+0), 
And(rprim_1_23==1, rechassigned_1_23==1, rx_1_23==wx_1_23+-1, ry_1_23==wy_1_23+-1), 
And(rprim_1_23==1, rechassigned_1_23==1, rx_1_23==wx_1_23+0, ry_1_23==wy_1_23+-1), 
And(rprim_1_23==1, rechassigned_1_23==1, rx_1_23==wx_1_23+1, ry_1_23==wy_1_23+-1), 
))))
# wprim = 2
s.add(Implies(wprim_1_24==2, 
And(wtraj_1_25==wtraj_1_24, ch_1_24<20, ch_1_25==ch_1_24+rech_amt_1_24, 
Or(
And(rprim_1_24==1, rechassigned_1_24==1, rx_1_24==wx_1_24+1, ry_1_24==wy_1_24+0), 
And(rprim_1_24==1, rechassigned_1_24==1, rx_1_24==wx_1_24+1, ry_1_24==wy_1_24+1), 
And(rprim_1_24==1, rechassigned_1_24==1, rx_1_24==wx_1_24+0, ry_1_24==wy_1_24+1), 
And(rprim_1_24==1, rechassigned_1_24==1, rx_1_24==wx_1_24+-1, ry_1_24==wy_1_24+1), 
And(rprim_1_24==1, rechassigned_1_24==1, rx_1_24==wx_1_24+-1, ry_1_24==wy_1_24+0), 
And(rprim_1_24==1, rechassigned_1_24==1, rx_1_24==wx_1_24+-1, ry_1_24==wy_1_24+-1), 
And(rprim_1_24==1, rechassigned_1_24==1, rx_1_24==wx_1_24+0, ry_1_24==wy_1_24+-1), 
And(rprim_1_24==1, rechassigned_1_24==1, rx_1_24==wx_1_24+1, ry_1_24==wy_1_24+-1), 
))))
# wprim = 2
s.add(Implies(wprim_1_25==2, 
And(wtraj_1_26==wtraj_1_25, ch_1_25<20, ch_1_26==ch_1_25+rech_amt_1_25, 
Or(
And(rprim_1_25==1, rechassigned_1_25==1, rx_1_25==wx_1_25+1, ry_1_25==wy_1_25+0), 
And(rprim_1_25==1, rechassigned_1_25==1, rx_1_25==wx_1_25+1, ry_1_25==wy_1_25+1), 
And(rprim_1_25==1, rechassigned_1_25==1, rx_1_25==wx_1_25+0, ry_1_25==wy_1_25+1), 
And(rprim_1_25==1, rechassigned_1_25==1, rx_1_25==wx_1_25+-1, ry_1_25==wy_1_25+1), 
And(rprim_1_25==1, rechassigned_1_25==1, rx_1_25==wx_1_25+-1, ry_1_25==wy_1_25+0), 
And(rprim_1_25==1, rechassigned_1_25==1, rx_1_25==wx_1_25+-1, ry_1_25==wy_1_25+-1), 
And(rprim_1_25==1, rechassigned_1_25==1, rx_1_25==wx_1_25+0, ry_1_25==wy_1_25+-1), 
And(rprim_1_25==1, rechassigned_1_25==1, rx_1_25==wx_1_25+1, ry_1_25==wy_1_25+-1), 
))))
# wprim = 2
s.add(Implies(wprim_1_26==2, 
And(wtraj_1_27==wtraj_1_26, ch_1_26<20, ch_1_27==ch_1_26+rech_amt_1_26, 
Or(
And(rprim_1_26==1, rechassigned_1_26==1, rx_1_26==wx_1_26+1, ry_1_26==wy_1_26+0), 
And(rprim_1_26==1, rechassigned_1_26==1, rx_1_26==wx_1_26+1, ry_1_26==wy_1_26+1), 
And(rprim_1_26==1, rechassigned_1_26==1, rx_1_26==wx_1_26+0, ry_1_26==wy_1_26+1), 
And(rprim_1_26==1, rechassigned_1_26==1, rx_1_26==wx_1_26+-1, ry_1_26==wy_1_26+1), 
And(rprim_1_26==1, rechassigned_1_26==1, rx_1_26==wx_1_26+-1, ry_1_26==wy_1_26+0), 
And(rprim_1_26==1, rechassigned_1_26==1, rx_1_26==wx_1_26+-1, ry_1_26==wy_1_26+-1), 
And(rprim_1_26==1, rechassigned_1_26==1, rx_1_26==wx_1_26+0, ry_1_26==wy_1_26+-1), 
And(rprim_1_26==1, rechassigned_1_26==1, rx_1_26==wx_1_26+1, ry_1_26==wy_1_26+-1), 
))))
# wprim = 2
s.add(Implies(wprim_1_27==2, 
And(wtraj_1_28==wtraj_1_27, ch_1_27<20, ch_1_28==ch_1_27+rech_amt_1_27, 
Or(
And(rprim_1_27==1, rechassigned_1_27==1, rx_1_27==wx_1_27+1, ry_1_27==wy_1_27+0), 
And(rprim_1_27==1, rechassigned_1_27==1, rx_1_27==wx_1_27+1, ry_1_27==wy_1_27+1), 
And(rprim_1_27==1, rechassigned_1_27==1, rx_1_27==wx_1_27+0, ry_1_27==wy_1_27+1), 
And(rprim_1_27==1, rechassigned_1_27==1, rx_1_27==wx_1_27+-1, ry_1_27==wy_1_27+1), 
And(rprim_1_27==1, rechassigned_1_27==1, rx_1_27==wx_1_27+-1, ry_1_27==wy_1_27+0), 
And(rprim_1_27==1, rechassigned_1_27==1, rx_1_27==wx_1_27+-1, ry_1_27==wy_1_27+-1), 
And(rprim_1_27==1, rechassigned_1_27==1, rx_1_27==wx_1_27+0, ry_1_27==wy_1_27+-1), 
And(rprim_1_27==1, rechassigned_1_27==1, rx_1_27==wx_1_27+1, ry_1_27==wy_1_27+-1), 
))))
# wprim = 2
s.add(Implies(wprim_1_28==2, 
And(wtraj_1_29==wtraj_1_28, ch_1_28<20, ch_1_29==ch_1_28+rech_amt_1_28, 
Or(
And(rprim_1_28==1, rechassigned_1_28==1, rx_1_28==wx_1_28+1, ry_1_28==wy_1_28+0), 
And(rprim_1_28==1, rechassigned_1_28==1, rx_1_28==wx_1_28+1, ry_1_28==wy_1_28+1), 
And(rprim_1_28==1, rechassigned_1_28==1, rx_1_28==wx_1_28+0, ry_1_28==wy_1_28+1), 
And(rprim_1_28==1, rechassigned_1_28==1, rx_1_28==wx_1_28+-1, ry_1_28==wy_1_28+1), 
And(rprim_1_28==1, rechassigned_1_28==1, rx_1_28==wx_1_28+-1, ry_1_28==wy_1_28+0), 
And(rprim_1_28==1, rechassigned_1_28==1, rx_1_28==wx_1_28+-1, ry_1_28==wy_1_28+-1), 
And(rprim_1_28==1, rechassigned_1_28==1, rx_1_28==wx_1_28+0, ry_1_28==wy_1_28+-1), 
And(rprim_1_28==1, rechassigned_1_28==1, rx_1_28==wx_1_28+1, ry_1_28==wy_1_28+-1), 
))))
# wprim = 2
s.add(Implies(wprim_1_29==2, 
And(wtraj_1_30==wtraj_1_29, ch_1_29<20, ch_1_30==ch_1_29+rech_amt_1_29, 
Or(
And(rprim_1_29==1, rechassigned_1_29==1, rx_1_29==wx_1_29+1, ry_1_29==wy_1_29+0), 
And(rprim_1_29==1, rechassigned_1_29==1, rx_1_29==wx_1_29+1, ry_1_29==wy_1_29+1), 
And(rprim_1_29==1, rechassigned_1_29==1, rx_1_29==wx_1_29+0, ry_1_29==wy_1_29+1), 
And(rprim_1_29==1, rechassigned_1_29==1, rx_1_29==wx_1_29+-1, ry_1_29==wy_1_29+1), 
And(rprim_1_29==1, rechassigned_1_29==1, rx_1_29==wx_1_29+-1, ry_1_29==wy_1_29+0), 
And(rprim_1_29==1, rechassigned_1_29==1, rx_1_29==wx_1_29+-1, ry_1_29==wy_1_29+-1), 
And(rprim_1_29==1, rechassigned_1_29==1, rx_1_29==wx_1_29+0, ry_1_29==wy_1_29+-1), 
And(rprim_1_29==1, rechassigned_1_29==1, rx_1_29==wx_1_29+1, ry_1_29==wy_1_29+-1), 
))))
# wprim = 2
s.add(Implies(wprim_1_30==2, 
And(wtraj_1_31==wtraj_1_30, ch_1_30<20, ch_1_31==ch_1_30+rech_amt_1_30, 
Or(
And(rprim_1_30==1, rechassigned_1_30==1, rx_1_30==wx_1_30+1, ry_1_30==wy_1_30+0), 
And(rprim_1_30==1, rechassigned_1_30==1, rx_1_30==wx_1_30+1, ry_1_30==wy_1_30+1), 
And(rprim_1_30==1, rechassigned_1_30==1, rx_1_30==wx_1_30+0, ry_1_30==wy_1_30+1), 
And(rprim_1_30==1, rechassigned_1_30==1, rx_1_30==wx_1_30+-1, ry_1_30==wy_1_30+1), 
And(rprim_1_30==1, rechassigned_1_30==1, rx_1_30==wx_1_30+-1, ry_1_30==wy_1_30+0), 
And(rprim_1_30==1, rechassigned_1_30==1, rx_1_30==wx_1_30+-1, ry_1_30==wy_1_30+-1), 
And(rprim_1_30==1, rechassigned_1_30==1, rx_1_30==wx_1_30+0, ry_1_30==wy_1_30+-1), 
And(rprim_1_30==1, rechassigned_1_30==1, rx_1_30==wx_1_30+1, ry_1_30==wy_1_30+-1), 
))))
# wprim = 2
s.add(Implies(wprim_1_31==2, 
And(wtraj_1_32==wtraj_1_31, ch_1_31<20, ch_1_32==ch_1_31+rech_amt_1_31, 
Or(
And(rprim_1_31==1, rechassigned_1_31==1, rx_1_31==wx_1_31+1, ry_1_31==wy_1_31+0), 
And(rprim_1_31==1, rechassigned_1_31==1, rx_1_31==wx_1_31+1, ry_1_31==wy_1_31+1), 
And(rprim_1_31==1, rechassigned_1_31==1, rx_1_31==wx_1_31+0, ry_1_31==wy_1_31+1), 
And(rprim_1_31==1, rechassigned_1_31==1, rx_1_31==wx_1_31+-1, ry_1_31==wy_1_31+1), 
And(rprim_1_31==1, rechassigned_1_31==1, rx_1_31==wx_1_31+-1, ry_1_31==wy_1_31+0), 
And(rprim_1_31==1, rechassigned_1_31==1, rx_1_31==wx_1_31+-1, ry_1_31==wy_1_31+-1), 
And(rprim_1_31==1, rechassigned_1_31==1, rx_1_31==wx_1_31+0, ry_1_31==wy_1_31+-1), 
And(rprim_1_31==1, rechassigned_1_31==1, rx_1_31==wx_1_31+1, ry_1_31==wy_1_31+-1), 
))))
# wprim = 2
s.add(Implies(wprim_1_32==2, 
And(wtraj_1_33==wtraj_1_32, ch_1_32<20, ch_1_33==ch_1_32+rech_amt_1_32, 
Or(
And(rprim_1_32==1, rechassigned_1_32==1, rx_1_32==wx_1_32+1, ry_1_32==wy_1_32+0), 
And(rprim_1_32==1, rechassigned_1_32==1, rx_1_32==wx_1_32+1, ry_1_32==wy_1_32+1), 
And(rprim_1_32==1, rechassigned_1_32==1, rx_1_32==wx_1_32+0, ry_1_32==wy_1_32+1), 
And(rprim_1_32==1, rechassigned_1_32==1, rx_1_32==wx_1_32+-1, ry_1_32==wy_1_32+1), 
And(rprim_1_32==1, rechassigned_1_32==1, rx_1_32==wx_1_32+-1, ry_1_32==wy_1_32+0), 
And(rprim_1_32==1, rechassigned_1_32==1, rx_1_32==wx_1_32+-1, ry_1_32==wy_1_32+-1), 
And(rprim_1_32==1, rechassigned_1_32==1, rx_1_32==wx_1_32+0, ry_1_32==wy_1_32+-1), 
And(rprim_1_32==1, rechassigned_1_32==1, rx_1_32==wx_1_32+1, ry_1_32==wy_1_32+-1), 
))))
# wprim = 2
s.add(Implies(wprim_1_33==2, 
And(wtraj_1_34==wtraj_1_33, ch_1_33<20, ch_1_34==ch_1_33+rech_amt_1_33, 
Or(
And(rprim_1_33==1, rechassigned_1_33==1, rx_1_33==wx_1_33+1, ry_1_33==wy_1_33+0), 
And(rprim_1_33==1, rechassigned_1_33==1, rx_1_33==wx_1_33+1, ry_1_33==wy_1_33+1), 
And(rprim_1_33==1, rechassigned_1_33==1, rx_1_33==wx_1_33+0, ry_1_33==wy_1_33+1), 
And(rprim_1_33==1, rechassigned_1_33==1, rx_1_33==wx_1_33+-1, ry_1_33==wy_1_33+1), 
And(rprim_1_33==1, rechassigned_1_33==1, rx_1_33==wx_1_33+-1, ry_1_33==wy_1_33+0), 
And(rprim_1_33==1, rechassigned_1_33==1, rx_1_33==wx_1_33+-1, ry_1_33==wy_1_33+-1), 
And(rprim_1_33==1, rechassigned_1_33==1, rx_1_33==wx_1_33+0, ry_1_33==wy_1_33+-1), 
And(rprim_1_33==1, rechassigned_1_33==1, rx_1_33==wx_1_33+1, ry_1_33==wy_1_33+-1), 
))))
# wprim = 2
s.add(Implies(wprim_1_34==2, 
And(wtraj_1_35==wtraj_1_34, ch_1_34<20, ch_1_35==ch_1_34+rech_amt_1_34, 
Or(
And(rprim_1_34==1, rechassigned_1_34==1, rx_1_34==wx_1_34+1, ry_1_34==wy_1_34+0), 
And(rprim_1_34==1, rechassigned_1_34==1, rx_1_34==wx_1_34+1, ry_1_34==wy_1_34+1), 
And(rprim_1_34==1, rechassigned_1_34==1, rx_1_34==wx_1_34+0, ry_1_34==wy_1_34+1), 
And(rprim_1_34==1, rechassigned_1_34==1, rx_1_34==wx_1_34+-1, ry_1_34==wy_1_34+1), 
And(rprim_1_34==1, rechassigned_1_34==1, rx_1_34==wx_1_34+-1, ry_1_34==wy_1_34+0), 
And(rprim_1_34==1, rechassigned_1_34==1, rx_1_34==wx_1_34+-1, ry_1_34==wy_1_34+-1), 
And(rprim_1_34==1, rechassigned_1_34==1, rx_1_34==wx_1_34+0, ry_1_34==wy_1_34+-1), 
And(rprim_1_34==1, rechassigned_1_34==1, rx_1_34==wx_1_34+1, ry_1_34==wy_1_34+-1), 
))))
# wprim = 2
s.add(Implies(wprim_1_35==2, 
And(wtraj_1_36==wtraj_1_35, ch_1_35<20, ch_1_36==ch_1_35+rech_amt_1_35, 
Or(
And(rprim_1_35==1, rechassigned_1_35==1, rx_1_35==wx_1_35+1, ry_1_35==wy_1_35+0), 
And(rprim_1_35==1, rechassigned_1_35==1, rx_1_35==wx_1_35+1, ry_1_35==wy_1_35+1), 
And(rprim_1_35==1, rechassigned_1_35==1, rx_1_35==wx_1_35+0, ry_1_35==wy_1_35+1), 
And(rprim_1_35==1, rechassigned_1_35==1, rx_1_35==wx_1_35+-1, ry_1_35==wy_1_35+1), 
And(rprim_1_35==1, rechassigned_1_35==1, rx_1_35==wx_1_35+-1, ry_1_35==wy_1_35+0), 
And(rprim_1_35==1, rechassigned_1_35==1, rx_1_35==wx_1_35+-1, ry_1_35==wy_1_35+-1), 
And(rprim_1_35==1, rechassigned_1_35==1, rx_1_35==wx_1_35+0, ry_1_35==wy_1_35+-1), 
And(rprim_1_35==1, rechassigned_1_35==1, rx_1_35==wx_1_35+1, ry_1_35==wy_1_35+-1), 
))))
# wprim = 2
s.add(Implies(wprim_1_36==2, 
And(wtraj_1_37==wtraj_1_36, ch_1_36<20, ch_1_37==ch_1_36+rech_amt_1_36, 
Or(
And(rprim_1_36==1, rechassigned_1_36==1, rx_1_36==wx_1_36+1, ry_1_36==wy_1_36+0), 
And(rprim_1_36==1, rechassigned_1_36==1, rx_1_36==wx_1_36+1, ry_1_36==wy_1_36+1), 
And(rprim_1_36==1, rechassigned_1_36==1, rx_1_36==wx_1_36+0, ry_1_36==wy_1_36+1), 
And(rprim_1_36==1, rechassigned_1_36==1, rx_1_36==wx_1_36+-1, ry_1_36==wy_1_36+1), 
And(rprim_1_36==1, rechassigned_1_36==1, rx_1_36==wx_1_36+-1, ry_1_36==wy_1_36+0), 
And(rprim_1_36==1, rechassigned_1_36==1, rx_1_36==wx_1_36+-1, ry_1_36==wy_1_36+-1), 
And(rprim_1_36==1, rechassigned_1_36==1, rx_1_36==wx_1_36+0, ry_1_36==wy_1_36+-1), 
And(rprim_1_36==1, rechassigned_1_36==1, rx_1_36==wx_1_36+1, ry_1_36==wy_1_36+-1), 
))))
# wprim = 2
s.add(Implies(wprim_1_37==2, 
And(wtraj_1_38==wtraj_1_37, ch_1_37<20, ch_1_38==ch_1_37+rech_amt_1_37, 
Or(
And(rprim_1_37==1, rechassigned_1_37==1, rx_1_37==wx_1_37+1, ry_1_37==wy_1_37+0), 
And(rprim_1_37==1, rechassigned_1_37==1, rx_1_37==wx_1_37+1, ry_1_37==wy_1_37+1), 
And(rprim_1_37==1, rechassigned_1_37==1, rx_1_37==wx_1_37+0, ry_1_37==wy_1_37+1), 
And(rprim_1_37==1, rechassigned_1_37==1, rx_1_37==wx_1_37+-1, ry_1_37==wy_1_37+1), 
And(rprim_1_37==1, rechassigned_1_37==1, rx_1_37==wx_1_37+-1, ry_1_37==wy_1_37+0), 
And(rprim_1_37==1, rechassigned_1_37==1, rx_1_37==wx_1_37+-1, ry_1_37==wy_1_37+-1), 
And(rprim_1_37==1, rechassigned_1_37==1, rx_1_37==wx_1_37+0, ry_1_37==wy_1_37+-1), 
And(rprim_1_37==1, rechassigned_1_37==1, rx_1_37==wx_1_37+1, ry_1_37==wy_1_37+-1), 
))))
# wprim = 2
s.add(Implies(wprim_1_38==2, 
And(wtraj_1_39==wtraj_1_38, ch_1_38<20, ch_1_39==ch_1_38+rech_amt_1_38, 
Or(
And(rprim_1_38==1, rechassigned_1_38==1, rx_1_38==wx_1_38+1, ry_1_38==wy_1_38+0), 
And(rprim_1_38==1, rechassigned_1_38==1, rx_1_38==wx_1_38+1, ry_1_38==wy_1_38+1), 
And(rprim_1_38==1, rechassigned_1_38==1, rx_1_38==wx_1_38+0, ry_1_38==wy_1_38+1), 
And(rprim_1_38==1, rechassigned_1_38==1, rx_1_38==wx_1_38+-1, ry_1_38==wy_1_38+1), 
And(rprim_1_38==1, rechassigned_1_38==1, rx_1_38==wx_1_38+-1, ry_1_38==wy_1_38+0), 
And(rprim_1_38==1, rechassigned_1_38==1, rx_1_38==wx_1_38+-1, ry_1_38==wy_1_38+-1), 
And(rprim_1_38==1, rechassigned_1_38==1, rx_1_38==wx_1_38+0, ry_1_38==wy_1_38+-1), 
And(rprim_1_38==1, rechassigned_1_38==1, rx_1_38==wx_1_38+1, ry_1_38==wy_1_38+-1), 
))))
# wprim = 2
s.add(Implies(wprim_1_39==2, 
And(wtraj_1_40==wtraj_1_39, ch_1_39<20, ch_1_40==ch_1_39+rech_amt_1_39, 
Or(
And(rprim_1_39==1, rechassigned_1_39==1, rx_1_39==wx_1_39+1, ry_1_39==wy_1_39+0), 
And(rprim_1_39==1, rechassigned_1_39==1, rx_1_39==wx_1_39+1, ry_1_39==wy_1_39+1), 
And(rprim_1_39==1, rechassigned_1_39==1, rx_1_39==wx_1_39+0, ry_1_39==wy_1_39+1), 
And(rprim_1_39==1, rechassigned_1_39==1, rx_1_39==wx_1_39+-1, ry_1_39==wy_1_39+1), 
And(rprim_1_39==1, rechassigned_1_39==1, rx_1_39==wx_1_39+-1, ry_1_39==wy_1_39+0), 
And(rprim_1_39==1, rechassigned_1_39==1, rx_1_39==wx_1_39+-1, ry_1_39==wy_1_39+-1), 
And(rprim_1_39==1, rechassigned_1_39==1, rx_1_39==wx_1_39+0, ry_1_39==wy_1_39+-1), 
And(rprim_1_39==1, rechassigned_1_39==1, rx_1_39==wx_1_39+1, ry_1_39==wy_1_39+-1), 
))))
# wprim = 2
s.add(Implies(wprim_1_40==2, 
And(wtraj_1_41==wtraj_1_40, ch_1_40<20, ch_1_41==ch_1_40+rech_amt_1_40, 
Or(
And(rprim_1_40==1, rechassigned_1_40==1, rx_1_40==wx_1_40+1, ry_1_40==wy_1_40+0), 
And(rprim_1_40==1, rechassigned_1_40==1, rx_1_40==wx_1_40+1, ry_1_40==wy_1_40+1), 
And(rprim_1_40==1, rechassigned_1_40==1, rx_1_40==wx_1_40+0, ry_1_40==wy_1_40+1), 
And(rprim_1_40==1, rechassigned_1_40==1, rx_1_40==wx_1_40+-1, ry_1_40==wy_1_40+1), 
And(rprim_1_40==1, rechassigned_1_40==1, rx_1_40==wx_1_40+-1, ry_1_40==wy_1_40+0), 
And(rprim_1_40==1, rechassigned_1_40==1, rx_1_40==wx_1_40+-1, ry_1_40==wy_1_40+-1), 
And(rprim_1_40==1, rechassigned_1_40==1, rx_1_40==wx_1_40+0, ry_1_40==wy_1_40+-1), 
And(rprim_1_40==1, rechassigned_1_40==1, rx_1_40==wx_1_40+1, ry_1_40==wy_1_40+-1), 
))))
# wprim = 2
s.add(Implies(wprim_1_41==2, 
And(wtraj_1_42==wtraj_1_41, ch_1_41<20, ch_1_42==ch_1_41+rech_amt_1_41, 
Or(
And(rprim_1_41==1, rechassigned_1_41==1, rx_1_41==wx_1_41+1, ry_1_41==wy_1_41+0), 
And(rprim_1_41==1, rechassigned_1_41==1, rx_1_41==wx_1_41+1, ry_1_41==wy_1_41+1), 
And(rprim_1_41==1, rechassigned_1_41==1, rx_1_41==wx_1_41+0, ry_1_41==wy_1_41+1), 
And(rprim_1_41==1, rechassigned_1_41==1, rx_1_41==wx_1_41+-1, ry_1_41==wy_1_41+1), 
And(rprim_1_41==1, rechassigned_1_41==1, rx_1_41==wx_1_41+-1, ry_1_41==wy_1_41+0), 
And(rprim_1_41==1, rechassigned_1_41==1, rx_1_41==wx_1_41+-1, ry_1_41==wy_1_41+-1), 
And(rprim_1_41==1, rechassigned_1_41==1, rx_1_41==wx_1_41+0, ry_1_41==wy_1_41+-1), 
And(rprim_1_41==1, rechassigned_1_41==1, rx_1_41==wx_1_41+1, ry_1_41==wy_1_41+-1), 
))))
# wprim = 2
s.add(Implies(wprim_1_42==2, 
And(wtraj_1_43==wtraj_1_42, ch_1_42<20, ch_1_43==ch_1_42+rech_amt_1_42, 
Or(
And(rprim_1_42==1, rechassigned_1_42==1, rx_1_42==wx_1_42+1, ry_1_42==wy_1_42+0), 
And(rprim_1_42==1, rechassigned_1_42==1, rx_1_42==wx_1_42+1, ry_1_42==wy_1_42+1), 
And(rprim_1_42==1, rechassigned_1_42==1, rx_1_42==wx_1_42+0, ry_1_42==wy_1_42+1), 
And(rprim_1_42==1, rechassigned_1_42==1, rx_1_42==wx_1_42+-1, ry_1_42==wy_1_42+1), 
And(rprim_1_42==1, rechassigned_1_42==1, rx_1_42==wx_1_42+-1, ry_1_42==wy_1_42+0), 
And(rprim_1_42==1, rechassigned_1_42==1, rx_1_42==wx_1_42+-1, ry_1_42==wy_1_42+-1), 
And(rprim_1_42==1, rechassigned_1_42==1, rx_1_42==wx_1_42+0, ry_1_42==wy_1_42+-1), 
And(rprim_1_42==1, rechassigned_1_42==1, rx_1_42==wx_1_42+1, ry_1_42==wy_1_42+-1), 
))))
# wprim = 2
s.add(Implies(wprim_1_43==2, 
And(wtraj_1_44==wtraj_1_43, ch_1_43<20, ch_1_44==ch_1_43+rech_amt_1_43, 
Or(
And(rprim_1_43==1, rechassigned_1_43==1, rx_1_43==wx_1_43+1, ry_1_43==wy_1_43+0), 
And(rprim_1_43==1, rechassigned_1_43==1, rx_1_43==wx_1_43+1, ry_1_43==wy_1_43+1), 
And(rprim_1_43==1, rechassigned_1_43==1, rx_1_43==wx_1_43+0, ry_1_43==wy_1_43+1), 
And(rprim_1_43==1, rechassigned_1_43==1, rx_1_43==wx_1_43+-1, ry_1_43==wy_1_43+1), 
And(rprim_1_43==1, rechassigned_1_43==1, rx_1_43==wx_1_43+-1, ry_1_43==wy_1_43+0), 
And(rprim_1_43==1, rechassigned_1_43==1, rx_1_43==wx_1_43+-1, ry_1_43==wy_1_43+-1), 
And(rprim_1_43==1, rechassigned_1_43==1, rx_1_43==wx_1_43+0, ry_1_43==wy_1_43+-1), 
And(rprim_1_43==1, rechassigned_1_43==1, rx_1_43==wx_1_43+1, ry_1_43==wy_1_43+-1), 
))))
# wprim = 2
s.add(Implies(wprim_1_44==2, 
And(wtraj_1_45==wtraj_1_44, ch_1_44<20, ch_1_45==ch_1_44+rech_amt_1_44, 
Or(
And(rprim_1_44==1, rechassigned_1_44==1, rx_1_44==wx_1_44+1, ry_1_44==wy_1_44+0), 
And(rprim_1_44==1, rechassigned_1_44==1, rx_1_44==wx_1_44+1, ry_1_44==wy_1_44+1), 
And(rprim_1_44==1, rechassigned_1_44==1, rx_1_44==wx_1_44+0, ry_1_44==wy_1_44+1), 
And(rprim_1_44==1, rechassigned_1_44==1, rx_1_44==wx_1_44+-1, ry_1_44==wy_1_44+1), 
And(rprim_1_44==1, rechassigned_1_44==1, rx_1_44==wx_1_44+-1, ry_1_44==wy_1_44+0), 
And(rprim_1_44==1, rechassigned_1_44==1, rx_1_44==wx_1_44+-1, ry_1_44==wy_1_44+-1), 
And(rprim_1_44==1, rechassigned_1_44==1, rx_1_44==wx_1_44+0, ry_1_44==wy_1_44+-1), 
And(rprim_1_44==1, rechassigned_1_44==1, rx_1_44==wx_1_44+1, ry_1_44==wy_1_44+-1), 
))))
# wprim = 2
s.add(Implies(wprim_1_45==2, 
And(wtraj_1_46==wtraj_1_45, ch_1_45<20, ch_1_46==ch_1_45+rech_amt_1_45, 
Or(
And(rprim_1_45==1, rechassigned_1_45==1, rx_1_45==wx_1_45+1, ry_1_45==wy_1_45+0), 
And(rprim_1_45==1, rechassigned_1_45==1, rx_1_45==wx_1_45+1, ry_1_45==wy_1_45+1), 
And(rprim_1_45==1, rechassigned_1_45==1, rx_1_45==wx_1_45+0, ry_1_45==wy_1_45+1), 
And(rprim_1_45==1, rechassigned_1_45==1, rx_1_45==wx_1_45+-1, ry_1_45==wy_1_45+1), 
And(rprim_1_45==1, rechassigned_1_45==1, rx_1_45==wx_1_45+-1, ry_1_45==wy_1_45+0), 
And(rprim_1_45==1, rechassigned_1_45==1, rx_1_45==wx_1_45+-1, ry_1_45==wy_1_45+-1), 
And(rprim_1_45==1, rechassigned_1_45==1, rx_1_45==wx_1_45+0, ry_1_45==wy_1_45+-1), 
And(rprim_1_45==1, rechassigned_1_45==1, rx_1_45==wx_1_45+1, ry_1_45==wy_1_45+-1), 
))))
# wprim = 2
s.add(Implies(wprim_1_46==2, 
And(wtraj_1_47==wtraj_1_46, ch_1_46<20, ch_1_47==ch_1_46+rech_amt_1_46, 
Or(
And(rprim_1_46==1, rechassigned_1_46==1, rx_1_46==wx_1_46+1, ry_1_46==wy_1_46+0), 
And(rprim_1_46==1, rechassigned_1_46==1, rx_1_46==wx_1_46+1, ry_1_46==wy_1_46+1), 
And(rprim_1_46==1, rechassigned_1_46==1, rx_1_46==wx_1_46+0, ry_1_46==wy_1_46+1), 
And(rprim_1_46==1, rechassigned_1_46==1, rx_1_46==wx_1_46+-1, ry_1_46==wy_1_46+1), 
And(rprim_1_46==1, rechassigned_1_46==1, rx_1_46==wx_1_46+-1, ry_1_46==wy_1_46+0), 
And(rprim_1_46==1, rechassigned_1_46==1, rx_1_46==wx_1_46+-1, ry_1_46==wy_1_46+-1), 
And(rprim_1_46==1, rechassigned_1_46==1, rx_1_46==wx_1_46+0, ry_1_46==wy_1_46+-1), 
And(rprim_1_46==1, rechassigned_1_46==1, rx_1_46==wx_1_46+1, ry_1_46==wy_1_46+-1), 
))))
# wprim = 2
s.add(Implies(wprim_1_47==2, 
And(wtraj_1_48==wtraj_1_47, ch_1_47<20, ch_1_48==ch_1_47+rech_amt_1_47, 
Or(
And(rprim_1_47==1, rechassigned_1_47==1, rx_1_47==wx_1_47+1, ry_1_47==wy_1_47+0), 
And(rprim_1_47==1, rechassigned_1_47==1, rx_1_47==wx_1_47+1, ry_1_47==wy_1_47+1), 
And(rprim_1_47==1, rechassigned_1_47==1, rx_1_47==wx_1_47+0, ry_1_47==wy_1_47+1), 
And(rprim_1_47==1, rechassigned_1_47==1, rx_1_47==wx_1_47+-1, ry_1_47==wy_1_47+1), 
And(rprim_1_47==1, rechassigned_1_47==1, rx_1_47==wx_1_47+-1, ry_1_47==wy_1_47+0), 
And(rprim_1_47==1, rechassigned_1_47==1, rx_1_47==wx_1_47+-1, ry_1_47==wy_1_47+-1), 
And(rprim_1_47==1, rechassigned_1_47==1, rx_1_47==wx_1_47+0, ry_1_47==wy_1_47+-1), 
And(rprim_1_47==1, rechassigned_1_47==1, rx_1_47==wx_1_47+1, ry_1_47==wy_1_47+-1), 
))))
# wprim = 2
s.add(Implies(wprim_1_48==2, 
And(wtraj_1_49==wtraj_1_48, ch_1_48<20, ch_1_49==ch_1_48+rech_amt_1_48, 
Or(
And(rprim_1_48==1, rechassigned_1_48==1, rx_1_48==wx_1_48+1, ry_1_48==wy_1_48+0), 
And(rprim_1_48==1, rechassigned_1_48==1, rx_1_48==wx_1_48+1, ry_1_48==wy_1_48+1), 
And(rprim_1_48==1, rechassigned_1_48==1, rx_1_48==wx_1_48+0, ry_1_48==wy_1_48+1), 
And(rprim_1_48==1, rechassigned_1_48==1, rx_1_48==wx_1_48+-1, ry_1_48==wy_1_48+1), 
And(rprim_1_48==1, rechassigned_1_48==1, rx_1_48==wx_1_48+-1, ry_1_48==wy_1_48+0), 
And(rprim_1_48==1, rechassigned_1_48==1, rx_1_48==wx_1_48+-1, ry_1_48==wy_1_48+-1), 
And(rprim_1_48==1, rechassigned_1_48==1, rx_1_48==wx_1_48+0, ry_1_48==wy_1_48+-1), 
And(rprim_1_48==1, rechassigned_1_48==1, rx_1_48==wx_1_48+1, ry_1_48==wy_1_48+-1), 
))))
# wprim = 2
s.add(Implies(wprim_2_1==2, 
And(wtraj_2_2==wtraj_2_1, ch_2_1<20, ch_2_2==ch_2_1+rech_amt_2_1, 
Or(
And(rprim_1_1==1, rechassigned_2_1==1, rx_1_1==wx_2_1+1, ry_1_1==wy_2_1+0), 
And(rprim_1_1==1, rechassigned_2_1==1, rx_1_1==wx_2_1+1, ry_1_1==wy_2_1+1), 
And(rprim_1_1==1, rechassigned_2_1==1, rx_1_1==wx_2_1+0, ry_1_1==wy_2_1+1), 
And(rprim_1_1==1, rechassigned_2_1==1, rx_1_1==wx_2_1+-1, ry_1_1==wy_2_1+1), 
And(rprim_1_1==1, rechassigned_2_1==1, rx_1_1==wx_2_1+-1, ry_1_1==wy_2_1+0), 
And(rprim_1_1==1, rechassigned_2_1==1, rx_1_1==wx_2_1+-1, ry_1_1==wy_2_1+-1), 
And(rprim_1_1==1, rechassigned_2_1==1, rx_1_1==wx_2_1+0, ry_1_1==wy_2_1+-1), 
And(rprim_1_1==1, rechassigned_2_1==1, rx_1_1==wx_2_1+1, ry_1_1==wy_2_1+-1), 
))))
# wprim = 2
s.add(Implies(wprim_2_2==2, 
And(wtraj_2_3==wtraj_2_2, ch_2_2<20, ch_2_3==ch_2_2+rech_amt_2_2, 
Or(
And(rprim_1_2==1, rechassigned_2_2==1, rx_1_2==wx_2_2+1, ry_1_2==wy_2_2+0), 
And(rprim_1_2==1, rechassigned_2_2==1, rx_1_2==wx_2_2+1, ry_1_2==wy_2_2+1), 
And(rprim_1_2==1, rechassigned_2_2==1, rx_1_2==wx_2_2+0, ry_1_2==wy_2_2+1), 
And(rprim_1_2==1, rechassigned_2_2==1, rx_1_2==wx_2_2+-1, ry_1_2==wy_2_2+1), 
And(rprim_1_2==1, rechassigned_2_2==1, rx_1_2==wx_2_2+-1, ry_1_2==wy_2_2+0), 
And(rprim_1_2==1, rechassigned_2_2==1, rx_1_2==wx_2_2+-1, ry_1_2==wy_2_2+-1), 
And(rprim_1_2==1, rechassigned_2_2==1, rx_1_2==wx_2_2+0, ry_1_2==wy_2_2+-1), 
And(rprim_1_2==1, rechassigned_2_2==1, rx_1_2==wx_2_2+1, ry_1_2==wy_2_2+-1), 
))))
# wprim = 2
s.add(Implies(wprim_2_3==2, 
And(wtraj_2_4==wtraj_2_3, ch_2_3<20, ch_2_4==ch_2_3+rech_amt_2_3, 
Or(
And(rprim_1_3==1, rechassigned_2_3==1, rx_1_3==wx_2_3+1, ry_1_3==wy_2_3+0), 
And(rprim_1_3==1, rechassigned_2_3==1, rx_1_3==wx_2_3+1, ry_1_3==wy_2_3+1), 
And(rprim_1_3==1, rechassigned_2_3==1, rx_1_3==wx_2_3+0, ry_1_3==wy_2_3+1), 
And(rprim_1_3==1, rechassigned_2_3==1, rx_1_3==wx_2_3+-1, ry_1_3==wy_2_3+1), 
And(rprim_1_3==1, rechassigned_2_3==1, rx_1_3==wx_2_3+-1, ry_1_3==wy_2_3+0), 
And(rprim_1_3==1, rechassigned_2_3==1, rx_1_3==wx_2_3+-1, ry_1_3==wy_2_3+-1), 
And(rprim_1_3==1, rechassigned_2_3==1, rx_1_3==wx_2_3+0, ry_1_3==wy_2_3+-1), 
And(rprim_1_3==1, rechassigned_2_3==1, rx_1_3==wx_2_3+1, ry_1_3==wy_2_3+-1), 
))))
# wprim = 2
s.add(Implies(wprim_2_4==2, 
And(wtraj_2_5==wtraj_2_4, ch_2_4<20, ch_2_5==ch_2_4+rech_amt_2_4, 
Or(
And(rprim_1_4==1, rechassigned_2_4==1, rx_1_4==wx_2_4+1, ry_1_4==wy_2_4+0), 
And(rprim_1_4==1, rechassigned_2_4==1, rx_1_4==wx_2_4+1, ry_1_4==wy_2_4+1), 
And(rprim_1_4==1, rechassigned_2_4==1, rx_1_4==wx_2_4+0, ry_1_4==wy_2_4+1), 
And(rprim_1_4==1, rechassigned_2_4==1, rx_1_4==wx_2_4+-1, ry_1_4==wy_2_4+1), 
And(rprim_1_4==1, rechassigned_2_4==1, rx_1_4==wx_2_4+-1, ry_1_4==wy_2_4+0), 
And(rprim_1_4==1, rechassigned_2_4==1, rx_1_4==wx_2_4+-1, ry_1_4==wy_2_4+-1), 
And(rprim_1_4==1, rechassigned_2_4==1, rx_1_4==wx_2_4+0, ry_1_4==wy_2_4+-1), 
And(rprim_1_4==1, rechassigned_2_4==1, rx_1_4==wx_2_4+1, ry_1_4==wy_2_4+-1), 
))))
# wprim = 2
s.add(Implies(wprim_2_5==2, 
And(wtraj_2_6==wtraj_2_5, ch_2_5<20, ch_2_6==ch_2_5+rech_amt_2_5, 
Or(
And(rprim_1_5==1, rechassigned_2_5==1, rx_1_5==wx_2_5+1, ry_1_5==wy_2_5+0), 
And(rprim_1_5==1, rechassigned_2_5==1, rx_1_5==wx_2_5+1, ry_1_5==wy_2_5+1), 
And(rprim_1_5==1, rechassigned_2_5==1, rx_1_5==wx_2_5+0, ry_1_5==wy_2_5+1), 
And(rprim_1_5==1, rechassigned_2_5==1, rx_1_5==wx_2_5+-1, ry_1_5==wy_2_5+1), 
And(rprim_1_5==1, rechassigned_2_5==1, rx_1_5==wx_2_5+-1, ry_1_5==wy_2_5+0), 
And(rprim_1_5==1, rechassigned_2_5==1, rx_1_5==wx_2_5+-1, ry_1_5==wy_2_5+-1), 
And(rprim_1_5==1, rechassigned_2_5==1, rx_1_5==wx_2_5+0, ry_1_5==wy_2_5+-1), 
And(rprim_1_5==1, rechassigned_2_5==1, rx_1_5==wx_2_5+1, ry_1_5==wy_2_5+-1), 
))))
# wprim = 2
s.add(Implies(wprim_2_6==2, 
And(wtraj_2_7==wtraj_2_6, ch_2_6<20, ch_2_7==ch_2_6+rech_amt_2_6, 
Or(
And(rprim_1_6==1, rechassigned_2_6==1, rx_1_6==wx_2_6+1, ry_1_6==wy_2_6+0), 
And(rprim_1_6==1, rechassigned_2_6==1, rx_1_6==wx_2_6+1, ry_1_6==wy_2_6+1), 
And(rprim_1_6==1, rechassigned_2_6==1, rx_1_6==wx_2_6+0, ry_1_6==wy_2_6+1), 
And(rprim_1_6==1, rechassigned_2_6==1, rx_1_6==wx_2_6+-1, ry_1_6==wy_2_6+1), 
And(rprim_1_6==1, rechassigned_2_6==1, rx_1_6==wx_2_6+-1, ry_1_6==wy_2_6+0), 
And(rprim_1_6==1, rechassigned_2_6==1, rx_1_6==wx_2_6+-1, ry_1_6==wy_2_6+-1), 
And(rprim_1_6==1, rechassigned_2_6==1, rx_1_6==wx_2_6+0, ry_1_6==wy_2_6+-1), 
And(rprim_1_6==1, rechassigned_2_6==1, rx_1_6==wx_2_6+1, ry_1_6==wy_2_6+-1), 
))))
# wprim = 2
s.add(Implies(wprim_2_7==2, 
And(wtraj_2_8==wtraj_2_7, ch_2_7<20, ch_2_8==ch_2_7+rech_amt_2_7, 
Or(
And(rprim_1_7==1, rechassigned_2_7==1, rx_1_7==wx_2_7+1, ry_1_7==wy_2_7+0), 
And(rprim_1_7==1, rechassigned_2_7==1, rx_1_7==wx_2_7+1, ry_1_7==wy_2_7+1), 
And(rprim_1_7==1, rechassigned_2_7==1, rx_1_7==wx_2_7+0, ry_1_7==wy_2_7+1), 
And(rprim_1_7==1, rechassigned_2_7==1, rx_1_7==wx_2_7+-1, ry_1_7==wy_2_7+1), 
And(rprim_1_7==1, rechassigned_2_7==1, rx_1_7==wx_2_7+-1, ry_1_7==wy_2_7+0), 
And(rprim_1_7==1, rechassigned_2_7==1, rx_1_7==wx_2_7+-1, ry_1_7==wy_2_7+-1), 
And(rprim_1_7==1, rechassigned_2_7==1, rx_1_7==wx_2_7+0, ry_1_7==wy_2_7+-1), 
And(rprim_1_7==1, rechassigned_2_7==1, rx_1_7==wx_2_7+1, ry_1_7==wy_2_7+-1), 
))))
# wprim = 2
s.add(Implies(wprim_2_8==2, 
And(wtraj_2_9==wtraj_2_8, ch_2_8<20, ch_2_9==ch_2_8+rech_amt_2_8, 
Or(
And(rprim_1_8==1, rechassigned_2_8==1, rx_1_8==wx_2_8+1, ry_1_8==wy_2_8+0), 
And(rprim_1_8==1, rechassigned_2_8==1, rx_1_8==wx_2_8+1, ry_1_8==wy_2_8+1), 
And(rprim_1_8==1, rechassigned_2_8==1, rx_1_8==wx_2_8+0, ry_1_8==wy_2_8+1), 
And(rprim_1_8==1, rechassigned_2_8==1, rx_1_8==wx_2_8+-1, ry_1_8==wy_2_8+1), 
And(rprim_1_8==1, rechassigned_2_8==1, rx_1_8==wx_2_8+-1, ry_1_8==wy_2_8+0), 
And(rprim_1_8==1, rechassigned_2_8==1, rx_1_8==wx_2_8+-1, ry_1_8==wy_2_8+-1), 
And(rprim_1_8==1, rechassigned_2_8==1, rx_1_8==wx_2_8+0, ry_1_8==wy_2_8+-1), 
And(rprim_1_8==1, rechassigned_2_8==1, rx_1_8==wx_2_8+1, ry_1_8==wy_2_8+-1), 
))))
# wprim = 2
s.add(Implies(wprim_2_9==2, 
And(wtraj_2_10==wtraj_2_9, ch_2_9<20, ch_2_10==ch_2_9+rech_amt_2_9, 
Or(
And(rprim_1_9==1, rechassigned_2_9==1, rx_1_9==wx_2_9+1, ry_1_9==wy_2_9+0), 
And(rprim_1_9==1, rechassigned_2_9==1, rx_1_9==wx_2_9+1, ry_1_9==wy_2_9+1), 
And(rprim_1_9==1, rechassigned_2_9==1, rx_1_9==wx_2_9+0, ry_1_9==wy_2_9+1), 
And(rprim_1_9==1, rechassigned_2_9==1, rx_1_9==wx_2_9+-1, ry_1_9==wy_2_9+1), 
And(rprim_1_9==1, rechassigned_2_9==1, rx_1_9==wx_2_9+-1, ry_1_9==wy_2_9+0), 
And(rprim_1_9==1, rechassigned_2_9==1, rx_1_9==wx_2_9+-1, ry_1_9==wy_2_9+-1), 
And(rprim_1_9==1, rechassigned_2_9==1, rx_1_9==wx_2_9+0, ry_1_9==wy_2_9+-1), 
And(rprim_1_9==1, rechassigned_2_9==1, rx_1_9==wx_2_9+1, ry_1_9==wy_2_9+-1), 
))))
# wprim = 2
s.add(Implies(wprim_2_10==2, 
And(wtraj_2_11==wtraj_2_10, ch_2_10<20, ch_2_11==ch_2_10+rech_amt_2_10, 
Or(
And(rprim_1_10==1, rechassigned_2_10==1, rx_1_10==wx_2_10+1, ry_1_10==wy_2_10+0), 
And(rprim_1_10==1, rechassigned_2_10==1, rx_1_10==wx_2_10+1, ry_1_10==wy_2_10+1), 
And(rprim_1_10==1, rechassigned_2_10==1, rx_1_10==wx_2_10+0, ry_1_10==wy_2_10+1), 
And(rprim_1_10==1, rechassigned_2_10==1, rx_1_10==wx_2_10+-1, ry_1_10==wy_2_10+1), 
And(rprim_1_10==1, rechassigned_2_10==1, rx_1_10==wx_2_10+-1, ry_1_10==wy_2_10+0), 
And(rprim_1_10==1, rechassigned_2_10==1, rx_1_10==wx_2_10+-1, ry_1_10==wy_2_10+-1), 
And(rprim_1_10==1, rechassigned_2_10==1, rx_1_10==wx_2_10+0, ry_1_10==wy_2_10+-1), 
And(rprim_1_10==1, rechassigned_2_10==1, rx_1_10==wx_2_10+1, ry_1_10==wy_2_10+-1), 
))))
# wprim = 2
s.add(Implies(wprim_2_11==2, 
And(wtraj_2_12==wtraj_2_11, ch_2_11<20, ch_2_12==ch_2_11+rech_amt_2_11, 
Or(
And(rprim_1_11==1, rechassigned_2_11==1, rx_1_11==wx_2_11+1, ry_1_11==wy_2_11+0), 
And(rprim_1_11==1, rechassigned_2_11==1, rx_1_11==wx_2_11+1, ry_1_11==wy_2_11+1), 
And(rprim_1_11==1, rechassigned_2_11==1, rx_1_11==wx_2_11+0, ry_1_11==wy_2_11+1), 
And(rprim_1_11==1, rechassigned_2_11==1, rx_1_11==wx_2_11+-1, ry_1_11==wy_2_11+1), 
And(rprim_1_11==1, rechassigned_2_11==1, rx_1_11==wx_2_11+-1, ry_1_11==wy_2_11+0), 
And(rprim_1_11==1, rechassigned_2_11==1, rx_1_11==wx_2_11+-1, ry_1_11==wy_2_11+-1), 
And(rprim_1_11==1, rechassigned_2_11==1, rx_1_11==wx_2_11+0, ry_1_11==wy_2_11+-1), 
And(rprim_1_11==1, rechassigned_2_11==1, rx_1_11==wx_2_11+1, ry_1_11==wy_2_11+-1), 
))))
# wprim = 2
s.add(Implies(wprim_2_12==2, 
And(wtraj_2_13==wtraj_2_12, ch_2_12<20, ch_2_13==ch_2_12+rech_amt_2_12, 
Or(
And(rprim_1_12==1, rechassigned_2_12==1, rx_1_12==wx_2_12+1, ry_1_12==wy_2_12+0), 
And(rprim_1_12==1, rechassigned_2_12==1, rx_1_12==wx_2_12+1, ry_1_12==wy_2_12+1), 
And(rprim_1_12==1, rechassigned_2_12==1, rx_1_12==wx_2_12+0, ry_1_12==wy_2_12+1), 
And(rprim_1_12==1, rechassigned_2_12==1, rx_1_12==wx_2_12+-1, ry_1_12==wy_2_12+1), 
And(rprim_1_12==1, rechassigned_2_12==1, rx_1_12==wx_2_12+-1, ry_1_12==wy_2_12+0), 
And(rprim_1_12==1, rechassigned_2_12==1, rx_1_12==wx_2_12+-1, ry_1_12==wy_2_12+-1), 
And(rprim_1_12==1, rechassigned_2_12==1, rx_1_12==wx_2_12+0, ry_1_12==wy_2_12+-1), 
And(rprim_1_12==1, rechassigned_2_12==1, rx_1_12==wx_2_12+1, ry_1_12==wy_2_12+-1), 
))))
# wprim = 2
s.add(Implies(wprim_2_13==2, 
And(wtraj_2_14==wtraj_2_13, ch_2_13<20, ch_2_14==ch_2_13+rech_amt_2_13, 
Or(
And(rprim_1_13==1, rechassigned_2_13==1, rx_1_13==wx_2_13+1, ry_1_13==wy_2_13+0), 
And(rprim_1_13==1, rechassigned_2_13==1, rx_1_13==wx_2_13+1, ry_1_13==wy_2_13+1), 
And(rprim_1_13==1, rechassigned_2_13==1, rx_1_13==wx_2_13+0, ry_1_13==wy_2_13+1), 
And(rprim_1_13==1, rechassigned_2_13==1, rx_1_13==wx_2_13+-1, ry_1_13==wy_2_13+1), 
And(rprim_1_13==1, rechassigned_2_13==1, rx_1_13==wx_2_13+-1, ry_1_13==wy_2_13+0), 
And(rprim_1_13==1, rechassigned_2_13==1, rx_1_13==wx_2_13+-1, ry_1_13==wy_2_13+-1), 
And(rprim_1_13==1, rechassigned_2_13==1, rx_1_13==wx_2_13+0, ry_1_13==wy_2_13+-1), 
And(rprim_1_13==1, rechassigned_2_13==1, rx_1_13==wx_2_13+1, ry_1_13==wy_2_13+-1), 
))))
# wprim = 2
s.add(Implies(wprim_2_14==2, 
And(wtraj_2_15==wtraj_2_14, ch_2_14<20, ch_2_15==ch_2_14+rech_amt_2_14, 
Or(
And(rprim_1_14==1, rechassigned_2_14==1, rx_1_14==wx_2_14+1, ry_1_14==wy_2_14+0), 
And(rprim_1_14==1, rechassigned_2_14==1, rx_1_14==wx_2_14+1, ry_1_14==wy_2_14+1), 
And(rprim_1_14==1, rechassigned_2_14==1, rx_1_14==wx_2_14+0, ry_1_14==wy_2_14+1), 
And(rprim_1_14==1, rechassigned_2_14==1, rx_1_14==wx_2_14+-1, ry_1_14==wy_2_14+1), 
And(rprim_1_14==1, rechassigned_2_14==1, rx_1_14==wx_2_14+-1, ry_1_14==wy_2_14+0), 
And(rprim_1_14==1, rechassigned_2_14==1, rx_1_14==wx_2_14+-1, ry_1_14==wy_2_14+-1), 
And(rprim_1_14==1, rechassigned_2_14==1, rx_1_14==wx_2_14+0, ry_1_14==wy_2_14+-1), 
And(rprim_1_14==1, rechassigned_2_14==1, rx_1_14==wx_2_14+1, ry_1_14==wy_2_14+-1), 
))))
# wprim = 2
s.add(Implies(wprim_2_15==2, 
And(wtraj_2_16==wtraj_2_15, ch_2_15<20, ch_2_16==ch_2_15+rech_amt_2_15, 
Or(
And(rprim_1_15==1, rechassigned_2_15==1, rx_1_15==wx_2_15+1, ry_1_15==wy_2_15+0), 
And(rprim_1_15==1, rechassigned_2_15==1, rx_1_15==wx_2_15+1, ry_1_15==wy_2_15+1), 
And(rprim_1_15==1, rechassigned_2_15==1, rx_1_15==wx_2_15+0, ry_1_15==wy_2_15+1), 
And(rprim_1_15==1, rechassigned_2_15==1, rx_1_15==wx_2_15+-1, ry_1_15==wy_2_15+1), 
And(rprim_1_15==1, rechassigned_2_15==1, rx_1_15==wx_2_15+-1, ry_1_15==wy_2_15+0), 
And(rprim_1_15==1, rechassigned_2_15==1, rx_1_15==wx_2_15+-1, ry_1_15==wy_2_15+-1), 
And(rprim_1_15==1, rechassigned_2_15==1, rx_1_15==wx_2_15+0, ry_1_15==wy_2_15+-1), 
And(rprim_1_15==1, rechassigned_2_15==1, rx_1_15==wx_2_15+1, ry_1_15==wy_2_15+-1), 
))))
# wprim = 2
s.add(Implies(wprim_2_16==2, 
And(wtraj_2_17==wtraj_2_16, ch_2_16<20, ch_2_17==ch_2_16+rech_amt_2_16, 
Or(
And(rprim_1_16==1, rechassigned_2_16==1, rx_1_16==wx_2_16+1, ry_1_16==wy_2_16+0), 
And(rprim_1_16==1, rechassigned_2_16==1, rx_1_16==wx_2_16+1, ry_1_16==wy_2_16+1), 
And(rprim_1_16==1, rechassigned_2_16==1, rx_1_16==wx_2_16+0, ry_1_16==wy_2_16+1), 
And(rprim_1_16==1, rechassigned_2_16==1, rx_1_16==wx_2_16+-1, ry_1_16==wy_2_16+1), 
And(rprim_1_16==1, rechassigned_2_16==1, rx_1_16==wx_2_16+-1, ry_1_16==wy_2_16+0), 
And(rprim_1_16==1, rechassigned_2_16==1, rx_1_16==wx_2_16+-1, ry_1_16==wy_2_16+-1), 
And(rprim_1_16==1, rechassigned_2_16==1, rx_1_16==wx_2_16+0, ry_1_16==wy_2_16+-1), 
And(rprim_1_16==1, rechassigned_2_16==1, rx_1_16==wx_2_16+1, ry_1_16==wy_2_16+-1), 
))))
# wprim = 2
s.add(Implies(wprim_2_17==2, 
And(wtraj_2_18==wtraj_2_17, ch_2_17<20, ch_2_18==ch_2_17+rech_amt_2_17, 
Or(
And(rprim_1_17==1, rechassigned_2_17==1, rx_1_17==wx_2_17+1, ry_1_17==wy_2_17+0), 
And(rprim_1_17==1, rechassigned_2_17==1, rx_1_17==wx_2_17+1, ry_1_17==wy_2_17+1), 
And(rprim_1_17==1, rechassigned_2_17==1, rx_1_17==wx_2_17+0, ry_1_17==wy_2_17+1), 
And(rprim_1_17==1, rechassigned_2_17==1, rx_1_17==wx_2_17+-1, ry_1_17==wy_2_17+1), 
And(rprim_1_17==1, rechassigned_2_17==1, rx_1_17==wx_2_17+-1, ry_1_17==wy_2_17+0), 
And(rprim_1_17==1, rechassigned_2_17==1, rx_1_17==wx_2_17+-1, ry_1_17==wy_2_17+-1), 
And(rprim_1_17==1, rechassigned_2_17==1, rx_1_17==wx_2_17+0, ry_1_17==wy_2_17+-1), 
And(rprim_1_17==1, rechassigned_2_17==1, rx_1_17==wx_2_17+1, ry_1_17==wy_2_17+-1), 
))))
# wprim = 2
s.add(Implies(wprim_2_18==2, 
And(wtraj_2_19==wtraj_2_18, ch_2_18<20, ch_2_19==ch_2_18+rech_amt_2_18, 
Or(
And(rprim_1_18==1, rechassigned_2_18==1, rx_1_18==wx_2_18+1, ry_1_18==wy_2_18+0), 
And(rprim_1_18==1, rechassigned_2_18==1, rx_1_18==wx_2_18+1, ry_1_18==wy_2_18+1), 
And(rprim_1_18==1, rechassigned_2_18==1, rx_1_18==wx_2_18+0, ry_1_18==wy_2_18+1), 
And(rprim_1_18==1, rechassigned_2_18==1, rx_1_18==wx_2_18+-1, ry_1_18==wy_2_18+1), 
And(rprim_1_18==1, rechassigned_2_18==1, rx_1_18==wx_2_18+-1, ry_1_18==wy_2_18+0), 
And(rprim_1_18==1, rechassigned_2_18==1, rx_1_18==wx_2_18+-1, ry_1_18==wy_2_18+-1), 
And(rprim_1_18==1, rechassigned_2_18==1, rx_1_18==wx_2_18+0, ry_1_18==wy_2_18+-1), 
And(rprim_1_18==1, rechassigned_2_18==1, rx_1_18==wx_2_18+1, ry_1_18==wy_2_18+-1), 
))))
# wprim = 2
s.add(Implies(wprim_2_19==2, 
And(wtraj_2_20==wtraj_2_19, ch_2_19<20, ch_2_20==ch_2_19+rech_amt_2_19, 
Or(
And(rprim_1_19==1, rechassigned_2_19==1, rx_1_19==wx_2_19+1, ry_1_19==wy_2_19+0), 
And(rprim_1_19==1, rechassigned_2_19==1, rx_1_19==wx_2_19+1, ry_1_19==wy_2_19+1), 
And(rprim_1_19==1, rechassigned_2_19==1, rx_1_19==wx_2_19+0, ry_1_19==wy_2_19+1), 
And(rprim_1_19==1, rechassigned_2_19==1, rx_1_19==wx_2_19+-1, ry_1_19==wy_2_19+1), 
And(rprim_1_19==1, rechassigned_2_19==1, rx_1_19==wx_2_19+-1, ry_1_19==wy_2_19+0), 
And(rprim_1_19==1, rechassigned_2_19==1, rx_1_19==wx_2_19+-1, ry_1_19==wy_2_19+-1), 
And(rprim_1_19==1, rechassigned_2_19==1, rx_1_19==wx_2_19+0, ry_1_19==wy_2_19+-1), 
And(rprim_1_19==1, rechassigned_2_19==1, rx_1_19==wx_2_19+1, ry_1_19==wy_2_19+-1), 
))))
# wprim = 2
s.add(Implies(wprim_2_20==2, 
And(wtraj_2_21==wtraj_2_20, ch_2_20<20, ch_2_21==ch_2_20+rech_amt_2_20, 
Or(
And(rprim_1_20==1, rechassigned_2_20==1, rx_1_20==wx_2_20+1, ry_1_20==wy_2_20+0), 
And(rprim_1_20==1, rechassigned_2_20==1, rx_1_20==wx_2_20+1, ry_1_20==wy_2_20+1), 
And(rprim_1_20==1, rechassigned_2_20==1, rx_1_20==wx_2_20+0, ry_1_20==wy_2_20+1), 
And(rprim_1_20==1, rechassigned_2_20==1, rx_1_20==wx_2_20+-1, ry_1_20==wy_2_20+1), 
And(rprim_1_20==1, rechassigned_2_20==1, rx_1_20==wx_2_20+-1, ry_1_20==wy_2_20+0), 
And(rprim_1_20==1, rechassigned_2_20==1, rx_1_20==wx_2_20+-1, ry_1_20==wy_2_20+-1), 
And(rprim_1_20==1, rechassigned_2_20==1, rx_1_20==wx_2_20+0, ry_1_20==wy_2_20+-1), 
And(rprim_1_20==1, rechassigned_2_20==1, rx_1_20==wx_2_20+1, ry_1_20==wy_2_20+-1), 
))))
# wprim = 2
s.add(Implies(wprim_2_21==2, 
And(wtraj_2_22==wtraj_2_21, ch_2_21<20, ch_2_22==ch_2_21+rech_amt_2_21, 
Or(
And(rprim_1_21==1, rechassigned_2_21==1, rx_1_21==wx_2_21+1, ry_1_21==wy_2_21+0), 
And(rprim_1_21==1, rechassigned_2_21==1, rx_1_21==wx_2_21+1, ry_1_21==wy_2_21+1), 
And(rprim_1_21==1, rechassigned_2_21==1, rx_1_21==wx_2_21+0, ry_1_21==wy_2_21+1), 
And(rprim_1_21==1, rechassigned_2_21==1, rx_1_21==wx_2_21+-1, ry_1_21==wy_2_21+1), 
And(rprim_1_21==1, rechassigned_2_21==1, rx_1_21==wx_2_21+-1, ry_1_21==wy_2_21+0), 
And(rprim_1_21==1, rechassigned_2_21==1, rx_1_21==wx_2_21+-1, ry_1_21==wy_2_21+-1), 
And(rprim_1_21==1, rechassigned_2_21==1, rx_1_21==wx_2_21+0, ry_1_21==wy_2_21+-1), 
And(rprim_1_21==1, rechassigned_2_21==1, rx_1_21==wx_2_21+1, ry_1_21==wy_2_21+-1), 
))))
# wprim = 2
s.add(Implies(wprim_2_22==2, 
And(wtraj_2_23==wtraj_2_22, ch_2_22<20, ch_2_23==ch_2_22+rech_amt_2_22, 
Or(
And(rprim_1_22==1, rechassigned_2_22==1, rx_1_22==wx_2_22+1, ry_1_22==wy_2_22+0), 
And(rprim_1_22==1, rechassigned_2_22==1, rx_1_22==wx_2_22+1, ry_1_22==wy_2_22+1), 
And(rprim_1_22==1, rechassigned_2_22==1, rx_1_22==wx_2_22+0, ry_1_22==wy_2_22+1), 
And(rprim_1_22==1, rechassigned_2_22==1, rx_1_22==wx_2_22+-1, ry_1_22==wy_2_22+1), 
And(rprim_1_22==1, rechassigned_2_22==1, rx_1_22==wx_2_22+-1, ry_1_22==wy_2_22+0), 
And(rprim_1_22==1, rechassigned_2_22==1, rx_1_22==wx_2_22+-1, ry_1_22==wy_2_22+-1), 
And(rprim_1_22==1, rechassigned_2_22==1, rx_1_22==wx_2_22+0, ry_1_22==wy_2_22+-1), 
And(rprim_1_22==1, rechassigned_2_22==1, rx_1_22==wx_2_22+1, ry_1_22==wy_2_22+-1), 
))))
# wprim = 2
s.add(Implies(wprim_2_23==2, 
And(wtraj_2_24==wtraj_2_23, ch_2_23<20, ch_2_24==ch_2_23+rech_amt_2_23, 
Or(
And(rprim_1_23==1, rechassigned_2_23==1, rx_1_23==wx_2_23+1, ry_1_23==wy_2_23+0), 
And(rprim_1_23==1, rechassigned_2_23==1, rx_1_23==wx_2_23+1, ry_1_23==wy_2_23+1), 
And(rprim_1_23==1, rechassigned_2_23==1, rx_1_23==wx_2_23+0, ry_1_23==wy_2_23+1), 
And(rprim_1_23==1, rechassigned_2_23==1, rx_1_23==wx_2_23+-1, ry_1_23==wy_2_23+1), 
And(rprim_1_23==1, rechassigned_2_23==1, rx_1_23==wx_2_23+-1, ry_1_23==wy_2_23+0), 
And(rprim_1_23==1, rechassigned_2_23==1, rx_1_23==wx_2_23+-1, ry_1_23==wy_2_23+-1), 
And(rprim_1_23==1, rechassigned_2_23==1, rx_1_23==wx_2_23+0, ry_1_23==wy_2_23+-1), 
And(rprim_1_23==1, rechassigned_2_23==1, rx_1_23==wx_2_23+1, ry_1_23==wy_2_23+-1), 
))))
# wprim = 2
s.add(Implies(wprim_2_24==2, 
And(wtraj_2_25==wtraj_2_24, ch_2_24<20, ch_2_25==ch_2_24+rech_amt_2_24, 
Or(
And(rprim_1_24==1, rechassigned_2_24==1, rx_1_24==wx_2_24+1, ry_1_24==wy_2_24+0), 
And(rprim_1_24==1, rechassigned_2_24==1, rx_1_24==wx_2_24+1, ry_1_24==wy_2_24+1), 
And(rprim_1_24==1, rechassigned_2_24==1, rx_1_24==wx_2_24+0, ry_1_24==wy_2_24+1), 
And(rprim_1_24==1, rechassigned_2_24==1, rx_1_24==wx_2_24+-1, ry_1_24==wy_2_24+1), 
And(rprim_1_24==1, rechassigned_2_24==1, rx_1_24==wx_2_24+-1, ry_1_24==wy_2_24+0), 
And(rprim_1_24==1, rechassigned_2_24==1, rx_1_24==wx_2_24+-1, ry_1_24==wy_2_24+-1), 
And(rprim_1_24==1, rechassigned_2_24==1, rx_1_24==wx_2_24+0, ry_1_24==wy_2_24+-1), 
And(rprim_1_24==1, rechassigned_2_24==1, rx_1_24==wx_2_24+1, ry_1_24==wy_2_24+-1), 
))))
# wprim = 2
s.add(Implies(wprim_2_25==2, 
And(wtraj_2_26==wtraj_2_25, ch_2_25<20, ch_2_26==ch_2_25+rech_amt_2_25, 
Or(
And(rprim_1_25==1, rechassigned_2_25==1, rx_1_25==wx_2_25+1, ry_1_25==wy_2_25+0), 
And(rprim_1_25==1, rechassigned_2_25==1, rx_1_25==wx_2_25+1, ry_1_25==wy_2_25+1), 
And(rprim_1_25==1, rechassigned_2_25==1, rx_1_25==wx_2_25+0, ry_1_25==wy_2_25+1), 
And(rprim_1_25==1, rechassigned_2_25==1, rx_1_25==wx_2_25+-1, ry_1_25==wy_2_25+1), 
And(rprim_1_25==1, rechassigned_2_25==1, rx_1_25==wx_2_25+-1, ry_1_25==wy_2_25+0), 
And(rprim_1_25==1, rechassigned_2_25==1, rx_1_25==wx_2_25+-1, ry_1_25==wy_2_25+-1), 
And(rprim_1_25==1, rechassigned_2_25==1, rx_1_25==wx_2_25+0, ry_1_25==wy_2_25+-1), 
And(rprim_1_25==1, rechassigned_2_25==1, rx_1_25==wx_2_25+1, ry_1_25==wy_2_25+-1), 
))))
# wprim = 2
s.add(Implies(wprim_2_26==2, 
And(wtraj_2_27==wtraj_2_26, ch_2_26<20, ch_2_27==ch_2_26+rech_amt_2_26, 
Or(
And(rprim_1_26==1, rechassigned_2_26==1, rx_1_26==wx_2_26+1, ry_1_26==wy_2_26+0), 
And(rprim_1_26==1, rechassigned_2_26==1, rx_1_26==wx_2_26+1, ry_1_26==wy_2_26+1), 
And(rprim_1_26==1, rechassigned_2_26==1, rx_1_26==wx_2_26+0, ry_1_26==wy_2_26+1), 
And(rprim_1_26==1, rechassigned_2_26==1, rx_1_26==wx_2_26+-1, ry_1_26==wy_2_26+1), 
And(rprim_1_26==1, rechassigned_2_26==1, rx_1_26==wx_2_26+-1, ry_1_26==wy_2_26+0), 
And(rprim_1_26==1, rechassigned_2_26==1, rx_1_26==wx_2_26+-1, ry_1_26==wy_2_26+-1), 
And(rprim_1_26==1, rechassigned_2_26==1, rx_1_26==wx_2_26+0, ry_1_26==wy_2_26+-1), 
And(rprim_1_26==1, rechassigned_2_26==1, rx_1_26==wx_2_26+1, ry_1_26==wy_2_26+-1), 
))))
# wprim = 2
s.add(Implies(wprim_2_27==2, 
And(wtraj_2_28==wtraj_2_27, ch_2_27<20, ch_2_28==ch_2_27+rech_amt_2_27, 
Or(
And(rprim_1_27==1, rechassigned_2_27==1, rx_1_27==wx_2_27+1, ry_1_27==wy_2_27+0), 
And(rprim_1_27==1, rechassigned_2_27==1, rx_1_27==wx_2_27+1, ry_1_27==wy_2_27+1), 
And(rprim_1_27==1, rechassigned_2_27==1, rx_1_27==wx_2_27+0, ry_1_27==wy_2_27+1), 
And(rprim_1_27==1, rechassigned_2_27==1, rx_1_27==wx_2_27+-1, ry_1_27==wy_2_27+1), 
And(rprim_1_27==1, rechassigned_2_27==1, rx_1_27==wx_2_27+-1, ry_1_27==wy_2_27+0), 
And(rprim_1_27==1, rechassigned_2_27==1, rx_1_27==wx_2_27+-1, ry_1_27==wy_2_27+-1), 
And(rprim_1_27==1, rechassigned_2_27==1, rx_1_27==wx_2_27+0, ry_1_27==wy_2_27+-1), 
And(rprim_1_27==1, rechassigned_2_27==1, rx_1_27==wx_2_27+1, ry_1_27==wy_2_27+-1), 
))))
# wprim = 2
s.add(Implies(wprim_2_28==2, 
And(wtraj_2_29==wtraj_2_28, ch_2_28<20, ch_2_29==ch_2_28+rech_amt_2_28, 
Or(
And(rprim_1_28==1, rechassigned_2_28==1, rx_1_28==wx_2_28+1, ry_1_28==wy_2_28+0), 
And(rprim_1_28==1, rechassigned_2_28==1, rx_1_28==wx_2_28+1, ry_1_28==wy_2_28+1), 
And(rprim_1_28==1, rechassigned_2_28==1, rx_1_28==wx_2_28+0, ry_1_28==wy_2_28+1), 
And(rprim_1_28==1, rechassigned_2_28==1, rx_1_28==wx_2_28+-1, ry_1_28==wy_2_28+1), 
And(rprim_1_28==1, rechassigned_2_28==1, rx_1_28==wx_2_28+-1, ry_1_28==wy_2_28+0), 
And(rprim_1_28==1, rechassigned_2_28==1, rx_1_28==wx_2_28+-1, ry_1_28==wy_2_28+-1), 
And(rprim_1_28==1, rechassigned_2_28==1, rx_1_28==wx_2_28+0, ry_1_28==wy_2_28+-1), 
And(rprim_1_28==1, rechassigned_2_28==1, rx_1_28==wx_2_28+1, ry_1_28==wy_2_28+-1), 
))))
# wprim = 2
s.add(Implies(wprim_2_29==2, 
And(wtraj_2_30==wtraj_2_29, ch_2_29<20, ch_2_30==ch_2_29+rech_amt_2_29, 
Or(
And(rprim_1_29==1, rechassigned_2_29==1, rx_1_29==wx_2_29+1, ry_1_29==wy_2_29+0), 
And(rprim_1_29==1, rechassigned_2_29==1, rx_1_29==wx_2_29+1, ry_1_29==wy_2_29+1), 
And(rprim_1_29==1, rechassigned_2_29==1, rx_1_29==wx_2_29+0, ry_1_29==wy_2_29+1), 
And(rprim_1_29==1, rechassigned_2_29==1, rx_1_29==wx_2_29+-1, ry_1_29==wy_2_29+1), 
And(rprim_1_29==1, rechassigned_2_29==1, rx_1_29==wx_2_29+-1, ry_1_29==wy_2_29+0), 
And(rprim_1_29==1, rechassigned_2_29==1, rx_1_29==wx_2_29+-1, ry_1_29==wy_2_29+-1), 
And(rprim_1_29==1, rechassigned_2_29==1, rx_1_29==wx_2_29+0, ry_1_29==wy_2_29+-1), 
And(rprim_1_29==1, rechassigned_2_29==1, rx_1_29==wx_2_29+1, ry_1_29==wy_2_29+-1), 
))))
# wprim = 2
s.add(Implies(wprim_2_30==2, 
And(wtraj_2_31==wtraj_2_30, ch_2_30<20, ch_2_31==ch_2_30+rech_amt_2_30, 
Or(
And(rprim_1_30==1, rechassigned_2_30==1, rx_1_30==wx_2_30+1, ry_1_30==wy_2_30+0), 
And(rprim_1_30==1, rechassigned_2_30==1, rx_1_30==wx_2_30+1, ry_1_30==wy_2_30+1), 
And(rprim_1_30==1, rechassigned_2_30==1, rx_1_30==wx_2_30+0, ry_1_30==wy_2_30+1), 
And(rprim_1_30==1, rechassigned_2_30==1, rx_1_30==wx_2_30+-1, ry_1_30==wy_2_30+1), 
And(rprim_1_30==1, rechassigned_2_30==1, rx_1_30==wx_2_30+-1, ry_1_30==wy_2_30+0), 
And(rprim_1_30==1, rechassigned_2_30==1, rx_1_30==wx_2_30+-1, ry_1_30==wy_2_30+-1), 
And(rprim_1_30==1, rechassigned_2_30==1, rx_1_30==wx_2_30+0, ry_1_30==wy_2_30+-1), 
And(rprim_1_30==1, rechassigned_2_30==1, rx_1_30==wx_2_30+1, ry_1_30==wy_2_30+-1), 
))))
# wprim = 2
s.add(Implies(wprim_2_31==2, 
And(wtraj_2_32==wtraj_2_31, ch_2_31<20, ch_2_32==ch_2_31+rech_amt_2_31, 
Or(
And(rprim_1_31==1, rechassigned_2_31==1, rx_1_31==wx_2_31+1, ry_1_31==wy_2_31+0), 
And(rprim_1_31==1, rechassigned_2_31==1, rx_1_31==wx_2_31+1, ry_1_31==wy_2_31+1), 
And(rprim_1_31==1, rechassigned_2_31==1, rx_1_31==wx_2_31+0, ry_1_31==wy_2_31+1), 
And(rprim_1_31==1, rechassigned_2_31==1, rx_1_31==wx_2_31+-1, ry_1_31==wy_2_31+1), 
And(rprim_1_31==1, rechassigned_2_31==1, rx_1_31==wx_2_31+-1, ry_1_31==wy_2_31+0), 
And(rprim_1_31==1, rechassigned_2_31==1, rx_1_31==wx_2_31+-1, ry_1_31==wy_2_31+-1), 
And(rprim_1_31==1, rechassigned_2_31==1, rx_1_31==wx_2_31+0, ry_1_31==wy_2_31+-1), 
And(rprim_1_31==1, rechassigned_2_31==1, rx_1_31==wx_2_31+1, ry_1_31==wy_2_31+-1), 
))))
# wprim = 2
s.add(Implies(wprim_2_32==2, 
And(wtraj_2_33==wtraj_2_32, ch_2_32<20, ch_2_33==ch_2_32+rech_amt_2_32, 
Or(
And(rprim_1_32==1, rechassigned_2_32==1, rx_1_32==wx_2_32+1, ry_1_32==wy_2_32+0), 
And(rprim_1_32==1, rechassigned_2_32==1, rx_1_32==wx_2_32+1, ry_1_32==wy_2_32+1), 
And(rprim_1_32==1, rechassigned_2_32==1, rx_1_32==wx_2_32+0, ry_1_32==wy_2_32+1), 
And(rprim_1_32==1, rechassigned_2_32==1, rx_1_32==wx_2_32+-1, ry_1_32==wy_2_32+1), 
And(rprim_1_32==1, rechassigned_2_32==1, rx_1_32==wx_2_32+-1, ry_1_32==wy_2_32+0), 
And(rprim_1_32==1, rechassigned_2_32==1, rx_1_32==wx_2_32+-1, ry_1_32==wy_2_32+-1), 
And(rprim_1_32==1, rechassigned_2_32==1, rx_1_32==wx_2_32+0, ry_1_32==wy_2_32+-1), 
And(rprim_1_32==1, rechassigned_2_32==1, rx_1_32==wx_2_32+1, ry_1_32==wy_2_32+-1), 
))))
# wprim = 2
s.add(Implies(wprim_2_33==2, 
And(wtraj_2_34==wtraj_2_33, ch_2_33<20, ch_2_34==ch_2_33+rech_amt_2_33, 
Or(
And(rprim_1_33==1, rechassigned_2_33==1, rx_1_33==wx_2_33+1, ry_1_33==wy_2_33+0), 
And(rprim_1_33==1, rechassigned_2_33==1, rx_1_33==wx_2_33+1, ry_1_33==wy_2_33+1), 
And(rprim_1_33==1, rechassigned_2_33==1, rx_1_33==wx_2_33+0, ry_1_33==wy_2_33+1), 
And(rprim_1_33==1, rechassigned_2_33==1, rx_1_33==wx_2_33+-1, ry_1_33==wy_2_33+1), 
And(rprim_1_33==1, rechassigned_2_33==1, rx_1_33==wx_2_33+-1, ry_1_33==wy_2_33+0), 
And(rprim_1_33==1, rechassigned_2_33==1, rx_1_33==wx_2_33+-1, ry_1_33==wy_2_33+-1), 
And(rprim_1_33==1, rechassigned_2_33==1, rx_1_33==wx_2_33+0, ry_1_33==wy_2_33+-1), 
And(rprim_1_33==1, rechassigned_2_33==1, rx_1_33==wx_2_33+1, ry_1_33==wy_2_33+-1), 
))))
# wprim = 2
s.add(Implies(wprim_2_34==2, 
And(wtraj_2_35==wtraj_2_34, ch_2_34<20, ch_2_35==ch_2_34+rech_amt_2_34, 
Or(
And(rprim_1_34==1, rechassigned_2_34==1, rx_1_34==wx_2_34+1, ry_1_34==wy_2_34+0), 
And(rprim_1_34==1, rechassigned_2_34==1, rx_1_34==wx_2_34+1, ry_1_34==wy_2_34+1), 
And(rprim_1_34==1, rechassigned_2_34==1, rx_1_34==wx_2_34+0, ry_1_34==wy_2_34+1), 
And(rprim_1_34==1, rechassigned_2_34==1, rx_1_34==wx_2_34+-1, ry_1_34==wy_2_34+1), 
And(rprim_1_34==1, rechassigned_2_34==1, rx_1_34==wx_2_34+-1, ry_1_34==wy_2_34+0), 
And(rprim_1_34==1, rechassigned_2_34==1, rx_1_34==wx_2_34+-1, ry_1_34==wy_2_34+-1), 
And(rprim_1_34==1, rechassigned_2_34==1, rx_1_34==wx_2_34+0, ry_1_34==wy_2_34+-1), 
And(rprim_1_34==1, rechassigned_2_34==1, rx_1_34==wx_2_34+1, ry_1_34==wy_2_34+-1), 
))))
# wprim = 2
s.add(Implies(wprim_2_35==2, 
And(wtraj_2_36==wtraj_2_35, ch_2_35<20, ch_2_36==ch_2_35+rech_amt_2_35, 
Or(
And(rprim_1_35==1, rechassigned_2_35==1, rx_1_35==wx_2_35+1, ry_1_35==wy_2_35+0), 
And(rprim_1_35==1, rechassigned_2_35==1, rx_1_35==wx_2_35+1, ry_1_35==wy_2_35+1), 
And(rprim_1_35==1, rechassigned_2_35==1, rx_1_35==wx_2_35+0, ry_1_35==wy_2_35+1), 
And(rprim_1_35==1, rechassigned_2_35==1, rx_1_35==wx_2_35+-1, ry_1_35==wy_2_35+1), 
And(rprim_1_35==1, rechassigned_2_35==1, rx_1_35==wx_2_35+-1, ry_1_35==wy_2_35+0), 
And(rprim_1_35==1, rechassigned_2_35==1, rx_1_35==wx_2_35+-1, ry_1_35==wy_2_35+-1), 
And(rprim_1_35==1, rechassigned_2_35==1, rx_1_35==wx_2_35+0, ry_1_35==wy_2_35+-1), 
And(rprim_1_35==1, rechassigned_2_35==1, rx_1_35==wx_2_35+1, ry_1_35==wy_2_35+-1), 
))))
# wprim = 2
s.add(Implies(wprim_2_36==2, 
And(wtraj_2_37==wtraj_2_36, ch_2_36<20, ch_2_37==ch_2_36+rech_amt_2_36, 
Or(
And(rprim_1_36==1, rechassigned_2_36==1, rx_1_36==wx_2_36+1, ry_1_36==wy_2_36+0), 
And(rprim_1_36==1, rechassigned_2_36==1, rx_1_36==wx_2_36+1, ry_1_36==wy_2_36+1), 
And(rprim_1_36==1, rechassigned_2_36==1, rx_1_36==wx_2_36+0, ry_1_36==wy_2_36+1), 
And(rprim_1_36==1, rechassigned_2_36==1, rx_1_36==wx_2_36+-1, ry_1_36==wy_2_36+1), 
And(rprim_1_36==1, rechassigned_2_36==1, rx_1_36==wx_2_36+-1, ry_1_36==wy_2_36+0), 
And(rprim_1_36==1, rechassigned_2_36==1, rx_1_36==wx_2_36+-1, ry_1_36==wy_2_36+-1), 
And(rprim_1_36==1, rechassigned_2_36==1, rx_1_36==wx_2_36+0, ry_1_36==wy_2_36+-1), 
And(rprim_1_36==1, rechassigned_2_36==1, rx_1_36==wx_2_36+1, ry_1_36==wy_2_36+-1), 
))))
# wprim = 2
s.add(Implies(wprim_2_37==2, 
And(wtraj_2_38==wtraj_2_37, ch_2_37<20, ch_2_38==ch_2_37+rech_amt_2_37, 
Or(
And(rprim_1_37==1, rechassigned_2_37==1, rx_1_37==wx_2_37+1, ry_1_37==wy_2_37+0), 
And(rprim_1_37==1, rechassigned_2_37==1, rx_1_37==wx_2_37+1, ry_1_37==wy_2_37+1), 
And(rprim_1_37==1, rechassigned_2_37==1, rx_1_37==wx_2_37+0, ry_1_37==wy_2_37+1), 
And(rprim_1_37==1, rechassigned_2_37==1, rx_1_37==wx_2_37+-1, ry_1_37==wy_2_37+1), 
And(rprim_1_37==1, rechassigned_2_37==1, rx_1_37==wx_2_37+-1, ry_1_37==wy_2_37+0), 
And(rprim_1_37==1, rechassigned_2_37==1, rx_1_37==wx_2_37+-1, ry_1_37==wy_2_37+-1), 
And(rprim_1_37==1, rechassigned_2_37==1, rx_1_37==wx_2_37+0, ry_1_37==wy_2_37+-1), 
And(rprim_1_37==1, rechassigned_2_37==1, rx_1_37==wx_2_37+1, ry_1_37==wy_2_37+-1), 
))))
# wprim = 2
s.add(Implies(wprim_2_38==2, 
And(wtraj_2_39==wtraj_2_38, ch_2_38<20, ch_2_39==ch_2_38+rech_amt_2_38, 
Or(
And(rprim_1_38==1, rechassigned_2_38==1, rx_1_38==wx_2_38+1, ry_1_38==wy_2_38+0), 
And(rprim_1_38==1, rechassigned_2_38==1, rx_1_38==wx_2_38+1, ry_1_38==wy_2_38+1), 
And(rprim_1_38==1, rechassigned_2_38==1, rx_1_38==wx_2_38+0, ry_1_38==wy_2_38+1), 
And(rprim_1_38==1, rechassigned_2_38==1, rx_1_38==wx_2_38+-1, ry_1_38==wy_2_38+1), 
And(rprim_1_38==1, rechassigned_2_38==1, rx_1_38==wx_2_38+-1, ry_1_38==wy_2_38+0), 
And(rprim_1_38==1, rechassigned_2_38==1, rx_1_38==wx_2_38+-1, ry_1_38==wy_2_38+-1), 
And(rprim_1_38==1, rechassigned_2_38==1, rx_1_38==wx_2_38+0, ry_1_38==wy_2_38+-1), 
And(rprim_1_38==1, rechassigned_2_38==1, rx_1_38==wx_2_38+1, ry_1_38==wy_2_38+-1), 
))))
# wprim = 2
s.add(Implies(wprim_2_39==2, 
And(wtraj_2_40==wtraj_2_39, ch_2_39<20, ch_2_40==ch_2_39+rech_amt_2_39, 
Or(
And(rprim_1_39==1, rechassigned_2_39==1, rx_1_39==wx_2_39+1, ry_1_39==wy_2_39+0), 
And(rprim_1_39==1, rechassigned_2_39==1, rx_1_39==wx_2_39+1, ry_1_39==wy_2_39+1), 
And(rprim_1_39==1, rechassigned_2_39==1, rx_1_39==wx_2_39+0, ry_1_39==wy_2_39+1), 
And(rprim_1_39==1, rechassigned_2_39==1, rx_1_39==wx_2_39+-1, ry_1_39==wy_2_39+1), 
And(rprim_1_39==1, rechassigned_2_39==1, rx_1_39==wx_2_39+-1, ry_1_39==wy_2_39+0), 
And(rprim_1_39==1, rechassigned_2_39==1, rx_1_39==wx_2_39+-1, ry_1_39==wy_2_39+-1), 
And(rprim_1_39==1, rechassigned_2_39==1, rx_1_39==wx_2_39+0, ry_1_39==wy_2_39+-1), 
And(rprim_1_39==1, rechassigned_2_39==1, rx_1_39==wx_2_39+1, ry_1_39==wy_2_39+-1), 
))))
# wprim = 2
s.add(Implies(wprim_2_40==2, 
And(wtraj_2_41==wtraj_2_40, ch_2_40<20, ch_2_41==ch_2_40+rech_amt_2_40, 
Or(
And(rprim_1_40==1, rechassigned_2_40==1, rx_1_40==wx_2_40+1, ry_1_40==wy_2_40+0), 
And(rprim_1_40==1, rechassigned_2_40==1, rx_1_40==wx_2_40+1, ry_1_40==wy_2_40+1), 
And(rprim_1_40==1, rechassigned_2_40==1, rx_1_40==wx_2_40+0, ry_1_40==wy_2_40+1), 
And(rprim_1_40==1, rechassigned_2_40==1, rx_1_40==wx_2_40+-1, ry_1_40==wy_2_40+1), 
And(rprim_1_40==1, rechassigned_2_40==1, rx_1_40==wx_2_40+-1, ry_1_40==wy_2_40+0), 
And(rprim_1_40==1, rechassigned_2_40==1, rx_1_40==wx_2_40+-1, ry_1_40==wy_2_40+-1), 
And(rprim_1_40==1, rechassigned_2_40==1, rx_1_40==wx_2_40+0, ry_1_40==wy_2_40+-1), 
And(rprim_1_40==1, rechassigned_2_40==1, rx_1_40==wx_2_40+1, ry_1_40==wy_2_40+-1), 
))))
# wprim = 2
s.add(Implies(wprim_2_41==2, 
And(wtraj_2_42==wtraj_2_41, ch_2_41<20, ch_2_42==ch_2_41+rech_amt_2_41, 
Or(
And(rprim_1_41==1, rechassigned_2_41==1, rx_1_41==wx_2_41+1, ry_1_41==wy_2_41+0), 
And(rprim_1_41==1, rechassigned_2_41==1, rx_1_41==wx_2_41+1, ry_1_41==wy_2_41+1), 
And(rprim_1_41==1, rechassigned_2_41==1, rx_1_41==wx_2_41+0, ry_1_41==wy_2_41+1), 
And(rprim_1_41==1, rechassigned_2_41==1, rx_1_41==wx_2_41+-1, ry_1_41==wy_2_41+1), 
And(rprim_1_41==1, rechassigned_2_41==1, rx_1_41==wx_2_41+-1, ry_1_41==wy_2_41+0), 
And(rprim_1_41==1, rechassigned_2_41==1, rx_1_41==wx_2_41+-1, ry_1_41==wy_2_41+-1), 
And(rprim_1_41==1, rechassigned_2_41==1, rx_1_41==wx_2_41+0, ry_1_41==wy_2_41+-1), 
And(rprim_1_41==1, rechassigned_2_41==1, rx_1_41==wx_2_41+1, ry_1_41==wy_2_41+-1), 
))))
# wprim = 2
s.add(Implies(wprim_2_42==2, 
And(wtraj_2_43==wtraj_2_42, ch_2_42<20, ch_2_43==ch_2_42+rech_amt_2_42, 
Or(
And(rprim_1_42==1, rechassigned_2_42==1, rx_1_42==wx_2_42+1, ry_1_42==wy_2_42+0), 
And(rprim_1_42==1, rechassigned_2_42==1, rx_1_42==wx_2_42+1, ry_1_42==wy_2_42+1), 
And(rprim_1_42==1, rechassigned_2_42==1, rx_1_42==wx_2_42+0, ry_1_42==wy_2_42+1), 
And(rprim_1_42==1, rechassigned_2_42==1, rx_1_42==wx_2_42+-1, ry_1_42==wy_2_42+1), 
And(rprim_1_42==1, rechassigned_2_42==1, rx_1_42==wx_2_42+-1, ry_1_42==wy_2_42+0), 
And(rprim_1_42==1, rechassigned_2_42==1, rx_1_42==wx_2_42+-1, ry_1_42==wy_2_42+-1), 
And(rprim_1_42==1, rechassigned_2_42==1, rx_1_42==wx_2_42+0, ry_1_42==wy_2_42+-1), 
And(rprim_1_42==1, rechassigned_2_42==1, rx_1_42==wx_2_42+1, ry_1_42==wy_2_42+-1), 
))))
# wprim = 2
s.add(Implies(wprim_2_43==2, 
And(wtraj_2_44==wtraj_2_43, ch_2_43<20, ch_2_44==ch_2_43+rech_amt_2_43, 
Or(
And(rprim_1_43==1, rechassigned_2_43==1, rx_1_43==wx_2_43+1, ry_1_43==wy_2_43+0), 
And(rprim_1_43==1, rechassigned_2_43==1, rx_1_43==wx_2_43+1, ry_1_43==wy_2_43+1), 
And(rprim_1_43==1, rechassigned_2_43==1, rx_1_43==wx_2_43+0, ry_1_43==wy_2_43+1), 
And(rprim_1_43==1, rechassigned_2_43==1, rx_1_43==wx_2_43+-1, ry_1_43==wy_2_43+1), 
And(rprim_1_43==1, rechassigned_2_43==1, rx_1_43==wx_2_43+-1, ry_1_43==wy_2_43+0), 
And(rprim_1_43==1, rechassigned_2_43==1, rx_1_43==wx_2_43+-1, ry_1_43==wy_2_43+-1), 
And(rprim_1_43==1, rechassigned_2_43==1, rx_1_43==wx_2_43+0, ry_1_43==wy_2_43+-1), 
And(rprim_1_43==1, rechassigned_2_43==1, rx_1_43==wx_2_43+1, ry_1_43==wy_2_43+-1), 
))))
# wprim = 2
s.add(Implies(wprim_2_44==2, 
And(wtraj_2_45==wtraj_2_44, ch_2_44<20, ch_2_45==ch_2_44+rech_amt_2_44, 
Or(
And(rprim_1_44==1, rechassigned_2_44==1, rx_1_44==wx_2_44+1, ry_1_44==wy_2_44+0), 
And(rprim_1_44==1, rechassigned_2_44==1, rx_1_44==wx_2_44+1, ry_1_44==wy_2_44+1), 
And(rprim_1_44==1, rechassigned_2_44==1, rx_1_44==wx_2_44+0, ry_1_44==wy_2_44+1), 
And(rprim_1_44==1, rechassigned_2_44==1, rx_1_44==wx_2_44+-1, ry_1_44==wy_2_44+1), 
And(rprim_1_44==1, rechassigned_2_44==1, rx_1_44==wx_2_44+-1, ry_1_44==wy_2_44+0), 
And(rprim_1_44==1, rechassigned_2_44==1, rx_1_44==wx_2_44+-1, ry_1_44==wy_2_44+-1), 
And(rprim_1_44==1, rechassigned_2_44==1, rx_1_44==wx_2_44+0, ry_1_44==wy_2_44+-1), 
And(rprim_1_44==1, rechassigned_2_44==1, rx_1_44==wx_2_44+1, ry_1_44==wy_2_44+-1), 
))))
# wprim = 2
s.add(Implies(wprim_2_45==2, 
And(wtraj_2_46==wtraj_2_45, ch_2_45<20, ch_2_46==ch_2_45+rech_amt_2_45, 
Or(
And(rprim_1_45==1, rechassigned_2_45==1, rx_1_45==wx_2_45+1, ry_1_45==wy_2_45+0), 
And(rprim_1_45==1, rechassigned_2_45==1, rx_1_45==wx_2_45+1, ry_1_45==wy_2_45+1), 
And(rprim_1_45==1, rechassigned_2_45==1, rx_1_45==wx_2_45+0, ry_1_45==wy_2_45+1), 
And(rprim_1_45==1, rechassigned_2_45==1, rx_1_45==wx_2_45+-1, ry_1_45==wy_2_45+1), 
And(rprim_1_45==1, rechassigned_2_45==1, rx_1_45==wx_2_45+-1, ry_1_45==wy_2_45+0), 
And(rprim_1_45==1, rechassigned_2_45==1, rx_1_45==wx_2_45+-1, ry_1_45==wy_2_45+-1), 
And(rprim_1_45==1, rechassigned_2_45==1, rx_1_45==wx_2_45+0, ry_1_45==wy_2_45+-1), 
And(rprim_1_45==1, rechassigned_2_45==1, rx_1_45==wx_2_45+1, ry_1_45==wy_2_45+-1), 
))))
# wprim = 2
s.add(Implies(wprim_2_46==2, 
And(wtraj_2_47==wtraj_2_46, ch_2_46<20, ch_2_47==ch_2_46+rech_amt_2_46, 
Or(
And(rprim_1_46==1, rechassigned_2_46==1, rx_1_46==wx_2_46+1, ry_1_46==wy_2_46+0), 
And(rprim_1_46==1, rechassigned_2_46==1, rx_1_46==wx_2_46+1, ry_1_46==wy_2_46+1), 
And(rprim_1_46==1, rechassigned_2_46==1, rx_1_46==wx_2_46+0, ry_1_46==wy_2_46+1), 
And(rprim_1_46==1, rechassigned_2_46==1, rx_1_46==wx_2_46+-1, ry_1_46==wy_2_46+1), 
And(rprim_1_46==1, rechassigned_2_46==1, rx_1_46==wx_2_46+-1, ry_1_46==wy_2_46+0), 
And(rprim_1_46==1, rechassigned_2_46==1, rx_1_46==wx_2_46+-1, ry_1_46==wy_2_46+-1), 
And(rprim_1_46==1, rechassigned_2_46==1, rx_1_46==wx_2_46+0, ry_1_46==wy_2_46+-1), 
And(rprim_1_46==1, rechassigned_2_46==1, rx_1_46==wx_2_46+1, ry_1_46==wy_2_46+-1), 
))))
# wprim = 2
s.add(Implies(wprim_2_47==2, 
And(wtraj_2_48==wtraj_2_47, ch_2_47<20, ch_2_48==ch_2_47+rech_amt_2_47, 
Or(
And(rprim_1_47==1, rechassigned_2_47==1, rx_1_47==wx_2_47+1, ry_1_47==wy_2_47+0), 
And(rprim_1_47==1, rechassigned_2_47==1, rx_1_47==wx_2_47+1, ry_1_47==wy_2_47+1), 
And(rprim_1_47==1, rechassigned_2_47==1, rx_1_47==wx_2_47+0, ry_1_47==wy_2_47+1), 
And(rprim_1_47==1, rechassigned_2_47==1, rx_1_47==wx_2_47+-1, ry_1_47==wy_2_47+1), 
And(rprim_1_47==1, rechassigned_2_47==1, rx_1_47==wx_2_47+-1, ry_1_47==wy_2_47+0), 
And(rprim_1_47==1, rechassigned_2_47==1, rx_1_47==wx_2_47+-1, ry_1_47==wy_2_47+-1), 
And(rprim_1_47==1, rechassigned_2_47==1, rx_1_47==wx_2_47+0, ry_1_47==wy_2_47+-1), 
And(rprim_1_47==1, rechassigned_2_47==1, rx_1_47==wx_2_47+1, ry_1_47==wy_2_47+-1), 
))))
# wprim = 2
s.add(Implies(wprim_2_48==2, 
And(wtraj_2_49==wtraj_2_48, ch_2_48<20, ch_2_49==ch_2_48+rech_amt_2_48, 
Or(
And(rprim_1_48==1, rechassigned_2_48==1, rx_1_48==wx_2_48+1, ry_1_48==wy_2_48+0), 
And(rprim_1_48==1, rechassigned_2_48==1, rx_1_48==wx_2_48+1, ry_1_48==wy_2_48+1), 
And(rprim_1_48==1, rechassigned_2_48==1, rx_1_48==wx_2_48+0, ry_1_48==wy_2_48+1), 
And(rprim_1_48==1, rechassigned_2_48==1, rx_1_48==wx_2_48+-1, ry_1_48==wy_2_48+1), 
And(rprim_1_48==1, rechassigned_2_48==1, rx_1_48==wx_2_48+-1, ry_1_48==wy_2_48+0), 
And(rprim_1_48==1, rechassigned_2_48==1, rx_1_48==wx_2_48+-1, ry_1_48==wy_2_48+-1), 
And(rprim_1_48==1, rechassigned_2_48==1, rx_1_48==wx_2_48+0, ry_1_48==wy_2_48+-1), 
And(rprim_1_48==1, rechassigned_2_48==1, rx_1_48==wx_2_48+1, ry_1_48==wy_2_48+-1), 
))))
# wprim = 2
s.add(Implies(wprim_3_1==2, 
And(wtraj_3_2==wtraj_3_1, ch_3_1<20, ch_3_2==ch_3_1+rech_amt_3_1, 
Or(
And(rprim_1_1==1, rechassigned_3_1==1, rx_1_1==wx_3_1+1, ry_1_1==wy_3_1+0), 
And(rprim_1_1==1, rechassigned_3_1==1, rx_1_1==wx_3_1+1, ry_1_1==wy_3_1+1), 
And(rprim_1_1==1, rechassigned_3_1==1, rx_1_1==wx_3_1+0, ry_1_1==wy_3_1+1), 
And(rprim_1_1==1, rechassigned_3_1==1, rx_1_1==wx_3_1+-1, ry_1_1==wy_3_1+1), 
And(rprim_1_1==1, rechassigned_3_1==1, rx_1_1==wx_3_1+-1, ry_1_1==wy_3_1+0), 
And(rprim_1_1==1, rechassigned_3_1==1, rx_1_1==wx_3_1+-1, ry_1_1==wy_3_1+-1), 
And(rprim_1_1==1, rechassigned_3_1==1, rx_1_1==wx_3_1+0, ry_1_1==wy_3_1+-1), 
And(rprim_1_1==1, rechassigned_3_1==1, rx_1_1==wx_3_1+1, ry_1_1==wy_3_1+-1), 
))))
# wprim = 2
s.add(Implies(wprim_3_2==2, 
And(wtraj_3_3==wtraj_3_2, ch_3_2<20, ch_3_3==ch_3_2+rech_amt_3_2, 
Or(
And(rprim_1_2==1, rechassigned_3_2==1, rx_1_2==wx_3_2+1, ry_1_2==wy_3_2+0), 
And(rprim_1_2==1, rechassigned_3_2==1, rx_1_2==wx_3_2+1, ry_1_2==wy_3_2+1), 
And(rprim_1_2==1, rechassigned_3_2==1, rx_1_2==wx_3_2+0, ry_1_2==wy_3_2+1), 
And(rprim_1_2==1, rechassigned_3_2==1, rx_1_2==wx_3_2+-1, ry_1_2==wy_3_2+1), 
And(rprim_1_2==1, rechassigned_3_2==1, rx_1_2==wx_3_2+-1, ry_1_2==wy_3_2+0), 
And(rprim_1_2==1, rechassigned_3_2==1, rx_1_2==wx_3_2+-1, ry_1_2==wy_3_2+-1), 
And(rprim_1_2==1, rechassigned_3_2==1, rx_1_2==wx_3_2+0, ry_1_2==wy_3_2+-1), 
And(rprim_1_2==1, rechassigned_3_2==1, rx_1_2==wx_3_2+1, ry_1_2==wy_3_2+-1), 
))))
# wprim = 2
s.add(Implies(wprim_3_3==2, 
And(wtraj_3_4==wtraj_3_3, ch_3_3<20, ch_3_4==ch_3_3+rech_amt_3_3, 
Or(
And(rprim_1_3==1, rechassigned_3_3==1, rx_1_3==wx_3_3+1, ry_1_3==wy_3_3+0), 
And(rprim_1_3==1, rechassigned_3_3==1, rx_1_3==wx_3_3+1, ry_1_3==wy_3_3+1), 
And(rprim_1_3==1, rechassigned_3_3==1, rx_1_3==wx_3_3+0, ry_1_3==wy_3_3+1), 
And(rprim_1_3==1, rechassigned_3_3==1, rx_1_3==wx_3_3+-1, ry_1_3==wy_3_3+1), 
And(rprim_1_3==1, rechassigned_3_3==1, rx_1_3==wx_3_3+-1, ry_1_3==wy_3_3+0), 
And(rprim_1_3==1, rechassigned_3_3==1, rx_1_3==wx_3_3+-1, ry_1_3==wy_3_3+-1), 
And(rprim_1_3==1, rechassigned_3_3==1, rx_1_3==wx_3_3+0, ry_1_3==wy_3_3+-1), 
And(rprim_1_3==1, rechassigned_3_3==1, rx_1_3==wx_3_3+1, ry_1_3==wy_3_3+-1), 
))))
# wprim = 2
s.add(Implies(wprim_3_4==2, 
And(wtraj_3_5==wtraj_3_4, ch_3_4<20, ch_3_5==ch_3_4+rech_amt_3_4, 
Or(
And(rprim_1_4==1, rechassigned_3_4==1, rx_1_4==wx_3_4+1, ry_1_4==wy_3_4+0), 
And(rprim_1_4==1, rechassigned_3_4==1, rx_1_4==wx_3_4+1, ry_1_4==wy_3_4+1), 
And(rprim_1_4==1, rechassigned_3_4==1, rx_1_4==wx_3_4+0, ry_1_4==wy_3_4+1), 
And(rprim_1_4==1, rechassigned_3_4==1, rx_1_4==wx_3_4+-1, ry_1_4==wy_3_4+1), 
And(rprim_1_4==1, rechassigned_3_4==1, rx_1_4==wx_3_4+-1, ry_1_4==wy_3_4+0), 
And(rprim_1_4==1, rechassigned_3_4==1, rx_1_4==wx_3_4+-1, ry_1_4==wy_3_4+-1), 
And(rprim_1_4==1, rechassigned_3_4==1, rx_1_4==wx_3_4+0, ry_1_4==wy_3_4+-1), 
And(rprim_1_4==1, rechassigned_3_4==1, rx_1_4==wx_3_4+1, ry_1_4==wy_3_4+-1), 
))))
# wprim = 2
s.add(Implies(wprim_3_5==2, 
And(wtraj_3_6==wtraj_3_5, ch_3_5<20, ch_3_6==ch_3_5+rech_amt_3_5, 
Or(
And(rprim_1_5==1, rechassigned_3_5==1, rx_1_5==wx_3_5+1, ry_1_5==wy_3_5+0), 
And(rprim_1_5==1, rechassigned_3_5==1, rx_1_5==wx_3_5+1, ry_1_5==wy_3_5+1), 
And(rprim_1_5==1, rechassigned_3_5==1, rx_1_5==wx_3_5+0, ry_1_5==wy_3_5+1), 
And(rprim_1_5==1, rechassigned_3_5==1, rx_1_5==wx_3_5+-1, ry_1_5==wy_3_5+1), 
And(rprim_1_5==1, rechassigned_3_5==1, rx_1_5==wx_3_5+-1, ry_1_5==wy_3_5+0), 
And(rprim_1_5==1, rechassigned_3_5==1, rx_1_5==wx_3_5+-1, ry_1_5==wy_3_5+-1), 
And(rprim_1_5==1, rechassigned_3_5==1, rx_1_5==wx_3_5+0, ry_1_5==wy_3_5+-1), 
And(rprim_1_5==1, rechassigned_3_5==1, rx_1_5==wx_3_5+1, ry_1_5==wy_3_5+-1), 
))))
# wprim = 2
s.add(Implies(wprim_3_6==2, 
And(wtraj_3_7==wtraj_3_6, ch_3_6<20, ch_3_7==ch_3_6+rech_amt_3_6, 
Or(
And(rprim_1_6==1, rechassigned_3_6==1, rx_1_6==wx_3_6+1, ry_1_6==wy_3_6+0), 
And(rprim_1_6==1, rechassigned_3_6==1, rx_1_6==wx_3_6+1, ry_1_6==wy_3_6+1), 
And(rprim_1_6==1, rechassigned_3_6==1, rx_1_6==wx_3_6+0, ry_1_6==wy_3_6+1), 
And(rprim_1_6==1, rechassigned_3_6==1, rx_1_6==wx_3_6+-1, ry_1_6==wy_3_6+1), 
And(rprim_1_6==1, rechassigned_3_6==1, rx_1_6==wx_3_6+-1, ry_1_6==wy_3_6+0), 
And(rprim_1_6==1, rechassigned_3_6==1, rx_1_6==wx_3_6+-1, ry_1_6==wy_3_6+-1), 
And(rprim_1_6==1, rechassigned_3_6==1, rx_1_6==wx_3_6+0, ry_1_6==wy_3_6+-1), 
And(rprim_1_6==1, rechassigned_3_6==1, rx_1_6==wx_3_6+1, ry_1_6==wy_3_6+-1), 
))))
# wprim = 2
s.add(Implies(wprim_3_7==2, 
And(wtraj_3_8==wtraj_3_7, ch_3_7<20, ch_3_8==ch_3_7+rech_amt_3_7, 
Or(
And(rprim_1_7==1, rechassigned_3_7==1, rx_1_7==wx_3_7+1, ry_1_7==wy_3_7+0), 
And(rprim_1_7==1, rechassigned_3_7==1, rx_1_7==wx_3_7+1, ry_1_7==wy_3_7+1), 
And(rprim_1_7==1, rechassigned_3_7==1, rx_1_7==wx_3_7+0, ry_1_7==wy_3_7+1), 
And(rprim_1_7==1, rechassigned_3_7==1, rx_1_7==wx_3_7+-1, ry_1_7==wy_3_7+1), 
And(rprim_1_7==1, rechassigned_3_7==1, rx_1_7==wx_3_7+-1, ry_1_7==wy_3_7+0), 
And(rprim_1_7==1, rechassigned_3_7==1, rx_1_7==wx_3_7+-1, ry_1_7==wy_3_7+-1), 
And(rprim_1_7==1, rechassigned_3_7==1, rx_1_7==wx_3_7+0, ry_1_7==wy_3_7+-1), 
And(rprim_1_7==1, rechassigned_3_7==1, rx_1_7==wx_3_7+1, ry_1_7==wy_3_7+-1), 
))))
# wprim = 2
s.add(Implies(wprim_3_8==2, 
And(wtraj_3_9==wtraj_3_8, ch_3_8<20, ch_3_9==ch_3_8+rech_amt_3_8, 
Or(
And(rprim_1_8==1, rechassigned_3_8==1, rx_1_8==wx_3_8+1, ry_1_8==wy_3_8+0), 
And(rprim_1_8==1, rechassigned_3_8==1, rx_1_8==wx_3_8+1, ry_1_8==wy_3_8+1), 
And(rprim_1_8==1, rechassigned_3_8==1, rx_1_8==wx_3_8+0, ry_1_8==wy_3_8+1), 
And(rprim_1_8==1, rechassigned_3_8==1, rx_1_8==wx_3_8+-1, ry_1_8==wy_3_8+1), 
And(rprim_1_8==1, rechassigned_3_8==1, rx_1_8==wx_3_8+-1, ry_1_8==wy_3_8+0), 
And(rprim_1_8==1, rechassigned_3_8==1, rx_1_8==wx_3_8+-1, ry_1_8==wy_3_8+-1), 
And(rprim_1_8==1, rechassigned_3_8==1, rx_1_8==wx_3_8+0, ry_1_8==wy_3_8+-1), 
And(rprim_1_8==1, rechassigned_3_8==1, rx_1_8==wx_3_8+1, ry_1_8==wy_3_8+-1), 
))))
# wprim = 2
s.add(Implies(wprim_3_9==2, 
And(wtraj_3_10==wtraj_3_9, ch_3_9<20, ch_3_10==ch_3_9+rech_amt_3_9, 
Or(
And(rprim_1_9==1, rechassigned_3_9==1, rx_1_9==wx_3_9+1, ry_1_9==wy_3_9+0), 
And(rprim_1_9==1, rechassigned_3_9==1, rx_1_9==wx_3_9+1, ry_1_9==wy_3_9+1), 
And(rprim_1_9==1, rechassigned_3_9==1, rx_1_9==wx_3_9+0, ry_1_9==wy_3_9+1), 
And(rprim_1_9==1, rechassigned_3_9==1, rx_1_9==wx_3_9+-1, ry_1_9==wy_3_9+1), 
And(rprim_1_9==1, rechassigned_3_9==1, rx_1_9==wx_3_9+-1, ry_1_9==wy_3_9+0), 
And(rprim_1_9==1, rechassigned_3_9==1, rx_1_9==wx_3_9+-1, ry_1_9==wy_3_9+-1), 
And(rprim_1_9==1, rechassigned_3_9==1, rx_1_9==wx_3_9+0, ry_1_9==wy_3_9+-1), 
And(rprim_1_9==1, rechassigned_3_9==1, rx_1_9==wx_3_9+1, ry_1_9==wy_3_9+-1), 
))))
# wprim = 2
s.add(Implies(wprim_3_10==2, 
And(wtraj_3_11==wtraj_3_10, ch_3_10<20, ch_3_11==ch_3_10+rech_amt_3_10, 
Or(
And(rprim_1_10==1, rechassigned_3_10==1, rx_1_10==wx_3_10+1, ry_1_10==wy_3_10+0), 
And(rprim_1_10==1, rechassigned_3_10==1, rx_1_10==wx_3_10+1, ry_1_10==wy_3_10+1), 
And(rprim_1_10==1, rechassigned_3_10==1, rx_1_10==wx_3_10+0, ry_1_10==wy_3_10+1), 
And(rprim_1_10==1, rechassigned_3_10==1, rx_1_10==wx_3_10+-1, ry_1_10==wy_3_10+1), 
And(rprim_1_10==1, rechassigned_3_10==1, rx_1_10==wx_3_10+-1, ry_1_10==wy_3_10+0), 
And(rprim_1_10==1, rechassigned_3_10==1, rx_1_10==wx_3_10+-1, ry_1_10==wy_3_10+-1), 
And(rprim_1_10==1, rechassigned_3_10==1, rx_1_10==wx_3_10+0, ry_1_10==wy_3_10+-1), 
And(rprim_1_10==1, rechassigned_3_10==1, rx_1_10==wx_3_10+1, ry_1_10==wy_3_10+-1), 
))))
# wprim = 2
s.add(Implies(wprim_3_11==2, 
And(wtraj_3_12==wtraj_3_11, ch_3_11<20, ch_3_12==ch_3_11+rech_amt_3_11, 
Or(
And(rprim_1_11==1, rechassigned_3_11==1, rx_1_11==wx_3_11+1, ry_1_11==wy_3_11+0), 
And(rprim_1_11==1, rechassigned_3_11==1, rx_1_11==wx_3_11+1, ry_1_11==wy_3_11+1), 
And(rprim_1_11==1, rechassigned_3_11==1, rx_1_11==wx_3_11+0, ry_1_11==wy_3_11+1), 
And(rprim_1_11==1, rechassigned_3_11==1, rx_1_11==wx_3_11+-1, ry_1_11==wy_3_11+1), 
And(rprim_1_11==1, rechassigned_3_11==1, rx_1_11==wx_3_11+-1, ry_1_11==wy_3_11+0), 
And(rprim_1_11==1, rechassigned_3_11==1, rx_1_11==wx_3_11+-1, ry_1_11==wy_3_11+-1), 
And(rprim_1_11==1, rechassigned_3_11==1, rx_1_11==wx_3_11+0, ry_1_11==wy_3_11+-1), 
And(rprim_1_11==1, rechassigned_3_11==1, rx_1_11==wx_3_11+1, ry_1_11==wy_3_11+-1), 
))))
# wprim = 2
s.add(Implies(wprim_3_12==2, 
And(wtraj_3_13==wtraj_3_12, ch_3_12<20, ch_3_13==ch_3_12+rech_amt_3_12, 
Or(
And(rprim_1_12==1, rechassigned_3_12==1, rx_1_12==wx_3_12+1, ry_1_12==wy_3_12+0), 
And(rprim_1_12==1, rechassigned_3_12==1, rx_1_12==wx_3_12+1, ry_1_12==wy_3_12+1), 
And(rprim_1_12==1, rechassigned_3_12==1, rx_1_12==wx_3_12+0, ry_1_12==wy_3_12+1), 
And(rprim_1_12==1, rechassigned_3_12==1, rx_1_12==wx_3_12+-1, ry_1_12==wy_3_12+1), 
And(rprim_1_12==1, rechassigned_3_12==1, rx_1_12==wx_3_12+-1, ry_1_12==wy_3_12+0), 
And(rprim_1_12==1, rechassigned_3_12==1, rx_1_12==wx_3_12+-1, ry_1_12==wy_3_12+-1), 
And(rprim_1_12==1, rechassigned_3_12==1, rx_1_12==wx_3_12+0, ry_1_12==wy_3_12+-1), 
And(rprim_1_12==1, rechassigned_3_12==1, rx_1_12==wx_3_12+1, ry_1_12==wy_3_12+-1), 
))))
# wprim = 2
s.add(Implies(wprim_3_13==2, 
And(wtraj_3_14==wtraj_3_13, ch_3_13<20, ch_3_14==ch_3_13+rech_amt_3_13, 
Or(
And(rprim_1_13==1, rechassigned_3_13==1, rx_1_13==wx_3_13+1, ry_1_13==wy_3_13+0), 
And(rprim_1_13==1, rechassigned_3_13==1, rx_1_13==wx_3_13+1, ry_1_13==wy_3_13+1), 
And(rprim_1_13==1, rechassigned_3_13==1, rx_1_13==wx_3_13+0, ry_1_13==wy_3_13+1), 
And(rprim_1_13==1, rechassigned_3_13==1, rx_1_13==wx_3_13+-1, ry_1_13==wy_3_13+1), 
And(rprim_1_13==1, rechassigned_3_13==1, rx_1_13==wx_3_13+-1, ry_1_13==wy_3_13+0), 
And(rprim_1_13==1, rechassigned_3_13==1, rx_1_13==wx_3_13+-1, ry_1_13==wy_3_13+-1), 
And(rprim_1_13==1, rechassigned_3_13==1, rx_1_13==wx_3_13+0, ry_1_13==wy_3_13+-1), 
And(rprim_1_13==1, rechassigned_3_13==1, rx_1_13==wx_3_13+1, ry_1_13==wy_3_13+-1), 
))))
# wprim = 2
s.add(Implies(wprim_3_14==2, 
And(wtraj_3_15==wtraj_3_14, ch_3_14<20, ch_3_15==ch_3_14+rech_amt_3_14, 
Or(
And(rprim_1_14==1, rechassigned_3_14==1, rx_1_14==wx_3_14+1, ry_1_14==wy_3_14+0), 
And(rprim_1_14==1, rechassigned_3_14==1, rx_1_14==wx_3_14+1, ry_1_14==wy_3_14+1), 
And(rprim_1_14==1, rechassigned_3_14==1, rx_1_14==wx_3_14+0, ry_1_14==wy_3_14+1), 
And(rprim_1_14==1, rechassigned_3_14==1, rx_1_14==wx_3_14+-1, ry_1_14==wy_3_14+1), 
And(rprim_1_14==1, rechassigned_3_14==1, rx_1_14==wx_3_14+-1, ry_1_14==wy_3_14+0), 
And(rprim_1_14==1, rechassigned_3_14==1, rx_1_14==wx_3_14+-1, ry_1_14==wy_3_14+-1), 
And(rprim_1_14==1, rechassigned_3_14==1, rx_1_14==wx_3_14+0, ry_1_14==wy_3_14+-1), 
And(rprim_1_14==1, rechassigned_3_14==1, rx_1_14==wx_3_14+1, ry_1_14==wy_3_14+-1), 
))))
# wprim = 2
s.add(Implies(wprim_3_15==2, 
And(wtraj_3_16==wtraj_3_15, ch_3_15<20, ch_3_16==ch_3_15+rech_amt_3_15, 
Or(
And(rprim_1_15==1, rechassigned_3_15==1, rx_1_15==wx_3_15+1, ry_1_15==wy_3_15+0), 
And(rprim_1_15==1, rechassigned_3_15==1, rx_1_15==wx_3_15+1, ry_1_15==wy_3_15+1), 
And(rprim_1_15==1, rechassigned_3_15==1, rx_1_15==wx_3_15+0, ry_1_15==wy_3_15+1), 
And(rprim_1_15==1, rechassigned_3_15==1, rx_1_15==wx_3_15+-1, ry_1_15==wy_3_15+1), 
And(rprim_1_15==1, rechassigned_3_15==1, rx_1_15==wx_3_15+-1, ry_1_15==wy_3_15+0), 
And(rprim_1_15==1, rechassigned_3_15==1, rx_1_15==wx_3_15+-1, ry_1_15==wy_3_15+-1), 
And(rprim_1_15==1, rechassigned_3_15==1, rx_1_15==wx_3_15+0, ry_1_15==wy_3_15+-1), 
And(rprim_1_15==1, rechassigned_3_15==1, rx_1_15==wx_3_15+1, ry_1_15==wy_3_15+-1), 
))))
# wprim = 2
s.add(Implies(wprim_3_16==2, 
And(wtraj_3_17==wtraj_3_16, ch_3_16<20, ch_3_17==ch_3_16+rech_amt_3_16, 
Or(
And(rprim_1_16==1, rechassigned_3_16==1, rx_1_16==wx_3_16+1, ry_1_16==wy_3_16+0), 
And(rprim_1_16==1, rechassigned_3_16==1, rx_1_16==wx_3_16+1, ry_1_16==wy_3_16+1), 
And(rprim_1_16==1, rechassigned_3_16==1, rx_1_16==wx_3_16+0, ry_1_16==wy_3_16+1), 
And(rprim_1_16==1, rechassigned_3_16==1, rx_1_16==wx_3_16+-1, ry_1_16==wy_3_16+1), 
And(rprim_1_16==1, rechassigned_3_16==1, rx_1_16==wx_3_16+-1, ry_1_16==wy_3_16+0), 
And(rprim_1_16==1, rechassigned_3_16==1, rx_1_16==wx_3_16+-1, ry_1_16==wy_3_16+-1), 
And(rprim_1_16==1, rechassigned_3_16==1, rx_1_16==wx_3_16+0, ry_1_16==wy_3_16+-1), 
And(rprim_1_16==1, rechassigned_3_16==1, rx_1_16==wx_3_16+1, ry_1_16==wy_3_16+-1), 
))))
# wprim = 2
s.add(Implies(wprim_3_17==2, 
And(wtraj_3_18==wtraj_3_17, ch_3_17<20, ch_3_18==ch_3_17+rech_amt_3_17, 
Or(
And(rprim_1_17==1, rechassigned_3_17==1, rx_1_17==wx_3_17+1, ry_1_17==wy_3_17+0), 
And(rprim_1_17==1, rechassigned_3_17==1, rx_1_17==wx_3_17+1, ry_1_17==wy_3_17+1), 
And(rprim_1_17==1, rechassigned_3_17==1, rx_1_17==wx_3_17+0, ry_1_17==wy_3_17+1), 
And(rprim_1_17==1, rechassigned_3_17==1, rx_1_17==wx_3_17+-1, ry_1_17==wy_3_17+1), 
And(rprim_1_17==1, rechassigned_3_17==1, rx_1_17==wx_3_17+-1, ry_1_17==wy_3_17+0), 
And(rprim_1_17==1, rechassigned_3_17==1, rx_1_17==wx_3_17+-1, ry_1_17==wy_3_17+-1), 
And(rprim_1_17==1, rechassigned_3_17==1, rx_1_17==wx_3_17+0, ry_1_17==wy_3_17+-1), 
And(rprim_1_17==1, rechassigned_3_17==1, rx_1_17==wx_3_17+1, ry_1_17==wy_3_17+-1), 
))))
# wprim = 2
s.add(Implies(wprim_3_18==2, 
And(wtraj_3_19==wtraj_3_18, ch_3_18<20, ch_3_19==ch_3_18+rech_amt_3_18, 
Or(
And(rprim_1_18==1, rechassigned_3_18==1, rx_1_18==wx_3_18+1, ry_1_18==wy_3_18+0), 
And(rprim_1_18==1, rechassigned_3_18==1, rx_1_18==wx_3_18+1, ry_1_18==wy_3_18+1), 
And(rprim_1_18==1, rechassigned_3_18==1, rx_1_18==wx_3_18+0, ry_1_18==wy_3_18+1), 
And(rprim_1_18==1, rechassigned_3_18==1, rx_1_18==wx_3_18+-1, ry_1_18==wy_3_18+1), 
And(rprim_1_18==1, rechassigned_3_18==1, rx_1_18==wx_3_18+-1, ry_1_18==wy_3_18+0), 
And(rprim_1_18==1, rechassigned_3_18==1, rx_1_18==wx_3_18+-1, ry_1_18==wy_3_18+-1), 
And(rprim_1_18==1, rechassigned_3_18==1, rx_1_18==wx_3_18+0, ry_1_18==wy_3_18+-1), 
And(rprim_1_18==1, rechassigned_3_18==1, rx_1_18==wx_3_18+1, ry_1_18==wy_3_18+-1), 
))))
# wprim = 2
s.add(Implies(wprim_3_19==2, 
And(wtraj_3_20==wtraj_3_19, ch_3_19<20, ch_3_20==ch_3_19+rech_amt_3_19, 
Or(
And(rprim_1_19==1, rechassigned_3_19==1, rx_1_19==wx_3_19+1, ry_1_19==wy_3_19+0), 
And(rprim_1_19==1, rechassigned_3_19==1, rx_1_19==wx_3_19+1, ry_1_19==wy_3_19+1), 
And(rprim_1_19==1, rechassigned_3_19==1, rx_1_19==wx_3_19+0, ry_1_19==wy_3_19+1), 
And(rprim_1_19==1, rechassigned_3_19==1, rx_1_19==wx_3_19+-1, ry_1_19==wy_3_19+1), 
And(rprim_1_19==1, rechassigned_3_19==1, rx_1_19==wx_3_19+-1, ry_1_19==wy_3_19+0), 
And(rprim_1_19==1, rechassigned_3_19==1, rx_1_19==wx_3_19+-1, ry_1_19==wy_3_19+-1), 
And(rprim_1_19==1, rechassigned_3_19==1, rx_1_19==wx_3_19+0, ry_1_19==wy_3_19+-1), 
And(rprim_1_19==1, rechassigned_3_19==1, rx_1_19==wx_3_19+1, ry_1_19==wy_3_19+-1), 
))))
# wprim = 2
s.add(Implies(wprim_3_20==2, 
And(wtraj_3_21==wtraj_3_20, ch_3_20<20, ch_3_21==ch_3_20+rech_amt_3_20, 
Or(
And(rprim_1_20==1, rechassigned_3_20==1, rx_1_20==wx_3_20+1, ry_1_20==wy_3_20+0), 
And(rprim_1_20==1, rechassigned_3_20==1, rx_1_20==wx_3_20+1, ry_1_20==wy_3_20+1), 
And(rprim_1_20==1, rechassigned_3_20==1, rx_1_20==wx_3_20+0, ry_1_20==wy_3_20+1), 
And(rprim_1_20==1, rechassigned_3_20==1, rx_1_20==wx_3_20+-1, ry_1_20==wy_3_20+1), 
And(rprim_1_20==1, rechassigned_3_20==1, rx_1_20==wx_3_20+-1, ry_1_20==wy_3_20+0), 
And(rprim_1_20==1, rechassigned_3_20==1, rx_1_20==wx_3_20+-1, ry_1_20==wy_3_20+-1), 
And(rprim_1_20==1, rechassigned_3_20==1, rx_1_20==wx_3_20+0, ry_1_20==wy_3_20+-1), 
And(rprim_1_20==1, rechassigned_3_20==1, rx_1_20==wx_3_20+1, ry_1_20==wy_3_20+-1), 
))))
# wprim = 2
s.add(Implies(wprim_3_21==2, 
And(wtraj_3_22==wtraj_3_21, ch_3_21<20, ch_3_22==ch_3_21+rech_amt_3_21, 
Or(
And(rprim_1_21==1, rechassigned_3_21==1, rx_1_21==wx_3_21+1, ry_1_21==wy_3_21+0), 
And(rprim_1_21==1, rechassigned_3_21==1, rx_1_21==wx_3_21+1, ry_1_21==wy_3_21+1), 
And(rprim_1_21==1, rechassigned_3_21==1, rx_1_21==wx_3_21+0, ry_1_21==wy_3_21+1), 
And(rprim_1_21==1, rechassigned_3_21==1, rx_1_21==wx_3_21+-1, ry_1_21==wy_3_21+1), 
And(rprim_1_21==1, rechassigned_3_21==1, rx_1_21==wx_3_21+-1, ry_1_21==wy_3_21+0), 
And(rprim_1_21==1, rechassigned_3_21==1, rx_1_21==wx_3_21+-1, ry_1_21==wy_3_21+-1), 
And(rprim_1_21==1, rechassigned_3_21==1, rx_1_21==wx_3_21+0, ry_1_21==wy_3_21+-1), 
And(rprim_1_21==1, rechassigned_3_21==1, rx_1_21==wx_3_21+1, ry_1_21==wy_3_21+-1), 
))))
# wprim = 2
s.add(Implies(wprim_3_22==2, 
And(wtraj_3_23==wtraj_3_22, ch_3_22<20, ch_3_23==ch_3_22+rech_amt_3_22, 
Or(
And(rprim_1_22==1, rechassigned_3_22==1, rx_1_22==wx_3_22+1, ry_1_22==wy_3_22+0), 
And(rprim_1_22==1, rechassigned_3_22==1, rx_1_22==wx_3_22+1, ry_1_22==wy_3_22+1), 
And(rprim_1_22==1, rechassigned_3_22==1, rx_1_22==wx_3_22+0, ry_1_22==wy_3_22+1), 
And(rprim_1_22==1, rechassigned_3_22==1, rx_1_22==wx_3_22+-1, ry_1_22==wy_3_22+1), 
And(rprim_1_22==1, rechassigned_3_22==1, rx_1_22==wx_3_22+-1, ry_1_22==wy_3_22+0), 
And(rprim_1_22==1, rechassigned_3_22==1, rx_1_22==wx_3_22+-1, ry_1_22==wy_3_22+-1), 
And(rprim_1_22==1, rechassigned_3_22==1, rx_1_22==wx_3_22+0, ry_1_22==wy_3_22+-1), 
And(rprim_1_22==1, rechassigned_3_22==1, rx_1_22==wx_3_22+1, ry_1_22==wy_3_22+-1), 
))))
# wprim = 2
s.add(Implies(wprim_3_23==2, 
And(wtraj_3_24==wtraj_3_23, ch_3_23<20, ch_3_24==ch_3_23+rech_amt_3_23, 
Or(
And(rprim_1_23==1, rechassigned_3_23==1, rx_1_23==wx_3_23+1, ry_1_23==wy_3_23+0), 
And(rprim_1_23==1, rechassigned_3_23==1, rx_1_23==wx_3_23+1, ry_1_23==wy_3_23+1), 
And(rprim_1_23==1, rechassigned_3_23==1, rx_1_23==wx_3_23+0, ry_1_23==wy_3_23+1), 
And(rprim_1_23==1, rechassigned_3_23==1, rx_1_23==wx_3_23+-1, ry_1_23==wy_3_23+1), 
And(rprim_1_23==1, rechassigned_3_23==1, rx_1_23==wx_3_23+-1, ry_1_23==wy_3_23+0), 
And(rprim_1_23==1, rechassigned_3_23==1, rx_1_23==wx_3_23+-1, ry_1_23==wy_3_23+-1), 
And(rprim_1_23==1, rechassigned_3_23==1, rx_1_23==wx_3_23+0, ry_1_23==wy_3_23+-1), 
And(rprim_1_23==1, rechassigned_3_23==1, rx_1_23==wx_3_23+1, ry_1_23==wy_3_23+-1), 
))))
# wprim = 2
s.add(Implies(wprim_3_24==2, 
And(wtraj_3_25==wtraj_3_24, ch_3_24<20, ch_3_25==ch_3_24+rech_amt_3_24, 
Or(
And(rprim_1_24==1, rechassigned_3_24==1, rx_1_24==wx_3_24+1, ry_1_24==wy_3_24+0), 
And(rprim_1_24==1, rechassigned_3_24==1, rx_1_24==wx_3_24+1, ry_1_24==wy_3_24+1), 
And(rprim_1_24==1, rechassigned_3_24==1, rx_1_24==wx_3_24+0, ry_1_24==wy_3_24+1), 
And(rprim_1_24==1, rechassigned_3_24==1, rx_1_24==wx_3_24+-1, ry_1_24==wy_3_24+1), 
And(rprim_1_24==1, rechassigned_3_24==1, rx_1_24==wx_3_24+-1, ry_1_24==wy_3_24+0), 
And(rprim_1_24==1, rechassigned_3_24==1, rx_1_24==wx_3_24+-1, ry_1_24==wy_3_24+-1), 
And(rprim_1_24==1, rechassigned_3_24==1, rx_1_24==wx_3_24+0, ry_1_24==wy_3_24+-1), 
And(rprim_1_24==1, rechassigned_3_24==1, rx_1_24==wx_3_24+1, ry_1_24==wy_3_24+-1), 
))))
# wprim = 2
s.add(Implies(wprim_3_25==2, 
And(wtraj_3_26==wtraj_3_25, ch_3_25<20, ch_3_26==ch_3_25+rech_amt_3_25, 
Or(
And(rprim_1_25==1, rechassigned_3_25==1, rx_1_25==wx_3_25+1, ry_1_25==wy_3_25+0), 
And(rprim_1_25==1, rechassigned_3_25==1, rx_1_25==wx_3_25+1, ry_1_25==wy_3_25+1), 
And(rprim_1_25==1, rechassigned_3_25==1, rx_1_25==wx_3_25+0, ry_1_25==wy_3_25+1), 
And(rprim_1_25==1, rechassigned_3_25==1, rx_1_25==wx_3_25+-1, ry_1_25==wy_3_25+1), 
And(rprim_1_25==1, rechassigned_3_25==1, rx_1_25==wx_3_25+-1, ry_1_25==wy_3_25+0), 
And(rprim_1_25==1, rechassigned_3_25==1, rx_1_25==wx_3_25+-1, ry_1_25==wy_3_25+-1), 
And(rprim_1_25==1, rechassigned_3_25==1, rx_1_25==wx_3_25+0, ry_1_25==wy_3_25+-1), 
And(rprim_1_25==1, rechassigned_3_25==1, rx_1_25==wx_3_25+1, ry_1_25==wy_3_25+-1), 
))))
# wprim = 2
s.add(Implies(wprim_3_26==2, 
And(wtraj_3_27==wtraj_3_26, ch_3_26<20, ch_3_27==ch_3_26+rech_amt_3_26, 
Or(
And(rprim_1_26==1, rechassigned_3_26==1, rx_1_26==wx_3_26+1, ry_1_26==wy_3_26+0), 
And(rprim_1_26==1, rechassigned_3_26==1, rx_1_26==wx_3_26+1, ry_1_26==wy_3_26+1), 
And(rprim_1_26==1, rechassigned_3_26==1, rx_1_26==wx_3_26+0, ry_1_26==wy_3_26+1), 
And(rprim_1_26==1, rechassigned_3_26==1, rx_1_26==wx_3_26+-1, ry_1_26==wy_3_26+1), 
And(rprim_1_26==1, rechassigned_3_26==1, rx_1_26==wx_3_26+-1, ry_1_26==wy_3_26+0), 
And(rprim_1_26==1, rechassigned_3_26==1, rx_1_26==wx_3_26+-1, ry_1_26==wy_3_26+-1), 
And(rprim_1_26==1, rechassigned_3_26==1, rx_1_26==wx_3_26+0, ry_1_26==wy_3_26+-1), 
And(rprim_1_26==1, rechassigned_3_26==1, rx_1_26==wx_3_26+1, ry_1_26==wy_3_26+-1), 
))))
# wprim = 2
s.add(Implies(wprim_3_27==2, 
And(wtraj_3_28==wtraj_3_27, ch_3_27<20, ch_3_28==ch_3_27+rech_amt_3_27, 
Or(
And(rprim_1_27==1, rechassigned_3_27==1, rx_1_27==wx_3_27+1, ry_1_27==wy_3_27+0), 
And(rprim_1_27==1, rechassigned_3_27==1, rx_1_27==wx_3_27+1, ry_1_27==wy_3_27+1), 
And(rprim_1_27==1, rechassigned_3_27==1, rx_1_27==wx_3_27+0, ry_1_27==wy_3_27+1), 
And(rprim_1_27==1, rechassigned_3_27==1, rx_1_27==wx_3_27+-1, ry_1_27==wy_3_27+1), 
And(rprim_1_27==1, rechassigned_3_27==1, rx_1_27==wx_3_27+-1, ry_1_27==wy_3_27+0), 
And(rprim_1_27==1, rechassigned_3_27==1, rx_1_27==wx_3_27+-1, ry_1_27==wy_3_27+-1), 
And(rprim_1_27==1, rechassigned_3_27==1, rx_1_27==wx_3_27+0, ry_1_27==wy_3_27+-1), 
And(rprim_1_27==1, rechassigned_3_27==1, rx_1_27==wx_3_27+1, ry_1_27==wy_3_27+-1), 
))))
# wprim = 2
s.add(Implies(wprim_3_28==2, 
And(wtraj_3_29==wtraj_3_28, ch_3_28<20, ch_3_29==ch_3_28+rech_amt_3_28, 
Or(
And(rprim_1_28==1, rechassigned_3_28==1, rx_1_28==wx_3_28+1, ry_1_28==wy_3_28+0), 
And(rprim_1_28==1, rechassigned_3_28==1, rx_1_28==wx_3_28+1, ry_1_28==wy_3_28+1), 
And(rprim_1_28==1, rechassigned_3_28==1, rx_1_28==wx_3_28+0, ry_1_28==wy_3_28+1), 
And(rprim_1_28==1, rechassigned_3_28==1, rx_1_28==wx_3_28+-1, ry_1_28==wy_3_28+1), 
And(rprim_1_28==1, rechassigned_3_28==1, rx_1_28==wx_3_28+-1, ry_1_28==wy_3_28+0), 
And(rprim_1_28==1, rechassigned_3_28==1, rx_1_28==wx_3_28+-1, ry_1_28==wy_3_28+-1), 
And(rprim_1_28==1, rechassigned_3_28==1, rx_1_28==wx_3_28+0, ry_1_28==wy_3_28+-1), 
And(rprim_1_28==1, rechassigned_3_28==1, rx_1_28==wx_3_28+1, ry_1_28==wy_3_28+-1), 
))))
# wprim = 2
s.add(Implies(wprim_3_29==2, 
And(wtraj_3_30==wtraj_3_29, ch_3_29<20, ch_3_30==ch_3_29+rech_amt_3_29, 
Or(
And(rprim_1_29==1, rechassigned_3_29==1, rx_1_29==wx_3_29+1, ry_1_29==wy_3_29+0), 
And(rprim_1_29==1, rechassigned_3_29==1, rx_1_29==wx_3_29+1, ry_1_29==wy_3_29+1), 
And(rprim_1_29==1, rechassigned_3_29==1, rx_1_29==wx_3_29+0, ry_1_29==wy_3_29+1), 
And(rprim_1_29==1, rechassigned_3_29==1, rx_1_29==wx_3_29+-1, ry_1_29==wy_3_29+1), 
And(rprim_1_29==1, rechassigned_3_29==1, rx_1_29==wx_3_29+-1, ry_1_29==wy_3_29+0), 
And(rprim_1_29==1, rechassigned_3_29==1, rx_1_29==wx_3_29+-1, ry_1_29==wy_3_29+-1), 
And(rprim_1_29==1, rechassigned_3_29==1, rx_1_29==wx_3_29+0, ry_1_29==wy_3_29+-1), 
And(rprim_1_29==1, rechassigned_3_29==1, rx_1_29==wx_3_29+1, ry_1_29==wy_3_29+-1), 
))))
# wprim = 2
s.add(Implies(wprim_3_30==2, 
And(wtraj_3_31==wtraj_3_30, ch_3_30<20, ch_3_31==ch_3_30+rech_amt_3_30, 
Or(
And(rprim_1_30==1, rechassigned_3_30==1, rx_1_30==wx_3_30+1, ry_1_30==wy_3_30+0), 
And(rprim_1_30==1, rechassigned_3_30==1, rx_1_30==wx_3_30+1, ry_1_30==wy_3_30+1), 
And(rprim_1_30==1, rechassigned_3_30==1, rx_1_30==wx_3_30+0, ry_1_30==wy_3_30+1), 
And(rprim_1_30==1, rechassigned_3_30==1, rx_1_30==wx_3_30+-1, ry_1_30==wy_3_30+1), 
And(rprim_1_30==1, rechassigned_3_30==1, rx_1_30==wx_3_30+-1, ry_1_30==wy_3_30+0), 
And(rprim_1_30==1, rechassigned_3_30==1, rx_1_30==wx_3_30+-1, ry_1_30==wy_3_30+-1), 
And(rprim_1_30==1, rechassigned_3_30==1, rx_1_30==wx_3_30+0, ry_1_30==wy_3_30+-1), 
And(rprim_1_30==1, rechassigned_3_30==1, rx_1_30==wx_3_30+1, ry_1_30==wy_3_30+-1), 
))))
# wprim = 2
s.add(Implies(wprim_3_31==2, 
And(wtraj_3_32==wtraj_3_31, ch_3_31<20, ch_3_32==ch_3_31+rech_amt_3_31, 
Or(
And(rprim_1_31==1, rechassigned_3_31==1, rx_1_31==wx_3_31+1, ry_1_31==wy_3_31+0), 
And(rprim_1_31==1, rechassigned_3_31==1, rx_1_31==wx_3_31+1, ry_1_31==wy_3_31+1), 
And(rprim_1_31==1, rechassigned_3_31==1, rx_1_31==wx_3_31+0, ry_1_31==wy_3_31+1), 
And(rprim_1_31==1, rechassigned_3_31==1, rx_1_31==wx_3_31+-1, ry_1_31==wy_3_31+1), 
And(rprim_1_31==1, rechassigned_3_31==1, rx_1_31==wx_3_31+-1, ry_1_31==wy_3_31+0), 
And(rprim_1_31==1, rechassigned_3_31==1, rx_1_31==wx_3_31+-1, ry_1_31==wy_3_31+-1), 
And(rprim_1_31==1, rechassigned_3_31==1, rx_1_31==wx_3_31+0, ry_1_31==wy_3_31+-1), 
And(rprim_1_31==1, rechassigned_3_31==1, rx_1_31==wx_3_31+1, ry_1_31==wy_3_31+-1), 
))))
# wprim = 2
s.add(Implies(wprim_3_32==2, 
And(wtraj_3_33==wtraj_3_32, ch_3_32<20, ch_3_33==ch_3_32+rech_amt_3_32, 
Or(
And(rprim_1_32==1, rechassigned_3_32==1, rx_1_32==wx_3_32+1, ry_1_32==wy_3_32+0), 
And(rprim_1_32==1, rechassigned_3_32==1, rx_1_32==wx_3_32+1, ry_1_32==wy_3_32+1), 
And(rprim_1_32==1, rechassigned_3_32==1, rx_1_32==wx_3_32+0, ry_1_32==wy_3_32+1), 
And(rprim_1_32==1, rechassigned_3_32==1, rx_1_32==wx_3_32+-1, ry_1_32==wy_3_32+1), 
And(rprim_1_32==1, rechassigned_3_32==1, rx_1_32==wx_3_32+-1, ry_1_32==wy_3_32+0), 
And(rprim_1_32==1, rechassigned_3_32==1, rx_1_32==wx_3_32+-1, ry_1_32==wy_3_32+-1), 
And(rprim_1_32==1, rechassigned_3_32==1, rx_1_32==wx_3_32+0, ry_1_32==wy_3_32+-1), 
And(rprim_1_32==1, rechassigned_3_32==1, rx_1_32==wx_3_32+1, ry_1_32==wy_3_32+-1), 
))))
# wprim = 2
s.add(Implies(wprim_3_33==2, 
And(wtraj_3_34==wtraj_3_33, ch_3_33<20, ch_3_34==ch_3_33+rech_amt_3_33, 
Or(
And(rprim_1_33==1, rechassigned_3_33==1, rx_1_33==wx_3_33+1, ry_1_33==wy_3_33+0), 
And(rprim_1_33==1, rechassigned_3_33==1, rx_1_33==wx_3_33+1, ry_1_33==wy_3_33+1), 
And(rprim_1_33==1, rechassigned_3_33==1, rx_1_33==wx_3_33+0, ry_1_33==wy_3_33+1), 
And(rprim_1_33==1, rechassigned_3_33==1, rx_1_33==wx_3_33+-1, ry_1_33==wy_3_33+1), 
And(rprim_1_33==1, rechassigned_3_33==1, rx_1_33==wx_3_33+-1, ry_1_33==wy_3_33+0), 
And(rprim_1_33==1, rechassigned_3_33==1, rx_1_33==wx_3_33+-1, ry_1_33==wy_3_33+-1), 
And(rprim_1_33==1, rechassigned_3_33==1, rx_1_33==wx_3_33+0, ry_1_33==wy_3_33+-1), 
And(rprim_1_33==1, rechassigned_3_33==1, rx_1_33==wx_3_33+1, ry_1_33==wy_3_33+-1), 
))))
# wprim = 2
s.add(Implies(wprim_3_34==2, 
And(wtraj_3_35==wtraj_3_34, ch_3_34<20, ch_3_35==ch_3_34+rech_amt_3_34, 
Or(
And(rprim_1_34==1, rechassigned_3_34==1, rx_1_34==wx_3_34+1, ry_1_34==wy_3_34+0), 
And(rprim_1_34==1, rechassigned_3_34==1, rx_1_34==wx_3_34+1, ry_1_34==wy_3_34+1), 
And(rprim_1_34==1, rechassigned_3_34==1, rx_1_34==wx_3_34+0, ry_1_34==wy_3_34+1), 
And(rprim_1_34==1, rechassigned_3_34==1, rx_1_34==wx_3_34+-1, ry_1_34==wy_3_34+1), 
And(rprim_1_34==1, rechassigned_3_34==1, rx_1_34==wx_3_34+-1, ry_1_34==wy_3_34+0), 
And(rprim_1_34==1, rechassigned_3_34==1, rx_1_34==wx_3_34+-1, ry_1_34==wy_3_34+-1), 
And(rprim_1_34==1, rechassigned_3_34==1, rx_1_34==wx_3_34+0, ry_1_34==wy_3_34+-1), 
And(rprim_1_34==1, rechassigned_3_34==1, rx_1_34==wx_3_34+1, ry_1_34==wy_3_34+-1), 
))))
# wprim = 2
s.add(Implies(wprim_3_35==2, 
And(wtraj_3_36==wtraj_3_35, ch_3_35<20, ch_3_36==ch_3_35+rech_amt_3_35, 
Or(
And(rprim_1_35==1, rechassigned_3_35==1, rx_1_35==wx_3_35+1, ry_1_35==wy_3_35+0), 
And(rprim_1_35==1, rechassigned_3_35==1, rx_1_35==wx_3_35+1, ry_1_35==wy_3_35+1), 
And(rprim_1_35==1, rechassigned_3_35==1, rx_1_35==wx_3_35+0, ry_1_35==wy_3_35+1), 
And(rprim_1_35==1, rechassigned_3_35==1, rx_1_35==wx_3_35+-1, ry_1_35==wy_3_35+1), 
And(rprim_1_35==1, rechassigned_3_35==1, rx_1_35==wx_3_35+-1, ry_1_35==wy_3_35+0), 
And(rprim_1_35==1, rechassigned_3_35==1, rx_1_35==wx_3_35+-1, ry_1_35==wy_3_35+-1), 
And(rprim_1_35==1, rechassigned_3_35==1, rx_1_35==wx_3_35+0, ry_1_35==wy_3_35+-1), 
And(rprim_1_35==1, rechassigned_3_35==1, rx_1_35==wx_3_35+1, ry_1_35==wy_3_35+-1), 
))))
# wprim = 2
s.add(Implies(wprim_3_36==2, 
And(wtraj_3_37==wtraj_3_36, ch_3_36<20, ch_3_37==ch_3_36+rech_amt_3_36, 
Or(
And(rprim_1_36==1, rechassigned_3_36==1, rx_1_36==wx_3_36+1, ry_1_36==wy_3_36+0), 
And(rprim_1_36==1, rechassigned_3_36==1, rx_1_36==wx_3_36+1, ry_1_36==wy_3_36+1), 
And(rprim_1_36==1, rechassigned_3_36==1, rx_1_36==wx_3_36+0, ry_1_36==wy_3_36+1), 
And(rprim_1_36==1, rechassigned_3_36==1, rx_1_36==wx_3_36+-1, ry_1_36==wy_3_36+1), 
And(rprim_1_36==1, rechassigned_3_36==1, rx_1_36==wx_3_36+-1, ry_1_36==wy_3_36+0), 
And(rprim_1_36==1, rechassigned_3_36==1, rx_1_36==wx_3_36+-1, ry_1_36==wy_3_36+-1), 
And(rprim_1_36==1, rechassigned_3_36==1, rx_1_36==wx_3_36+0, ry_1_36==wy_3_36+-1), 
And(rprim_1_36==1, rechassigned_3_36==1, rx_1_36==wx_3_36+1, ry_1_36==wy_3_36+-1), 
))))
# wprim = 2
s.add(Implies(wprim_3_37==2, 
And(wtraj_3_38==wtraj_3_37, ch_3_37<20, ch_3_38==ch_3_37+rech_amt_3_37, 
Or(
And(rprim_1_37==1, rechassigned_3_37==1, rx_1_37==wx_3_37+1, ry_1_37==wy_3_37+0), 
And(rprim_1_37==1, rechassigned_3_37==1, rx_1_37==wx_3_37+1, ry_1_37==wy_3_37+1), 
And(rprim_1_37==1, rechassigned_3_37==1, rx_1_37==wx_3_37+0, ry_1_37==wy_3_37+1), 
And(rprim_1_37==1, rechassigned_3_37==1, rx_1_37==wx_3_37+-1, ry_1_37==wy_3_37+1), 
And(rprim_1_37==1, rechassigned_3_37==1, rx_1_37==wx_3_37+-1, ry_1_37==wy_3_37+0), 
And(rprim_1_37==1, rechassigned_3_37==1, rx_1_37==wx_3_37+-1, ry_1_37==wy_3_37+-1), 
And(rprim_1_37==1, rechassigned_3_37==1, rx_1_37==wx_3_37+0, ry_1_37==wy_3_37+-1), 
And(rprim_1_37==1, rechassigned_3_37==1, rx_1_37==wx_3_37+1, ry_1_37==wy_3_37+-1), 
))))
# wprim = 2
s.add(Implies(wprim_3_38==2, 
And(wtraj_3_39==wtraj_3_38, ch_3_38<20, ch_3_39==ch_3_38+rech_amt_3_38, 
Or(
And(rprim_1_38==1, rechassigned_3_38==1, rx_1_38==wx_3_38+1, ry_1_38==wy_3_38+0), 
And(rprim_1_38==1, rechassigned_3_38==1, rx_1_38==wx_3_38+1, ry_1_38==wy_3_38+1), 
And(rprim_1_38==1, rechassigned_3_38==1, rx_1_38==wx_3_38+0, ry_1_38==wy_3_38+1), 
And(rprim_1_38==1, rechassigned_3_38==1, rx_1_38==wx_3_38+-1, ry_1_38==wy_3_38+1), 
And(rprim_1_38==1, rechassigned_3_38==1, rx_1_38==wx_3_38+-1, ry_1_38==wy_3_38+0), 
And(rprim_1_38==1, rechassigned_3_38==1, rx_1_38==wx_3_38+-1, ry_1_38==wy_3_38+-1), 
And(rprim_1_38==1, rechassigned_3_38==1, rx_1_38==wx_3_38+0, ry_1_38==wy_3_38+-1), 
And(rprim_1_38==1, rechassigned_3_38==1, rx_1_38==wx_3_38+1, ry_1_38==wy_3_38+-1), 
))))
# wprim = 2
s.add(Implies(wprim_3_39==2, 
And(wtraj_3_40==wtraj_3_39, ch_3_39<20, ch_3_40==ch_3_39+rech_amt_3_39, 
Or(
And(rprim_1_39==1, rechassigned_3_39==1, rx_1_39==wx_3_39+1, ry_1_39==wy_3_39+0), 
And(rprim_1_39==1, rechassigned_3_39==1, rx_1_39==wx_3_39+1, ry_1_39==wy_3_39+1), 
And(rprim_1_39==1, rechassigned_3_39==1, rx_1_39==wx_3_39+0, ry_1_39==wy_3_39+1), 
And(rprim_1_39==1, rechassigned_3_39==1, rx_1_39==wx_3_39+-1, ry_1_39==wy_3_39+1), 
And(rprim_1_39==1, rechassigned_3_39==1, rx_1_39==wx_3_39+-1, ry_1_39==wy_3_39+0), 
And(rprim_1_39==1, rechassigned_3_39==1, rx_1_39==wx_3_39+-1, ry_1_39==wy_3_39+-1), 
And(rprim_1_39==1, rechassigned_3_39==1, rx_1_39==wx_3_39+0, ry_1_39==wy_3_39+-1), 
And(rprim_1_39==1, rechassigned_3_39==1, rx_1_39==wx_3_39+1, ry_1_39==wy_3_39+-1), 
))))
# wprim = 2
s.add(Implies(wprim_3_40==2, 
And(wtraj_3_41==wtraj_3_40, ch_3_40<20, ch_3_41==ch_3_40+rech_amt_3_40, 
Or(
And(rprim_1_40==1, rechassigned_3_40==1, rx_1_40==wx_3_40+1, ry_1_40==wy_3_40+0), 
And(rprim_1_40==1, rechassigned_3_40==1, rx_1_40==wx_3_40+1, ry_1_40==wy_3_40+1), 
And(rprim_1_40==1, rechassigned_3_40==1, rx_1_40==wx_3_40+0, ry_1_40==wy_3_40+1), 
And(rprim_1_40==1, rechassigned_3_40==1, rx_1_40==wx_3_40+-1, ry_1_40==wy_3_40+1), 
And(rprim_1_40==1, rechassigned_3_40==1, rx_1_40==wx_3_40+-1, ry_1_40==wy_3_40+0), 
And(rprim_1_40==1, rechassigned_3_40==1, rx_1_40==wx_3_40+-1, ry_1_40==wy_3_40+-1), 
And(rprim_1_40==1, rechassigned_3_40==1, rx_1_40==wx_3_40+0, ry_1_40==wy_3_40+-1), 
And(rprim_1_40==1, rechassigned_3_40==1, rx_1_40==wx_3_40+1, ry_1_40==wy_3_40+-1), 
))))
# wprim = 2
s.add(Implies(wprim_3_41==2, 
And(wtraj_3_42==wtraj_3_41, ch_3_41<20, ch_3_42==ch_3_41+rech_amt_3_41, 
Or(
And(rprim_1_41==1, rechassigned_3_41==1, rx_1_41==wx_3_41+1, ry_1_41==wy_3_41+0), 
And(rprim_1_41==1, rechassigned_3_41==1, rx_1_41==wx_3_41+1, ry_1_41==wy_3_41+1), 
And(rprim_1_41==1, rechassigned_3_41==1, rx_1_41==wx_3_41+0, ry_1_41==wy_3_41+1), 
And(rprim_1_41==1, rechassigned_3_41==1, rx_1_41==wx_3_41+-1, ry_1_41==wy_3_41+1), 
And(rprim_1_41==1, rechassigned_3_41==1, rx_1_41==wx_3_41+-1, ry_1_41==wy_3_41+0), 
And(rprim_1_41==1, rechassigned_3_41==1, rx_1_41==wx_3_41+-1, ry_1_41==wy_3_41+-1), 
And(rprim_1_41==1, rechassigned_3_41==1, rx_1_41==wx_3_41+0, ry_1_41==wy_3_41+-1), 
And(rprim_1_41==1, rechassigned_3_41==1, rx_1_41==wx_3_41+1, ry_1_41==wy_3_41+-1), 
))))
# wprim = 2
s.add(Implies(wprim_3_42==2, 
And(wtraj_3_43==wtraj_3_42, ch_3_42<20, ch_3_43==ch_3_42+rech_amt_3_42, 
Or(
And(rprim_1_42==1, rechassigned_3_42==1, rx_1_42==wx_3_42+1, ry_1_42==wy_3_42+0), 
And(rprim_1_42==1, rechassigned_3_42==1, rx_1_42==wx_3_42+1, ry_1_42==wy_3_42+1), 
And(rprim_1_42==1, rechassigned_3_42==1, rx_1_42==wx_3_42+0, ry_1_42==wy_3_42+1), 
And(rprim_1_42==1, rechassigned_3_42==1, rx_1_42==wx_3_42+-1, ry_1_42==wy_3_42+1), 
And(rprim_1_42==1, rechassigned_3_42==1, rx_1_42==wx_3_42+-1, ry_1_42==wy_3_42+0), 
And(rprim_1_42==1, rechassigned_3_42==1, rx_1_42==wx_3_42+-1, ry_1_42==wy_3_42+-1), 
And(rprim_1_42==1, rechassigned_3_42==1, rx_1_42==wx_3_42+0, ry_1_42==wy_3_42+-1), 
And(rprim_1_42==1, rechassigned_3_42==1, rx_1_42==wx_3_42+1, ry_1_42==wy_3_42+-1), 
))))
# wprim = 2
s.add(Implies(wprim_3_43==2, 
And(wtraj_3_44==wtraj_3_43, ch_3_43<20, ch_3_44==ch_3_43+rech_amt_3_43, 
Or(
And(rprim_1_43==1, rechassigned_3_43==1, rx_1_43==wx_3_43+1, ry_1_43==wy_3_43+0), 
And(rprim_1_43==1, rechassigned_3_43==1, rx_1_43==wx_3_43+1, ry_1_43==wy_3_43+1), 
And(rprim_1_43==1, rechassigned_3_43==1, rx_1_43==wx_3_43+0, ry_1_43==wy_3_43+1), 
And(rprim_1_43==1, rechassigned_3_43==1, rx_1_43==wx_3_43+-1, ry_1_43==wy_3_43+1), 
And(rprim_1_43==1, rechassigned_3_43==1, rx_1_43==wx_3_43+-1, ry_1_43==wy_3_43+0), 
And(rprim_1_43==1, rechassigned_3_43==1, rx_1_43==wx_3_43+-1, ry_1_43==wy_3_43+-1), 
And(rprim_1_43==1, rechassigned_3_43==1, rx_1_43==wx_3_43+0, ry_1_43==wy_3_43+-1), 
And(rprim_1_43==1, rechassigned_3_43==1, rx_1_43==wx_3_43+1, ry_1_43==wy_3_43+-1), 
))))
# wprim = 2
s.add(Implies(wprim_3_44==2, 
And(wtraj_3_45==wtraj_3_44, ch_3_44<20, ch_3_45==ch_3_44+rech_amt_3_44, 
Or(
And(rprim_1_44==1, rechassigned_3_44==1, rx_1_44==wx_3_44+1, ry_1_44==wy_3_44+0), 
And(rprim_1_44==1, rechassigned_3_44==1, rx_1_44==wx_3_44+1, ry_1_44==wy_3_44+1), 
And(rprim_1_44==1, rechassigned_3_44==1, rx_1_44==wx_3_44+0, ry_1_44==wy_3_44+1), 
And(rprim_1_44==1, rechassigned_3_44==1, rx_1_44==wx_3_44+-1, ry_1_44==wy_3_44+1), 
And(rprim_1_44==1, rechassigned_3_44==1, rx_1_44==wx_3_44+-1, ry_1_44==wy_3_44+0), 
And(rprim_1_44==1, rechassigned_3_44==1, rx_1_44==wx_3_44+-1, ry_1_44==wy_3_44+-1), 
And(rprim_1_44==1, rechassigned_3_44==1, rx_1_44==wx_3_44+0, ry_1_44==wy_3_44+-1), 
And(rprim_1_44==1, rechassigned_3_44==1, rx_1_44==wx_3_44+1, ry_1_44==wy_3_44+-1), 
))))
# wprim = 2
s.add(Implies(wprim_3_45==2, 
And(wtraj_3_46==wtraj_3_45, ch_3_45<20, ch_3_46==ch_3_45+rech_amt_3_45, 
Or(
And(rprim_1_45==1, rechassigned_3_45==1, rx_1_45==wx_3_45+1, ry_1_45==wy_3_45+0), 
And(rprim_1_45==1, rechassigned_3_45==1, rx_1_45==wx_3_45+1, ry_1_45==wy_3_45+1), 
And(rprim_1_45==1, rechassigned_3_45==1, rx_1_45==wx_3_45+0, ry_1_45==wy_3_45+1), 
And(rprim_1_45==1, rechassigned_3_45==1, rx_1_45==wx_3_45+-1, ry_1_45==wy_3_45+1), 
And(rprim_1_45==1, rechassigned_3_45==1, rx_1_45==wx_3_45+-1, ry_1_45==wy_3_45+0), 
And(rprim_1_45==1, rechassigned_3_45==1, rx_1_45==wx_3_45+-1, ry_1_45==wy_3_45+-1), 
And(rprim_1_45==1, rechassigned_3_45==1, rx_1_45==wx_3_45+0, ry_1_45==wy_3_45+-1), 
And(rprim_1_45==1, rechassigned_3_45==1, rx_1_45==wx_3_45+1, ry_1_45==wy_3_45+-1), 
))))
# wprim = 2
s.add(Implies(wprim_3_46==2, 
And(wtraj_3_47==wtraj_3_46, ch_3_46<20, ch_3_47==ch_3_46+rech_amt_3_46, 
Or(
And(rprim_1_46==1, rechassigned_3_46==1, rx_1_46==wx_3_46+1, ry_1_46==wy_3_46+0), 
And(rprim_1_46==1, rechassigned_3_46==1, rx_1_46==wx_3_46+1, ry_1_46==wy_3_46+1), 
And(rprim_1_46==1, rechassigned_3_46==1, rx_1_46==wx_3_46+0, ry_1_46==wy_3_46+1), 
And(rprim_1_46==1, rechassigned_3_46==1, rx_1_46==wx_3_46+-1, ry_1_46==wy_3_46+1), 
And(rprim_1_46==1, rechassigned_3_46==1, rx_1_46==wx_3_46+-1, ry_1_46==wy_3_46+0), 
And(rprim_1_46==1, rechassigned_3_46==1, rx_1_46==wx_3_46+-1, ry_1_46==wy_3_46+-1), 
And(rprim_1_46==1, rechassigned_3_46==1, rx_1_46==wx_3_46+0, ry_1_46==wy_3_46+-1), 
And(rprim_1_46==1, rechassigned_3_46==1, rx_1_46==wx_3_46+1, ry_1_46==wy_3_46+-1), 
))))
# wprim = 2
s.add(Implies(wprim_3_47==2, 
And(wtraj_3_48==wtraj_3_47, ch_3_47<20, ch_3_48==ch_3_47+rech_amt_3_47, 
Or(
And(rprim_1_47==1, rechassigned_3_47==1, rx_1_47==wx_3_47+1, ry_1_47==wy_3_47+0), 
And(rprim_1_47==1, rechassigned_3_47==1, rx_1_47==wx_3_47+1, ry_1_47==wy_3_47+1), 
And(rprim_1_47==1, rechassigned_3_47==1, rx_1_47==wx_3_47+0, ry_1_47==wy_3_47+1), 
And(rprim_1_47==1, rechassigned_3_47==1, rx_1_47==wx_3_47+-1, ry_1_47==wy_3_47+1), 
And(rprim_1_47==1, rechassigned_3_47==1, rx_1_47==wx_3_47+-1, ry_1_47==wy_3_47+0), 
And(rprim_1_47==1, rechassigned_3_47==1, rx_1_47==wx_3_47+-1, ry_1_47==wy_3_47+-1), 
And(rprim_1_47==1, rechassigned_3_47==1, rx_1_47==wx_3_47+0, ry_1_47==wy_3_47+-1), 
And(rprim_1_47==1, rechassigned_3_47==1, rx_1_47==wx_3_47+1, ry_1_47==wy_3_47+-1), 
))))
# wprim = 2
s.add(Implies(wprim_3_48==2, 
And(wtraj_3_49==wtraj_3_48, ch_3_48<20, ch_3_49==ch_3_48+rech_amt_3_48, 
Or(
And(rprim_1_48==1, rechassigned_3_48==1, rx_1_48==wx_3_48+1, ry_1_48==wy_3_48+0), 
And(rprim_1_48==1, rechassigned_3_48==1, rx_1_48==wx_3_48+1, ry_1_48==wy_3_48+1), 
And(rprim_1_48==1, rechassigned_3_48==1, rx_1_48==wx_3_48+0, ry_1_48==wy_3_48+1), 
And(rprim_1_48==1, rechassigned_3_48==1, rx_1_48==wx_3_48+-1, ry_1_48==wy_3_48+1), 
And(rprim_1_48==1, rechassigned_3_48==1, rx_1_48==wx_3_48+-1, ry_1_48==wy_3_48+0), 
And(rprim_1_48==1, rechassigned_3_48==1, rx_1_48==wx_3_48+-1, ry_1_48==wy_3_48+-1), 
And(rprim_1_48==1, rechassigned_3_48==1, rx_1_48==wx_3_48+0, ry_1_48==wy_3_48+-1), 
And(rprim_1_48==1, rechassigned_3_48==1, rx_1_48==wx_3_48+1, ry_1_48==wy_3_48+-1), 
))))
# wprim = 2
s.add(Implies(wprim_4_1==2, 
And(wtraj_4_2==wtraj_4_1, ch_4_1<20, ch_4_2==ch_4_1+rech_amt_4_1, 
Or(
And(rprim_1_1==1, rechassigned_4_1==1, rx_1_1==wx_4_1+1, ry_1_1==wy_4_1+0), 
And(rprim_1_1==1, rechassigned_4_1==1, rx_1_1==wx_4_1+1, ry_1_1==wy_4_1+1), 
And(rprim_1_1==1, rechassigned_4_1==1, rx_1_1==wx_4_1+0, ry_1_1==wy_4_1+1), 
And(rprim_1_1==1, rechassigned_4_1==1, rx_1_1==wx_4_1+-1, ry_1_1==wy_4_1+1), 
And(rprim_1_1==1, rechassigned_4_1==1, rx_1_1==wx_4_1+-1, ry_1_1==wy_4_1+0), 
And(rprim_1_1==1, rechassigned_4_1==1, rx_1_1==wx_4_1+-1, ry_1_1==wy_4_1+-1), 
And(rprim_1_1==1, rechassigned_4_1==1, rx_1_1==wx_4_1+0, ry_1_1==wy_4_1+-1), 
And(rprim_1_1==1, rechassigned_4_1==1, rx_1_1==wx_4_1+1, ry_1_1==wy_4_1+-1), 
))))
# wprim = 2
s.add(Implies(wprim_4_2==2, 
And(wtraj_4_3==wtraj_4_2, ch_4_2<20, ch_4_3==ch_4_2+rech_amt_4_2, 
Or(
And(rprim_1_2==1, rechassigned_4_2==1, rx_1_2==wx_4_2+1, ry_1_2==wy_4_2+0), 
And(rprim_1_2==1, rechassigned_4_2==1, rx_1_2==wx_4_2+1, ry_1_2==wy_4_2+1), 
And(rprim_1_2==1, rechassigned_4_2==1, rx_1_2==wx_4_2+0, ry_1_2==wy_4_2+1), 
And(rprim_1_2==1, rechassigned_4_2==1, rx_1_2==wx_4_2+-1, ry_1_2==wy_4_2+1), 
And(rprim_1_2==1, rechassigned_4_2==1, rx_1_2==wx_4_2+-1, ry_1_2==wy_4_2+0), 
And(rprim_1_2==1, rechassigned_4_2==1, rx_1_2==wx_4_2+-1, ry_1_2==wy_4_2+-1), 
And(rprim_1_2==1, rechassigned_4_2==1, rx_1_2==wx_4_2+0, ry_1_2==wy_4_2+-1), 
And(rprim_1_2==1, rechassigned_4_2==1, rx_1_2==wx_4_2+1, ry_1_2==wy_4_2+-1), 
))))
# wprim = 2
s.add(Implies(wprim_4_3==2, 
And(wtraj_4_4==wtraj_4_3, ch_4_3<20, ch_4_4==ch_4_3+rech_amt_4_3, 
Or(
And(rprim_1_3==1, rechassigned_4_3==1, rx_1_3==wx_4_3+1, ry_1_3==wy_4_3+0), 
And(rprim_1_3==1, rechassigned_4_3==1, rx_1_3==wx_4_3+1, ry_1_3==wy_4_3+1), 
And(rprim_1_3==1, rechassigned_4_3==1, rx_1_3==wx_4_3+0, ry_1_3==wy_4_3+1), 
And(rprim_1_3==1, rechassigned_4_3==1, rx_1_3==wx_4_3+-1, ry_1_3==wy_4_3+1), 
And(rprim_1_3==1, rechassigned_4_3==1, rx_1_3==wx_4_3+-1, ry_1_3==wy_4_3+0), 
And(rprim_1_3==1, rechassigned_4_3==1, rx_1_3==wx_4_3+-1, ry_1_3==wy_4_3+-1), 
And(rprim_1_3==1, rechassigned_4_3==1, rx_1_3==wx_4_3+0, ry_1_3==wy_4_3+-1), 
And(rprim_1_3==1, rechassigned_4_3==1, rx_1_3==wx_4_3+1, ry_1_3==wy_4_3+-1), 
))))
# wprim = 2
s.add(Implies(wprim_4_4==2, 
And(wtraj_4_5==wtraj_4_4, ch_4_4<20, ch_4_5==ch_4_4+rech_amt_4_4, 
Or(
And(rprim_1_4==1, rechassigned_4_4==1, rx_1_4==wx_4_4+1, ry_1_4==wy_4_4+0), 
And(rprim_1_4==1, rechassigned_4_4==1, rx_1_4==wx_4_4+1, ry_1_4==wy_4_4+1), 
And(rprim_1_4==1, rechassigned_4_4==1, rx_1_4==wx_4_4+0, ry_1_4==wy_4_4+1), 
And(rprim_1_4==1, rechassigned_4_4==1, rx_1_4==wx_4_4+-1, ry_1_4==wy_4_4+1), 
And(rprim_1_4==1, rechassigned_4_4==1, rx_1_4==wx_4_4+-1, ry_1_4==wy_4_4+0), 
And(rprim_1_4==1, rechassigned_4_4==1, rx_1_4==wx_4_4+-1, ry_1_4==wy_4_4+-1), 
And(rprim_1_4==1, rechassigned_4_4==1, rx_1_4==wx_4_4+0, ry_1_4==wy_4_4+-1), 
And(rprim_1_4==1, rechassigned_4_4==1, rx_1_4==wx_4_4+1, ry_1_4==wy_4_4+-1), 
))))
# wprim = 2
s.add(Implies(wprim_4_5==2, 
And(wtraj_4_6==wtraj_4_5, ch_4_5<20, ch_4_6==ch_4_5+rech_amt_4_5, 
Or(
And(rprim_1_5==1, rechassigned_4_5==1, rx_1_5==wx_4_5+1, ry_1_5==wy_4_5+0), 
And(rprim_1_5==1, rechassigned_4_5==1, rx_1_5==wx_4_5+1, ry_1_5==wy_4_5+1), 
And(rprim_1_5==1, rechassigned_4_5==1, rx_1_5==wx_4_5+0, ry_1_5==wy_4_5+1), 
And(rprim_1_5==1, rechassigned_4_5==1, rx_1_5==wx_4_5+-1, ry_1_5==wy_4_5+1), 
And(rprim_1_5==1, rechassigned_4_5==1, rx_1_5==wx_4_5+-1, ry_1_5==wy_4_5+0), 
And(rprim_1_5==1, rechassigned_4_5==1, rx_1_5==wx_4_5+-1, ry_1_5==wy_4_5+-1), 
And(rprim_1_5==1, rechassigned_4_5==1, rx_1_5==wx_4_5+0, ry_1_5==wy_4_5+-1), 
And(rprim_1_5==1, rechassigned_4_5==1, rx_1_5==wx_4_5+1, ry_1_5==wy_4_5+-1), 
))))
# wprim = 2
s.add(Implies(wprim_4_6==2, 
And(wtraj_4_7==wtraj_4_6, ch_4_6<20, ch_4_7==ch_4_6+rech_amt_4_6, 
Or(
And(rprim_1_6==1, rechassigned_4_6==1, rx_1_6==wx_4_6+1, ry_1_6==wy_4_6+0), 
And(rprim_1_6==1, rechassigned_4_6==1, rx_1_6==wx_4_6+1, ry_1_6==wy_4_6+1), 
And(rprim_1_6==1, rechassigned_4_6==1, rx_1_6==wx_4_6+0, ry_1_6==wy_4_6+1), 
And(rprim_1_6==1, rechassigned_4_6==1, rx_1_6==wx_4_6+-1, ry_1_6==wy_4_6+1), 
And(rprim_1_6==1, rechassigned_4_6==1, rx_1_6==wx_4_6+-1, ry_1_6==wy_4_6+0), 
And(rprim_1_6==1, rechassigned_4_6==1, rx_1_6==wx_4_6+-1, ry_1_6==wy_4_6+-1), 
And(rprim_1_6==1, rechassigned_4_6==1, rx_1_6==wx_4_6+0, ry_1_6==wy_4_6+-1), 
And(rprim_1_6==1, rechassigned_4_6==1, rx_1_6==wx_4_6+1, ry_1_6==wy_4_6+-1), 
))))
# wprim = 2
s.add(Implies(wprim_4_7==2, 
And(wtraj_4_8==wtraj_4_7, ch_4_7<20, ch_4_8==ch_4_7+rech_amt_4_7, 
Or(
And(rprim_1_7==1, rechassigned_4_7==1, rx_1_7==wx_4_7+1, ry_1_7==wy_4_7+0), 
And(rprim_1_7==1, rechassigned_4_7==1, rx_1_7==wx_4_7+1, ry_1_7==wy_4_7+1), 
And(rprim_1_7==1, rechassigned_4_7==1, rx_1_7==wx_4_7+0, ry_1_7==wy_4_7+1), 
And(rprim_1_7==1, rechassigned_4_7==1, rx_1_7==wx_4_7+-1, ry_1_7==wy_4_7+1), 
And(rprim_1_7==1, rechassigned_4_7==1, rx_1_7==wx_4_7+-1, ry_1_7==wy_4_7+0), 
And(rprim_1_7==1, rechassigned_4_7==1, rx_1_7==wx_4_7+-1, ry_1_7==wy_4_7+-1), 
And(rprim_1_7==1, rechassigned_4_7==1, rx_1_7==wx_4_7+0, ry_1_7==wy_4_7+-1), 
And(rprim_1_7==1, rechassigned_4_7==1, rx_1_7==wx_4_7+1, ry_1_7==wy_4_7+-1), 
))))
# wprim = 2
s.add(Implies(wprim_4_8==2, 
And(wtraj_4_9==wtraj_4_8, ch_4_8<20, ch_4_9==ch_4_8+rech_amt_4_8, 
Or(
And(rprim_1_8==1, rechassigned_4_8==1, rx_1_8==wx_4_8+1, ry_1_8==wy_4_8+0), 
And(rprim_1_8==1, rechassigned_4_8==1, rx_1_8==wx_4_8+1, ry_1_8==wy_4_8+1), 
And(rprim_1_8==1, rechassigned_4_8==1, rx_1_8==wx_4_8+0, ry_1_8==wy_4_8+1), 
And(rprim_1_8==1, rechassigned_4_8==1, rx_1_8==wx_4_8+-1, ry_1_8==wy_4_8+1), 
And(rprim_1_8==1, rechassigned_4_8==1, rx_1_8==wx_4_8+-1, ry_1_8==wy_4_8+0), 
And(rprim_1_8==1, rechassigned_4_8==1, rx_1_8==wx_4_8+-1, ry_1_8==wy_4_8+-1), 
And(rprim_1_8==1, rechassigned_4_8==1, rx_1_8==wx_4_8+0, ry_1_8==wy_4_8+-1), 
And(rprim_1_8==1, rechassigned_4_8==1, rx_1_8==wx_4_8+1, ry_1_8==wy_4_8+-1), 
))))
# wprim = 2
s.add(Implies(wprim_4_9==2, 
And(wtraj_4_10==wtraj_4_9, ch_4_9<20, ch_4_10==ch_4_9+rech_amt_4_9, 
Or(
And(rprim_1_9==1, rechassigned_4_9==1, rx_1_9==wx_4_9+1, ry_1_9==wy_4_9+0), 
And(rprim_1_9==1, rechassigned_4_9==1, rx_1_9==wx_4_9+1, ry_1_9==wy_4_9+1), 
And(rprim_1_9==1, rechassigned_4_9==1, rx_1_9==wx_4_9+0, ry_1_9==wy_4_9+1), 
And(rprim_1_9==1, rechassigned_4_9==1, rx_1_9==wx_4_9+-1, ry_1_9==wy_4_9+1), 
And(rprim_1_9==1, rechassigned_4_9==1, rx_1_9==wx_4_9+-1, ry_1_9==wy_4_9+0), 
And(rprim_1_9==1, rechassigned_4_9==1, rx_1_9==wx_4_9+-1, ry_1_9==wy_4_9+-1), 
And(rprim_1_9==1, rechassigned_4_9==1, rx_1_9==wx_4_9+0, ry_1_9==wy_4_9+-1), 
And(rprim_1_9==1, rechassigned_4_9==1, rx_1_9==wx_4_9+1, ry_1_9==wy_4_9+-1), 
))))
# wprim = 2
s.add(Implies(wprim_4_10==2, 
And(wtraj_4_11==wtraj_4_10, ch_4_10<20, ch_4_11==ch_4_10+rech_amt_4_10, 
Or(
And(rprim_1_10==1, rechassigned_4_10==1, rx_1_10==wx_4_10+1, ry_1_10==wy_4_10+0), 
And(rprim_1_10==1, rechassigned_4_10==1, rx_1_10==wx_4_10+1, ry_1_10==wy_4_10+1), 
And(rprim_1_10==1, rechassigned_4_10==1, rx_1_10==wx_4_10+0, ry_1_10==wy_4_10+1), 
And(rprim_1_10==1, rechassigned_4_10==1, rx_1_10==wx_4_10+-1, ry_1_10==wy_4_10+1), 
And(rprim_1_10==1, rechassigned_4_10==1, rx_1_10==wx_4_10+-1, ry_1_10==wy_4_10+0), 
And(rprim_1_10==1, rechassigned_4_10==1, rx_1_10==wx_4_10+-1, ry_1_10==wy_4_10+-1), 
And(rprim_1_10==1, rechassigned_4_10==1, rx_1_10==wx_4_10+0, ry_1_10==wy_4_10+-1), 
And(rprim_1_10==1, rechassigned_4_10==1, rx_1_10==wx_4_10+1, ry_1_10==wy_4_10+-1), 
))))
# wprim = 2
s.add(Implies(wprim_4_11==2, 
And(wtraj_4_12==wtraj_4_11, ch_4_11<20, ch_4_12==ch_4_11+rech_amt_4_11, 
Or(
And(rprim_1_11==1, rechassigned_4_11==1, rx_1_11==wx_4_11+1, ry_1_11==wy_4_11+0), 
And(rprim_1_11==1, rechassigned_4_11==1, rx_1_11==wx_4_11+1, ry_1_11==wy_4_11+1), 
And(rprim_1_11==1, rechassigned_4_11==1, rx_1_11==wx_4_11+0, ry_1_11==wy_4_11+1), 
And(rprim_1_11==1, rechassigned_4_11==1, rx_1_11==wx_4_11+-1, ry_1_11==wy_4_11+1), 
And(rprim_1_11==1, rechassigned_4_11==1, rx_1_11==wx_4_11+-1, ry_1_11==wy_4_11+0), 
And(rprim_1_11==1, rechassigned_4_11==1, rx_1_11==wx_4_11+-1, ry_1_11==wy_4_11+-1), 
And(rprim_1_11==1, rechassigned_4_11==1, rx_1_11==wx_4_11+0, ry_1_11==wy_4_11+-1), 
And(rprim_1_11==1, rechassigned_4_11==1, rx_1_11==wx_4_11+1, ry_1_11==wy_4_11+-1), 
))))
# wprim = 2
s.add(Implies(wprim_4_12==2, 
And(wtraj_4_13==wtraj_4_12, ch_4_12<20, ch_4_13==ch_4_12+rech_amt_4_12, 
Or(
And(rprim_1_12==1, rechassigned_4_12==1, rx_1_12==wx_4_12+1, ry_1_12==wy_4_12+0), 
And(rprim_1_12==1, rechassigned_4_12==1, rx_1_12==wx_4_12+1, ry_1_12==wy_4_12+1), 
And(rprim_1_12==1, rechassigned_4_12==1, rx_1_12==wx_4_12+0, ry_1_12==wy_4_12+1), 
And(rprim_1_12==1, rechassigned_4_12==1, rx_1_12==wx_4_12+-1, ry_1_12==wy_4_12+1), 
And(rprim_1_12==1, rechassigned_4_12==1, rx_1_12==wx_4_12+-1, ry_1_12==wy_4_12+0), 
And(rprim_1_12==1, rechassigned_4_12==1, rx_1_12==wx_4_12+-1, ry_1_12==wy_4_12+-1), 
And(rprim_1_12==1, rechassigned_4_12==1, rx_1_12==wx_4_12+0, ry_1_12==wy_4_12+-1), 
And(rprim_1_12==1, rechassigned_4_12==1, rx_1_12==wx_4_12+1, ry_1_12==wy_4_12+-1), 
))))
# wprim = 2
s.add(Implies(wprim_4_13==2, 
And(wtraj_4_14==wtraj_4_13, ch_4_13<20, ch_4_14==ch_4_13+rech_amt_4_13, 
Or(
And(rprim_1_13==1, rechassigned_4_13==1, rx_1_13==wx_4_13+1, ry_1_13==wy_4_13+0), 
And(rprim_1_13==1, rechassigned_4_13==1, rx_1_13==wx_4_13+1, ry_1_13==wy_4_13+1), 
And(rprim_1_13==1, rechassigned_4_13==1, rx_1_13==wx_4_13+0, ry_1_13==wy_4_13+1), 
And(rprim_1_13==1, rechassigned_4_13==1, rx_1_13==wx_4_13+-1, ry_1_13==wy_4_13+1), 
And(rprim_1_13==1, rechassigned_4_13==1, rx_1_13==wx_4_13+-1, ry_1_13==wy_4_13+0), 
And(rprim_1_13==1, rechassigned_4_13==1, rx_1_13==wx_4_13+-1, ry_1_13==wy_4_13+-1), 
And(rprim_1_13==1, rechassigned_4_13==1, rx_1_13==wx_4_13+0, ry_1_13==wy_4_13+-1), 
And(rprim_1_13==1, rechassigned_4_13==1, rx_1_13==wx_4_13+1, ry_1_13==wy_4_13+-1), 
))))
# wprim = 2
s.add(Implies(wprim_4_14==2, 
And(wtraj_4_15==wtraj_4_14, ch_4_14<20, ch_4_15==ch_4_14+rech_amt_4_14, 
Or(
And(rprim_1_14==1, rechassigned_4_14==1, rx_1_14==wx_4_14+1, ry_1_14==wy_4_14+0), 
And(rprim_1_14==1, rechassigned_4_14==1, rx_1_14==wx_4_14+1, ry_1_14==wy_4_14+1), 
And(rprim_1_14==1, rechassigned_4_14==1, rx_1_14==wx_4_14+0, ry_1_14==wy_4_14+1), 
And(rprim_1_14==1, rechassigned_4_14==1, rx_1_14==wx_4_14+-1, ry_1_14==wy_4_14+1), 
And(rprim_1_14==1, rechassigned_4_14==1, rx_1_14==wx_4_14+-1, ry_1_14==wy_4_14+0), 
And(rprim_1_14==1, rechassigned_4_14==1, rx_1_14==wx_4_14+-1, ry_1_14==wy_4_14+-1), 
And(rprim_1_14==1, rechassigned_4_14==1, rx_1_14==wx_4_14+0, ry_1_14==wy_4_14+-1), 
And(rprim_1_14==1, rechassigned_4_14==1, rx_1_14==wx_4_14+1, ry_1_14==wy_4_14+-1), 
))))
# wprim = 2
s.add(Implies(wprim_4_15==2, 
And(wtraj_4_16==wtraj_4_15, ch_4_15<20, ch_4_16==ch_4_15+rech_amt_4_15, 
Or(
And(rprim_1_15==1, rechassigned_4_15==1, rx_1_15==wx_4_15+1, ry_1_15==wy_4_15+0), 
And(rprim_1_15==1, rechassigned_4_15==1, rx_1_15==wx_4_15+1, ry_1_15==wy_4_15+1), 
And(rprim_1_15==1, rechassigned_4_15==1, rx_1_15==wx_4_15+0, ry_1_15==wy_4_15+1), 
And(rprim_1_15==1, rechassigned_4_15==1, rx_1_15==wx_4_15+-1, ry_1_15==wy_4_15+1), 
And(rprim_1_15==1, rechassigned_4_15==1, rx_1_15==wx_4_15+-1, ry_1_15==wy_4_15+0), 
And(rprim_1_15==1, rechassigned_4_15==1, rx_1_15==wx_4_15+-1, ry_1_15==wy_4_15+-1), 
And(rprim_1_15==1, rechassigned_4_15==1, rx_1_15==wx_4_15+0, ry_1_15==wy_4_15+-1), 
And(rprim_1_15==1, rechassigned_4_15==1, rx_1_15==wx_4_15+1, ry_1_15==wy_4_15+-1), 
))))
# wprim = 2
s.add(Implies(wprim_4_16==2, 
And(wtraj_4_17==wtraj_4_16, ch_4_16<20, ch_4_17==ch_4_16+rech_amt_4_16, 
Or(
And(rprim_1_16==1, rechassigned_4_16==1, rx_1_16==wx_4_16+1, ry_1_16==wy_4_16+0), 
And(rprim_1_16==1, rechassigned_4_16==1, rx_1_16==wx_4_16+1, ry_1_16==wy_4_16+1), 
And(rprim_1_16==1, rechassigned_4_16==1, rx_1_16==wx_4_16+0, ry_1_16==wy_4_16+1), 
And(rprim_1_16==1, rechassigned_4_16==1, rx_1_16==wx_4_16+-1, ry_1_16==wy_4_16+1), 
And(rprim_1_16==1, rechassigned_4_16==1, rx_1_16==wx_4_16+-1, ry_1_16==wy_4_16+0), 
And(rprim_1_16==1, rechassigned_4_16==1, rx_1_16==wx_4_16+-1, ry_1_16==wy_4_16+-1), 
And(rprim_1_16==1, rechassigned_4_16==1, rx_1_16==wx_4_16+0, ry_1_16==wy_4_16+-1), 
And(rprim_1_16==1, rechassigned_4_16==1, rx_1_16==wx_4_16+1, ry_1_16==wy_4_16+-1), 
))))
# wprim = 2
s.add(Implies(wprim_4_17==2, 
And(wtraj_4_18==wtraj_4_17, ch_4_17<20, ch_4_18==ch_4_17+rech_amt_4_17, 
Or(
And(rprim_1_17==1, rechassigned_4_17==1, rx_1_17==wx_4_17+1, ry_1_17==wy_4_17+0), 
And(rprim_1_17==1, rechassigned_4_17==1, rx_1_17==wx_4_17+1, ry_1_17==wy_4_17+1), 
And(rprim_1_17==1, rechassigned_4_17==1, rx_1_17==wx_4_17+0, ry_1_17==wy_4_17+1), 
And(rprim_1_17==1, rechassigned_4_17==1, rx_1_17==wx_4_17+-1, ry_1_17==wy_4_17+1), 
And(rprim_1_17==1, rechassigned_4_17==1, rx_1_17==wx_4_17+-1, ry_1_17==wy_4_17+0), 
And(rprim_1_17==1, rechassigned_4_17==1, rx_1_17==wx_4_17+-1, ry_1_17==wy_4_17+-1), 
And(rprim_1_17==1, rechassigned_4_17==1, rx_1_17==wx_4_17+0, ry_1_17==wy_4_17+-1), 
And(rprim_1_17==1, rechassigned_4_17==1, rx_1_17==wx_4_17+1, ry_1_17==wy_4_17+-1), 
))))
# wprim = 2
s.add(Implies(wprim_4_18==2, 
And(wtraj_4_19==wtraj_4_18, ch_4_18<20, ch_4_19==ch_4_18+rech_amt_4_18, 
Or(
And(rprim_1_18==1, rechassigned_4_18==1, rx_1_18==wx_4_18+1, ry_1_18==wy_4_18+0), 
And(rprim_1_18==1, rechassigned_4_18==1, rx_1_18==wx_4_18+1, ry_1_18==wy_4_18+1), 
And(rprim_1_18==1, rechassigned_4_18==1, rx_1_18==wx_4_18+0, ry_1_18==wy_4_18+1), 
And(rprim_1_18==1, rechassigned_4_18==1, rx_1_18==wx_4_18+-1, ry_1_18==wy_4_18+1), 
And(rprim_1_18==1, rechassigned_4_18==1, rx_1_18==wx_4_18+-1, ry_1_18==wy_4_18+0), 
And(rprim_1_18==1, rechassigned_4_18==1, rx_1_18==wx_4_18+-1, ry_1_18==wy_4_18+-1), 
And(rprim_1_18==1, rechassigned_4_18==1, rx_1_18==wx_4_18+0, ry_1_18==wy_4_18+-1), 
And(rprim_1_18==1, rechassigned_4_18==1, rx_1_18==wx_4_18+1, ry_1_18==wy_4_18+-1), 
))))
# wprim = 2
s.add(Implies(wprim_4_19==2, 
And(wtraj_4_20==wtraj_4_19, ch_4_19<20, ch_4_20==ch_4_19+rech_amt_4_19, 
Or(
And(rprim_1_19==1, rechassigned_4_19==1, rx_1_19==wx_4_19+1, ry_1_19==wy_4_19+0), 
And(rprim_1_19==1, rechassigned_4_19==1, rx_1_19==wx_4_19+1, ry_1_19==wy_4_19+1), 
And(rprim_1_19==1, rechassigned_4_19==1, rx_1_19==wx_4_19+0, ry_1_19==wy_4_19+1), 
And(rprim_1_19==1, rechassigned_4_19==1, rx_1_19==wx_4_19+-1, ry_1_19==wy_4_19+1), 
And(rprim_1_19==1, rechassigned_4_19==1, rx_1_19==wx_4_19+-1, ry_1_19==wy_4_19+0), 
And(rprim_1_19==1, rechassigned_4_19==1, rx_1_19==wx_4_19+-1, ry_1_19==wy_4_19+-1), 
And(rprim_1_19==1, rechassigned_4_19==1, rx_1_19==wx_4_19+0, ry_1_19==wy_4_19+-1), 
And(rprim_1_19==1, rechassigned_4_19==1, rx_1_19==wx_4_19+1, ry_1_19==wy_4_19+-1), 
))))
# wprim = 2
s.add(Implies(wprim_4_20==2, 
And(wtraj_4_21==wtraj_4_20, ch_4_20<20, ch_4_21==ch_4_20+rech_amt_4_20, 
Or(
And(rprim_1_20==1, rechassigned_4_20==1, rx_1_20==wx_4_20+1, ry_1_20==wy_4_20+0), 
And(rprim_1_20==1, rechassigned_4_20==1, rx_1_20==wx_4_20+1, ry_1_20==wy_4_20+1), 
And(rprim_1_20==1, rechassigned_4_20==1, rx_1_20==wx_4_20+0, ry_1_20==wy_4_20+1), 
And(rprim_1_20==1, rechassigned_4_20==1, rx_1_20==wx_4_20+-1, ry_1_20==wy_4_20+1), 
And(rprim_1_20==1, rechassigned_4_20==1, rx_1_20==wx_4_20+-1, ry_1_20==wy_4_20+0), 
And(rprim_1_20==1, rechassigned_4_20==1, rx_1_20==wx_4_20+-1, ry_1_20==wy_4_20+-1), 
And(rprim_1_20==1, rechassigned_4_20==1, rx_1_20==wx_4_20+0, ry_1_20==wy_4_20+-1), 
And(rprim_1_20==1, rechassigned_4_20==1, rx_1_20==wx_4_20+1, ry_1_20==wy_4_20+-1), 
))))
# wprim = 2
s.add(Implies(wprim_4_21==2, 
And(wtraj_4_22==wtraj_4_21, ch_4_21<20, ch_4_22==ch_4_21+rech_amt_4_21, 
Or(
And(rprim_1_21==1, rechassigned_4_21==1, rx_1_21==wx_4_21+1, ry_1_21==wy_4_21+0), 
And(rprim_1_21==1, rechassigned_4_21==1, rx_1_21==wx_4_21+1, ry_1_21==wy_4_21+1), 
And(rprim_1_21==1, rechassigned_4_21==1, rx_1_21==wx_4_21+0, ry_1_21==wy_4_21+1), 
And(rprim_1_21==1, rechassigned_4_21==1, rx_1_21==wx_4_21+-1, ry_1_21==wy_4_21+1), 
And(rprim_1_21==1, rechassigned_4_21==1, rx_1_21==wx_4_21+-1, ry_1_21==wy_4_21+0), 
And(rprim_1_21==1, rechassigned_4_21==1, rx_1_21==wx_4_21+-1, ry_1_21==wy_4_21+-1), 
And(rprim_1_21==1, rechassigned_4_21==1, rx_1_21==wx_4_21+0, ry_1_21==wy_4_21+-1), 
And(rprim_1_21==1, rechassigned_4_21==1, rx_1_21==wx_4_21+1, ry_1_21==wy_4_21+-1), 
))))
# wprim = 2
s.add(Implies(wprim_4_22==2, 
And(wtraj_4_23==wtraj_4_22, ch_4_22<20, ch_4_23==ch_4_22+rech_amt_4_22, 
Or(
And(rprim_1_22==1, rechassigned_4_22==1, rx_1_22==wx_4_22+1, ry_1_22==wy_4_22+0), 
And(rprim_1_22==1, rechassigned_4_22==1, rx_1_22==wx_4_22+1, ry_1_22==wy_4_22+1), 
And(rprim_1_22==1, rechassigned_4_22==1, rx_1_22==wx_4_22+0, ry_1_22==wy_4_22+1), 
And(rprim_1_22==1, rechassigned_4_22==1, rx_1_22==wx_4_22+-1, ry_1_22==wy_4_22+1), 
And(rprim_1_22==1, rechassigned_4_22==1, rx_1_22==wx_4_22+-1, ry_1_22==wy_4_22+0), 
And(rprim_1_22==1, rechassigned_4_22==1, rx_1_22==wx_4_22+-1, ry_1_22==wy_4_22+-1), 
And(rprim_1_22==1, rechassigned_4_22==1, rx_1_22==wx_4_22+0, ry_1_22==wy_4_22+-1), 
And(rprim_1_22==1, rechassigned_4_22==1, rx_1_22==wx_4_22+1, ry_1_22==wy_4_22+-1), 
))))
# wprim = 2
s.add(Implies(wprim_4_23==2, 
And(wtraj_4_24==wtraj_4_23, ch_4_23<20, ch_4_24==ch_4_23+rech_amt_4_23, 
Or(
And(rprim_1_23==1, rechassigned_4_23==1, rx_1_23==wx_4_23+1, ry_1_23==wy_4_23+0), 
And(rprim_1_23==1, rechassigned_4_23==1, rx_1_23==wx_4_23+1, ry_1_23==wy_4_23+1), 
And(rprim_1_23==1, rechassigned_4_23==1, rx_1_23==wx_4_23+0, ry_1_23==wy_4_23+1), 
And(rprim_1_23==1, rechassigned_4_23==1, rx_1_23==wx_4_23+-1, ry_1_23==wy_4_23+1), 
And(rprim_1_23==1, rechassigned_4_23==1, rx_1_23==wx_4_23+-1, ry_1_23==wy_4_23+0), 
And(rprim_1_23==1, rechassigned_4_23==1, rx_1_23==wx_4_23+-1, ry_1_23==wy_4_23+-1), 
And(rprim_1_23==1, rechassigned_4_23==1, rx_1_23==wx_4_23+0, ry_1_23==wy_4_23+-1), 
And(rprim_1_23==1, rechassigned_4_23==1, rx_1_23==wx_4_23+1, ry_1_23==wy_4_23+-1), 
))))
# wprim = 2
s.add(Implies(wprim_4_24==2, 
And(wtraj_4_25==wtraj_4_24, ch_4_24<20, ch_4_25==ch_4_24+rech_amt_4_24, 
Or(
And(rprim_1_24==1, rechassigned_4_24==1, rx_1_24==wx_4_24+1, ry_1_24==wy_4_24+0), 
And(rprim_1_24==1, rechassigned_4_24==1, rx_1_24==wx_4_24+1, ry_1_24==wy_4_24+1), 
And(rprim_1_24==1, rechassigned_4_24==1, rx_1_24==wx_4_24+0, ry_1_24==wy_4_24+1), 
And(rprim_1_24==1, rechassigned_4_24==1, rx_1_24==wx_4_24+-1, ry_1_24==wy_4_24+1), 
And(rprim_1_24==1, rechassigned_4_24==1, rx_1_24==wx_4_24+-1, ry_1_24==wy_4_24+0), 
And(rprim_1_24==1, rechassigned_4_24==1, rx_1_24==wx_4_24+-1, ry_1_24==wy_4_24+-1), 
And(rprim_1_24==1, rechassigned_4_24==1, rx_1_24==wx_4_24+0, ry_1_24==wy_4_24+-1), 
And(rprim_1_24==1, rechassigned_4_24==1, rx_1_24==wx_4_24+1, ry_1_24==wy_4_24+-1), 
))))
# wprim = 2
s.add(Implies(wprim_4_25==2, 
And(wtraj_4_26==wtraj_4_25, ch_4_25<20, ch_4_26==ch_4_25+rech_amt_4_25, 
Or(
And(rprim_1_25==1, rechassigned_4_25==1, rx_1_25==wx_4_25+1, ry_1_25==wy_4_25+0), 
And(rprim_1_25==1, rechassigned_4_25==1, rx_1_25==wx_4_25+1, ry_1_25==wy_4_25+1), 
And(rprim_1_25==1, rechassigned_4_25==1, rx_1_25==wx_4_25+0, ry_1_25==wy_4_25+1), 
And(rprim_1_25==1, rechassigned_4_25==1, rx_1_25==wx_4_25+-1, ry_1_25==wy_4_25+1), 
And(rprim_1_25==1, rechassigned_4_25==1, rx_1_25==wx_4_25+-1, ry_1_25==wy_4_25+0), 
And(rprim_1_25==1, rechassigned_4_25==1, rx_1_25==wx_4_25+-1, ry_1_25==wy_4_25+-1), 
And(rprim_1_25==1, rechassigned_4_25==1, rx_1_25==wx_4_25+0, ry_1_25==wy_4_25+-1), 
And(rprim_1_25==1, rechassigned_4_25==1, rx_1_25==wx_4_25+1, ry_1_25==wy_4_25+-1), 
))))
# wprim = 2
s.add(Implies(wprim_4_26==2, 
And(wtraj_4_27==wtraj_4_26, ch_4_26<20, ch_4_27==ch_4_26+rech_amt_4_26, 
Or(
And(rprim_1_26==1, rechassigned_4_26==1, rx_1_26==wx_4_26+1, ry_1_26==wy_4_26+0), 
And(rprim_1_26==1, rechassigned_4_26==1, rx_1_26==wx_4_26+1, ry_1_26==wy_4_26+1), 
And(rprim_1_26==1, rechassigned_4_26==1, rx_1_26==wx_4_26+0, ry_1_26==wy_4_26+1), 
And(rprim_1_26==1, rechassigned_4_26==1, rx_1_26==wx_4_26+-1, ry_1_26==wy_4_26+1), 
And(rprim_1_26==1, rechassigned_4_26==1, rx_1_26==wx_4_26+-1, ry_1_26==wy_4_26+0), 
And(rprim_1_26==1, rechassigned_4_26==1, rx_1_26==wx_4_26+-1, ry_1_26==wy_4_26+-1), 
And(rprim_1_26==1, rechassigned_4_26==1, rx_1_26==wx_4_26+0, ry_1_26==wy_4_26+-1), 
And(rprim_1_26==1, rechassigned_4_26==1, rx_1_26==wx_4_26+1, ry_1_26==wy_4_26+-1), 
))))
# wprim = 2
s.add(Implies(wprim_4_27==2, 
And(wtraj_4_28==wtraj_4_27, ch_4_27<20, ch_4_28==ch_4_27+rech_amt_4_27, 
Or(
And(rprim_1_27==1, rechassigned_4_27==1, rx_1_27==wx_4_27+1, ry_1_27==wy_4_27+0), 
And(rprim_1_27==1, rechassigned_4_27==1, rx_1_27==wx_4_27+1, ry_1_27==wy_4_27+1), 
And(rprim_1_27==1, rechassigned_4_27==1, rx_1_27==wx_4_27+0, ry_1_27==wy_4_27+1), 
And(rprim_1_27==1, rechassigned_4_27==1, rx_1_27==wx_4_27+-1, ry_1_27==wy_4_27+1), 
And(rprim_1_27==1, rechassigned_4_27==1, rx_1_27==wx_4_27+-1, ry_1_27==wy_4_27+0), 
And(rprim_1_27==1, rechassigned_4_27==1, rx_1_27==wx_4_27+-1, ry_1_27==wy_4_27+-1), 
And(rprim_1_27==1, rechassigned_4_27==1, rx_1_27==wx_4_27+0, ry_1_27==wy_4_27+-1), 
And(rprim_1_27==1, rechassigned_4_27==1, rx_1_27==wx_4_27+1, ry_1_27==wy_4_27+-1), 
))))
# wprim = 2
s.add(Implies(wprim_4_28==2, 
And(wtraj_4_29==wtraj_4_28, ch_4_28<20, ch_4_29==ch_4_28+rech_amt_4_28, 
Or(
And(rprim_1_28==1, rechassigned_4_28==1, rx_1_28==wx_4_28+1, ry_1_28==wy_4_28+0), 
And(rprim_1_28==1, rechassigned_4_28==1, rx_1_28==wx_4_28+1, ry_1_28==wy_4_28+1), 
And(rprim_1_28==1, rechassigned_4_28==1, rx_1_28==wx_4_28+0, ry_1_28==wy_4_28+1), 
And(rprim_1_28==1, rechassigned_4_28==1, rx_1_28==wx_4_28+-1, ry_1_28==wy_4_28+1), 
And(rprim_1_28==1, rechassigned_4_28==1, rx_1_28==wx_4_28+-1, ry_1_28==wy_4_28+0), 
And(rprim_1_28==1, rechassigned_4_28==1, rx_1_28==wx_4_28+-1, ry_1_28==wy_4_28+-1), 
And(rprim_1_28==1, rechassigned_4_28==1, rx_1_28==wx_4_28+0, ry_1_28==wy_4_28+-1), 
And(rprim_1_28==1, rechassigned_4_28==1, rx_1_28==wx_4_28+1, ry_1_28==wy_4_28+-1), 
))))
# wprim = 2
s.add(Implies(wprim_4_29==2, 
And(wtraj_4_30==wtraj_4_29, ch_4_29<20, ch_4_30==ch_4_29+rech_amt_4_29, 
Or(
And(rprim_1_29==1, rechassigned_4_29==1, rx_1_29==wx_4_29+1, ry_1_29==wy_4_29+0), 
And(rprim_1_29==1, rechassigned_4_29==1, rx_1_29==wx_4_29+1, ry_1_29==wy_4_29+1), 
And(rprim_1_29==1, rechassigned_4_29==1, rx_1_29==wx_4_29+0, ry_1_29==wy_4_29+1), 
And(rprim_1_29==1, rechassigned_4_29==1, rx_1_29==wx_4_29+-1, ry_1_29==wy_4_29+1), 
And(rprim_1_29==1, rechassigned_4_29==1, rx_1_29==wx_4_29+-1, ry_1_29==wy_4_29+0), 
And(rprim_1_29==1, rechassigned_4_29==1, rx_1_29==wx_4_29+-1, ry_1_29==wy_4_29+-1), 
And(rprim_1_29==1, rechassigned_4_29==1, rx_1_29==wx_4_29+0, ry_1_29==wy_4_29+-1), 
And(rprim_1_29==1, rechassigned_4_29==1, rx_1_29==wx_4_29+1, ry_1_29==wy_4_29+-1), 
))))
# wprim = 2
s.add(Implies(wprim_4_30==2, 
And(wtraj_4_31==wtraj_4_30, ch_4_30<20, ch_4_31==ch_4_30+rech_amt_4_30, 
Or(
And(rprim_1_30==1, rechassigned_4_30==1, rx_1_30==wx_4_30+1, ry_1_30==wy_4_30+0), 
And(rprim_1_30==1, rechassigned_4_30==1, rx_1_30==wx_4_30+1, ry_1_30==wy_4_30+1), 
And(rprim_1_30==1, rechassigned_4_30==1, rx_1_30==wx_4_30+0, ry_1_30==wy_4_30+1), 
And(rprim_1_30==1, rechassigned_4_30==1, rx_1_30==wx_4_30+-1, ry_1_30==wy_4_30+1), 
And(rprim_1_30==1, rechassigned_4_30==1, rx_1_30==wx_4_30+-1, ry_1_30==wy_4_30+0), 
And(rprim_1_30==1, rechassigned_4_30==1, rx_1_30==wx_4_30+-1, ry_1_30==wy_4_30+-1), 
And(rprim_1_30==1, rechassigned_4_30==1, rx_1_30==wx_4_30+0, ry_1_30==wy_4_30+-1), 
And(rprim_1_30==1, rechassigned_4_30==1, rx_1_30==wx_4_30+1, ry_1_30==wy_4_30+-1), 
))))
# wprim = 2
s.add(Implies(wprim_4_31==2, 
And(wtraj_4_32==wtraj_4_31, ch_4_31<20, ch_4_32==ch_4_31+rech_amt_4_31, 
Or(
And(rprim_1_31==1, rechassigned_4_31==1, rx_1_31==wx_4_31+1, ry_1_31==wy_4_31+0), 
And(rprim_1_31==1, rechassigned_4_31==1, rx_1_31==wx_4_31+1, ry_1_31==wy_4_31+1), 
And(rprim_1_31==1, rechassigned_4_31==1, rx_1_31==wx_4_31+0, ry_1_31==wy_4_31+1), 
And(rprim_1_31==1, rechassigned_4_31==1, rx_1_31==wx_4_31+-1, ry_1_31==wy_4_31+1), 
And(rprim_1_31==1, rechassigned_4_31==1, rx_1_31==wx_4_31+-1, ry_1_31==wy_4_31+0), 
And(rprim_1_31==1, rechassigned_4_31==1, rx_1_31==wx_4_31+-1, ry_1_31==wy_4_31+-1), 
And(rprim_1_31==1, rechassigned_4_31==1, rx_1_31==wx_4_31+0, ry_1_31==wy_4_31+-1), 
And(rprim_1_31==1, rechassigned_4_31==1, rx_1_31==wx_4_31+1, ry_1_31==wy_4_31+-1), 
))))
# wprim = 2
s.add(Implies(wprim_4_32==2, 
And(wtraj_4_33==wtraj_4_32, ch_4_32<20, ch_4_33==ch_4_32+rech_amt_4_32, 
Or(
And(rprim_1_32==1, rechassigned_4_32==1, rx_1_32==wx_4_32+1, ry_1_32==wy_4_32+0), 
And(rprim_1_32==1, rechassigned_4_32==1, rx_1_32==wx_4_32+1, ry_1_32==wy_4_32+1), 
And(rprim_1_32==1, rechassigned_4_32==1, rx_1_32==wx_4_32+0, ry_1_32==wy_4_32+1), 
And(rprim_1_32==1, rechassigned_4_32==1, rx_1_32==wx_4_32+-1, ry_1_32==wy_4_32+1), 
And(rprim_1_32==1, rechassigned_4_32==1, rx_1_32==wx_4_32+-1, ry_1_32==wy_4_32+0), 
And(rprim_1_32==1, rechassigned_4_32==1, rx_1_32==wx_4_32+-1, ry_1_32==wy_4_32+-1), 
And(rprim_1_32==1, rechassigned_4_32==1, rx_1_32==wx_4_32+0, ry_1_32==wy_4_32+-1), 
And(rprim_1_32==1, rechassigned_4_32==1, rx_1_32==wx_4_32+1, ry_1_32==wy_4_32+-1), 
))))
# wprim = 2
s.add(Implies(wprim_4_33==2, 
And(wtraj_4_34==wtraj_4_33, ch_4_33<20, ch_4_34==ch_4_33+rech_amt_4_33, 
Or(
And(rprim_1_33==1, rechassigned_4_33==1, rx_1_33==wx_4_33+1, ry_1_33==wy_4_33+0), 
And(rprim_1_33==1, rechassigned_4_33==1, rx_1_33==wx_4_33+1, ry_1_33==wy_4_33+1), 
And(rprim_1_33==1, rechassigned_4_33==1, rx_1_33==wx_4_33+0, ry_1_33==wy_4_33+1), 
And(rprim_1_33==1, rechassigned_4_33==1, rx_1_33==wx_4_33+-1, ry_1_33==wy_4_33+1), 
And(rprim_1_33==1, rechassigned_4_33==1, rx_1_33==wx_4_33+-1, ry_1_33==wy_4_33+0), 
And(rprim_1_33==1, rechassigned_4_33==1, rx_1_33==wx_4_33+-1, ry_1_33==wy_4_33+-1), 
And(rprim_1_33==1, rechassigned_4_33==1, rx_1_33==wx_4_33+0, ry_1_33==wy_4_33+-1), 
And(rprim_1_33==1, rechassigned_4_33==1, rx_1_33==wx_4_33+1, ry_1_33==wy_4_33+-1), 
))))
# wprim = 2
s.add(Implies(wprim_4_34==2, 
And(wtraj_4_35==wtraj_4_34, ch_4_34<20, ch_4_35==ch_4_34+rech_amt_4_34, 
Or(
And(rprim_1_34==1, rechassigned_4_34==1, rx_1_34==wx_4_34+1, ry_1_34==wy_4_34+0), 
And(rprim_1_34==1, rechassigned_4_34==1, rx_1_34==wx_4_34+1, ry_1_34==wy_4_34+1), 
And(rprim_1_34==1, rechassigned_4_34==1, rx_1_34==wx_4_34+0, ry_1_34==wy_4_34+1), 
And(rprim_1_34==1, rechassigned_4_34==1, rx_1_34==wx_4_34+-1, ry_1_34==wy_4_34+1), 
And(rprim_1_34==1, rechassigned_4_34==1, rx_1_34==wx_4_34+-1, ry_1_34==wy_4_34+0), 
And(rprim_1_34==1, rechassigned_4_34==1, rx_1_34==wx_4_34+-1, ry_1_34==wy_4_34+-1), 
And(rprim_1_34==1, rechassigned_4_34==1, rx_1_34==wx_4_34+0, ry_1_34==wy_4_34+-1), 
And(rprim_1_34==1, rechassigned_4_34==1, rx_1_34==wx_4_34+1, ry_1_34==wy_4_34+-1), 
))))
# wprim = 2
s.add(Implies(wprim_4_35==2, 
And(wtraj_4_36==wtraj_4_35, ch_4_35<20, ch_4_36==ch_4_35+rech_amt_4_35, 
Or(
And(rprim_1_35==1, rechassigned_4_35==1, rx_1_35==wx_4_35+1, ry_1_35==wy_4_35+0), 
And(rprim_1_35==1, rechassigned_4_35==1, rx_1_35==wx_4_35+1, ry_1_35==wy_4_35+1), 
And(rprim_1_35==1, rechassigned_4_35==1, rx_1_35==wx_4_35+0, ry_1_35==wy_4_35+1), 
And(rprim_1_35==1, rechassigned_4_35==1, rx_1_35==wx_4_35+-1, ry_1_35==wy_4_35+1), 
And(rprim_1_35==1, rechassigned_4_35==1, rx_1_35==wx_4_35+-1, ry_1_35==wy_4_35+0), 
And(rprim_1_35==1, rechassigned_4_35==1, rx_1_35==wx_4_35+-1, ry_1_35==wy_4_35+-1), 
And(rprim_1_35==1, rechassigned_4_35==1, rx_1_35==wx_4_35+0, ry_1_35==wy_4_35+-1), 
And(rprim_1_35==1, rechassigned_4_35==1, rx_1_35==wx_4_35+1, ry_1_35==wy_4_35+-1), 
))))
# wprim = 2
s.add(Implies(wprim_4_36==2, 
And(wtraj_4_37==wtraj_4_36, ch_4_36<20, ch_4_37==ch_4_36+rech_amt_4_36, 
Or(
And(rprim_1_36==1, rechassigned_4_36==1, rx_1_36==wx_4_36+1, ry_1_36==wy_4_36+0), 
And(rprim_1_36==1, rechassigned_4_36==1, rx_1_36==wx_4_36+1, ry_1_36==wy_4_36+1), 
And(rprim_1_36==1, rechassigned_4_36==1, rx_1_36==wx_4_36+0, ry_1_36==wy_4_36+1), 
And(rprim_1_36==1, rechassigned_4_36==1, rx_1_36==wx_4_36+-1, ry_1_36==wy_4_36+1), 
And(rprim_1_36==1, rechassigned_4_36==1, rx_1_36==wx_4_36+-1, ry_1_36==wy_4_36+0), 
And(rprim_1_36==1, rechassigned_4_36==1, rx_1_36==wx_4_36+-1, ry_1_36==wy_4_36+-1), 
And(rprim_1_36==1, rechassigned_4_36==1, rx_1_36==wx_4_36+0, ry_1_36==wy_4_36+-1), 
And(rprim_1_36==1, rechassigned_4_36==1, rx_1_36==wx_4_36+1, ry_1_36==wy_4_36+-1), 
))))
# wprim = 2
s.add(Implies(wprim_4_37==2, 
And(wtraj_4_38==wtraj_4_37, ch_4_37<20, ch_4_38==ch_4_37+rech_amt_4_37, 
Or(
And(rprim_1_37==1, rechassigned_4_37==1, rx_1_37==wx_4_37+1, ry_1_37==wy_4_37+0), 
And(rprim_1_37==1, rechassigned_4_37==1, rx_1_37==wx_4_37+1, ry_1_37==wy_4_37+1), 
And(rprim_1_37==1, rechassigned_4_37==1, rx_1_37==wx_4_37+0, ry_1_37==wy_4_37+1), 
And(rprim_1_37==1, rechassigned_4_37==1, rx_1_37==wx_4_37+-1, ry_1_37==wy_4_37+1), 
And(rprim_1_37==1, rechassigned_4_37==1, rx_1_37==wx_4_37+-1, ry_1_37==wy_4_37+0), 
And(rprim_1_37==1, rechassigned_4_37==1, rx_1_37==wx_4_37+-1, ry_1_37==wy_4_37+-1), 
And(rprim_1_37==1, rechassigned_4_37==1, rx_1_37==wx_4_37+0, ry_1_37==wy_4_37+-1), 
And(rprim_1_37==1, rechassigned_4_37==1, rx_1_37==wx_4_37+1, ry_1_37==wy_4_37+-1), 
))))
# wprim = 2
s.add(Implies(wprim_4_38==2, 
And(wtraj_4_39==wtraj_4_38, ch_4_38<20, ch_4_39==ch_4_38+rech_amt_4_38, 
Or(
And(rprim_1_38==1, rechassigned_4_38==1, rx_1_38==wx_4_38+1, ry_1_38==wy_4_38+0), 
And(rprim_1_38==1, rechassigned_4_38==1, rx_1_38==wx_4_38+1, ry_1_38==wy_4_38+1), 
And(rprim_1_38==1, rechassigned_4_38==1, rx_1_38==wx_4_38+0, ry_1_38==wy_4_38+1), 
And(rprim_1_38==1, rechassigned_4_38==1, rx_1_38==wx_4_38+-1, ry_1_38==wy_4_38+1), 
And(rprim_1_38==1, rechassigned_4_38==1, rx_1_38==wx_4_38+-1, ry_1_38==wy_4_38+0), 
And(rprim_1_38==1, rechassigned_4_38==1, rx_1_38==wx_4_38+-1, ry_1_38==wy_4_38+-1), 
And(rprim_1_38==1, rechassigned_4_38==1, rx_1_38==wx_4_38+0, ry_1_38==wy_4_38+-1), 
And(rprim_1_38==1, rechassigned_4_38==1, rx_1_38==wx_4_38+1, ry_1_38==wy_4_38+-1), 
))))
# wprim = 2
s.add(Implies(wprim_4_39==2, 
And(wtraj_4_40==wtraj_4_39, ch_4_39<20, ch_4_40==ch_4_39+rech_amt_4_39, 
Or(
And(rprim_1_39==1, rechassigned_4_39==1, rx_1_39==wx_4_39+1, ry_1_39==wy_4_39+0), 
And(rprim_1_39==1, rechassigned_4_39==1, rx_1_39==wx_4_39+1, ry_1_39==wy_4_39+1), 
And(rprim_1_39==1, rechassigned_4_39==1, rx_1_39==wx_4_39+0, ry_1_39==wy_4_39+1), 
And(rprim_1_39==1, rechassigned_4_39==1, rx_1_39==wx_4_39+-1, ry_1_39==wy_4_39+1), 
And(rprim_1_39==1, rechassigned_4_39==1, rx_1_39==wx_4_39+-1, ry_1_39==wy_4_39+0), 
And(rprim_1_39==1, rechassigned_4_39==1, rx_1_39==wx_4_39+-1, ry_1_39==wy_4_39+-1), 
And(rprim_1_39==1, rechassigned_4_39==1, rx_1_39==wx_4_39+0, ry_1_39==wy_4_39+-1), 
And(rprim_1_39==1, rechassigned_4_39==1, rx_1_39==wx_4_39+1, ry_1_39==wy_4_39+-1), 
))))
# wprim = 2
s.add(Implies(wprim_4_40==2, 
And(wtraj_4_41==wtraj_4_40, ch_4_40<20, ch_4_41==ch_4_40+rech_amt_4_40, 
Or(
And(rprim_1_40==1, rechassigned_4_40==1, rx_1_40==wx_4_40+1, ry_1_40==wy_4_40+0), 
And(rprim_1_40==1, rechassigned_4_40==1, rx_1_40==wx_4_40+1, ry_1_40==wy_4_40+1), 
And(rprim_1_40==1, rechassigned_4_40==1, rx_1_40==wx_4_40+0, ry_1_40==wy_4_40+1), 
And(rprim_1_40==1, rechassigned_4_40==1, rx_1_40==wx_4_40+-1, ry_1_40==wy_4_40+1), 
And(rprim_1_40==1, rechassigned_4_40==1, rx_1_40==wx_4_40+-1, ry_1_40==wy_4_40+0), 
And(rprim_1_40==1, rechassigned_4_40==1, rx_1_40==wx_4_40+-1, ry_1_40==wy_4_40+-1), 
And(rprim_1_40==1, rechassigned_4_40==1, rx_1_40==wx_4_40+0, ry_1_40==wy_4_40+-1), 
And(rprim_1_40==1, rechassigned_4_40==1, rx_1_40==wx_4_40+1, ry_1_40==wy_4_40+-1), 
))))
# wprim = 2
s.add(Implies(wprim_4_41==2, 
And(wtraj_4_42==wtraj_4_41, ch_4_41<20, ch_4_42==ch_4_41+rech_amt_4_41, 
Or(
And(rprim_1_41==1, rechassigned_4_41==1, rx_1_41==wx_4_41+1, ry_1_41==wy_4_41+0), 
And(rprim_1_41==1, rechassigned_4_41==1, rx_1_41==wx_4_41+1, ry_1_41==wy_4_41+1), 
And(rprim_1_41==1, rechassigned_4_41==1, rx_1_41==wx_4_41+0, ry_1_41==wy_4_41+1), 
And(rprim_1_41==1, rechassigned_4_41==1, rx_1_41==wx_4_41+-1, ry_1_41==wy_4_41+1), 
And(rprim_1_41==1, rechassigned_4_41==1, rx_1_41==wx_4_41+-1, ry_1_41==wy_4_41+0), 
And(rprim_1_41==1, rechassigned_4_41==1, rx_1_41==wx_4_41+-1, ry_1_41==wy_4_41+-1), 
And(rprim_1_41==1, rechassigned_4_41==1, rx_1_41==wx_4_41+0, ry_1_41==wy_4_41+-1), 
And(rprim_1_41==1, rechassigned_4_41==1, rx_1_41==wx_4_41+1, ry_1_41==wy_4_41+-1), 
))))
# wprim = 2
s.add(Implies(wprim_4_42==2, 
And(wtraj_4_43==wtraj_4_42, ch_4_42<20, ch_4_43==ch_4_42+rech_amt_4_42, 
Or(
And(rprim_1_42==1, rechassigned_4_42==1, rx_1_42==wx_4_42+1, ry_1_42==wy_4_42+0), 
And(rprim_1_42==1, rechassigned_4_42==1, rx_1_42==wx_4_42+1, ry_1_42==wy_4_42+1), 
And(rprim_1_42==1, rechassigned_4_42==1, rx_1_42==wx_4_42+0, ry_1_42==wy_4_42+1), 
And(rprim_1_42==1, rechassigned_4_42==1, rx_1_42==wx_4_42+-1, ry_1_42==wy_4_42+1), 
And(rprim_1_42==1, rechassigned_4_42==1, rx_1_42==wx_4_42+-1, ry_1_42==wy_4_42+0), 
And(rprim_1_42==1, rechassigned_4_42==1, rx_1_42==wx_4_42+-1, ry_1_42==wy_4_42+-1), 
And(rprim_1_42==1, rechassigned_4_42==1, rx_1_42==wx_4_42+0, ry_1_42==wy_4_42+-1), 
And(rprim_1_42==1, rechassigned_4_42==1, rx_1_42==wx_4_42+1, ry_1_42==wy_4_42+-1), 
))))
# wprim = 2
s.add(Implies(wprim_4_43==2, 
And(wtraj_4_44==wtraj_4_43, ch_4_43<20, ch_4_44==ch_4_43+rech_amt_4_43, 
Or(
And(rprim_1_43==1, rechassigned_4_43==1, rx_1_43==wx_4_43+1, ry_1_43==wy_4_43+0), 
And(rprim_1_43==1, rechassigned_4_43==1, rx_1_43==wx_4_43+1, ry_1_43==wy_4_43+1), 
And(rprim_1_43==1, rechassigned_4_43==1, rx_1_43==wx_4_43+0, ry_1_43==wy_4_43+1), 
And(rprim_1_43==1, rechassigned_4_43==1, rx_1_43==wx_4_43+-1, ry_1_43==wy_4_43+1), 
And(rprim_1_43==1, rechassigned_4_43==1, rx_1_43==wx_4_43+-1, ry_1_43==wy_4_43+0), 
And(rprim_1_43==1, rechassigned_4_43==1, rx_1_43==wx_4_43+-1, ry_1_43==wy_4_43+-1), 
And(rprim_1_43==1, rechassigned_4_43==1, rx_1_43==wx_4_43+0, ry_1_43==wy_4_43+-1), 
And(rprim_1_43==1, rechassigned_4_43==1, rx_1_43==wx_4_43+1, ry_1_43==wy_4_43+-1), 
))))
# wprim = 2
s.add(Implies(wprim_4_44==2, 
And(wtraj_4_45==wtraj_4_44, ch_4_44<20, ch_4_45==ch_4_44+rech_amt_4_44, 
Or(
And(rprim_1_44==1, rechassigned_4_44==1, rx_1_44==wx_4_44+1, ry_1_44==wy_4_44+0), 
And(rprim_1_44==1, rechassigned_4_44==1, rx_1_44==wx_4_44+1, ry_1_44==wy_4_44+1), 
And(rprim_1_44==1, rechassigned_4_44==1, rx_1_44==wx_4_44+0, ry_1_44==wy_4_44+1), 
And(rprim_1_44==1, rechassigned_4_44==1, rx_1_44==wx_4_44+-1, ry_1_44==wy_4_44+1), 
And(rprim_1_44==1, rechassigned_4_44==1, rx_1_44==wx_4_44+-1, ry_1_44==wy_4_44+0), 
And(rprim_1_44==1, rechassigned_4_44==1, rx_1_44==wx_4_44+-1, ry_1_44==wy_4_44+-1), 
And(rprim_1_44==1, rechassigned_4_44==1, rx_1_44==wx_4_44+0, ry_1_44==wy_4_44+-1), 
And(rprim_1_44==1, rechassigned_4_44==1, rx_1_44==wx_4_44+1, ry_1_44==wy_4_44+-1), 
))))
# wprim = 2
s.add(Implies(wprim_4_45==2, 
And(wtraj_4_46==wtraj_4_45, ch_4_45<20, ch_4_46==ch_4_45+rech_amt_4_45, 
Or(
And(rprim_1_45==1, rechassigned_4_45==1, rx_1_45==wx_4_45+1, ry_1_45==wy_4_45+0), 
And(rprim_1_45==1, rechassigned_4_45==1, rx_1_45==wx_4_45+1, ry_1_45==wy_4_45+1), 
And(rprim_1_45==1, rechassigned_4_45==1, rx_1_45==wx_4_45+0, ry_1_45==wy_4_45+1), 
And(rprim_1_45==1, rechassigned_4_45==1, rx_1_45==wx_4_45+-1, ry_1_45==wy_4_45+1), 
And(rprim_1_45==1, rechassigned_4_45==1, rx_1_45==wx_4_45+-1, ry_1_45==wy_4_45+0), 
And(rprim_1_45==1, rechassigned_4_45==1, rx_1_45==wx_4_45+-1, ry_1_45==wy_4_45+-1), 
And(rprim_1_45==1, rechassigned_4_45==1, rx_1_45==wx_4_45+0, ry_1_45==wy_4_45+-1), 
And(rprim_1_45==1, rechassigned_4_45==1, rx_1_45==wx_4_45+1, ry_1_45==wy_4_45+-1), 
))))
# wprim = 2
s.add(Implies(wprim_4_46==2, 
And(wtraj_4_47==wtraj_4_46, ch_4_46<20, ch_4_47==ch_4_46+rech_amt_4_46, 
Or(
And(rprim_1_46==1, rechassigned_4_46==1, rx_1_46==wx_4_46+1, ry_1_46==wy_4_46+0), 
And(rprim_1_46==1, rechassigned_4_46==1, rx_1_46==wx_4_46+1, ry_1_46==wy_4_46+1), 
And(rprim_1_46==1, rechassigned_4_46==1, rx_1_46==wx_4_46+0, ry_1_46==wy_4_46+1), 
And(rprim_1_46==1, rechassigned_4_46==1, rx_1_46==wx_4_46+-1, ry_1_46==wy_4_46+1), 
And(rprim_1_46==1, rechassigned_4_46==1, rx_1_46==wx_4_46+-1, ry_1_46==wy_4_46+0), 
And(rprim_1_46==1, rechassigned_4_46==1, rx_1_46==wx_4_46+-1, ry_1_46==wy_4_46+-1), 
And(rprim_1_46==1, rechassigned_4_46==1, rx_1_46==wx_4_46+0, ry_1_46==wy_4_46+-1), 
And(rprim_1_46==1, rechassigned_4_46==1, rx_1_46==wx_4_46+1, ry_1_46==wy_4_46+-1), 
))))
# wprim = 2
s.add(Implies(wprim_4_47==2, 
And(wtraj_4_48==wtraj_4_47, ch_4_47<20, ch_4_48==ch_4_47+rech_amt_4_47, 
Or(
And(rprim_1_47==1, rechassigned_4_47==1, rx_1_47==wx_4_47+1, ry_1_47==wy_4_47+0), 
And(rprim_1_47==1, rechassigned_4_47==1, rx_1_47==wx_4_47+1, ry_1_47==wy_4_47+1), 
And(rprim_1_47==1, rechassigned_4_47==1, rx_1_47==wx_4_47+0, ry_1_47==wy_4_47+1), 
And(rprim_1_47==1, rechassigned_4_47==1, rx_1_47==wx_4_47+-1, ry_1_47==wy_4_47+1), 
And(rprim_1_47==1, rechassigned_4_47==1, rx_1_47==wx_4_47+-1, ry_1_47==wy_4_47+0), 
And(rprim_1_47==1, rechassigned_4_47==1, rx_1_47==wx_4_47+-1, ry_1_47==wy_4_47+-1), 
And(rprim_1_47==1, rechassigned_4_47==1, rx_1_47==wx_4_47+0, ry_1_47==wy_4_47+-1), 
And(rprim_1_47==1, rechassigned_4_47==1, rx_1_47==wx_4_47+1, ry_1_47==wy_4_47+-1), 
))))
# wprim = 2
s.add(Implies(wprim_4_48==2, 
And(wtraj_4_49==wtraj_4_48, ch_4_48<20, ch_4_49==ch_4_48+rech_amt_4_48, 
Or(
And(rprim_1_48==1, rechassigned_4_48==1, rx_1_48==wx_4_48+1, ry_1_48==wy_4_48+0), 
And(rprim_1_48==1, rechassigned_4_48==1, rx_1_48==wx_4_48+1, ry_1_48==wy_4_48+1), 
And(rprim_1_48==1, rechassigned_4_48==1, rx_1_48==wx_4_48+0, ry_1_48==wy_4_48+1), 
And(rprim_1_48==1, rechassigned_4_48==1, rx_1_48==wx_4_48+-1, ry_1_48==wy_4_48+1), 
And(rprim_1_48==1, rechassigned_4_48==1, rx_1_48==wx_4_48+-1, ry_1_48==wy_4_48+0), 
And(rprim_1_48==1, rechassigned_4_48==1, rx_1_48==wx_4_48+-1, ry_1_48==wy_4_48+-1), 
And(rprim_1_48==1, rechassigned_4_48==1, rx_1_48==wx_4_48+0, ry_1_48==wy_4_48+-1), 
And(rprim_1_48==1, rechassigned_4_48==1, rx_1_48==wx_4_48+1, ry_1_48==wy_4_48+-1), 
))))

# transition : rechargers

s.add(rprim_1_1>=1, rprim_1_1<=21)
s.add(rprim_1_2>=1, rprim_1_2<=21)
s.add(rprim_1_3>=1, rprim_1_3<=21)
s.add(rprim_1_4>=1, rprim_1_4<=21)
s.add(rprim_1_5>=1, rprim_1_5<=21)
s.add(rprim_1_6>=1, rprim_1_6<=21)
s.add(rprim_1_7>=1, rprim_1_7<=21)
s.add(rprim_1_8>=1, rprim_1_8<=21)
s.add(rprim_1_9>=1, rprim_1_9<=21)
s.add(rprim_1_10>=1, rprim_1_10<=21)
s.add(rprim_1_11>=1, rprim_1_11<=21)
s.add(rprim_1_12>=1, rprim_1_12<=21)
s.add(rprim_1_13>=1, rprim_1_13<=21)
s.add(rprim_1_14>=1, rprim_1_14<=21)
s.add(rprim_1_15>=1, rprim_1_15<=21)
s.add(rprim_1_16>=1, rprim_1_16<=21)
s.add(rprim_1_17>=1, rprim_1_17<=21)
s.add(rprim_1_18>=1, rprim_1_18<=21)
s.add(rprim_1_19>=1, rprim_1_19<=21)
s.add(rprim_1_20>=1, rprim_1_20<=21)
s.add(rprim_1_21>=1, rprim_1_21<=21)
s.add(rprim_1_22>=1, rprim_1_22<=21)
s.add(rprim_1_23>=1, rprim_1_23<=21)
s.add(rprim_1_24>=1, rprim_1_24<=21)
s.add(rprim_1_25>=1, rprim_1_25<=21)
s.add(rprim_1_26>=1, rprim_1_26<=21)
s.add(rprim_1_27>=1, rprim_1_27<=21)
s.add(rprim_1_28>=1, rprim_1_28<=21)
s.add(rprim_1_29>=1, rprim_1_29<=21)
s.add(rprim_1_30>=1, rprim_1_30<=21)
s.add(rprim_1_31>=1, rprim_1_31<=21)
s.add(rprim_1_32>=1, rprim_1_32<=21)
s.add(rprim_1_33>=1, rprim_1_33<=21)
s.add(rprim_1_34>=1, rprim_1_34<=21)
s.add(rprim_1_35>=1, rprim_1_35<=21)
s.add(rprim_1_36>=1, rprim_1_36<=21)
s.add(rprim_1_37>=1, rprim_1_37<=21)
s.add(rprim_1_38>=1, rprim_1_38<=21)
s.add(rprim_1_39>=1, rprim_1_39<=21)
s.add(rprim_1_40>=1, rprim_1_40<=21)
s.add(rprim_1_41>=1, rprim_1_41<=21)
s.add(rprim_1_42>=1, rprim_1_42<=21)
s.add(rprim_1_43>=1, rprim_1_43<=21)
s.add(rprim_1_44>=1, rprim_1_44<=21)
s.add(rprim_1_45>=1, rprim_1_45<=21)
s.add(rprim_1_46>=1, rprim_1_46<=21)
s.add(rprim_1_47>=1, rprim_1_47<=21)
s.add(rprim_1_48>=1, rprim_1_48<=21)

s.add(rx_1_1>=0, rx_1_1<=18)
s.add(rx_1_2>=0, rx_1_2<=18)
s.add(rx_1_3>=0, rx_1_3<=18)
s.add(rx_1_4>=0, rx_1_4<=18)
s.add(rx_1_5>=0, rx_1_5<=18)
s.add(rx_1_6>=0, rx_1_6<=18)
s.add(rx_1_7>=0, rx_1_7<=18)
s.add(rx_1_8>=0, rx_1_8<=18)
s.add(rx_1_9>=0, rx_1_9<=18)
s.add(rx_1_10>=0, rx_1_10<=18)
s.add(rx_1_11>=0, rx_1_11<=18)
s.add(rx_1_12>=0, rx_1_12<=18)
s.add(rx_1_13>=0, rx_1_13<=18)
s.add(rx_1_14>=0, rx_1_14<=18)
s.add(rx_1_15>=0, rx_1_15<=18)
s.add(rx_1_16>=0, rx_1_16<=18)
s.add(rx_1_17>=0, rx_1_17<=18)
s.add(rx_1_18>=0, rx_1_18<=18)
s.add(rx_1_19>=0, rx_1_19<=18)
s.add(rx_1_20>=0, rx_1_20<=18)
s.add(rx_1_21>=0, rx_1_21<=18)
s.add(rx_1_22>=0, rx_1_22<=18)
s.add(rx_1_23>=0, rx_1_23<=18)
s.add(rx_1_24>=0, rx_1_24<=18)
s.add(rx_1_25>=0, rx_1_25<=18)
s.add(rx_1_26>=0, rx_1_26<=18)
s.add(rx_1_27>=0, rx_1_27<=18)
s.add(rx_1_28>=0, rx_1_28<=18)
s.add(rx_1_29>=0, rx_1_29<=18)
s.add(rx_1_30>=0, rx_1_30<=18)
s.add(rx_1_31>=0, rx_1_31<=18)
s.add(rx_1_32>=0, rx_1_32<=18)
s.add(rx_1_33>=0, rx_1_33<=18)
s.add(rx_1_34>=0, rx_1_34<=18)
s.add(rx_1_35>=0, rx_1_35<=18)
s.add(rx_1_36>=0, rx_1_36<=18)
s.add(rx_1_37>=0, rx_1_37<=18)
s.add(rx_1_38>=0, rx_1_38<=18)
s.add(rx_1_39>=0, rx_1_39<=18)
s.add(rx_1_40>=0, rx_1_40<=18)
s.add(rx_1_41>=0, rx_1_41<=18)
s.add(rx_1_42>=0, rx_1_42<=18)
s.add(rx_1_43>=0, rx_1_43<=18)
s.add(rx_1_44>=0, rx_1_44<=18)
s.add(rx_1_45>=0, rx_1_45<=18)
s.add(rx_1_46>=0, rx_1_46<=18)
s.add(rx_1_47>=0, rx_1_47<=18)
s.add(rx_1_48>=0, rx_1_48<=18)
s.add(rx_1_49>=0, rx_1_49<=18)

s.add(ry_1_2>=0, ry_1_2<=18)
s.add(ry_1_3>=0, ry_1_3<=18)
s.add(ry_1_4>=0, ry_1_4<=18)
s.add(ry_1_5>=0, ry_1_5<=18)
s.add(ry_1_6>=0, ry_1_6<=18)
s.add(ry_1_7>=0, ry_1_7<=18)
s.add(ry_1_8>=0, ry_1_8<=18)
s.add(ry_1_9>=0, ry_1_9<=18)
s.add(ry_1_10>=0, ry_1_10<=18)
s.add(ry_1_11>=0, ry_1_11<=18)
s.add(ry_1_12>=0, ry_1_12<=18)
s.add(ry_1_13>=0, ry_1_13<=18)
s.add(ry_1_14>=0, ry_1_14<=18)
s.add(ry_1_15>=0, ry_1_15<=18)
s.add(ry_1_16>=0, ry_1_16<=18)
s.add(ry_1_17>=0, ry_1_17<=18)
s.add(ry_1_18>=0, ry_1_18<=18)
s.add(ry_1_19>=0, ry_1_19<=18)
s.add(ry_1_20>=0, ry_1_20<=18)
s.add(ry_1_21>=0, ry_1_21<=18)
s.add(ry_1_22>=0, ry_1_22<=18)
s.add(ry_1_23>=0, ry_1_23<=18)
s.add(ry_1_24>=0, ry_1_24<=18)
s.add(ry_1_25>=0, ry_1_25<=18)
s.add(ry_1_26>=0, ry_1_26<=18)
s.add(ry_1_27>=0, ry_1_27<=18)
s.add(ry_1_28>=0, ry_1_28<=18)
s.add(ry_1_29>=0, ry_1_29<=18)
s.add(ry_1_30>=0, ry_1_30<=18)
s.add(ry_1_31>=0, ry_1_31<=18)
s.add(ry_1_32>=0, ry_1_32<=18)
s.add(ry_1_33>=0, ry_1_33<=18)
s.add(ry_1_34>=0, ry_1_34<=18)
s.add(ry_1_35>=0, ry_1_35<=18)
s.add(ry_1_36>=0, ry_1_36<=18)
s.add(ry_1_37>=0, ry_1_37<=18)
s.add(ry_1_38>=0, ry_1_38<=18)
s.add(ry_1_39>=0, ry_1_39<=18)
s.add(ry_1_40>=0, ry_1_40<=18)
s.add(ry_1_41>=0, ry_1_41<=18)
s.add(ry_1_42>=0, ry_1_42<=18)
s.add(ry_1_43>=0, ry_1_43<=18)
s.add(ry_1_44>=0, ry_1_44<=18)
s.add(ry_1_45>=0, ry_1_45<=18)
s.add(ry_1_46>=0, ry_1_46<=18)
s.add(ry_1_47>=0, ry_1_47<=18)
s.add(ry_1_48>=0, ry_1_48<=18)
s.add(ry_1_49>=0, ry_1_49<=18)

s.add(obstacle(0,0)==False)
s.add(obstacle(0,1)==False)
s.add(obstacle(0,2)==False)
s.add(obstacle(0,3)==False)
s.add(obstacle(0,4)==False)
s.add(obstacle(0,5)==False)
s.add(obstacle(0,6)==False)
s.add(obstacle(0,7)==False)
s.add(obstacle(0,8)==False)
s.add(obstacle(0,9)==False)
s.add(obstacle(0,10)==False)
s.add(obstacle(0,11)==False)
s.add(obstacle(0,12)==False)
s.add(obstacle(0,13)==False)
s.add(obstacle(0,14)==False)
s.add(obstacle(0,15)==False)
s.add(obstacle(0,16)==False)
s.add(obstacle(0,17)==False)
s.add(obstacle(0,18)==False)
s.add(obstacle(1,0)==False)
s.add(obstacle(1,1)==False)
s.add(obstacle(1,2)==False)
s.add(obstacle(1,3)==False)
s.add(obstacle(1,4)==False)
s.add(obstacle(1,5)==False)
s.add(obstacle(1,6)==False)
s.add(obstacle(1,7)==False)
s.add(obstacle(1,8)==False)
s.add(obstacle(1,9)==False)
s.add(obstacle(1,10)==False)
s.add(obstacle(1,11)==False)
s.add(obstacle(1,12)==False)
s.add(obstacle(1,13)==False)
s.add(obstacle(1,14)==False)
s.add(obstacle(1,15)==False)
s.add(obstacle(1,16)==False)
s.add(obstacle(1,17)==False)
s.add(obstacle(1,18)==False)
s.add(obstacle(2,0)==False)
s.add(obstacle(2,1)==False)
s.add(obstacle(2,2)==True)
s.add(obstacle(2,3)==True)
s.add(obstacle(2,4)==True)
s.add(obstacle(2,5)==False)
s.add(obstacle(2,6)==False)
s.add(obstacle(2,7)==False)
s.add(obstacle(2,8)==True)
s.add(obstacle(2,9)==True)
s.add(obstacle(2,10)==True)
s.add(obstacle(2,11)==False)
s.add(obstacle(2,12)==False)
s.add(obstacle(2,13)==False)
s.add(obstacle(2,14)==True)
s.add(obstacle(2,15)==True)
s.add(obstacle(2,16)==True)
s.add(obstacle(2,17)==False)
s.add(obstacle(2,18)==False)
s.add(obstacle(3,0)==False)
s.add(obstacle(3,1)==False)
s.add(obstacle(3,2)==True)
s.add(obstacle(3,3)==True)
s.add(obstacle(3,4)==True)
s.add(obstacle(3,5)==False)
s.add(obstacle(3,6)==False)
s.add(obstacle(3,7)==False)
s.add(obstacle(3,8)==True)
s.add(obstacle(3,9)==True)
s.add(obstacle(3,10)==True)
s.add(obstacle(3,11)==False)
s.add(obstacle(3,12)==False)
s.add(obstacle(3,13)==False)
s.add(obstacle(3,14)==True)
s.add(obstacle(3,15)==True)
s.add(obstacle(3,16)==True)
s.add(obstacle(3,17)==False)
s.add(obstacle(3,18)==False)
s.add(obstacle(4,0)==False)
s.add(obstacle(4,1)==False)
s.add(obstacle(4,2)==True)
s.add(obstacle(4,3)==True)
s.add(obstacle(4,4)==True)
s.add(obstacle(4,5)==False)
s.add(obstacle(4,6)==False)
s.add(obstacle(4,7)==False)
s.add(obstacle(4,8)==True)
s.add(obstacle(4,9)==True)
s.add(obstacle(4,10)==True)
s.add(obstacle(4,11)==False)
s.add(obstacle(4,12)==False)
s.add(obstacle(4,13)==False)
s.add(obstacle(4,14)==True)
s.add(obstacle(4,15)==True)
s.add(obstacle(4,16)==True)
s.add(obstacle(4,17)==False)
s.add(obstacle(4,18)==False)
s.add(obstacle(5,0)==False)
s.add(obstacle(5,1)==False)
s.add(obstacle(5,2)==True)
s.add(obstacle(5,3)==True)
s.add(obstacle(5,4)==True)
s.add(obstacle(5,5)==False)
s.add(obstacle(5,6)==False)
s.add(obstacle(5,7)==False)
s.add(obstacle(5,8)==True)
s.add(obstacle(5,9)==True)
s.add(obstacle(5,10)==True)
s.add(obstacle(5,11)==False)
s.add(obstacle(5,12)==False)
s.add(obstacle(5,13)==False)
s.add(obstacle(5,14)==True)
s.add(obstacle(5,15)==True)
s.add(obstacle(5,16)==True)
s.add(obstacle(5,17)==False)
s.add(obstacle(5,18)==False)
s.add(obstacle(6,0)==False)
s.add(obstacle(6,1)==False)
s.add(obstacle(6,2)==True)
s.add(obstacle(6,3)==True)
s.add(obstacle(6,4)==True)
s.add(obstacle(6,5)==False)
s.add(obstacle(6,6)==False)
s.add(obstacle(6,7)==False)
s.add(obstacle(6,8)==True)
s.add(obstacle(6,9)==True)
s.add(obstacle(6,10)==True)
s.add(obstacle(6,11)==False)
s.add(obstacle(6,12)==False)
s.add(obstacle(6,13)==False)
s.add(obstacle(6,14)==True)
s.add(obstacle(6,15)==True)
s.add(obstacle(6,16)==True)
s.add(obstacle(6,17)==False)
s.add(obstacle(6,18)==False)
s.add(obstacle(7,0)==False)
s.add(obstacle(7,1)==False)
s.add(obstacle(7,2)==False)
s.add(obstacle(7,3)==False)
s.add(obstacle(7,4)==False)
s.add(obstacle(7,5)==False)
s.add(obstacle(7,6)==False)
s.add(obstacle(7,7)==False)
s.add(obstacle(7,8)==False)
s.add(obstacle(7,9)==False)
s.add(obstacle(7,10)==False)
s.add(obstacle(7,11)==False)
s.add(obstacle(7,12)==False)
s.add(obstacle(7,13)==False)
s.add(obstacle(7,14)==False)
s.add(obstacle(7,15)==False)
s.add(obstacle(7,16)==False)
s.add(obstacle(7,17)==False)
s.add(obstacle(7,18)==False)
s.add(obstacle(8,0)==False)
s.add(obstacle(8,1)==False)
s.add(obstacle(8,2)==False)
s.add(obstacle(8,3)==False)
s.add(obstacle(8,4)==False)
s.add(obstacle(8,5)==False)
s.add(obstacle(8,6)==False)
s.add(obstacle(8,7)==False)
s.add(obstacle(8,8)==False)
s.add(obstacle(8,9)==False)
s.add(obstacle(8,10)==False)
s.add(obstacle(8,11)==False)
s.add(obstacle(8,12)==False)
s.add(obstacle(8,13)==False)
s.add(obstacle(8,14)==False)
s.add(obstacle(8,15)==False)
s.add(obstacle(8,16)==False)
s.add(obstacle(8,17)==False)
s.add(obstacle(8,18)==False)
s.add(obstacle(9,0)==False)
s.add(obstacle(9,1)==False)
s.add(obstacle(9,2)==False)
s.add(obstacle(9,3)==False)
s.add(obstacle(9,4)==False)
s.add(obstacle(9,5)==False)
s.add(obstacle(9,6)==False)
s.add(obstacle(9,7)==False)
s.add(obstacle(9,8)==False)
s.add(obstacle(9,9)==False)
s.add(obstacle(9,10)==False)
s.add(obstacle(9,11)==False)
s.add(obstacle(9,12)==False)
s.add(obstacle(9,13)==False)
s.add(obstacle(9,14)==False)
s.add(obstacle(9,15)==False)
s.add(obstacle(9,16)==False)
s.add(obstacle(9,17)==False)
s.add(obstacle(9,18)==False)
s.add(obstacle(10,0)==False)
s.add(obstacle(10,1)==False)
s.add(obstacle(10,2)==False)
s.add(obstacle(10,3)==False)
s.add(obstacle(10,4)==False)
s.add(obstacle(10,5)==False)
s.add(obstacle(10,6)==False)
s.add(obstacle(10,7)==False)
s.add(obstacle(10,8)==False)
s.add(obstacle(10,9)==False)
s.add(obstacle(10,10)==False)
s.add(obstacle(10,11)==False)
s.add(obstacle(10,12)==False)
s.add(obstacle(10,13)==False)
s.add(obstacle(10,14)==False)
s.add(obstacle(10,15)==False)
s.add(obstacle(10,16)==False)
s.add(obstacle(10,17)==False)
s.add(obstacle(10,18)==False)
s.add(obstacle(11,0)==False)
s.add(obstacle(11,1)==False)
s.add(obstacle(11,2)==False)
s.add(obstacle(11,3)==False)
s.add(obstacle(11,4)==False)
s.add(obstacle(11,5)==False)
s.add(obstacle(11,6)==False)
s.add(obstacle(11,7)==False)
s.add(obstacle(11,8)==False)
s.add(obstacle(11,9)==False)
s.add(obstacle(11,10)==False)
s.add(obstacle(11,11)==False)
s.add(obstacle(11,12)==False)
s.add(obstacle(11,13)==False)
s.add(obstacle(11,14)==False)
s.add(obstacle(11,15)==False)
s.add(obstacle(11,16)==False)
s.add(obstacle(11,17)==False)
s.add(obstacle(11,18)==False)
s.add(obstacle(12,0)==False)
s.add(obstacle(12,1)==False)
s.add(obstacle(12,2)==True)
s.add(obstacle(12,3)==True)
s.add(obstacle(12,4)==True)
s.add(obstacle(12,5)==False)
s.add(obstacle(12,6)==False)
s.add(obstacle(12,7)==False)
s.add(obstacle(12,8)==True)
s.add(obstacle(12,9)==True)
s.add(obstacle(12,10)==True)
s.add(obstacle(12,11)==False)
s.add(obstacle(12,12)==False)
s.add(obstacle(12,13)==False)
s.add(obstacle(12,14)==True)
s.add(obstacle(12,15)==True)
s.add(obstacle(12,16)==True)
s.add(obstacle(12,17)==False)
s.add(obstacle(12,18)==False)
s.add(obstacle(13,0)==False)
s.add(obstacle(13,1)==False)
s.add(obstacle(13,2)==True)
s.add(obstacle(13,3)==True)
s.add(obstacle(13,4)==True)
s.add(obstacle(13,5)==False)
s.add(obstacle(13,6)==False)
s.add(obstacle(13,7)==False)
s.add(obstacle(13,8)==True)
s.add(obstacle(13,9)==True)
s.add(obstacle(13,10)==True)
s.add(obstacle(13,11)==False)
s.add(obstacle(13,12)==False)
s.add(obstacle(13,13)==False)
s.add(obstacle(13,14)==True)
s.add(obstacle(13,15)==True)
s.add(obstacle(13,16)==True)
s.add(obstacle(13,17)==False)
s.add(obstacle(13,18)==False)
s.add(obstacle(14,0)==False)
s.add(obstacle(14,1)==False)
s.add(obstacle(14,2)==True)
s.add(obstacle(14,3)==True)
s.add(obstacle(14,4)==True)
s.add(obstacle(14,5)==False)
s.add(obstacle(14,6)==False)
s.add(obstacle(14,7)==False)
s.add(obstacle(14,8)==True)
s.add(obstacle(14,9)==True)
s.add(obstacle(14,10)==True)
s.add(obstacle(14,11)==False)
s.add(obstacle(14,12)==False)
s.add(obstacle(14,13)==False)
s.add(obstacle(14,14)==True)
s.add(obstacle(14,15)==True)
s.add(obstacle(14,16)==True)
s.add(obstacle(14,17)==False)
s.add(obstacle(14,18)==False)
s.add(obstacle(15,0)==False)
s.add(obstacle(15,1)==False)
s.add(obstacle(15,2)==True)
s.add(obstacle(15,3)==True)
s.add(obstacle(15,4)==True)
s.add(obstacle(15,5)==False)
s.add(obstacle(15,6)==False)
s.add(obstacle(15,7)==False)
s.add(obstacle(15,8)==True)
s.add(obstacle(15,9)==True)
s.add(obstacle(15,10)==True)
s.add(obstacle(15,11)==False)
s.add(obstacle(15,12)==False)
s.add(obstacle(15,13)==False)
s.add(obstacle(15,14)==True)
s.add(obstacle(15,15)==True)
s.add(obstacle(15,16)==True)
s.add(obstacle(15,17)==False)
s.add(obstacle(15,18)==False)
s.add(obstacle(16,0)==False)
s.add(obstacle(16,1)==False)
s.add(obstacle(16,2)==True)
s.add(obstacle(16,3)==True)
s.add(obstacle(16,4)==True)
s.add(obstacle(16,5)==False)
s.add(obstacle(16,6)==False)
s.add(obstacle(16,7)==False)
s.add(obstacle(16,8)==True)
s.add(obstacle(16,9)==True)
s.add(obstacle(16,10)==True)
s.add(obstacle(16,11)==False)
s.add(obstacle(16,12)==False)
s.add(obstacle(16,13)==False)
s.add(obstacle(16,14)==True)
s.add(obstacle(16,15)==True)
s.add(obstacle(16,16)==True)
s.add(obstacle(16,17)==False)
s.add(obstacle(16,18)==False)
s.add(obstacle(17,0)==False)
s.add(obstacle(17,1)==False)
s.add(obstacle(17,2)==False)
s.add(obstacle(17,3)==False)
s.add(obstacle(17,4)==False)
s.add(obstacle(17,5)==False)
s.add(obstacle(17,6)==False)
s.add(obstacle(17,7)==False)
s.add(obstacle(17,8)==False)
s.add(obstacle(17,9)==False)
s.add(obstacle(17,10)==False)
s.add(obstacle(17,11)==False)
s.add(obstacle(17,12)==False)
s.add(obstacle(17,13)==False)
s.add(obstacle(17,14)==False)
s.add(obstacle(17,15)==False)
s.add(obstacle(17,16)==False)
s.add(obstacle(17,17)==False)
s.add(obstacle(17,18)==False)
s.add(obstacle(18,0)==False)
s.add(obstacle(18,1)==False)
s.add(obstacle(18,2)==False)
s.add(obstacle(18,3)==False)
s.add(obstacle(18,4)==False)
s.add(obstacle(18,5)==False)
s.add(obstacle(18,6)==False)
s.add(obstacle(18,7)==False)
s.add(obstacle(18,8)==False)
s.add(obstacle(18,9)==False)
s.add(obstacle(18,10)==False)
s.add(obstacle(18,11)==False)
s.add(obstacle(18,12)==False)
s.add(obstacle(18,13)==False)
s.add(obstacle(18,14)==False)
s.add(obstacle(18,15)==False)
s.add(obstacle(18,16)==False)
s.add(obstacle(18,17)==False)
s.add(obstacle(18,18)==False)

# motion primitives : rechargers
s.add(Or(rprim_1_1!=1,
And(rx_f_1_1==0, ry_f_1_1==0, rcost_1_1==0, 
obstacle(rx_1_1 + 0, ry_1_1 + 0)==False, 
)))
s.add(Or(rprim_1_1!=2,
And(rx_f_1_1==1, ry_f_1_1==0, rcost_1_1==2, 
obstacle(rx_1_1 + 0, ry_1_1 + 0)==False, 
obstacle(rx_1_1 + 1, ry_1_1 + 0)==False, 
)))
s.add(Or(rprim_1_1!=3,
And(rx_f_1_1==0, ry_f_1_1==-1, rcost_1_1==2, 
obstacle(rx_1_1 + 0, ry_1_1 + 0)==False, 
obstacle(rx_1_1 + 0, ry_1_1 + -1)==False, 
)))
s.add(Or(rprim_1_1!=4,
And(rx_f_1_1==-1, ry_f_1_1==0, rcost_1_1==2, 
obstacle(rx_1_1 + 0, ry_1_1 + 0)==False, 
obstacle(rx_1_1 + -1, ry_1_1 + 0)==False, 
)))
s.add(Or(rprim_1_1!=5,
And(rx_f_1_1==0, ry_f_1_1==1, rcost_1_1==2, 
obstacle(rx_1_1 + 0, ry_1_1 + 0)==False, 
obstacle(rx_1_1 + 0, ry_1_1 + 1)==False, 
)))
s.add(Or(rprim_1_1!=6,
And(rx_f_1_1==1, ry_f_1_1==1, rcost_1_1==3, 
obstacle(rx_1_1 + 0, ry_1_1 + 0)==False, 
obstacle(rx_1_1 + 1, ry_1_1 + 1)==False, 
)))
s.add(Or(rprim_1_1!=7,
And(rx_f_1_1==-1, ry_f_1_1==1, rcost_1_1==3, 
obstacle(rx_1_1 + 0, ry_1_1 + 0)==False, 
obstacle(rx_1_1 + -1, ry_1_1 + 1)==False, 
)))
s.add(Or(rprim_1_1!=8,
And(rx_f_1_1==-1, ry_f_1_1==-1, rcost_1_1==3, 
obstacle(rx_1_1 + 0, ry_1_1 + 0)==False, 
obstacle(rx_1_1 + -1, ry_1_1 + -1)==False, 
)))
s.add(Or(rprim_1_1!=9,
And(rx_f_1_1==1, ry_f_1_1==-1, rcost_1_1==3, 
obstacle(rx_1_1 + 0, ry_1_1 + 0)==False, 
obstacle(rx_1_1 + 1, ry_1_1 + -1)==False, 
)))
s.add(Or(rprim_1_1!=10,
And(rx_f_1_1==2, ry_f_1_1==0, rcost_1_1==3, 
obstacle(rx_1_1 + 0, ry_1_1 + 0)==False, 
obstacle(rx_1_1 + 1, ry_1_1 + 0)==False, 
obstacle(rx_1_1 + 2, ry_1_1 + 0)==False, 
)))
s.add(Or(rprim_1_1!=11,
And(rx_f_1_1==0, ry_f_1_1==2, rcost_1_1==3, 
obstacle(rx_1_1 + 0, ry_1_1 + 0)==False, 
obstacle(rx_1_1 + 0, ry_1_1 + 1)==False, 
obstacle(rx_1_1 + 0, ry_1_1 + 2)==False, 
)))
s.add(Or(rprim_1_1!=12,
And(rx_f_1_1==-2, ry_f_1_1==0, rcost_1_1==3, 
obstacle(rx_1_1 + 0, ry_1_1 + 0)==False, 
obstacle(rx_1_1 + -1, ry_1_1 + 0)==False, 
obstacle(rx_1_1 + -2, ry_1_1 + 0)==False, 
)))
s.add(Or(rprim_1_1!=13,
And(rx_f_1_1==0, ry_f_1_1==-2, rcost_1_1==3, 
obstacle(rx_1_1 + 0, ry_1_1 + 0)==False, 
obstacle(rx_1_1 + 0, ry_1_1 + -1)==False, 
obstacle(rx_1_1 + 0, ry_1_1 + -2)==False, 
)))
s.add(Or(rprim_1_1!=14,
And(rx_f_1_1==2, ry_f_1_1==2, rcost_1_1==4, 
obstacle(rx_1_1 + 0, ry_1_1 + 0)==False, 
obstacle(rx_1_1 + 1, ry_1_1 + 1)==False, 
obstacle(rx_1_1 + 2, ry_1_1 + 2)==False, 
)))
s.add(Or(rprim_1_1!=15,
And(rx_f_1_1==-2, ry_f_1_1==2, rcost_1_1==4, 
obstacle(rx_1_1 + 0, ry_1_1 + 0)==False, 
obstacle(rx_1_1 + -1, ry_1_1 + 1)==False, 
obstacle(rx_1_1 + -2, ry_1_1 + 2)==False, 
)))
s.add(Or(rprim_1_1!=16,
And(rx_f_1_1==-2, ry_f_1_1==-2, rcost_1_1==4, 
obstacle(rx_1_1 + 0, ry_1_1 + 0)==False, 
obstacle(rx_1_1 + -1, ry_1_1 + -1)==False, 
obstacle(rx_1_1 + -2, ry_1_1 + -2)==False, 
)))
s.add(Or(rprim_1_1!=17,
And(rx_f_1_1==2, ry_f_1_1==-2, rcost_1_1==4, 
obstacle(rx_1_1 + 0, ry_1_1 + 0)==False, 
obstacle(rx_1_1 + 1, ry_1_1 + -1)==False, 
obstacle(rx_1_1 + 2, ry_1_1 + -2)==False, 
)))
s.add(Or(rprim_1_1!=18,
And(rx_f_1_1==3, ry_f_1_1==0, rcost_1_1==4, 
obstacle(rx_1_1 + 0, ry_1_1 + 0)==False, 
obstacle(rx_1_1 + 1, ry_1_1 + 0)==False, 
obstacle(rx_1_1 + 2, ry_1_1 + 0)==False, 
obstacle(rx_1_1 + 3, ry_1_1 + 0)==False, 
)))
s.add(Or(rprim_1_1!=19,
And(rx_f_1_1==0, ry_f_1_1==3, rcost_1_1==4, 
obstacle(rx_1_1 + 0, ry_1_1 + 0)==False, 
obstacle(rx_1_1 + 0, ry_1_1 + 1)==False, 
obstacle(rx_1_1 + 0, ry_1_1 + 2)==False, 
obstacle(rx_1_1 + 0, ry_1_1 + 3)==False, 
)))
s.add(Or(rprim_1_1!=20,
And(rx_f_1_1==-3, ry_f_1_1==0, rcost_1_1==4, 
obstacle(rx_1_1 + 0, ry_1_1 + 0)==False, 
obstacle(rx_1_1 + -1, ry_1_1 + 0)==False, 
obstacle(rx_1_1 + -2, ry_1_1 + 0)==False, 
obstacle(rx_1_1 + -3, ry_1_1 + 0)==False, 
)))
s.add(Or(rprim_1_1!=21,
And(rx_f_1_1==0, ry_f_1_1==-3, rcost_1_1==4, 
obstacle(rx_1_1 + 0, ry_1_1 + 0)==False, 
obstacle(rx_1_1 + 0, ry_1_1 + -1)==False, 
obstacle(rx_1_1 + 0, ry_1_1 + -2)==False, 
obstacle(rx_1_1 + 0, ry_1_1 + -3)==False, 
)))
s.add(Or(rprim_1_2!=1,
And(rx_f_1_2==0, ry_f_1_2==0, rcost_1_2==0, 
obstacle(rx_1_2 + 0, ry_1_2 + 0)==False, 
)))
s.add(Or(rprim_1_2!=2,
And(rx_f_1_2==1, ry_f_1_2==0, rcost_1_2==2, 
obstacle(rx_1_2 + 0, ry_1_2 + 0)==False, 
obstacle(rx_1_2 + 1, ry_1_2 + 0)==False, 
)))
s.add(Or(rprim_1_2!=3,
And(rx_f_1_2==0, ry_f_1_2==-1, rcost_1_2==2, 
obstacle(rx_1_2 + 0, ry_1_2 + 0)==False, 
obstacle(rx_1_2 + 0, ry_1_2 + -1)==False, 
)))
s.add(Or(rprim_1_2!=4,
And(rx_f_1_2==-1, ry_f_1_2==0, rcost_1_2==2, 
obstacle(rx_1_2 + 0, ry_1_2 + 0)==False, 
obstacle(rx_1_2 + -1, ry_1_2 + 0)==False, 
)))
s.add(Or(rprim_1_2!=5,
And(rx_f_1_2==0, ry_f_1_2==1, rcost_1_2==2, 
obstacle(rx_1_2 + 0, ry_1_2 + 0)==False, 
obstacle(rx_1_2 + 0, ry_1_2 + 1)==False, 
)))
s.add(Or(rprim_1_2!=6,
And(rx_f_1_2==1, ry_f_1_2==1, rcost_1_2==3, 
obstacle(rx_1_2 + 0, ry_1_2 + 0)==False, 
obstacle(rx_1_2 + 1, ry_1_2 + 1)==False, 
)))
s.add(Or(rprim_1_2!=7,
And(rx_f_1_2==-1, ry_f_1_2==1, rcost_1_2==3, 
obstacle(rx_1_2 + 0, ry_1_2 + 0)==False, 
obstacle(rx_1_2 + -1, ry_1_2 + 1)==False, 
)))
s.add(Or(rprim_1_2!=8,
And(rx_f_1_2==-1, ry_f_1_2==-1, rcost_1_2==3, 
obstacle(rx_1_2 + 0, ry_1_2 + 0)==False, 
obstacle(rx_1_2 + -1, ry_1_2 + -1)==False, 
)))
s.add(Or(rprim_1_2!=9,
And(rx_f_1_2==1, ry_f_1_2==-1, rcost_1_2==3, 
obstacle(rx_1_2 + 0, ry_1_2 + 0)==False, 
obstacle(rx_1_2 + 1, ry_1_2 + -1)==False, 
)))
s.add(Or(rprim_1_2!=10,
And(rx_f_1_2==2, ry_f_1_2==0, rcost_1_2==3, 
obstacle(rx_1_2 + 0, ry_1_2 + 0)==False, 
obstacle(rx_1_2 + 1, ry_1_2 + 0)==False, 
obstacle(rx_1_2 + 2, ry_1_2 + 0)==False, 
)))
s.add(Or(rprim_1_2!=11,
And(rx_f_1_2==0, ry_f_1_2==2, rcost_1_2==3, 
obstacle(rx_1_2 + 0, ry_1_2 + 0)==False, 
obstacle(rx_1_2 + 0, ry_1_2 + 1)==False, 
obstacle(rx_1_2 + 0, ry_1_2 + 2)==False, 
)))
s.add(Or(rprim_1_2!=12,
And(rx_f_1_2==-2, ry_f_1_2==0, rcost_1_2==3, 
obstacle(rx_1_2 + 0, ry_1_2 + 0)==False, 
obstacle(rx_1_2 + -1, ry_1_2 + 0)==False, 
obstacle(rx_1_2 + -2, ry_1_2 + 0)==False, 
)))
s.add(Or(rprim_1_2!=13,
And(rx_f_1_2==0, ry_f_1_2==-2, rcost_1_2==3, 
obstacle(rx_1_2 + 0, ry_1_2 + 0)==False, 
obstacle(rx_1_2 + 0, ry_1_2 + -1)==False, 
obstacle(rx_1_2 + 0, ry_1_2 + -2)==False, 
)))
s.add(Or(rprim_1_2!=14,
And(rx_f_1_2==2, ry_f_1_2==2, rcost_1_2==4, 
obstacle(rx_1_2 + 0, ry_1_2 + 0)==False, 
obstacle(rx_1_2 + 1, ry_1_2 + 1)==False, 
obstacle(rx_1_2 + 2, ry_1_2 + 2)==False, 
)))
s.add(Or(rprim_1_2!=15,
And(rx_f_1_2==-2, ry_f_1_2==2, rcost_1_2==4, 
obstacle(rx_1_2 + 0, ry_1_2 + 0)==False, 
obstacle(rx_1_2 + -1, ry_1_2 + 1)==False, 
obstacle(rx_1_2 + -2, ry_1_2 + 2)==False, 
)))
s.add(Or(rprim_1_2!=16,
And(rx_f_1_2==-2, ry_f_1_2==-2, rcost_1_2==4, 
obstacle(rx_1_2 + 0, ry_1_2 + 0)==False, 
obstacle(rx_1_2 + -1, ry_1_2 + -1)==False, 
obstacle(rx_1_2 + -2, ry_1_2 + -2)==False, 
)))
s.add(Or(rprim_1_2!=17,
And(rx_f_1_2==2, ry_f_1_2==-2, rcost_1_2==4, 
obstacle(rx_1_2 + 0, ry_1_2 + 0)==False, 
obstacle(rx_1_2 + 1, ry_1_2 + -1)==False, 
obstacle(rx_1_2 + 2, ry_1_2 + -2)==False, 
)))
s.add(Or(rprim_1_2!=18,
And(rx_f_1_2==3, ry_f_1_2==0, rcost_1_2==4, 
obstacle(rx_1_2 + 0, ry_1_2 + 0)==False, 
obstacle(rx_1_2 + 1, ry_1_2 + 0)==False, 
obstacle(rx_1_2 + 2, ry_1_2 + 0)==False, 
obstacle(rx_1_2 + 3, ry_1_2 + 0)==False, 
)))
s.add(Or(rprim_1_2!=19,
And(rx_f_1_2==0, ry_f_1_2==3, rcost_1_2==4, 
obstacle(rx_1_2 + 0, ry_1_2 + 0)==False, 
obstacle(rx_1_2 + 0, ry_1_2 + 1)==False, 
obstacle(rx_1_2 + 0, ry_1_2 + 2)==False, 
obstacle(rx_1_2 + 0, ry_1_2 + 3)==False, 
)))
s.add(Or(rprim_1_2!=20,
And(rx_f_1_2==-3, ry_f_1_2==0, rcost_1_2==4, 
obstacle(rx_1_2 + 0, ry_1_2 + 0)==False, 
obstacle(rx_1_2 + -1, ry_1_2 + 0)==False, 
obstacle(rx_1_2 + -2, ry_1_2 + 0)==False, 
obstacle(rx_1_2 + -3, ry_1_2 + 0)==False, 
)))
s.add(Or(rprim_1_2!=21,
And(rx_f_1_2==0, ry_f_1_2==-3, rcost_1_2==4, 
obstacle(rx_1_2 + 0, ry_1_2 + 0)==False, 
obstacle(rx_1_2 + 0, ry_1_2 + -1)==False, 
obstacle(rx_1_2 + 0, ry_1_2 + -2)==False, 
obstacle(rx_1_2 + 0, ry_1_2 + -3)==False, 
)))
s.add(Or(rprim_1_3!=1,
And(rx_f_1_3==0, ry_f_1_3==0, rcost_1_3==0, 
obstacle(rx_1_3 + 0, ry_1_3 + 0)==False, 
)))
s.add(Or(rprim_1_3!=2,
And(rx_f_1_3==1, ry_f_1_3==0, rcost_1_3==2, 
obstacle(rx_1_3 + 0, ry_1_3 + 0)==False, 
obstacle(rx_1_3 + 1, ry_1_3 + 0)==False, 
)))
s.add(Or(rprim_1_3!=3,
And(rx_f_1_3==0, ry_f_1_3==-1, rcost_1_3==2, 
obstacle(rx_1_3 + 0, ry_1_3 + 0)==False, 
obstacle(rx_1_3 + 0, ry_1_3 + -1)==False, 
)))
s.add(Or(rprim_1_3!=4,
And(rx_f_1_3==-1, ry_f_1_3==0, rcost_1_3==2, 
obstacle(rx_1_3 + 0, ry_1_3 + 0)==False, 
obstacle(rx_1_3 + -1, ry_1_3 + 0)==False, 
)))
s.add(Or(rprim_1_3!=5,
And(rx_f_1_3==0, ry_f_1_3==1, rcost_1_3==2, 
obstacle(rx_1_3 + 0, ry_1_3 + 0)==False, 
obstacle(rx_1_3 + 0, ry_1_3 + 1)==False, 
)))
s.add(Or(rprim_1_3!=6,
And(rx_f_1_3==1, ry_f_1_3==1, rcost_1_3==3, 
obstacle(rx_1_3 + 0, ry_1_3 + 0)==False, 
obstacle(rx_1_3 + 1, ry_1_3 + 1)==False, 
)))
s.add(Or(rprim_1_3!=7,
And(rx_f_1_3==-1, ry_f_1_3==1, rcost_1_3==3, 
obstacle(rx_1_3 + 0, ry_1_3 + 0)==False, 
obstacle(rx_1_3 + -1, ry_1_3 + 1)==False, 
)))
s.add(Or(rprim_1_3!=8,
And(rx_f_1_3==-1, ry_f_1_3==-1, rcost_1_3==3, 
obstacle(rx_1_3 + 0, ry_1_3 + 0)==False, 
obstacle(rx_1_3 + -1, ry_1_3 + -1)==False, 
)))
s.add(Or(rprim_1_3!=9,
And(rx_f_1_3==1, ry_f_1_3==-1, rcost_1_3==3, 
obstacle(rx_1_3 + 0, ry_1_3 + 0)==False, 
obstacle(rx_1_3 + 1, ry_1_3 + -1)==False, 
)))
s.add(Or(rprim_1_3!=10,
And(rx_f_1_3==2, ry_f_1_3==0, rcost_1_3==3, 
obstacle(rx_1_3 + 0, ry_1_3 + 0)==False, 
obstacle(rx_1_3 + 1, ry_1_3 + 0)==False, 
obstacle(rx_1_3 + 2, ry_1_3 + 0)==False, 
)))
s.add(Or(rprim_1_3!=11,
And(rx_f_1_3==0, ry_f_1_3==2, rcost_1_3==3, 
obstacle(rx_1_3 + 0, ry_1_3 + 0)==False, 
obstacle(rx_1_3 + 0, ry_1_3 + 1)==False, 
obstacle(rx_1_3 + 0, ry_1_3 + 2)==False, 
)))
s.add(Or(rprim_1_3!=12,
And(rx_f_1_3==-2, ry_f_1_3==0, rcost_1_3==3, 
obstacle(rx_1_3 + 0, ry_1_3 + 0)==False, 
obstacle(rx_1_3 + -1, ry_1_3 + 0)==False, 
obstacle(rx_1_3 + -2, ry_1_3 + 0)==False, 
)))
s.add(Or(rprim_1_3!=13,
And(rx_f_1_3==0, ry_f_1_3==-2, rcost_1_3==3, 
obstacle(rx_1_3 + 0, ry_1_3 + 0)==False, 
obstacle(rx_1_3 + 0, ry_1_3 + -1)==False, 
obstacle(rx_1_3 + 0, ry_1_3 + -2)==False, 
)))
s.add(Or(rprim_1_3!=14,
And(rx_f_1_3==2, ry_f_1_3==2, rcost_1_3==4, 
obstacle(rx_1_3 + 0, ry_1_3 + 0)==False, 
obstacle(rx_1_3 + 1, ry_1_3 + 1)==False, 
obstacle(rx_1_3 + 2, ry_1_3 + 2)==False, 
)))
s.add(Or(rprim_1_3!=15,
And(rx_f_1_3==-2, ry_f_1_3==2, rcost_1_3==4, 
obstacle(rx_1_3 + 0, ry_1_3 + 0)==False, 
obstacle(rx_1_3 + -1, ry_1_3 + 1)==False, 
obstacle(rx_1_3 + -2, ry_1_3 + 2)==False, 
)))
s.add(Or(rprim_1_3!=16,
And(rx_f_1_3==-2, ry_f_1_3==-2, rcost_1_3==4, 
obstacle(rx_1_3 + 0, ry_1_3 + 0)==False, 
obstacle(rx_1_3 + -1, ry_1_3 + -1)==False, 
obstacle(rx_1_3 + -2, ry_1_3 + -2)==False, 
)))
s.add(Or(rprim_1_3!=17,
And(rx_f_1_3==2, ry_f_1_3==-2, rcost_1_3==4, 
obstacle(rx_1_3 + 0, ry_1_3 + 0)==False, 
obstacle(rx_1_3 + 1, ry_1_3 + -1)==False, 
obstacle(rx_1_3 + 2, ry_1_3 + -2)==False, 
)))
s.add(Or(rprim_1_3!=18,
And(rx_f_1_3==3, ry_f_1_3==0, rcost_1_3==4, 
obstacle(rx_1_3 + 0, ry_1_3 + 0)==False, 
obstacle(rx_1_3 + 1, ry_1_3 + 0)==False, 
obstacle(rx_1_3 + 2, ry_1_3 + 0)==False, 
obstacle(rx_1_3 + 3, ry_1_3 + 0)==False, 
)))
s.add(Or(rprim_1_3!=19,
And(rx_f_1_3==0, ry_f_1_3==3, rcost_1_3==4, 
obstacle(rx_1_3 + 0, ry_1_3 + 0)==False, 
obstacle(rx_1_3 + 0, ry_1_3 + 1)==False, 
obstacle(rx_1_3 + 0, ry_1_3 + 2)==False, 
obstacle(rx_1_3 + 0, ry_1_3 + 3)==False, 
)))
s.add(Or(rprim_1_3!=20,
And(rx_f_1_3==-3, ry_f_1_3==0, rcost_1_3==4, 
obstacle(rx_1_3 + 0, ry_1_3 + 0)==False, 
obstacle(rx_1_3 + -1, ry_1_3 + 0)==False, 
obstacle(rx_1_3 + -2, ry_1_3 + 0)==False, 
obstacle(rx_1_3 + -3, ry_1_3 + 0)==False, 
)))
s.add(Or(rprim_1_3!=21,
And(rx_f_1_3==0, ry_f_1_3==-3, rcost_1_3==4, 
obstacle(rx_1_3 + 0, ry_1_3 + 0)==False, 
obstacle(rx_1_3 + 0, ry_1_3 + -1)==False, 
obstacle(rx_1_3 + 0, ry_1_3 + -2)==False, 
obstacle(rx_1_3 + 0, ry_1_3 + -3)==False, 
)))
s.add(Or(rprim_1_4!=1,
And(rx_f_1_4==0, ry_f_1_4==0, rcost_1_4==0, 
obstacle(rx_1_4 + 0, ry_1_4 + 0)==False, 
)))
s.add(Or(rprim_1_4!=2,
And(rx_f_1_4==1, ry_f_1_4==0, rcost_1_4==2, 
obstacle(rx_1_4 + 0, ry_1_4 + 0)==False, 
obstacle(rx_1_4 + 1, ry_1_4 + 0)==False, 
)))
s.add(Or(rprim_1_4!=3,
And(rx_f_1_4==0, ry_f_1_4==-1, rcost_1_4==2, 
obstacle(rx_1_4 + 0, ry_1_4 + 0)==False, 
obstacle(rx_1_4 + 0, ry_1_4 + -1)==False, 
)))
s.add(Or(rprim_1_4!=4,
And(rx_f_1_4==-1, ry_f_1_4==0, rcost_1_4==2, 
obstacle(rx_1_4 + 0, ry_1_4 + 0)==False, 
obstacle(rx_1_4 + -1, ry_1_4 + 0)==False, 
)))
s.add(Or(rprim_1_4!=5,
And(rx_f_1_4==0, ry_f_1_4==1, rcost_1_4==2, 
obstacle(rx_1_4 + 0, ry_1_4 + 0)==False, 
obstacle(rx_1_4 + 0, ry_1_4 + 1)==False, 
)))
s.add(Or(rprim_1_4!=6,
And(rx_f_1_4==1, ry_f_1_4==1, rcost_1_4==3, 
obstacle(rx_1_4 + 0, ry_1_4 + 0)==False, 
obstacle(rx_1_4 + 1, ry_1_4 + 1)==False, 
)))
s.add(Or(rprim_1_4!=7,
And(rx_f_1_4==-1, ry_f_1_4==1, rcost_1_4==3, 
obstacle(rx_1_4 + 0, ry_1_4 + 0)==False, 
obstacle(rx_1_4 + -1, ry_1_4 + 1)==False, 
)))
s.add(Or(rprim_1_4!=8,
And(rx_f_1_4==-1, ry_f_1_4==-1, rcost_1_4==3, 
obstacle(rx_1_4 + 0, ry_1_4 + 0)==False, 
obstacle(rx_1_4 + -1, ry_1_4 + -1)==False, 
)))
s.add(Or(rprim_1_4!=9,
And(rx_f_1_4==1, ry_f_1_4==-1, rcost_1_4==3, 
obstacle(rx_1_4 + 0, ry_1_4 + 0)==False, 
obstacle(rx_1_4 + 1, ry_1_4 + -1)==False, 
)))
s.add(Or(rprim_1_4!=10,
And(rx_f_1_4==2, ry_f_1_4==0, rcost_1_4==3, 
obstacle(rx_1_4 + 0, ry_1_4 + 0)==False, 
obstacle(rx_1_4 + 1, ry_1_4 + 0)==False, 
obstacle(rx_1_4 + 2, ry_1_4 + 0)==False, 
)))
s.add(Or(rprim_1_4!=11,
And(rx_f_1_4==0, ry_f_1_4==2, rcost_1_4==3, 
obstacle(rx_1_4 + 0, ry_1_4 + 0)==False, 
obstacle(rx_1_4 + 0, ry_1_4 + 1)==False, 
obstacle(rx_1_4 + 0, ry_1_4 + 2)==False, 
)))
s.add(Or(rprim_1_4!=12,
And(rx_f_1_4==-2, ry_f_1_4==0, rcost_1_4==3, 
obstacle(rx_1_4 + 0, ry_1_4 + 0)==False, 
obstacle(rx_1_4 + -1, ry_1_4 + 0)==False, 
obstacle(rx_1_4 + -2, ry_1_4 + 0)==False, 
)))
s.add(Or(rprim_1_4!=13,
And(rx_f_1_4==0, ry_f_1_4==-2, rcost_1_4==3, 
obstacle(rx_1_4 + 0, ry_1_4 + 0)==False, 
obstacle(rx_1_4 + 0, ry_1_4 + -1)==False, 
obstacle(rx_1_4 + 0, ry_1_4 + -2)==False, 
)))
s.add(Or(rprim_1_4!=14,
And(rx_f_1_4==2, ry_f_1_4==2, rcost_1_4==4, 
obstacle(rx_1_4 + 0, ry_1_4 + 0)==False, 
obstacle(rx_1_4 + 1, ry_1_4 + 1)==False, 
obstacle(rx_1_4 + 2, ry_1_4 + 2)==False, 
)))
s.add(Or(rprim_1_4!=15,
And(rx_f_1_4==-2, ry_f_1_4==2, rcost_1_4==4, 
obstacle(rx_1_4 + 0, ry_1_4 + 0)==False, 
obstacle(rx_1_4 + -1, ry_1_4 + 1)==False, 
obstacle(rx_1_4 + -2, ry_1_4 + 2)==False, 
)))
s.add(Or(rprim_1_4!=16,
And(rx_f_1_4==-2, ry_f_1_4==-2, rcost_1_4==4, 
obstacle(rx_1_4 + 0, ry_1_4 + 0)==False, 
obstacle(rx_1_4 + -1, ry_1_4 + -1)==False, 
obstacle(rx_1_4 + -2, ry_1_4 + -2)==False, 
)))
s.add(Or(rprim_1_4!=17,
And(rx_f_1_4==2, ry_f_1_4==-2, rcost_1_4==4, 
obstacle(rx_1_4 + 0, ry_1_4 + 0)==False, 
obstacle(rx_1_4 + 1, ry_1_4 + -1)==False, 
obstacle(rx_1_4 + 2, ry_1_4 + -2)==False, 
)))
s.add(Or(rprim_1_4!=18,
And(rx_f_1_4==3, ry_f_1_4==0, rcost_1_4==4, 
obstacle(rx_1_4 + 0, ry_1_4 + 0)==False, 
obstacle(rx_1_4 + 1, ry_1_4 + 0)==False, 
obstacle(rx_1_4 + 2, ry_1_4 + 0)==False, 
obstacle(rx_1_4 + 3, ry_1_4 + 0)==False, 
)))
s.add(Or(rprim_1_4!=19,
And(rx_f_1_4==0, ry_f_1_4==3, rcost_1_4==4, 
obstacle(rx_1_4 + 0, ry_1_4 + 0)==False, 
obstacle(rx_1_4 + 0, ry_1_4 + 1)==False, 
obstacle(rx_1_4 + 0, ry_1_4 + 2)==False, 
obstacle(rx_1_4 + 0, ry_1_4 + 3)==False, 
)))
s.add(Or(rprim_1_4!=20,
And(rx_f_1_4==-3, ry_f_1_4==0, rcost_1_4==4, 
obstacle(rx_1_4 + 0, ry_1_4 + 0)==False, 
obstacle(rx_1_4 + -1, ry_1_4 + 0)==False, 
obstacle(rx_1_4 + -2, ry_1_4 + 0)==False, 
obstacle(rx_1_4 + -3, ry_1_4 + 0)==False, 
)))
s.add(Or(rprim_1_4!=21,
And(rx_f_1_4==0, ry_f_1_4==-3, rcost_1_4==4, 
obstacle(rx_1_4 + 0, ry_1_4 + 0)==False, 
obstacle(rx_1_4 + 0, ry_1_4 + -1)==False, 
obstacle(rx_1_4 + 0, ry_1_4 + -2)==False, 
obstacle(rx_1_4 + 0, ry_1_4 + -3)==False, 
)))
s.add(Or(rprim_1_5!=1,
And(rx_f_1_5==0, ry_f_1_5==0, rcost_1_5==0, 
obstacle(rx_1_5 + 0, ry_1_5 + 0)==False, 
)))
s.add(Or(rprim_1_5!=2,
And(rx_f_1_5==1, ry_f_1_5==0, rcost_1_5==2, 
obstacle(rx_1_5 + 0, ry_1_5 + 0)==False, 
obstacle(rx_1_5 + 1, ry_1_5 + 0)==False, 
)))
s.add(Or(rprim_1_5!=3,
And(rx_f_1_5==0, ry_f_1_5==-1, rcost_1_5==2, 
obstacle(rx_1_5 + 0, ry_1_5 + 0)==False, 
obstacle(rx_1_5 + 0, ry_1_5 + -1)==False, 
)))
s.add(Or(rprim_1_5!=4,
And(rx_f_1_5==-1, ry_f_1_5==0, rcost_1_5==2, 
obstacle(rx_1_5 + 0, ry_1_5 + 0)==False, 
obstacle(rx_1_5 + -1, ry_1_5 + 0)==False, 
)))
s.add(Or(rprim_1_5!=5,
And(rx_f_1_5==0, ry_f_1_5==1, rcost_1_5==2, 
obstacle(rx_1_5 + 0, ry_1_5 + 0)==False, 
obstacle(rx_1_5 + 0, ry_1_5 + 1)==False, 
)))
s.add(Or(rprim_1_5!=6,
And(rx_f_1_5==1, ry_f_1_5==1, rcost_1_5==3, 
obstacle(rx_1_5 + 0, ry_1_5 + 0)==False, 
obstacle(rx_1_5 + 1, ry_1_5 + 1)==False, 
)))
s.add(Or(rprim_1_5!=7,
And(rx_f_1_5==-1, ry_f_1_5==1, rcost_1_5==3, 
obstacle(rx_1_5 + 0, ry_1_5 + 0)==False, 
obstacle(rx_1_5 + -1, ry_1_5 + 1)==False, 
)))
s.add(Or(rprim_1_5!=8,
And(rx_f_1_5==-1, ry_f_1_5==-1, rcost_1_5==3, 
obstacle(rx_1_5 + 0, ry_1_5 + 0)==False, 
obstacle(rx_1_5 + -1, ry_1_5 + -1)==False, 
)))
s.add(Or(rprim_1_5!=9,
And(rx_f_1_5==1, ry_f_1_5==-1, rcost_1_5==3, 
obstacle(rx_1_5 + 0, ry_1_5 + 0)==False, 
obstacle(rx_1_5 + 1, ry_1_5 + -1)==False, 
)))
s.add(Or(rprim_1_5!=10,
And(rx_f_1_5==2, ry_f_1_5==0, rcost_1_5==3, 
obstacle(rx_1_5 + 0, ry_1_5 + 0)==False, 
obstacle(rx_1_5 + 1, ry_1_5 + 0)==False, 
obstacle(rx_1_5 + 2, ry_1_5 + 0)==False, 
)))
s.add(Or(rprim_1_5!=11,
And(rx_f_1_5==0, ry_f_1_5==2, rcost_1_5==3, 
obstacle(rx_1_5 + 0, ry_1_5 + 0)==False, 
obstacle(rx_1_5 + 0, ry_1_5 + 1)==False, 
obstacle(rx_1_5 + 0, ry_1_5 + 2)==False, 
)))
s.add(Or(rprim_1_5!=12,
And(rx_f_1_5==-2, ry_f_1_5==0, rcost_1_5==3, 
obstacle(rx_1_5 + 0, ry_1_5 + 0)==False, 
obstacle(rx_1_5 + -1, ry_1_5 + 0)==False, 
obstacle(rx_1_5 + -2, ry_1_5 + 0)==False, 
)))
s.add(Or(rprim_1_5!=13,
And(rx_f_1_5==0, ry_f_1_5==-2, rcost_1_5==3, 
obstacle(rx_1_5 + 0, ry_1_5 + 0)==False, 
obstacle(rx_1_5 + 0, ry_1_5 + -1)==False, 
obstacle(rx_1_5 + 0, ry_1_5 + -2)==False, 
)))
s.add(Or(rprim_1_5!=14,
And(rx_f_1_5==2, ry_f_1_5==2, rcost_1_5==4, 
obstacle(rx_1_5 + 0, ry_1_5 + 0)==False, 
obstacle(rx_1_5 + 1, ry_1_5 + 1)==False, 
obstacle(rx_1_5 + 2, ry_1_5 + 2)==False, 
)))
s.add(Or(rprim_1_5!=15,
And(rx_f_1_5==-2, ry_f_1_5==2, rcost_1_5==4, 
obstacle(rx_1_5 + 0, ry_1_5 + 0)==False, 
obstacle(rx_1_5 + -1, ry_1_5 + 1)==False, 
obstacle(rx_1_5 + -2, ry_1_5 + 2)==False, 
)))
s.add(Or(rprim_1_5!=16,
And(rx_f_1_5==-2, ry_f_1_5==-2, rcost_1_5==4, 
obstacle(rx_1_5 + 0, ry_1_5 + 0)==False, 
obstacle(rx_1_5 + -1, ry_1_5 + -1)==False, 
obstacle(rx_1_5 + -2, ry_1_5 + -2)==False, 
)))
s.add(Or(rprim_1_5!=17,
And(rx_f_1_5==2, ry_f_1_5==-2, rcost_1_5==4, 
obstacle(rx_1_5 + 0, ry_1_5 + 0)==False, 
obstacle(rx_1_5 + 1, ry_1_5 + -1)==False, 
obstacle(rx_1_5 + 2, ry_1_5 + -2)==False, 
)))
s.add(Or(rprim_1_5!=18,
And(rx_f_1_5==3, ry_f_1_5==0, rcost_1_5==4, 
obstacle(rx_1_5 + 0, ry_1_5 + 0)==False, 
obstacle(rx_1_5 + 1, ry_1_5 + 0)==False, 
obstacle(rx_1_5 + 2, ry_1_5 + 0)==False, 
obstacle(rx_1_5 + 3, ry_1_5 + 0)==False, 
)))
s.add(Or(rprim_1_5!=19,
And(rx_f_1_5==0, ry_f_1_5==3, rcost_1_5==4, 
obstacle(rx_1_5 + 0, ry_1_5 + 0)==False, 
obstacle(rx_1_5 + 0, ry_1_5 + 1)==False, 
obstacle(rx_1_5 + 0, ry_1_5 + 2)==False, 
obstacle(rx_1_5 + 0, ry_1_5 + 3)==False, 
)))
s.add(Or(rprim_1_5!=20,
And(rx_f_1_5==-3, ry_f_1_5==0, rcost_1_5==4, 
obstacle(rx_1_5 + 0, ry_1_5 + 0)==False, 
obstacle(rx_1_5 + -1, ry_1_5 + 0)==False, 
obstacle(rx_1_5 + -2, ry_1_5 + 0)==False, 
obstacle(rx_1_5 + -3, ry_1_5 + 0)==False, 
)))
s.add(Or(rprim_1_5!=21,
And(rx_f_1_5==0, ry_f_1_5==-3, rcost_1_5==4, 
obstacle(rx_1_5 + 0, ry_1_5 + 0)==False, 
obstacle(rx_1_5 + 0, ry_1_5 + -1)==False, 
obstacle(rx_1_5 + 0, ry_1_5 + -2)==False, 
obstacle(rx_1_5 + 0, ry_1_5 + -3)==False, 
)))
s.add(Or(rprim_1_6!=1,
And(rx_f_1_6==0, ry_f_1_6==0, rcost_1_6==0, 
obstacle(rx_1_6 + 0, ry_1_6 + 0)==False, 
)))
s.add(Or(rprim_1_6!=2,
And(rx_f_1_6==1, ry_f_1_6==0, rcost_1_6==2, 
obstacle(rx_1_6 + 0, ry_1_6 + 0)==False, 
obstacle(rx_1_6 + 1, ry_1_6 + 0)==False, 
)))
s.add(Or(rprim_1_6!=3,
And(rx_f_1_6==0, ry_f_1_6==-1, rcost_1_6==2, 
obstacle(rx_1_6 + 0, ry_1_6 + 0)==False, 
obstacle(rx_1_6 + 0, ry_1_6 + -1)==False, 
)))
s.add(Or(rprim_1_6!=4,
And(rx_f_1_6==-1, ry_f_1_6==0, rcost_1_6==2, 
obstacle(rx_1_6 + 0, ry_1_6 + 0)==False, 
obstacle(rx_1_6 + -1, ry_1_6 + 0)==False, 
)))
s.add(Or(rprim_1_6!=5,
And(rx_f_1_6==0, ry_f_1_6==1, rcost_1_6==2, 
obstacle(rx_1_6 + 0, ry_1_6 + 0)==False, 
obstacle(rx_1_6 + 0, ry_1_6 + 1)==False, 
)))
s.add(Or(rprim_1_6!=6,
And(rx_f_1_6==1, ry_f_1_6==1, rcost_1_6==3, 
obstacle(rx_1_6 + 0, ry_1_6 + 0)==False, 
obstacle(rx_1_6 + 1, ry_1_6 + 1)==False, 
)))
s.add(Or(rprim_1_6!=7,
And(rx_f_1_6==-1, ry_f_1_6==1, rcost_1_6==3, 
obstacle(rx_1_6 + 0, ry_1_6 + 0)==False, 
obstacle(rx_1_6 + -1, ry_1_6 + 1)==False, 
)))
s.add(Or(rprim_1_6!=8,
And(rx_f_1_6==-1, ry_f_1_6==-1, rcost_1_6==3, 
obstacle(rx_1_6 + 0, ry_1_6 + 0)==False, 
obstacle(rx_1_6 + -1, ry_1_6 + -1)==False, 
)))
s.add(Or(rprim_1_6!=9,
And(rx_f_1_6==1, ry_f_1_6==-1, rcost_1_6==3, 
obstacle(rx_1_6 + 0, ry_1_6 + 0)==False, 
obstacle(rx_1_6 + 1, ry_1_6 + -1)==False, 
)))
s.add(Or(rprim_1_6!=10,
And(rx_f_1_6==2, ry_f_1_6==0, rcost_1_6==3, 
obstacle(rx_1_6 + 0, ry_1_6 + 0)==False, 
obstacle(rx_1_6 + 1, ry_1_6 + 0)==False, 
obstacle(rx_1_6 + 2, ry_1_6 + 0)==False, 
)))
s.add(Or(rprim_1_6!=11,
And(rx_f_1_6==0, ry_f_1_6==2, rcost_1_6==3, 
obstacle(rx_1_6 + 0, ry_1_6 + 0)==False, 
obstacle(rx_1_6 + 0, ry_1_6 + 1)==False, 
obstacle(rx_1_6 + 0, ry_1_6 + 2)==False, 
)))
s.add(Or(rprim_1_6!=12,
And(rx_f_1_6==-2, ry_f_1_6==0, rcost_1_6==3, 
obstacle(rx_1_6 + 0, ry_1_6 + 0)==False, 
obstacle(rx_1_6 + -1, ry_1_6 + 0)==False, 
obstacle(rx_1_6 + -2, ry_1_6 + 0)==False, 
)))
s.add(Or(rprim_1_6!=13,
And(rx_f_1_6==0, ry_f_1_6==-2, rcost_1_6==3, 
obstacle(rx_1_6 + 0, ry_1_6 + 0)==False, 
obstacle(rx_1_6 + 0, ry_1_6 + -1)==False, 
obstacle(rx_1_6 + 0, ry_1_6 + -2)==False, 
)))
s.add(Or(rprim_1_6!=14,
And(rx_f_1_6==2, ry_f_1_6==2, rcost_1_6==4, 
obstacle(rx_1_6 + 0, ry_1_6 + 0)==False, 
obstacle(rx_1_6 + 1, ry_1_6 + 1)==False, 
obstacle(rx_1_6 + 2, ry_1_6 + 2)==False, 
)))
s.add(Or(rprim_1_6!=15,
And(rx_f_1_6==-2, ry_f_1_6==2, rcost_1_6==4, 
obstacle(rx_1_6 + 0, ry_1_6 + 0)==False, 
obstacle(rx_1_6 + -1, ry_1_6 + 1)==False, 
obstacle(rx_1_6 + -2, ry_1_6 + 2)==False, 
)))
s.add(Or(rprim_1_6!=16,
And(rx_f_1_6==-2, ry_f_1_6==-2, rcost_1_6==4, 
obstacle(rx_1_6 + 0, ry_1_6 + 0)==False, 
obstacle(rx_1_6 + -1, ry_1_6 + -1)==False, 
obstacle(rx_1_6 + -2, ry_1_6 + -2)==False, 
)))
s.add(Or(rprim_1_6!=17,
And(rx_f_1_6==2, ry_f_1_6==-2, rcost_1_6==4, 
obstacle(rx_1_6 + 0, ry_1_6 + 0)==False, 
obstacle(rx_1_6 + 1, ry_1_6 + -1)==False, 
obstacle(rx_1_6 + 2, ry_1_6 + -2)==False, 
)))
s.add(Or(rprim_1_6!=18,
And(rx_f_1_6==3, ry_f_1_6==0, rcost_1_6==4, 
obstacle(rx_1_6 + 0, ry_1_6 + 0)==False, 
obstacle(rx_1_6 + 1, ry_1_6 + 0)==False, 
obstacle(rx_1_6 + 2, ry_1_6 + 0)==False, 
obstacle(rx_1_6 + 3, ry_1_6 + 0)==False, 
)))
s.add(Or(rprim_1_6!=19,
And(rx_f_1_6==0, ry_f_1_6==3, rcost_1_6==4, 
obstacle(rx_1_6 + 0, ry_1_6 + 0)==False, 
obstacle(rx_1_6 + 0, ry_1_6 + 1)==False, 
obstacle(rx_1_6 + 0, ry_1_6 + 2)==False, 
obstacle(rx_1_6 + 0, ry_1_6 + 3)==False, 
)))
s.add(Or(rprim_1_6!=20,
And(rx_f_1_6==-3, ry_f_1_6==0, rcost_1_6==4, 
obstacle(rx_1_6 + 0, ry_1_6 + 0)==False, 
obstacle(rx_1_6 + -1, ry_1_6 + 0)==False, 
obstacle(rx_1_6 + -2, ry_1_6 + 0)==False, 
obstacle(rx_1_6 + -3, ry_1_6 + 0)==False, 
)))
s.add(Or(rprim_1_6!=21,
And(rx_f_1_6==0, ry_f_1_6==-3, rcost_1_6==4, 
obstacle(rx_1_6 + 0, ry_1_6 + 0)==False, 
obstacle(rx_1_6 + 0, ry_1_6 + -1)==False, 
obstacle(rx_1_6 + 0, ry_1_6 + -2)==False, 
obstacle(rx_1_6 + 0, ry_1_6 + -3)==False, 
)))
s.add(Or(rprim_1_7!=1,
And(rx_f_1_7==0, ry_f_1_7==0, rcost_1_7==0, 
obstacle(rx_1_7 + 0, ry_1_7 + 0)==False, 
)))
s.add(Or(rprim_1_7!=2,
And(rx_f_1_7==1, ry_f_1_7==0, rcost_1_7==2, 
obstacle(rx_1_7 + 0, ry_1_7 + 0)==False, 
obstacle(rx_1_7 + 1, ry_1_7 + 0)==False, 
)))
s.add(Or(rprim_1_7!=3,
And(rx_f_1_7==0, ry_f_1_7==-1, rcost_1_7==2, 
obstacle(rx_1_7 + 0, ry_1_7 + 0)==False, 
obstacle(rx_1_7 + 0, ry_1_7 + -1)==False, 
)))
s.add(Or(rprim_1_7!=4,
And(rx_f_1_7==-1, ry_f_1_7==0, rcost_1_7==2, 
obstacle(rx_1_7 + 0, ry_1_7 + 0)==False, 
obstacle(rx_1_7 + -1, ry_1_7 + 0)==False, 
)))
s.add(Or(rprim_1_7!=5,
And(rx_f_1_7==0, ry_f_1_7==1, rcost_1_7==2, 
obstacle(rx_1_7 + 0, ry_1_7 + 0)==False, 
obstacle(rx_1_7 + 0, ry_1_7 + 1)==False, 
)))
s.add(Or(rprim_1_7!=6,
And(rx_f_1_7==1, ry_f_1_7==1, rcost_1_7==3, 
obstacle(rx_1_7 + 0, ry_1_7 + 0)==False, 
obstacle(rx_1_7 + 1, ry_1_7 + 1)==False, 
)))
s.add(Or(rprim_1_7!=7,
And(rx_f_1_7==-1, ry_f_1_7==1, rcost_1_7==3, 
obstacle(rx_1_7 + 0, ry_1_7 + 0)==False, 
obstacle(rx_1_7 + -1, ry_1_7 + 1)==False, 
)))
s.add(Or(rprim_1_7!=8,
And(rx_f_1_7==-1, ry_f_1_7==-1, rcost_1_7==3, 
obstacle(rx_1_7 + 0, ry_1_7 + 0)==False, 
obstacle(rx_1_7 + -1, ry_1_7 + -1)==False, 
)))
s.add(Or(rprim_1_7!=9,
And(rx_f_1_7==1, ry_f_1_7==-1, rcost_1_7==3, 
obstacle(rx_1_7 + 0, ry_1_7 + 0)==False, 
obstacle(rx_1_7 + 1, ry_1_7 + -1)==False, 
)))
s.add(Or(rprim_1_7!=10,
And(rx_f_1_7==2, ry_f_1_7==0, rcost_1_7==3, 
obstacle(rx_1_7 + 0, ry_1_7 + 0)==False, 
obstacle(rx_1_7 + 1, ry_1_7 + 0)==False, 
obstacle(rx_1_7 + 2, ry_1_7 + 0)==False, 
)))
s.add(Or(rprim_1_7!=11,
And(rx_f_1_7==0, ry_f_1_7==2, rcost_1_7==3, 
obstacle(rx_1_7 + 0, ry_1_7 + 0)==False, 
obstacle(rx_1_7 + 0, ry_1_7 + 1)==False, 
obstacle(rx_1_7 + 0, ry_1_7 + 2)==False, 
)))
s.add(Or(rprim_1_7!=12,
And(rx_f_1_7==-2, ry_f_1_7==0, rcost_1_7==3, 
obstacle(rx_1_7 + 0, ry_1_7 + 0)==False, 
obstacle(rx_1_7 + -1, ry_1_7 + 0)==False, 
obstacle(rx_1_7 + -2, ry_1_7 + 0)==False, 
)))
s.add(Or(rprim_1_7!=13,
And(rx_f_1_7==0, ry_f_1_7==-2, rcost_1_7==3, 
obstacle(rx_1_7 + 0, ry_1_7 + 0)==False, 
obstacle(rx_1_7 + 0, ry_1_7 + -1)==False, 
obstacle(rx_1_7 + 0, ry_1_7 + -2)==False, 
)))
s.add(Or(rprim_1_7!=14,
And(rx_f_1_7==2, ry_f_1_7==2, rcost_1_7==4, 
obstacle(rx_1_7 + 0, ry_1_7 + 0)==False, 
obstacle(rx_1_7 + 1, ry_1_7 + 1)==False, 
obstacle(rx_1_7 + 2, ry_1_7 + 2)==False, 
)))
s.add(Or(rprim_1_7!=15,
And(rx_f_1_7==-2, ry_f_1_7==2, rcost_1_7==4, 
obstacle(rx_1_7 + 0, ry_1_7 + 0)==False, 
obstacle(rx_1_7 + -1, ry_1_7 + 1)==False, 
obstacle(rx_1_7 + -2, ry_1_7 + 2)==False, 
)))
s.add(Or(rprim_1_7!=16,
And(rx_f_1_7==-2, ry_f_1_7==-2, rcost_1_7==4, 
obstacle(rx_1_7 + 0, ry_1_7 + 0)==False, 
obstacle(rx_1_7 + -1, ry_1_7 + -1)==False, 
obstacle(rx_1_7 + -2, ry_1_7 + -2)==False, 
)))
s.add(Or(rprim_1_7!=17,
And(rx_f_1_7==2, ry_f_1_7==-2, rcost_1_7==4, 
obstacle(rx_1_7 + 0, ry_1_7 + 0)==False, 
obstacle(rx_1_7 + 1, ry_1_7 + -1)==False, 
obstacle(rx_1_7 + 2, ry_1_7 + -2)==False, 
)))
s.add(Or(rprim_1_7!=18,
And(rx_f_1_7==3, ry_f_1_7==0, rcost_1_7==4, 
obstacle(rx_1_7 + 0, ry_1_7 + 0)==False, 
obstacle(rx_1_7 + 1, ry_1_7 + 0)==False, 
obstacle(rx_1_7 + 2, ry_1_7 + 0)==False, 
obstacle(rx_1_7 + 3, ry_1_7 + 0)==False, 
)))
s.add(Or(rprim_1_7!=19,
And(rx_f_1_7==0, ry_f_1_7==3, rcost_1_7==4, 
obstacle(rx_1_7 + 0, ry_1_7 + 0)==False, 
obstacle(rx_1_7 + 0, ry_1_7 + 1)==False, 
obstacle(rx_1_7 + 0, ry_1_7 + 2)==False, 
obstacle(rx_1_7 + 0, ry_1_7 + 3)==False, 
)))
s.add(Or(rprim_1_7!=20,
And(rx_f_1_7==-3, ry_f_1_7==0, rcost_1_7==4, 
obstacle(rx_1_7 + 0, ry_1_7 + 0)==False, 
obstacle(rx_1_7 + -1, ry_1_7 + 0)==False, 
obstacle(rx_1_7 + -2, ry_1_7 + 0)==False, 
obstacle(rx_1_7 + -3, ry_1_7 + 0)==False, 
)))
s.add(Or(rprim_1_7!=21,
And(rx_f_1_7==0, ry_f_1_7==-3, rcost_1_7==4, 
obstacle(rx_1_7 + 0, ry_1_7 + 0)==False, 
obstacle(rx_1_7 + 0, ry_1_7 + -1)==False, 
obstacle(rx_1_7 + 0, ry_1_7 + -2)==False, 
obstacle(rx_1_7 + 0, ry_1_7 + -3)==False, 
)))
s.add(Or(rprim_1_8!=1,
And(rx_f_1_8==0, ry_f_1_8==0, rcost_1_8==0, 
obstacle(rx_1_8 + 0, ry_1_8 + 0)==False, 
)))
s.add(Or(rprim_1_8!=2,
And(rx_f_1_8==1, ry_f_1_8==0, rcost_1_8==2, 
obstacle(rx_1_8 + 0, ry_1_8 + 0)==False, 
obstacle(rx_1_8 + 1, ry_1_8 + 0)==False, 
)))
s.add(Or(rprim_1_8!=3,
And(rx_f_1_8==0, ry_f_1_8==-1, rcost_1_8==2, 
obstacle(rx_1_8 + 0, ry_1_8 + 0)==False, 
obstacle(rx_1_8 + 0, ry_1_8 + -1)==False, 
)))
s.add(Or(rprim_1_8!=4,
And(rx_f_1_8==-1, ry_f_1_8==0, rcost_1_8==2, 
obstacle(rx_1_8 + 0, ry_1_8 + 0)==False, 
obstacle(rx_1_8 + -1, ry_1_8 + 0)==False, 
)))
s.add(Or(rprim_1_8!=5,
And(rx_f_1_8==0, ry_f_1_8==1, rcost_1_8==2, 
obstacle(rx_1_8 + 0, ry_1_8 + 0)==False, 
obstacle(rx_1_8 + 0, ry_1_8 + 1)==False, 
)))
s.add(Or(rprim_1_8!=6,
And(rx_f_1_8==1, ry_f_1_8==1, rcost_1_8==3, 
obstacle(rx_1_8 + 0, ry_1_8 + 0)==False, 
obstacle(rx_1_8 + 1, ry_1_8 + 1)==False, 
)))
s.add(Or(rprim_1_8!=7,
And(rx_f_1_8==-1, ry_f_1_8==1, rcost_1_8==3, 
obstacle(rx_1_8 + 0, ry_1_8 + 0)==False, 
obstacle(rx_1_8 + -1, ry_1_8 + 1)==False, 
)))
s.add(Or(rprim_1_8!=8,
And(rx_f_1_8==-1, ry_f_1_8==-1, rcost_1_8==3, 
obstacle(rx_1_8 + 0, ry_1_8 + 0)==False, 
obstacle(rx_1_8 + -1, ry_1_8 + -1)==False, 
)))
s.add(Or(rprim_1_8!=9,
And(rx_f_1_8==1, ry_f_1_8==-1, rcost_1_8==3, 
obstacle(rx_1_8 + 0, ry_1_8 + 0)==False, 
obstacle(rx_1_8 + 1, ry_1_8 + -1)==False, 
)))
s.add(Or(rprim_1_8!=10,
And(rx_f_1_8==2, ry_f_1_8==0, rcost_1_8==3, 
obstacle(rx_1_8 + 0, ry_1_8 + 0)==False, 
obstacle(rx_1_8 + 1, ry_1_8 + 0)==False, 
obstacle(rx_1_8 + 2, ry_1_8 + 0)==False, 
)))
s.add(Or(rprim_1_8!=11,
And(rx_f_1_8==0, ry_f_1_8==2, rcost_1_8==3, 
obstacle(rx_1_8 + 0, ry_1_8 + 0)==False, 
obstacle(rx_1_8 + 0, ry_1_8 + 1)==False, 
obstacle(rx_1_8 + 0, ry_1_8 + 2)==False, 
)))
s.add(Or(rprim_1_8!=12,
And(rx_f_1_8==-2, ry_f_1_8==0, rcost_1_8==3, 
obstacle(rx_1_8 + 0, ry_1_8 + 0)==False, 
obstacle(rx_1_8 + -1, ry_1_8 + 0)==False, 
obstacle(rx_1_8 + -2, ry_1_8 + 0)==False, 
)))
s.add(Or(rprim_1_8!=13,
And(rx_f_1_8==0, ry_f_1_8==-2, rcost_1_8==3, 
obstacle(rx_1_8 + 0, ry_1_8 + 0)==False, 
obstacle(rx_1_8 + 0, ry_1_8 + -1)==False, 
obstacle(rx_1_8 + 0, ry_1_8 + -2)==False, 
)))
s.add(Or(rprim_1_8!=14,
And(rx_f_1_8==2, ry_f_1_8==2, rcost_1_8==4, 
obstacle(rx_1_8 + 0, ry_1_8 + 0)==False, 
obstacle(rx_1_8 + 1, ry_1_8 + 1)==False, 
obstacle(rx_1_8 + 2, ry_1_8 + 2)==False, 
)))
s.add(Or(rprim_1_8!=15,
And(rx_f_1_8==-2, ry_f_1_8==2, rcost_1_8==4, 
obstacle(rx_1_8 + 0, ry_1_8 + 0)==False, 
obstacle(rx_1_8 + -1, ry_1_8 + 1)==False, 
obstacle(rx_1_8 + -2, ry_1_8 + 2)==False, 
)))
s.add(Or(rprim_1_8!=16,
And(rx_f_1_8==-2, ry_f_1_8==-2, rcost_1_8==4, 
obstacle(rx_1_8 + 0, ry_1_8 + 0)==False, 
obstacle(rx_1_8 + -1, ry_1_8 + -1)==False, 
obstacle(rx_1_8 + -2, ry_1_8 + -2)==False, 
)))
s.add(Or(rprim_1_8!=17,
And(rx_f_1_8==2, ry_f_1_8==-2, rcost_1_8==4, 
obstacle(rx_1_8 + 0, ry_1_8 + 0)==False, 
obstacle(rx_1_8 + 1, ry_1_8 + -1)==False, 
obstacle(rx_1_8 + 2, ry_1_8 + -2)==False, 
)))
s.add(Or(rprim_1_8!=18,
And(rx_f_1_8==3, ry_f_1_8==0, rcost_1_8==4, 
obstacle(rx_1_8 + 0, ry_1_8 + 0)==False, 
obstacle(rx_1_8 + 1, ry_1_8 + 0)==False, 
obstacle(rx_1_8 + 2, ry_1_8 + 0)==False, 
obstacle(rx_1_8 + 3, ry_1_8 + 0)==False, 
)))
s.add(Or(rprim_1_8!=19,
And(rx_f_1_8==0, ry_f_1_8==3, rcost_1_8==4, 
obstacle(rx_1_8 + 0, ry_1_8 + 0)==False, 
obstacle(rx_1_8 + 0, ry_1_8 + 1)==False, 
obstacle(rx_1_8 + 0, ry_1_8 + 2)==False, 
obstacle(rx_1_8 + 0, ry_1_8 + 3)==False, 
)))
s.add(Or(rprim_1_8!=20,
And(rx_f_1_8==-3, ry_f_1_8==0, rcost_1_8==4, 
obstacle(rx_1_8 + 0, ry_1_8 + 0)==False, 
obstacle(rx_1_8 + -1, ry_1_8 + 0)==False, 
obstacle(rx_1_8 + -2, ry_1_8 + 0)==False, 
obstacle(rx_1_8 + -3, ry_1_8 + 0)==False, 
)))
s.add(Or(rprim_1_8!=21,
And(rx_f_1_8==0, ry_f_1_8==-3, rcost_1_8==4, 
obstacle(rx_1_8 + 0, ry_1_8 + 0)==False, 
obstacle(rx_1_8 + 0, ry_1_8 + -1)==False, 
obstacle(rx_1_8 + 0, ry_1_8 + -2)==False, 
obstacle(rx_1_8 + 0, ry_1_8 + -3)==False, 
)))
s.add(Or(rprim_1_9!=1,
And(rx_f_1_9==0, ry_f_1_9==0, rcost_1_9==0, 
obstacle(rx_1_9 + 0, ry_1_9 + 0)==False, 
)))
s.add(Or(rprim_1_9!=2,
And(rx_f_1_9==1, ry_f_1_9==0, rcost_1_9==2, 
obstacle(rx_1_9 + 0, ry_1_9 + 0)==False, 
obstacle(rx_1_9 + 1, ry_1_9 + 0)==False, 
)))
s.add(Or(rprim_1_9!=3,
And(rx_f_1_9==0, ry_f_1_9==-1, rcost_1_9==2, 
obstacle(rx_1_9 + 0, ry_1_9 + 0)==False, 
obstacle(rx_1_9 + 0, ry_1_9 + -1)==False, 
)))
s.add(Or(rprim_1_9!=4,
And(rx_f_1_9==-1, ry_f_1_9==0, rcost_1_9==2, 
obstacle(rx_1_9 + 0, ry_1_9 + 0)==False, 
obstacle(rx_1_9 + -1, ry_1_9 + 0)==False, 
)))
s.add(Or(rprim_1_9!=5,
And(rx_f_1_9==0, ry_f_1_9==1, rcost_1_9==2, 
obstacle(rx_1_9 + 0, ry_1_9 + 0)==False, 
obstacle(rx_1_9 + 0, ry_1_9 + 1)==False, 
)))
s.add(Or(rprim_1_9!=6,
And(rx_f_1_9==1, ry_f_1_9==1, rcost_1_9==3, 
obstacle(rx_1_9 + 0, ry_1_9 + 0)==False, 
obstacle(rx_1_9 + 1, ry_1_9 + 1)==False, 
)))
s.add(Or(rprim_1_9!=7,
And(rx_f_1_9==-1, ry_f_1_9==1, rcost_1_9==3, 
obstacle(rx_1_9 + 0, ry_1_9 + 0)==False, 
obstacle(rx_1_9 + -1, ry_1_9 + 1)==False, 
)))
s.add(Or(rprim_1_9!=8,
And(rx_f_1_9==-1, ry_f_1_9==-1, rcost_1_9==3, 
obstacle(rx_1_9 + 0, ry_1_9 + 0)==False, 
obstacle(rx_1_9 + -1, ry_1_9 + -1)==False, 
)))
s.add(Or(rprim_1_9!=9,
And(rx_f_1_9==1, ry_f_1_9==-1, rcost_1_9==3, 
obstacle(rx_1_9 + 0, ry_1_9 + 0)==False, 
obstacle(rx_1_9 + 1, ry_1_9 + -1)==False, 
)))
s.add(Or(rprim_1_9!=10,
And(rx_f_1_9==2, ry_f_1_9==0, rcost_1_9==3, 
obstacle(rx_1_9 + 0, ry_1_9 + 0)==False, 
obstacle(rx_1_9 + 1, ry_1_9 + 0)==False, 
obstacle(rx_1_9 + 2, ry_1_9 + 0)==False, 
)))
s.add(Or(rprim_1_9!=11,
And(rx_f_1_9==0, ry_f_1_9==2, rcost_1_9==3, 
obstacle(rx_1_9 + 0, ry_1_9 + 0)==False, 
obstacle(rx_1_9 + 0, ry_1_9 + 1)==False, 
obstacle(rx_1_9 + 0, ry_1_9 + 2)==False, 
)))
s.add(Or(rprim_1_9!=12,
And(rx_f_1_9==-2, ry_f_1_9==0, rcost_1_9==3, 
obstacle(rx_1_9 + 0, ry_1_9 + 0)==False, 
obstacle(rx_1_9 + -1, ry_1_9 + 0)==False, 
obstacle(rx_1_9 + -2, ry_1_9 + 0)==False, 
)))
s.add(Or(rprim_1_9!=13,
And(rx_f_1_9==0, ry_f_1_9==-2, rcost_1_9==3, 
obstacle(rx_1_9 + 0, ry_1_9 + 0)==False, 
obstacle(rx_1_9 + 0, ry_1_9 + -1)==False, 
obstacle(rx_1_9 + 0, ry_1_9 + -2)==False, 
)))
s.add(Or(rprim_1_9!=14,
And(rx_f_1_9==2, ry_f_1_9==2, rcost_1_9==4, 
obstacle(rx_1_9 + 0, ry_1_9 + 0)==False, 
obstacle(rx_1_9 + 1, ry_1_9 + 1)==False, 
obstacle(rx_1_9 + 2, ry_1_9 + 2)==False, 
)))
s.add(Or(rprim_1_9!=15,
And(rx_f_1_9==-2, ry_f_1_9==2, rcost_1_9==4, 
obstacle(rx_1_9 + 0, ry_1_9 + 0)==False, 
obstacle(rx_1_9 + -1, ry_1_9 + 1)==False, 
obstacle(rx_1_9 + -2, ry_1_9 + 2)==False, 
)))
s.add(Or(rprim_1_9!=16,
And(rx_f_1_9==-2, ry_f_1_9==-2, rcost_1_9==4, 
obstacle(rx_1_9 + 0, ry_1_9 + 0)==False, 
obstacle(rx_1_9 + -1, ry_1_9 + -1)==False, 
obstacle(rx_1_9 + -2, ry_1_9 + -2)==False, 
)))
s.add(Or(rprim_1_9!=17,
And(rx_f_1_9==2, ry_f_1_9==-2, rcost_1_9==4, 
obstacle(rx_1_9 + 0, ry_1_9 + 0)==False, 
obstacle(rx_1_9 + 1, ry_1_9 + -1)==False, 
obstacle(rx_1_9 + 2, ry_1_9 + -2)==False, 
)))
s.add(Or(rprim_1_9!=18,
And(rx_f_1_9==3, ry_f_1_9==0, rcost_1_9==4, 
obstacle(rx_1_9 + 0, ry_1_9 + 0)==False, 
obstacle(rx_1_9 + 1, ry_1_9 + 0)==False, 
obstacle(rx_1_9 + 2, ry_1_9 + 0)==False, 
obstacle(rx_1_9 + 3, ry_1_9 + 0)==False, 
)))
s.add(Or(rprim_1_9!=19,
And(rx_f_1_9==0, ry_f_1_9==3, rcost_1_9==4, 
obstacle(rx_1_9 + 0, ry_1_9 + 0)==False, 
obstacle(rx_1_9 + 0, ry_1_9 + 1)==False, 
obstacle(rx_1_9 + 0, ry_1_9 + 2)==False, 
obstacle(rx_1_9 + 0, ry_1_9 + 3)==False, 
)))
s.add(Or(rprim_1_9!=20,
And(rx_f_1_9==-3, ry_f_1_9==0, rcost_1_9==4, 
obstacle(rx_1_9 + 0, ry_1_9 + 0)==False, 
obstacle(rx_1_9 + -1, ry_1_9 + 0)==False, 
obstacle(rx_1_9 + -2, ry_1_9 + 0)==False, 
obstacle(rx_1_9 + -3, ry_1_9 + 0)==False, 
)))
s.add(Or(rprim_1_9!=21,
And(rx_f_1_9==0, ry_f_1_9==-3, rcost_1_9==4, 
obstacle(rx_1_9 + 0, ry_1_9 + 0)==False, 
obstacle(rx_1_9 + 0, ry_1_9 + -1)==False, 
obstacle(rx_1_9 + 0, ry_1_9 + -2)==False, 
obstacle(rx_1_9 + 0, ry_1_9 + -3)==False, 
)))
s.add(Or(rprim_1_10!=1,
And(rx_f_1_10==0, ry_f_1_10==0, rcost_1_10==0, 
obstacle(rx_1_10 + 0, ry_1_10 + 0)==False, 
)))
s.add(Or(rprim_1_10!=2,
And(rx_f_1_10==1, ry_f_1_10==0, rcost_1_10==2, 
obstacle(rx_1_10 + 0, ry_1_10 + 0)==False, 
obstacle(rx_1_10 + 1, ry_1_10 + 0)==False, 
)))
s.add(Or(rprim_1_10!=3,
And(rx_f_1_10==0, ry_f_1_10==-1, rcost_1_10==2, 
obstacle(rx_1_10 + 0, ry_1_10 + 0)==False, 
obstacle(rx_1_10 + 0, ry_1_10 + -1)==False, 
)))
s.add(Or(rprim_1_10!=4,
And(rx_f_1_10==-1, ry_f_1_10==0, rcost_1_10==2, 
obstacle(rx_1_10 + 0, ry_1_10 + 0)==False, 
obstacle(rx_1_10 + -1, ry_1_10 + 0)==False, 
)))
s.add(Or(rprim_1_10!=5,
And(rx_f_1_10==0, ry_f_1_10==1, rcost_1_10==2, 
obstacle(rx_1_10 + 0, ry_1_10 + 0)==False, 
obstacle(rx_1_10 + 0, ry_1_10 + 1)==False, 
)))
s.add(Or(rprim_1_10!=6,
And(rx_f_1_10==1, ry_f_1_10==1, rcost_1_10==3, 
obstacle(rx_1_10 + 0, ry_1_10 + 0)==False, 
obstacle(rx_1_10 + 1, ry_1_10 + 1)==False, 
)))
s.add(Or(rprim_1_10!=7,
And(rx_f_1_10==-1, ry_f_1_10==1, rcost_1_10==3, 
obstacle(rx_1_10 + 0, ry_1_10 + 0)==False, 
obstacle(rx_1_10 + -1, ry_1_10 + 1)==False, 
)))
s.add(Or(rprim_1_10!=8,
And(rx_f_1_10==-1, ry_f_1_10==-1, rcost_1_10==3, 
obstacle(rx_1_10 + 0, ry_1_10 + 0)==False, 
obstacle(rx_1_10 + -1, ry_1_10 + -1)==False, 
)))
s.add(Or(rprim_1_10!=9,
And(rx_f_1_10==1, ry_f_1_10==-1, rcost_1_10==3, 
obstacle(rx_1_10 + 0, ry_1_10 + 0)==False, 
obstacle(rx_1_10 + 1, ry_1_10 + -1)==False, 
)))
s.add(Or(rprim_1_10!=10,
And(rx_f_1_10==2, ry_f_1_10==0, rcost_1_10==3, 
obstacle(rx_1_10 + 0, ry_1_10 + 0)==False, 
obstacle(rx_1_10 + 1, ry_1_10 + 0)==False, 
obstacle(rx_1_10 + 2, ry_1_10 + 0)==False, 
)))
s.add(Or(rprim_1_10!=11,
And(rx_f_1_10==0, ry_f_1_10==2, rcost_1_10==3, 
obstacle(rx_1_10 + 0, ry_1_10 + 0)==False, 
obstacle(rx_1_10 + 0, ry_1_10 + 1)==False, 
obstacle(rx_1_10 + 0, ry_1_10 + 2)==False, 
)))
s.add(Or(rprim_1_10!=12,
And(rx_f_1_10==-2, ry_f_1_10==0, rcost_1_10==3, 
obstacle(rx_1_10 + 0, ry_1_10 + 0)==False, 
obstacle(rx_1_10 + -1, ry_1_10 + 0)==False, 
obstacle(rx_1_10 + -2, ry_1_10 + 0)==False, 
)))
s.add(Or(rprim_1_10!=13,
And(rx_f_1_10==0, ry_f_1_10==-2, rcost_1_10==3, 
obstacle(rx_1_10 + 0, ry_1_10 + 0)==False, 
obstacle(rx_1_10 + 0, ry_1_10 + -1)==False, 
obstacle(rx_1_10 + 0, ry_1_10 + -2)==False, 
)))
s.add(Or(rprim_1_10!=14,
And(rx_f_1_10==2, ry_f_1_10==2, rcost_1_10==4, 
obstacle(rx_1_10 + 0, ry_1_10 + 0)==False, 
obstacle(rx_1_10 + 1, ry_1_10 + 1)==False, 
obstacle(rx_1_10 + 2, ry_1_10 + 2)==False, 
)))
s.add(Or(rprim_1_10!=15,
And(rx_f_1_10==-2, ry_f_1_10==2, rcost_1_10==4, 
obstacle(rx_1_10 + 0, ry_1_10 + 0)==False, 
obstacle(rx_1_10 + -1, ry_1_10 + 1)==False, 
obstacle(rx_1_10 + -2, ry_1_10 + 2)==False, 
)))
s.add(Or(rprim_1_10!=16,
And(rx_f_1_10==-2, ry_f_1_10==-2, rcost_1_10==4, 
obstacle(rx_1_10 + 0, ry_1_10 + 0)==False, 
obstacle(rx_1_10 + -1, ry_1_10 + -1)==False, 
obstacle(rx_1_10 + -2, ry_1_10 + -2)==False, 
)))
s.add(Or(rprim_1_10!=17,
And(rx_f_1_10==2, ry_f_1_10==-2, rcost_1_10==4, 
obstacle(rx_1_10 + 0, ry_1_10 + 0)==False, 
obstacle(rx_1_10 + 1, ry_1_10 + -1)==False, 
obstacle(rx_1_10 + 2, ry_1_10 + -2)==False, 
)))
s.add(Or(rprim_1_10!=18,
And(rx_f_1_10==3, ry_f_1_10==0, rcost_1_10==4, 
obstacle(rx_1_10 + 0, ry_1_10 + 0)==False, 
obstacle(rx_1_10 + 1, ry_1_10 + 0)==False, 
obstacle(rx_1_10 + 2, ry_1_10 + 0)==False, 
obstacle(rx_1_10 + 3, ry_1_10 + 0)==False, 
)))
s.add(Or(rprim_1_10!=19,
And(rx_f_1_10==0, ry_f_1_10==3, rcost_1_10==4, 
obstacle(rx_1_10 + 0, ry_1_10 + 0)==False, 
obstacle(rx_1_10 + 0, ry_1_10 + 1)==False, 
obstacle(rx_1_10 + 0, ry_1_10 + 2)==False, 
obstacle(rx_1_10 + 0, ry_1_10 + 3)==False, 
)))
s.add(Or(rprim_1_10!=20,
And(rx_f_1_10==-3, ry_f_1_10==0, rcost_1_10==4, 
obstacle(rx_1_10 + 0, ry_1_10 + 0)==False, 
obstacle(rx_1_10 + -1, ry_1_10 + 0)==False, 
obstacle(rx_1_10 + -2, ry_1_10 + 0)==False, 
obstacle(rx_1_10 + -3, ry_1_10 + 0)==False, 
)))
s.add(Or(rprim_1_10!=21,
And(rx_f_1_10==0, ry_f_1_10==-3, rcost_1_10==4, 
obstacle(rx_1_10 + 0, ry_1_10 + 0)==False, 
obstacle(rx_1_10 + 0, ry_1_10 + -1)==False, 
obstacle(rx_1_10 + 0, ry_1_10 + -2)==False, 
obstacle(rx_1_10 + 0, ry_1_10 + -3)==False, 
)))
s.add(Or(rprim_1_11!=1,
And(rx_f_1_11==0, ry_f_1_11==0, rcost_1_11==0, 
obstacle(rx_1_11 + 0, ry_1_11 + 0)==False, 
)))
s.add(Or(rprim_1_11!=2,
And(rx_f_1_11==1, ry_f_1_11==0, rcost_1_11==2, 
obstacle(rx_1_11 + 0, ry_1_11 + 0)==False, 
obstacle(rx_1_11 + 1, ry_1_11 + 0)==False, 
)))
s.add(Or(rprim_1_11!=3,
And(rx_f_1_11==0, ry_f_1_11==-1, rcost_1_11==2, 
obstacle(rx_1_11 + 0, ry_1_11 + 0)==False, 
obstacle(rx_1_11 + 0, ry_1_11 + -1)==False, 
)))
s.add(Or(rprim_1_11!=4,
And(rx_f_1_11==-1, ry_f_1_11==0, rcost_1_11==2, 
obstacle(rx_1_11 + 0, ry_1_11 + 0)==False, 
obstacle(rx_1_11 + -1, ry_1_11 + 0)==False, 
)))
s.add(Or(rprim_1_11!=5,
And(rx_f_1_11==0, ry_f_1_11==1, rcost_1_11==2, 
obstacle(rx_1_11 + 0, ry_1_11 + 0)==False, 
obstacle(rx_1_11 + 0, ry_1_11 + 1)==False, 
)))
s.add(Or(rprim_1_11!=6,
And(rx_f_1_11==1, ry_f_1_11==1, rcost_1_11==3, 
obstacle(rx_1_11 + 0, ry_1_11 + 0)==False, 
obstacle(rx_1_11 + 1, ry_1_11 + 1)==False, 
)))
s.add(Or(rprim_1_11!=7,
And(rx_f_1_11==-1, ry_f_1_11==1, rcost_1_11==3, 
obstacle(rx_1_11 + 0, ry_1_11 + 0)==False, 
obstacle(rx_1_11 + -1, ry_1_11 + 1)==False, 
)))
s.add(Or(rprim_1_11!=8,
And(rx_f_1_11==-1, ry_f_1_11==-1, rcost_1_11==3, 
obstacle(rx_1_11 + 0, ry_1_11 + 0)==False, 
obstacle(rx_1_11 + -1, ry_1_11 + -1)==False, 
)))
s.add(Or(rprim_1_11!=9,
And(rx_f_1_11==1, ry_f_1_11==-1, rcost_1_11==3, 
obstacle(rx_1_11 + 0, ry_1_11 + 0)==False, 
obstacle(rx_1_11 + 1, ry_1_11 + -1)==False, 
)))
s.add(Or(rprim_1_11!=10,
And(rx_f_1_11==2, ry_f_1_11==0, rcost_1_11==3, 
obstacle(rx_1_11 + 0, ry_1_11 + 0)==False, 
obstacle(rx_1_11 + 1, ry_1_11 + 0)==False, 
obstacle(rx_1_11 + 2, ry_1_11 + 0)==False, 
)))
s.add(Or(rprim_1_11!=11,
And(rx_f_1_11==0, ry_f_1_11==2, rcost_1_11==3, 
obstacle(rx_1_11 + 0, ry_1_11 + 0)==False, 
obstacle(rx_1_11 + 0, ry_1_11 + 1)==False, 
obstacle(rx_1_11 + 0, ry_1_11 + 2)==False, 
)))
s.add(Or(rprim_1_11!=12,
And(rx_f_1_11==-2, ry_f_1_11==0, rcost_1_11==3, 
obstacle(rx_1_11 + 0, ry_1_11 + 0)==False, 
obstacle(rx_1_11 + -1, ry_1_11 + 0)==False, 
obstacle(rx_1_11 + -2, ry_1_11 + 0)==False, 
)))
s.add(Or(rprim_1_11!=13,
And(rx_f_1_11==0, ry_f_1_11==-2, rcost_1_11==3, 
obstacle(rx_1_11 + 0, ry_1_11 + 0)==False, 
obstacle(rx_1_11 + 0, ry_1_11 + -1)==False, 
obstacle(rx_1_11 + 0, ry_1_11 + -2)==False, 
)))
s.add(Or(rprim_1_11!=14,
And(rx_f_1_11==2, ry_f_1_11==2, rcost_1_11==4, 
obstacle(rx_1_11 + 0, ry_1_11 + 0)==False, 
obstacle(rx_1_11 + 1, ry_1_11 + 1)==False, 
obstacle(rx_1_11 + 2, ry_1_11 + 2)==False, 
)))
s.add(Or(rprim_1_11!=15,
And(rx_f_1_11==-2, ry_f_1_11==2, rcost_1_11==4, 
obstacle(rx_1_11 + 0, ry_1_11 + 0)==False, 
obstacle(rx_1_11 + -1, ry_1_11 + 1)==False, 
obstacle(rx_1_11 + -2, ry_1_11 + 2)==False, 
)))
s.add(Or(rprim_1_11!=16,
And(rx_f_1_11==-2, ry_f_1_11==-2, rcost_1_11==4, 
obstacle(rx_1_11 + 0, ry_1_11 + 0)==False, 
obstacle(rx_1_11 + -1, ry_1_11 + -1)==False, 
obstacle(rx_1_11 + -2, ry_1_11 + -2)==False, 
)))
s.add(Or(rprim_1_11!=17,
And(rx_f_1_11==2, ry_f_1_11==-2, rcost_1_11==4, 
obstacle(rx_1_11 + 0, ry_1_11 + 0)==False, 
obstacle(rx_1_11 + 1, ry_1_11 + -1)==False, 
obstacle(rx_1_11 + 2, ry_1_11 + -2)==False, 
)))
s.add(Or(rprim_1_11!=18,
And(rx_f_1_11==3, ry_f_1_11==0, rcost_1_11==4, 
obstacle(rx_1_11 + 0, ry_1_11 + 0)==False, 
obstacle(rx_1_11 + 1, ry_1_11 + 0)==False, 
obstacle(rx_1_11 + 2, ry_1_11 + 0)==False, 
obstacle(rx_1_11 + 3, ry_1_11 + 0)==False, 
)))
s.add(Or(rprim_1_11!=19,
And(rx_f_1_11==0, ry_f_1_11==3, rcost_1_11==4, 
obstacle(rx_1_11 + 0, ry_1_11 + 0)==False, 
obstacle(rx_1_11 + 0, ry_1_11 + 1)==False, 
obstacle(rx_1_11 + 0, ry_1_11 + 2)==False, 
obstacle(rx_1_11 + 0, ry_1_11 + 3)==False, 
)))
s.add(Or(rprim_1_11!=20,
And(rx_f_1_11==-3, ry_f_1_11==0, rcost_1_11==4, 
obstacle(rx_1_11 + 0, ry_1_11 + 0)==False, 
obstacle(rx_1_11 + -1, ry_1_11 + 0)==False, 
obstacle(rx_1_11 + -2, ry_1_11 + 0)==False, 
obstacle(rx_1_11 + -3, ry_1_11 + 0)==False, 
)))
s.add(Or(rprim_1_11!=21,
And(rx_f_1_11==0, ry_f_1_11==-3, rcost_1_11==4, 
obstacle(rx_1_11 + 0, ry_1_11 + 0)==False, 
obstacle(rx_1_11 + 0, ry_1_11 + -1)==False, 
obstacle(rx_1_11 + 0, ry_1_11 + -2)==False, 
obstacle(rx_1_11 + 0, ry_1_11 + -3)==False, 
)))
s.add(Or(rprim_1_12!=1,
And(rx_f_1_12==0, ry_f_1_12==0, rcost_1_12==0, 
obstacle(rx_1_12 + 0, ry_1_12 + 0)==False, 
)))
s.add(Or(rprim_1_12!=2,
And(rx_f_1_12==1, ry_f_1_12==0, rcost_1_12==2, 
obstacle(rx_1_12 + 0, ry_1_12 + 0)==False, 
obstacle(rx_1_12 + 1, ry_1_12 + 0)==False, 
)))
s.add(Or(rprim_1_12!=3,
And(rx_f_1_12==0, ry_f_1_12==-1, rcost_1_12==2, 
obstacle(rx_1_12 + 0, ry_1_12 + 0)==False, 
obstacle(rx_1_12 + 0, ry_1_12 + -1)==False, 
)))
s.add(Or(rprim_1_12!=4,
And(rx_f_1_12==-1, ry_f_1_12==0, rcost_1_12==2, 
obstacle(rx_1_12 + 0, ry_1_12 + 0)==False, 
obstacle(rx_1_12 + -1, ry_1_12 + 0)==False, 
)))
s.add(Or(rprim_1_12!=5,
And(rx_f_1_12==0, ry_f_1_12==1, rcost_1_12==2, 
obstacle(rx_1_12 + 0, ry_1_12 + 0)==False, 
obstacle(rx_1_12 + 0, ry_1_12 + 1)==False, 
)))
s.add(Or(rprim_1_12!=6,
And(rx_f_1_12==1, ry_f_1_12==1, rcost_1_12==3, 
obstacle(rx_1_12 + 0, ry_1_12 + 0)==False, 
obstacle(rx_1_12 + 1, ry_1_12 + 1)==False, 
)))
s.add(Or(rprim_1_12!=7,
And(rx_f_1_12==-1, ry_f_1_12==1, rcost_1_12==3, 
obstacle(rx_1_12 + 0, ry_1_12 + 0)==False, 
obstacle(rx_1_12 + -1, ry_1_12 + 1)==False, 
)))
s.add(Or(rprim_1_12!=8,
And(rx_f_1_12==-1, ry_f_1_12==-1, rcost_1_12==3, 
obstacle(rx_1_12 + 0, ry_1_12 + 0)==False, 
obstacle(rx_1_12 + -1, ry_1_12 + -1)==False, 
)))
s.add(Or(rprim_1_12!=9,
And(rx_f_1_12==1, ry_f_1_12==-1, rcost_1_12==3, 
obstacle(rx_1_12 + 0, ry_1_12 + 0)==False, 
obstacle(rx_1_12 + 1, ry_1_12 + -1)==False, 
)))
s.add(Or(rprim_1_12!=10,
And(rx_f_1_12==2, ry_f_1_12==0, rcost_1_12==3, 
obstacle(rx_1_12 + 0, ry_1_12 + 0)==False, 
obstacle(rx_1_12 + 1, ry_1_12 + 0)==False, 
obstacle(rx_1_12 + 2, ry_1_12 + 0)==False, 
)))
s.add(Or(rprim_1_12!=11,
And(rx_f_1_12==0, ry_f_1_12==2, rcost_1_12==3, 
obstacle(rx_1_12 + 0, ry_1_12 + 0)==False, 
obstacle(rx_1_12 + 0, ry_1_12 + 1)==False, 
obstacle(rx_1_12 + 0, ry_1_12 + 2)==False, 
)))
s.add(Or(rprim_1_12!=12,
And(rx_f_1_12==-2, ry_f_1_12==0, rcost_1_12==3, 
obstacle(rx_1_12 + 0, ry_1_12 + 0)==False, 
obstacle(rx_1_12 + -1, ry_1_12 + 0)==False, 
obstacle(rx_1_12 + -2, ry_1_12 + 0)==False, 
)))
s.add(Or(rprim_1_12!=13,
And(rx_f_1_12==0, ry_f_1_12==-2, rcost_1_12==3, 
obstacle(rx_1_12 + 0, ry_1_12 + 0)==False, 
obstacle(rx_1_12 + 0, ry_1_12 + -1)==False, 
obstacle(rx_1_12 + 0, ry_1_12 + -2)==False, 
)))
s.add(Or(rprim_1_12!=14,
And(rx_f_1_12==2, ry_f_1_12==2, rcost_1_12==4, 
obstacle(rx_1_12 + 0, ry_1_12 + 0)==False, 
obstacle(rx_1_12 + 1, ry_1_12 + 1)==False, 
obstacle(rx_1_12 + 2, ry_1_12 + 2)==False, 
)))
s.add(Or(rprim_1_12!=15,
And(rx_f_1_12==-2, ry_f_1_12==2, rcost_1_12==4, 
obstacle(rx_1_12 + 0, ry_1_12 + 0)==False, 
obstacle(rx_1_12 + -1, ry_1_12 + 1)==False, 
obstacle(rx_1_12 + -2, ry_1_12 + 2)==False, 
)))
s.add(Or(rprim_1_12!=16,
And(rx_f_1_12==-2, ry_f_1_12==-2, rcost_1_12==4, 
obstacle(rx_1_12 + 0, ry_1_12 + 0)==False, 
obstacle(rx_1_12 + -1, ry_1_12 + -1)==False, 
obstacle(rx_1_12 + -2, ry_1_12 + -2)==False, 
)))
s.add(Or(rprim_1_12!=17,
And(rx_f_1_12==2, ry_f_1_12==-2, rcost_1_12==4, 
obstacle(rx_1_12 + 0, ry_1_12 + 0)==False, 
obstacle(rx_1_12 + 1, ry_1_12 + -1)==False, 
obstacle(rx_1_12 + 2, ry_1_12 + -2)==False, 
)))
s.add(Or(rprim_1_12!=18,
And(rx_f_1_12==3, ry_f_1_12==0, rcost_1_12==4, 
obstacle(rx_1_12 + 0, ry_1_12 + 0)==False, 
obstacle(rx_1_12 + 1, ry_1_12 + 0)==False, 
obstacle(rx_1_12 + 2, ry_1_12 + 0)==False, 
obstacle(rx_1_12 + 3, ry_1_12 + 0)==False, 
)))
s.add(Or(rprim_1_12!=19,
And(rx_f_1_12==0, ry_f_1_12==3, rcost_1_12==4, 
obstacle(rx_1_12 + 0, ry_1_12 + 0)==False, 
obstacle(rx_1_12 + 0, ry_1_12 + 1)==False, 
obstacle(rx_1_12 + 0, ry_1_12 + 2)==False, 
obstacle(rx_1_12 + 0, ry_1_12 + 3)==False, 
)))
s.add(Or(rprim_1_12!=20,
And(rx_f_1_12==-3, ry_f_1_12==0, rcost_1_12==4, 
obstacle(rx_1_12 + 0, ry_1_12 + 0)==False, 
obstacle(rx_1_12 + -1, ry_1_12 + 0)==False, 
obstacle(rx_1_12 + -2, ry_1_12 + 0)==False, 
obstacle(rx_1_12 + -3, ry_1_12 + 0)==False, 
)))
s.add(Or(rprim_1_12!=21,
And(rx_f_1_12==0, ry_f_1_12==-3, rcost_1_12==4, 
obstacle(rx_1_12 + 0, ry_1_12 + 0)==False, 
obstacle(rx_1_12 + 0, ry_1_12 + -1)==False, 
obstacle(rx_1_12 + 0, ry_1_12 + -2)==False, 
obstacle(rx_1_12 + 0, ry_1_12 + -3)==False, 
)))
s.add(Or(rprim_1_13!=1,
And(rx_f_1_13==0, ry_f_1_13==0, rcost_1_13==0, 
obstacle(rx_1_13 + 0, ry_1_13 + 0)==False, 
)))
s.add(Or(rprim_1_13!=2,
And(rx_f_1_13==1, ry_f_1_13==0, rcost_1_13==2, 
obstacle(rx_1_13 + 0, ry_1_13 + 0)==False, 
obstacle(rx_1_13 + 1, ry_1_13 + 0)==False, 
)))
s.add(Or(rprim_1_13!=3,
And(rx_f_1_13==0, ry_f_1_13==-1, rcost_1_13==2, 
obstacle(rx_1_13 + 0, ry_1_13 + 0)==False, 
obstacle(rx_1_13 + 0, ry_1_13 + -1)==False, 
)))
s.add(Or(rprim_1_13!=4,
And(rx_f_1_13==-1, ry_f_1_13==0, rcost_1_13==2, 
obstacle(rx_1_13 + 0, ry_1_13 + 0)==False, 
obstacle(rx_1_13 + -1, ry_1_13 + 0)==False, 
)))
s.add(Or(rprim_1_13!=5,
And(rx_f_1_13==0, ry_f_1_13==1, rcost_1_13==2, 
obstacle(rx_1_13 + 0, ry_1_13 + 0)==False, 
obstacle(rx_1_13 + 0, ry_1_13 + 1)==False, 
)))
s.add(Or(rprim_1_13!=6,
And(rx_f_1_13==1, ry_f_1_13==1, rcost_1_13==3, 
obstacle(rx_1_13 + 0, ry_1_13 + 0)==False, 
obstacle(rx_1_13 + 1, ry_1_13 + 1)==False, 
)))
s.add(Or(rprim_1_13!=7,
And(rx_f_1_13==-1, ry_f_1_13==1, rcost_1_13==3, 
obstacle(rx_1_13 + 0, ry_1_13 + 0)==False, 
obstacle(rx_1_13 + -1, ry_1_13 + 1)==False, 
)))
s.add(Or(rprim_1_13!=8,
And(rx_f_1_13==-1, ry_f_1_13==-1, rcost_1_13==3, 
obstacle(rx_1_13 + 0, ry_1_13 + 0)==False, 
obstacle(rx_1_13 + -1, ry_1_13 + -1)==False, 
)))
s.add(Or(rprim_1_13!=9,
And(rx_f_1_13==1, ry_f_1_13==-1, rcost_1_13==3, 
obstacle(rx_1_13 + 0, ry_1_13 + 0)==False, 
obstacle(rx_1_13 + 1, ry_1_13 + -1)==False, 
)))
s.add(Or(rprim_1_13!=10,
And(rx_f_1_13==2, ry_f_1_13==0, rcost_1_13==3, 
obstacle(rx_1_13 + 0, ry_1_13 + 0)==False, 
obstacle(rx_1_13 + 1, ry_1_13 + 0)==False, 
obstacle(rx_1_13 + 2, ry_1_13 + 0)==False, 
)))
s.add(Or(rprim_1_13!=11,
And(rx_f_1_13==0, ry_f_1_13==2, rcost_1_13==3, 
obstacle(rx_1_13 + 0, ry_1_13 + 0)==False, 
obstacle(rx_1_13 + 0, ry_1_13 + 1)==False, 
obstacle(rx_1_13 + 0, ry_1_13 + 2)==False, 
)))
s.add(Or(rprim_1_13!=12,
And(rx_f_1_13==-2, ry_f_1_13==0, rcost_1_13==3, 
obstacle(rx_1_13 + 0, ry_1_13 + 0)==False, 
obstacle(rx_1_13 + -1, ry_1_13 + 0)==False, 
obstacle(rx_1_13 + -2, ry_1_13 + 0)==False, 
)))
s.add(Or(rprim_1_13!=13,
And(rx_f_1_13==0, ry_f_1_13==-2, rcost_1_13==3, 
obstacle(rx_1_13 + 0, ry_1_13 + 0)==False, 
obstacle(rx_1_13 + 0, ry_1_13 + -1)==False, 
obstacle(rx_1_13 + 0, ry_1_13 + -2)==False, 
)))
s.add(Or(rprim_1_13!=14,
And(rx_f_1_13==2, ry_f_1_13==2, rcost_1_13==4, 
obstacle(rx_1_13 + 0, ry_1_13 + 0)==False, 
obstacle(rx_1_13 + 1, ry_1_13 + 1)==False, 
obstacle(rx_1_13 + 2, ry_1_13 + 2)==False, 
)))
s.add(Or(rprim_1_13!=15,
And(rx_f_1_13==-2, ry_f_1_13==2, rcost_1_13==4, 
obstacle(rx_1_13 + 0, ry_1_13 + 0)==False, 
obstacle(rx_1_13 + -1, ry_1_13 + 1)==False, 
obstacle(rx_1_13 + -2, ry_1_13 + 2)==False, 
)))
s.add(Or(rprim_1_13!=16,
And(rx_f_1_13==-2, ry_f_1_13==-2, rcost_1_13==4, 
obstacle(rx_1_13 + 0, ry_1_13 + 0)==False, 
obstacle(rx_1_13 + -1, ry_1_13 + -1)==False, 
obstacle(rx_1_13 + -2, ry_1_13 + -2)==False, 
)))
s.add(Or(rprim_1_13!=17,
And(rx_f_1_13==2, ry_f_1_13==-2, rcost_1_13==4, 
obstacle(rx_1_13 + 0, ry_1_13 + 0)==False, 
obstacle(rx_1_13 + 1, ry_1_13 + -1)==False, 
obstacle(rx_1_13 + 2, ry_1_13 + -2)==False, 
)))
s.add(Or(rprim_1_13!=18,
And(rx_f_1_13==3, ry_f_1_13==0, rcost_1_13==4, 
obstacle(rx_1_13 + 0, ry_1_13 + 0)==False, 
obstacle(rx_1_13 + 1, ry_1_13 + 0)==False, 
obstacle(rx_1_13 + 2, ry_1_13 + 0)==False, 
obstacle(rx_1_13 + 3, ry_1_13 + 0)==False, 
)))
s.add(Or(rprim_1_13!=19,
And(rx_f_1_13==0, ry_f_1_13==3, rcost_1_13==4, 
obstacle(rx_1_13 + 0, ry_1_13 + 0)==False, 
obstacle(rx_1_13 + 0, ry_1_13 + 1)==False, 
obstacle(rx_1_13 + 0, ry_1_13 + 2)==False, 
obstacle(rx_1_13 + 0, ry_1_13 + 3)==False, 
)))
s.add(Or(rprim_1_13!=20,
And(rx_f_1_13==-3, ry_f_1_13==0, rcost_1_13==4, 
obstacle(rx_1_13 + 0, ry_1_13 + 0)==False, 
obstacle(rx_1_13 + -1, ry_1_13 + 0)==False, 
obstacle(rx_1_13 + -2, ry_1_13 + 0)==False, 
obstacle(rx_1_13 + -3, ry_1_13 + 0)==False, 
)))
s.add(Or(rprim_1_13!=21,
And(rx_f_1_13==0, ry_f_1_13==-3, rcost_1_13==4, 
obstacle(rx_1_13 + 0, ry_1_13 + 0)==False, 
obstacle(rx_1_13 + 0, ry_1_13 + -1)==False, 
obstacle(rx_1_13 + 0, ry_1_13 + -2)==False, 
obstacle(rx_1_13 + 0, ry_1_13 + -3)==False, 
)))
s.add(Or(rprim_1_14!=1,
And(rx_f_1_14==0, ry_f_1_14==0, rcost_1_14==0, 
obstacle(rx_1_14 + 0, ry_1_14 + 0)==False, 
)))
s.add(Or(rprim_1_14!=2,
And(rx_f_1_14==1, ry_f_1_14==0, rcost_1_14==2, 
obstacle(rx_1_14 + 0, ry_1_14 + 0)==False, 
obstacle(rx_1_14 + 1, ry_1_14 + 0)==False, 
)))
s.add(Or(rprim_1_14!=3,
And(rx_f_1_14==0, ry_f_1_14==-1, rcost_1_14==2, 
obstacle(rx_1_14 + 0, ry_1_14 + 0)==False, 
obstacle(rx_1_14 + 0, ry_1_14 + -1)==False, 
)))
s.add(Or(rprim_1_14!=4,
And(rx_f_1_14==-1, ry_f_1_14==0, rcost_1_14==2, 
obstacle(rx_1_14 + 0, ry_1_14 + 0)==False, 
obstacle(rx_1_14 + -1, ry_1_14 + 0)==False, 
)))
s.add(Or(rprim_1_14!=5,
And(rx_f_1_14==0, ry_f_1_14==1, rcost_1_14==2, 
obstacle(rx_1_14 + 0, ry_1_14 + 0)==False, 
obstacle(rx_1_14 + 0, ry_1_14 + 1)==False, 
)))
s.add(Or(rprim_1_14!=6,
And(rx_f_1_14==1, ry_f_1_14==1, rcost_1_14==3, 
obstacle(rx_1_14 + 0, ry_1_14 + 0)==False, 
obstacle(rx_1_14 + 1, ry_1_14 + 1)==False, 
)))
s.add(Or(rprim_1_14!=7,
And(rx_f_1_14==-1, ry_f_1_14==1, rcost_1_14==3, 
obstacle(rx_1_14 + 0, ry_1_14 + 0)==False, 
obstacle(rx_1_14 + -1, ry_1_14 + 1)==False, 
)))
s.add(Or(rprim_1_14!=8,
And(rx_f_1_14==-1, ry_f_1_14==-1, rcost_1_14==3, 
obstacle(rx_1_14 + 0, ry_1_14 + 0)==False, 
obstacle(rx_1_14 + -1, ry_1_14 + -1)==False, 
)))
s.add(Or(rprim_1_14!=9,
And(rx_f_1_14==1, ry_f_1_14==-1, rcost_1_14==3, 
obstacle(rx_1_14 + 0, ry_1_14 + 0)==False, 
obstacle(rx_1_14 + 1, ry_1_14 + -1)==False, 
)))
s.add(Or(rprim_1_14!=10,
And(rx_f_1_14==2, ry_f_1_14==0, rcost_1_14==3, 
obstacle(rx_1_14 + 0, ry_1_14 + 0)==False, 
obstacle(rx_1_14 + 1, ry_1_14 + 0)==False, 
obstacle(rx_1_14 + 2, ry_1_14 + 0)==False, 
)))
s.add(Or(rprim_1_14!=11,
And(rx_f_1_14==0, ry_f_1_14==2, rcost_1_14==3, 
obstacle(rx_1_14 + 0, ry_1_14 + 0)==False, 
obstacle(rx_1_14 + 0, ry_1_14 + 1)==False, 
obstacle(rx_1_14 + 0, ry_1_14 + 2)==False, 
)))
s.add(Or(rprim_1_14!=12,
And(rx_f_1_14==-2, ry_f_1_14==0, rcost_1_14==3, 
obstacle(rx_1_14 + 0, ry_1_14 + 0)==False, 
obstacle(rx_1_14 + -1, ry_1_14 + 0)==False, 
obstacle(rx_1_14 + -2, ry_1_14 + 0)==False, 
)))
s.add(Or(rprim_1_14!=13,
And(rx_f_1_14==0, ry_f_1_14==-2, rcost_1_14==3, 
obstacle(rx_1_14 + 0, ry_1_14 + 0)==False, 
obstacle(rx_1_14 + 0, ry_1_14 + -1)==False, 
obstacle(rx_1_14 + 0, ry_1_14 + -2)==False, 
)))
s.add(Or(rprim_1_14!=14,
And(rx_f_1_14==2, ry_f_1_14==2, rcost_1_14==4, 
obstacle(rx_1_14 + 0, ry_1_14 + 0)==False, 
obstacle(rx_1_14 + 1, ry_1_14 + 1)==False, 
obstacle(rx_1_14 + 2, ry_1_14 + 2)==False, 
)))
s.add(Or(rprim_1_14!=15,
And(rx_f_1_14==-2, ry_f_1_14==2, rcost_1_14==4, 
obstacle(rx_1_14 + 0, ry_1_14 + 0)==False, 
obstacle(rx_1_14 + -1, ry_1_14 + 1)==False, 
obstacle(rx_1_14 + -2, ry_1_14 + 2)==False, 
)))
s.add(Or(rprim_1_14!=16,
And(rx_f_1_14==-2, ry_f_1_14==-2, rcost_1_14==4, 
obstacle(rx_1_14 + 0, ry_1_14 + 0)==False, 
obstacle(rx_1_14 + -1, ry_1_14 + -1)==False, 
obstacle(rx_1_14 + -2, ry_1_14 + -2)==False, 
)))
s.add(Or(rprim_1_14!=17,
And(rx_f_1_14==2, ry_f_1_14==-2, rcost_1_14==4, 
obstacle(rx_1_14 + 0, ry_1_14 + 0)==False, 
obstacle(rx_1_14 + 1, ry_1_14 + -1)==False, 
obstacle(rx_1_14 + 2, ry_1_14 + -2)==False, 
)))
s.add(Or(rprim_1_14!=18,
And(rx_f_1_14==3, ry_f_1_14==0, rcost_1_14==4, 
obstacle(rx_1_14 + 0, ry_1_14 + 0)==False, 
obstacle(rx_1_14 + 1, ry_1_14 + 0)==False, 
obstacle(rx_1_14 + 2, ry_1_14 + 0)==False, 
obstacle(rx_1_14 + 3, ry_1_14 + 0)==False, 
)))
s.add(Or(rprim_1_14!=19,
And(rx_f_1_14==0, ry_f_1_14==3, rcost_1_14==4, 
obstacle(rx_1_14 + 0, ry_1_14 + 0)==False, 
obstacle(rx_1_14 + 0, ry_1_14 + 1)==False, 
obstacle(rx_1_14 + 0, ry_1_14 + 2)==False, 
obstacle(rx_1_14 + 0, ry_1_14 + 3)==False, 
)))
s.add(Or(rprim_1_14!=20,
And(rx_f_1_14==-3, ry_f_1_14==0, rcost_1_14==4, 
obstacle(rx_1_14 + 0, ry_1_14 + 0)==False, 
obstacle(rx_1_14 + -1, ry_1_14 + 0)==False, 
obstacle(rx_1_14 + -2, ry_1_14 + 0)==False, 
obstacle(rx_1_14 + -3, ry_1_14 + 0)==False, 
)))
s.add(Or(rprim_1_14!=21,
And(rx_f_1_14==0, ry_f_1_14==-3, rcost_1_14==4, 
obstacle(rx_1_14 + 0, ry_1_14 + 0)==False, 
obstacle(rx_1_14 + 0, ry_1_14 + -1)==False, 
obstacle(rx_1_14 + 0, ry_1_14 + -2)==False, 
obstacle(rx_1_14 + 0, ry_1_14 + -3)==False, 
)))
s.add(Or(rprim_1_15!=1,
And(rx_f_1_15==0, ry_f_1_15==0, rcost_1_15==0, 
obstacle(rx_1_15 + 0, ry_1_15 + 0)==False, 
)))
s.add(Or(rprim_1_15!=2,
And(rx_f_1_15==1, ry_f_1_15==0, rcost_1_15==2, 
obstacle(rx_1_15 + 0, ry_1_15 + 0)==False, 
obstacle(rx_1_15 + 1, ry_1_15 + 0)==False, 
)))
s.add(Or(rprim_1_15!=3,
And(rx_f_1_15==0, ry_f_1_15==-1, rcost_1_15==2, 
obstacle(rx_1_15 + 0, ry_1_15 + 0)==False, 
obstacle(rx_1_15 + 0, ry_1_15 + -1)==False, 
)))
s.add(Or(rprim_1_15!=4,
And(rx_f_1_15==-1, ry_f_1_15==0, rcost_1_15==2, 
obstacle(rx_1_15 + 0, ry_1_15 + 0)==False, 
obstacle(rx_1_15 + -1, ry_1_15 + 0)==False, 
)))
s.add(Or(rprim_1_15!=5,
And(rx_f_1_15==0, ry_f_1_15==1, rcost_1_15==2, 
obstacle(rx_1_15 + 0, ry_1_15 + 0)==False, 
obstacle(rx_1_15 + 0, ry_1_15 + 1)==False, 
)))
s.add(Or(rprim_1_15!=6,
And(rx_f_1_15==1, ry_f_1_15==1, rcost_1_15==3, 
obstacle(rx_1_15 + 0, ry_1_15 + 0)==False, 
obstacle(rx_1_15 + 1, ry_1_15 + 1)==False, 
)))
s.add(Or(rprim_1_15!=7,
And(rx_f_1_15==-1, ry_f_1_15==1, rcost_1_15==3, 
obstacle(rx_1_15 + 0, ry_1_15 + 0)==False, 
obstacle(rx_1_15 + -1, ry_1_15 + 1)==False, 
)))
s.add(Or(rprim_1_15!=8,
And(rx_f_1_15==-1, ry_f_1_15==-1, rcost_1_15==3, 
obstacle(rx_1_15 + 0, ry_1_15 + 0)==False, 
obstacle(rx_1_15 + -1, ry_1_15 + -1)==False, 
)))
s.add(Or(rprim_1_15!=9,
And(rx_f_1_15==1, ry_f_1_15==-1, rcost_1_15==3, 
obstacle(rx_1_15 + 0, ry_1_15 + 0)==False, 
obstacle(rx_1_15 + 1, ry_1_15 + -1)==False, 
)))
s.add(Or(rprim_1_15!=10,
And(rx_f_1_15==2, ry_f_1_15==0, rcost_1_15==3, 
obstacle(rx_1_15 + 0, ry_1_15 + 0)==False, 
obstacle(rx_1_15 + 1, ry_1_15 + 0)==False, 
obstacle(rx_1_15 + 2, ry_1_15 + 0)==False, 
)))
s.add(Or(rprim_1_15!=11,
And(rx_f_1_15==0, ry_f_1_15==2, rcost_1_15==3, 
obstacle(rx_1_15 + 0, ry_1_15 + 0)==False, 
obstacle(rx_1_15 + 0, ry_1_15 + 1)==False, 
obstacle(rx_1_15 + 0, ry_1_15 + 2)==False, 
)))
s.add(Or(rprim_1_15!=12,
And(rx_f_1_15==-2, ry_f_1_15==0, rcost_1_15==3, 
obstacle(rx_1_15 + 0, ry_1_15 + 0)==False, 
obstacle(rx_1_15 + -1, ry_1_15 + 0)==False, 
obstacle(rx_1_15 + -2, ry_1_15 + 0)==False, 
)))
s.add(Or(rprim_1_15!=13,
And(rx_f_1_15==0, ry_f_1_15==-2, rcost_1_15==3, 
obstacle(rx_1_15 + 0, ry_1_15 + 0)==False, 
obstacle(rx_1_15 + 0, ry_1_15 + -1)==False, 
obstacle(rx_1_15 + 0, ry_1_15 + -2)==False, 
)))
s.add(Or(rprim_1_15!=14,
And(rx_f_1_15==2, ry_f_1_15==2, rcost_1_15==4, 
obstacle(rx_1_15 + 0, ry_1_15 + 0)==False, 
obstacle(rx_1_15 + 1, ry_1_15 + 1)==False, 
obstacle(rx_1_15 + 2, ry_1_15 + 2)==False, 
)))
s.add(Or(rprim_1_15!=15,
And(rx_f_1_15==-2, ry_f_1_15==2, rcost_1_15==4, 
obstacle(rx_1_15 + 0, ry_1_15 + 0)==False, 
obstacle(rx_1_15 + -1, ry_1_15 + 1)==False, 
obstacle(rx_1_15 + -2, ry_1_15 + 2)==False, 
)))
s.add(Or(rprim_1_15!=16,
And(rx_f_1_15==-2, ry_f_1_15==-2, rcost_1_15==4, 
obstacle(rx_1_15 + 0, ry_1_15 + 0)==False, 
obstacle(rx_1_15 + -1, ry_1_15 + -1)==False, 
obstacle(rx_1_15 + -2, ry_1_15 + -2)==False, 
)))
s.add(Or(rprim_1_15!=17,
And(rx_f_1_15==2, ry_f_1_15==-2, rcost_1_15==4, 
obstacle(rx_1_15 + 0, ry_1_15 + 0)==False, 
obstacle(rx_1_15 + 1, ry_1_15 + -1)==False, 
obstacle(rx_1_15 + 2, ry_1_15 + -2)==False, 
)))
s.add(Or(rprim_1_15!=18,
And(rx_f_1_15==3, ry_f_1_15==0, rcost_1_15==4, 
obstacle(rx_1_15 + 0, ry_1_15 + 0)==False, 
obstacle(rx_1_15 + 1, ry_1_15 + 0)==False, 
obstacle(rx_1_15 + 2, ry_1_15 + 0)==False, 
obstacle(rx_1_15 + 3, ry_1_15 + 0)==False, 
)))
s.add(Or(rprim_1_15!=19,
And(rx_f_1_15==0, ry_f_1_15==3, rcost_1_15==4, 
obstacle(rx_1_15 + 0, ry_1_15 + 0)==False, 
obstacle(rx_1_15 + 0, ry_1_15 + 1)==False, 
obstacle(rx_1_15 + 0, ry_1_15 + 2)==False, 
obstacle(rx_1_15 + 0, ry_1_15 + 3)==False, 
)))
s.add(Or(rprim_1_15!=20,
And(rx_f_1_15==-3, ry_f_1_15==0, rcost_1_15==4, 
obstacle(rx_1_15 + 0, ry_1_15 + 0)==False, 
obstacle(rx_1_15 + -1, ry_1_15 + 0)==False, 
obstacle(rx_1_15 + -2, ry_1_15 + 0)==False, 
obstacle(rx_1_15 + -3, ry_1_15 + 0)==False, 
)))
s.add(Or(rprim_1_15!=21,
And(rx_f_1_15==0, ry_f_1_15==-3, rcost_1_15==4, 
obstacle(rx_1_15 + 0, ry_1_15 + 0)==False, 
obstacle(rx_1_15 + 0, ry_1_15 + -1)==False, 
obstacle(rx_1_15 + 0, ry_1_15 + -2)==False, 
obstacle(rx_1_15 + 0, ry_1_15 + -3)==False, 
)))
s.add(Or(rprim_1_16!=1,
And(rx_f_1_16==0, ry_f_1_16==0, rcost_1_16==0, 
obstacle(rx_1_16 + 0, ry_1_16 + 0)==False, 
)))
s.add(Or(rprim_1_16!=2,
And(rx_f_1_16==1, ry_f_1_16==0, rcost_1_16==2, 
obstacle(rx_1_16 + 0, ry_1_16 + 0)==False, 
obstacle(rx_1_16 + 1, ry_1_16 + 0)==False, 
)))
s.add(Or(rprim_1_16!=3,
And(rx_f_1_16==0, ry_f_1_16==-1, rcost_1_16==2, 
obstacle(rx_1_16 + 0, ry_1_16 + 0)==False, 
obstacle(rx_1_16 + 0, ry_1_16 + -1)==False, 
)))
s.add(Or(rprim_1_16!=4,
And(rx_f_1_16==-1, ry_f_1_16==0, rcost_1_16==2, 
obstacle(rx_1_16 + 0, ry_1_16 + 0)==False, 
obstacle(rx_1_16 + -1, ry_1_16 + 0)==False, 
)))
s.add(Or(rprim_1_16!=5,
And(rx_f_1_16==0, ry_f_1_16==1, rcost_1_16==2, 
obstacle(rx_1_16 + 0, ry_1_16 + 0)==False, 
obstacle(rx_1_16 + 0, ry_1_16 + 1)==False, 
)))
s.add(Or(rprim_1_16!=6,
And(rx_f_1_16==1, ry_f_1_16==1, rcost_1_16==3, 
obstacle(rx_1_16 + 0, ry_1_16 + 0)==False, 
obstacle(rx_1_16 + 1, ry_1_16 + 1)==False, 
)))
s.add(Or(rprim_1_16!=7,
And(rx_f_1_16==-1, ry_f_1_16==1, rcost_1_16==3, 
obstacle(rx_1_16 + 0, ry_1_16 + 0)==False, 
obstacle(rx_1_16 + -1, ry_1_16 + 1)==False, 
)))
s.add(Or(rprim_1_16!=8,
And(rx_f_1_16==-1, ry_f_1_16==-1, rcost_1_16==3, 
obstacle(rx_1_16 + 0, ry_1_16 + 0)==False, 
obstacle(rx_1_16 + -1, ry_1_16 + -1)==False, 
)))
s.add(Or(rprim_1_16!=9,
And(rx_f_1_16==1, ry_f_1_16==-1, rcost_1_16==3, 
obstacle(rx_1_16 + 0, ry_1_16 + 0)==False, 
obstacle(rx_1_16 + 1, ry_1_16 + -1)==False, 
)))
s.add(Or(rprim_1_16!=10,
And(rx_f_1_16==2, ry_f_1_16==0, rcost_1_16==3, 
obstacle(rx_1_16 + 0, ry_1_16 + 0)==False, 
obstacle(rx_1_16 + 1, ry_1_16 + 0)==False, 
obstacle(rx_1_16 + 2, ry_1_16 + 0)==False, 
)))
s.add(Or(rprim_1_16!=11,
And(rx_f_1_16==0, ry_f_1_16==2, rcost_1_16==3, 
obstacle(rx_1_16 + 0, ry_1_16 + 0)==False, 
obstacle(rx_1_16 + 0, ry_1_16 + 1)==False, 
obstacle(rx_1_16 + 0, ry_1_16 + 2)==False, 
)))
s.add(Or(rprim_1_16!=12,
And(rx_f_1_16==-2, ry_f_1_16==0, rcost_1_16==3, 
obstacle(rx_1_16 + 0, ry_1_16 + 0)==False, 
obstacle(rx_1_16 + -1, ry_1_16 + 0)==False, 
obstacle(rx_1_16 + -2, ry_1_16 + 0)==False, 
)))
s.add(Or(rprim_1_16!=13,
And(rx_f_1_16==0, ry_f_1_16==-2, rcost_1_16==3, 
obstacle(rx_1_16 + 0, ry_1_16 + 0)==False, 
obstacle(rx_1_16 + 0, ry_1_16 + -1)==False, 
obstacle(rx_1_16 + 0, ry_1_16 + -2)==False, 
)))
s.add(Or(rprim_1_16!=14,
And(rx_f_1_16==2, ry_f_1_16==2, rcost_1_16==4, 
obstacle(rx_1_16 + 0, ry_1_16 + 0)==False, 
obstacle(rx_1_16 + 1, ry_1_16 + 1)==False, 
obstacle(rx_1_16 + 2, ry_1_16 + 2)==False, 
)))
s.add(Or(rprim_1_16!=15,
And(rx_f_1_16==-2, ry_f_1_16==2, rcost_1_16==4, 
obstacle(rx_1_16 + 0, ry_1_16 + 0)==False, 
obstacle(rx_1_16 + -1, ry_1_16 + 1)==False, 
obstacle(rx_1_16 + -2, ry_1_16 + 2)==False, 
)))
s.add(Or(rprim_1_16!=16,
And(rx_f_1_16==-2, ry_f_1_16==-2, rcost_1_16==4, 
obstacle(rx_1_16 + 0, ry_1_16 + 0)==False, 
obstacle(rx_1_16 + -1, ry_1_16 + -1)==False, 
obstacle(rx_1_16 + -2, ry_1_16 + -2)==False, 
)))
s.add(Or(rprim_1_16!=17,
And(rx_f_1_16==2, ry_f_1_16==-2, rcost_1_16==4, 
obstacle(rx_1_16 + 0, ry_1_16 + 0)==False, 
obstacle(rx_1_16 + 1, ry_1_16 + -1)==False, 
obstacle(rx_1_16 + 2, ry_1_16 + -2)==False, 
)))
s.add(Or(rprim_1_16!=18,
And(rx_f_1_16==3, ry_f_1_16==0, rcost_1_16==4, 
obstacle(rx_1_16 + 0, ry_1_16 + 0)==False, 
obstacle(rx_1_16 + 1, ry_1_16 + 0)==False, 
obstacle(rx_1_16 + 2, ry_1_16 + 0)==False, 
obstacle(rx_1_16 + 3, ry_1_16 + 0)==False, 
)))
s.add(Or(rprim_1_16!=19,
And(rx_f_1_16==0, ry_f_1_16==3, rcost_1_16==4, 
obstacle(rx_1_16 + 0, ry_1_16 + 0)==False, 
obstacle(rx_1_16 + 0, ry_1_16 + 1)==False, 
obstacle(rx_1_16 + 0, ry_1_16 + 2)==False, 
obstacle(rx_1_16 + 0, ry_1_16 + 3)==False, 
)))
s.add(Or(rprim_1_16!=20,
And(rx_f_1_16==-3, ry_f_1_16==0, rcost_1_16==4, 
obstacle(rx_1_16 + 0, ry_1_16 + 0)==False, 
obstacle(rx_1_16 + -1, ry_1_16 + 0)==False, 
obstacle(rx_1_16 + -2, ry_1_16 + 0)==False, 
obstacle(rx_1_16 + -3, ry_1_16 + 0)==False, 
)))
s.add(Or(rprim_1_16!=21,
And(rx_f_1_16==0, ry_f_1_16==-3, rcost_1_16==4, 
obstacle(rx_1_16 + 0, ry_1_16 + 0)==False, 
obstacle(rx_1_16 + 0, ry_1_16 + -1)==False, 
obstacle(rx_1_16 + 0, ry_1_16 + -2)==False, 
obstacle(rx_1_16 + 0, ry_1_16 + -3)==False, 
)))
s.add(Or(rprim_1_17!=1,
And(rx_f_1_17==0, ry_f_1_17==0, rcost_1_17==0, 
obstacle(rx_1_17 + 0, ry_1_17 + 0)==False, 
)))
s.add(Or(rprim_1_17!=2,
And(rx_f_1_17==1, ry_f_1_17==0, rcost_1_17==2, 
obstacle(rx_1_17 + 0, ry_1_17 + 0)==False, 
obstacle(rx_1_17 + 1, ry_1_17 + 0)==False, 
)))
s.add(Or(rprim_1_17!=3,
And(rx_f_1_17==0, ry_f_1_17==-1, rcost_1_17==2, 
obstacle(rx_1_17 + 0, ry_1_17 + 0)==False, 
obstacle(rx_1_17 + 0, ry_1_17 + -1)==False, 
)))
s.add(Or(rprim_1_17!=4,
And(rx_f_1_17==-1, ry_f_1_17==0, rcost_1_17==2, 
obstacle(rx_1_17 + 0, ry_1_17 + 0)==False, 
obstacle(rx_1_17 + -1, ry_1_17 + 0)==False, 
)))
s.add(Or(rprim_1_17!=5,
And(rx_f_1_17==0, ry_f_1_17==1, rcost_1_17==2, 
obstacle(rx_1_17 + 0, ry_1_17 + 0)==False, 
obstacle(rx_1_17 + 0, ry_1_17 + 1)==False, 
)))
s.add(Or(rprim_1_17!=6,
And(rx_f_1_17==1, ry_f_1_17==1, rcost_1_17==3, 
obstacle(rx_1_17 + 0, ry_1_17 + 0)==False, 
obstacle(rx_1_17 + 1, ry_1_17 + 1)==False, 
)))
s.add(Or(rprim_1_17!=7,
And(rx_f_1_17==-1, ry_f_1_17==1, rcost_1_17==3, 
obstacle(rx_1_17 + 0, ry_1_17 + 0)==False, 
obstacle(rx_1_17 + -1, ry_1_17 + 1)==False, 
)))
s.add(Or(rprim_1_17!=8,
And(rx_f_1_17==-1, ry_f_1_17==-1, rcost_1_17==3, 
obstacle(rx_1_17 + 0, ry_1_17 + 0)==False, 
obstacle(rx_1_17 + -1, ry_1_17 + -1)==False, 
)))
s.add(Or(rprim_1_17!=9,
And(rx_f_1_17==1, ry_f_1_17==-1, rcost_1_17==3, 
obstacle(rx_1_17 + 0, ry_1_17 + 0)==False, 
obstacle(rx_1_17 + 1, ry_1_17 + -1)==False, 
)))
s.add(Or(rprim_1_17!=10,
And(rx_f_1_17==2, ry_f_1_17==0, rcost_1_17==3, 
obstacle(rx_1_17 + 0, ry_1_17 + 0)==False, 
obstacle(rx_1_17 + 1, ry_1_17 + 0)==False, 
obstacle(rx_1_17 + 2, ry_1_17 + 0)==False, 
)))
s.add(Or(rprim_1_17!=11,
And(rx_f_1_17==0, ry_f_1_17==2, rcost_1_17==3, 
obstacle(rx_1_17 + 0, ry_1_17 + 0)==False, 
obstacle(rx_1_17 + 0, ry_1_17 + 1)==False, 
obstacle(rx_1_17 + 0, ry_1_17 + 2)==False, 
)))
s.add(Or(rprim_1_17!=12,
And(rx_f_1_17==-2, ry_f_1_17==0, rcost_1_17==3, 
obstacle(rx_1_17 + 0, ry_1_17 + 0)==False, 
obstacle(rx_1_17 + -1, ry_1_17 + 0)==False, 
obstacle(rx_1_17 + -2, ry_1_17 + 0)==False, 
)))
s.add(Or(rprim_1_17!=13,
And(rx_f_1_17==0, ry_f_1_17==-2, rcost_1_17==3, 
obstacle(rx_1_17 + 0, ry_1_17 + 0)==False, 
obstacle(rx_1_17 + 0, ry_1_17 + -1)==False, 
obstacle(rx_1_17 + 0, ry_1_17 + -2)==False, 
)))
s.add(Or(rprim_1_17!=14,
And(rx_f_1_17==2, ry_f_1_17==2, rcost_1_17==4, 
obstacle(rx_1_17 + 0, ry_1_17 + 0)==False, 
obstacle(rx_1_17 + 1, ry_1_17 + 1)==False, 
obstacle(rx_1_17 + 2, ry_1_17 + 2)==False, 
)))
s.add(Or(rprim_1_17!=15,
And(rx_f_1_17==-2, ry_f_1_17==2, rcost_1_17==4, 
obstacle(rx_1_17 + 0, ry_1_17 + 0)==False, 
obstacle(rx_1_17 + -1, ry_1_17 + 1)==False, 
obstacle(rx_1_17 + -2, ry_1_17 + 2)==False, 
)))
s.add(Or(rprim_1_17!=16,
And(rx_f_1_17==-2, ry_f_1_17==-2, rcost_1_17==4, 
obstacle(rx_1_17 + 0, ry_1_17 + 0)==False, 
obstacle(rx_1_17 + -1, ry_1_17 + -1)==False, 
obstacle(rx_1_17 + -2, ry_1_17 + -2)==False, 
)))
s.add(Or(rprim_1_17!=17,
And(rx_f_1_17==2, ry_f_1_17==-2, rcost_1_17==4, 
obstacle(rx_1_17 + 0, ry_1_17 + 0)==False, 
obstacle(rx_1_17 + 1, ry_1_17 + -1)==False, 
obstacle(rx_1_17 + 2, ry_1_17 + -2)==False, 
)))
s.add(Or(rprim_1_17!=18,
And(rx_f_1_17==3, ry_f_1_17==0, rcost_1_17==4, 
obstacle(rx_1_17 + 0, ry_1_17 + 0)==False, 
obstacle(rx_1_17 + 1, ry_1_17 + 0)==False, 
obstacle(rx_1_17 + 2, ry_1_17 + 0)==False, 
obstacle(rx_1_17 + 3, ry_1_17 + 0)==False, 
)))
s.add(Or(rprim_1_17!=19,
And(rx_f_1_17==0, ry_f_1_17==3, rcost_1_17==4, 
obstacle(rx_1_17 + 0, ry_1_17 + 0)==False, 
obstacle(rx_1_17 + 0, ry_1_17 + 1)==False, 
obstacle(rx_1_17 + 0, ry_1_17 + 2)==False, 
obstacle(rx_1_17 + 0, ry_1_17 + 3)==False, 
)))
s.add(Or(rprim_1_17!=20,
And(rx_f_1_17==-3, ry_f_1_17==0, rcost_1_17==4, 
obstacle(rx_1_17 + 0, ry_1_17 + 0)==False, 
obstacle(rx_1_17 + -1, ry_1_17 + 0)==False, 
obstacle(rx_1_17 + -2, ry_1_17 + 0)==False, 
obstacle(rx_1_17 + -3, ry_1_17 + 0)==False, 
)))
s.add(Or(rprim_1_17!=21,
And(rx_f_1_17==0, ry_f_1_17==-3, rcost_1_17==4, 
obstacle(rx_1_17 + 0, ry_1_17 + 0)==False, 
obstacle(rx_1_17 + 0, ry_1_17 + -1)==False, 
obstacle(rx_1_17 + 0, ry_1_17 + -2)==False, 
obstacle(rx_1_17 + 0, ry_1_17 + -3)==False, 
)))
s.add(Or(rprim_1_18!=1,
And(rx_f_1_18==0, ry_f_1_18==0, rcost_1_18==0, 
obstacle(rx_1_18 + 0, ry_1_18 + 0)==False, 
)))
s.add(Or(rprim_1_18!=2,
And(rx_f_1_18==1, ry_f_1_18==0, rcost_1_18==2, 
obstacle(rx_1_18 + 0, ry_1_18 + 0)==False, 
obstacle(rx_1_18 + 1, ry_1_18 + 0)==False, 
)))
s.add(Or(rprim_1_18!=3,
And(rx_f_1_18==0, ry_f_1_18==-1, rcost_1_18==2, 
obstacle(rx_1_18 + 0, ry_1_18 + 0)==False, 
obstacle(rx_1_18 + 0, ry_1_18 + -1)==False, 
)))
s.add(Or(rprim_1_18!=4,
And(rx_f_1_18==-1, ry_f_1_18==0, rcost_1_18==2, 
obstacle(rx_1_18 + 0, ry_1_18 + 0)==False, 
obstacle(rx_1_18 + -1, ry_1_18 + 0)==False, 
)))
s.add(Or(rprim_1_18!=5,
And(rx_f_1_18==0, ry_f_1_18==1, rcost_1_18==2, 
obstacle(rx_1_18 + 0, ry_1_18 + 0)==False, 
obstacle(rx_1_18 + 0, ry_1_18 + 1)==False, 
)))
s.add(Or(rprim_1_18!=6,
And(rx_f_1_18==1, ry_f_1_18==1, rcost_1_18==3, 
obstacle(rx_1_18 + 0, ry_1_18 + 0)==False, 
obstacle(rx_1_18 + 1, ry_1_18 + 1)==False, 
)))
s.add(Or(rprim_1_18!=7,
And(rx_f_1_18==-1, ry_f_1_18==1, rcost_1_18==3, 
obstacle(rx_1_18 + 0, ry_1_18 + 0)==False, 
obstacle(rx_1_18 + -1, ry_1_18 + 1)==False, 
)))
s.add(Or(rprim_1_18!=8,
And(rx_f_1_18==-1, ry_f_1_18==-1, rcost_1_18==3, 
obstacle(rx_1_18 + 0, ry_1_18 + 0)==False, 
obstacle(rx_1_18 + -1, ry_1_18 + -1)==False, 
)))
s.add(Or(rprim_1_18!=9,
And(rx_f_1_18==1, ry_f_1_18==-1, rcost_1_18==3, 
obstacle(rx_1_18 + 0, ry_1_18 + 0)==False, 
obstacle(rx_1_18 + 1, ry_1_18 + -1)==False, 
)))
s.add(Or(rprim_1_18!=10,
And(rx_f_1_18==2, ry_f_1_18==0, rcost_1_18==3, 
obstacle(rx_1_18 + 0, ry_1_18 + 0)==False, 
obstacle(rx_1_18 + 1, ry_1_18 + 0)==False, 
obstacle(rx_1_18 + 2, ry_1_18 + 0)==False, 
)))
s.add(Or(rprim_1_18!=11,
And(rx_f_1_18==0, ry_f_1_18==2, rcost_1_18==3, 
obstacle(rx_1_18 + 0, ry_1_18 + 0)==False, 
obstacle(rx_1_18 + 0, ry_1_18 + 1)==False, 
obstacle(rx_1_18 + 0, ry_1_18 + 2)==False, 
)))
s.add(Or(rprim_1_18!=12,
And(rx_f_1_18==-2, ry_f_1_18==0, rcost_1_18==3, 
obstacle(rx_1_18 + 0, ry_1_18 + 0)==False, 
obstacle(rx_1_18 + -1, ry_1_18 + 0)==False, 
obstacle(rx_1_18 + -2, ry_1_18 + 0)==False, 
)))
s.add(Or(rprim_1_18!=13,
And(rx_f_1_18==0, ry_f_1_18==-2, rcost_1_18==3, 
obstacle(rx_1_18 + 0, ry_1_18 + 0)==False, 
obstacle(rx_1_18 + 0, ry_1_18 + -1)==False, 
obstacle(rx_1_18 + 0, ry_1_18 + -2)==False, 
)))
s.add(Or(rprim_1_18!=14,
And(rx_f_1_18==2, ry_f_1_18==2, rcost_1_18==4, 
obstacle(rx_1_18 + 0, ry_1_18 + 0)==False, 
obstacle(rx_1_18 + 1, ry_1_18 + 1)==False, 
obstacle(rx_1_18 + 2, ry_1_18 + 2)==False, 
)))
s.add(Or(rprim_1_18!=15,
And(rx_f_1_18==-2, ry_f_1_18==2, rcost_1_18==4, 
obstacle(rx_1_18 + 0, ry_1_18 + 0)==False, 
obstacle(rx_1_18 + -1, ry_1_18 + 1)==False, 
obstacle(rx_1_18 + -2, ry_1_18 + 2)==False, 
)))
s.add(Or(rprim_1_18!=16,
And(rx_f_1_18==-2, ry_f_1_18==-2, rcost_1_18==4, 
obstacle(rx_1_18 + 0, ry_1_18 + 0)==False, 
obstacle(rx_1_18 + -1, ry_1_18 + -1)==False, 
obstacle(rx_1_18 + -2, ry_1_18 + -2)==False, 
)))
s.add(Or(rprim_1_18!=17,
And(rx_f_1_18==2, ry_f_1_18==-2, rcost_1_18==4, 
obstacle(rx_1_18 + 0, ry_1_18 + 0)==False, 
obstacle(rx_1_18 + 1, ry_1_18 + -1)==False, 
obstacle(rx_1_18 + 2, ry_1_18 + -2)==False, 
)))
s.add(Or(rprim_1_18!=18,
And(rx_f_1_18==3, ry_f_1_18==0, rcost_1_18==4, 
obstacle(rx_1_18 + 0, ry_1_18 + 0)==False, 
obstacle(rx_1_18 + 1, ry_1_18 + 0)==False, 
obstacle(rx_1_18 + 2, ry_1_18 + 0)==False, 
obstacle(rx_1_18 + 3, ry_1_18 + 0)==False, 
)))
s.add(Or(rprim_1_18!=19,
And(rx_f_1_18==0, ry_f_1_18==3, rcost_1_18==4, 
obstacle(rx_1_18 + 0, ry_1_18 + 0)==False, 
obstacle(rx_1_18 + 0, ry_1_18 + 1)==False, 
obstacle(rx_1_18 + 0, ry_1_18 + 2)==False, 
obstacle(rx_1_18 + 0, ry_1_18 + 3)==False, 
)))
s.add(Or(rprim_1_18!=20,
And(rx_f_1_18==-3, ry_f_1_18==0, rcost_1_18==4, 
obstacle(rx_1_18 + 0, ry_1_18 + 0)==False, 
obstacle(rx_1_18 + -1, ry_1_18 + 0)==False, 
obstacle(rx_1_18 + -2, ry_1_18 + 0)==False, 
obstacle(rx_1_18 + -3, ry_1_18 + 0)==False, 
)))
s.add(Or(rprim_1_18!=21,
And(rx_f_1_18==0, ry_f_1_18==-3, rcost_1_18==4, 
obstacle(rx_1_18 + 0, ry_1_18 + 0)==False, 
obstacle(rx_1_18 + 0, ry_1_18 + -1)==False, 
obstacle(rx_1_18 + 0, ry_1_18 + -2)==False, 
obstacle(rx_1_18 + 0, ry_1_18 + -3)==False, 
)))
s.add(Or(rprim_1_19!=1,
And(rx_f_1_19==0, ry_f_1_19==0, rcost_1_19==0, 
obstacle(rx_1_19 + 0, ry_1_19 + 0)==False, 
)))
s.add(Or(rprim_1_19!=2,
And(rx_f_1_19==1, ry_f_1_19==0, rcost_1_19==2, 
obstacle(rx_1_19 + 0, ry_1_19 + 0)==False, 
obstacle(rx_1_19 + 1, ry_1_19 + 0)==False, 
)))
s.add(Or(rprim_1_19!=3,
And(rx_f_1_19==0, ry_f_1_19==-1, rcost_1_19==2, 
obstacle(rx_1_19 + 0, ry_1_19 + 0)==False, 
obstacle(rx_1_19 + 0, ry_1_19 + -1)==False, 
)))
s.add(Or(rprim_1_19!=4,
And(rx_f_1_19==-1, ry_f_1_19==0, rcost_1_19==2, 
obstacle(rx_1_19 + 0, ry_1_19 + 0)==False, 
obstacle(rx_1_19 + -1, ry_1_19 + 0)==False, 
)))
s.add(Or(rprim_1_19!=5,
And(rx_f_1_19==0, ry_f_1_19==1, rcost_1_19==2, 
obstacle(rx_1_19 + 0, ry_1_19 + 0)==False, 
obstacle(rx_1_19 + 0, ry_1_19 + 1)==False, 
)))
s.add(Or(rprim_1_19!=6,
And(rx_f_1_19==1, ry_f_1_19==1, rcost_1_19==3, 
obstacle(rx_1_19 + 0, ry_1_19 + 0)==False, 
obstacle(rx_1_19 + 1, ry_1_19 + 1)==False, 
)))
s.add(Or(rprim_1_19!=7,
And(rx_f_1_19==-1, ry_f_1_19==1, rcost_1_19==3, 
obstacle(rx_1_19 + 0, ry_1_19 + 0)==False, 
obstacle(rx_1_19 + -1, ry_1_19 + 1)==False, 
)))
s.add(Or(rprim_1_19!=8,
And(rx_f_1_19==-1, ry_f_1_19==-1, rcost_1_19==3, 
obstacle(rx_1_19 + 0, ry_1_19 + 0)==False, 
obstacle(rx_1_19 + -1, ry_1_19 + -1)==False, 
)))
s.add(Or(rprim_1_19!=9,
And(rx_f_1_19==1, ry_f_1_19==-1, rcost_1_19==3, 
obstacle(rx_1_19 + 0, ry_1_19 + 0)==False, 
obstacle(rx_1_19 + 1, ry_1_19 + -1)==False, 
)))
s.add(Or(rprim_1_19!=10,
And(rx_f_1_19==2, ry_f_1_19==0, rcost_1_19==3, 
obstacle(rx_1_19 + 0, ry_1_19 + 0)==False, 
obstacle(rx_1_19 + 1, ry_1_19 + 0)==False, 
obstacle(rx_1_19 + 2, ry_1_19 + 0)==False, 
)))
s.add(Or(rprim_1_19!=11,
And(rx_f_1_19==0, ry_f_1_19==2, rcost_1_19==3, 
obstacle(rx_1_19 + 0, ry_1_19 + 0)==False, 
obstacle(rx_1_19 + 0, ry_1_19 + 1)==False, 
obstacle(rx_1_19 + 0, ry_1_19 + 2)==False, 
)))
s.add(Or(rprim_1_19!=12,
And(rx_f_1_19==-2, ry_f_1_19==0, rcost_1_19==3, 
obstacle(rx_1_19 + 0, ry_1_19 + 0)==False, 
obstacle(rx_1_19 + -1, ry_1_19 + 0)==False, 
obstacle(rx_1_19 + -2, ry_1_19 + 0)==False, 
)))
s.add(Or(rprim_1_19!=13,
And(rx_f_1_19==0, ry_f_1_19==-2, rcost_1_19==3, 
obstacle(rx_1_19 + 0, ry_1_19 + 0)==False, 
obstacle(rx_1_19 + 0, ry_1_19 + -1)==False, 
obstacle(rx_1_19 + 0, ry_1_19 + -2)==False, 
)))
s.add(Or(rprim_1_19!=14,
And(rx_f_1_19==2, ry_f_1_19==2, rcost_1_19==4, 
obstacle(rx_1_19 + 0, ry_1_19 + 0)==False, 
obstacle(rx_1_19 + 1, ry_1_19 + 1)==False, 
obstacle(rx_1_19 + 2, ry_1_19 + 2)==False, 
)))
s.add(Or(rprim_1_19!=15,
And(rx_f_1_19==-2, ry_f_1_19==2, rcost_1_19==4, 
obstacle(rx_1_19 + 0, ry_1_19 + 0)==False, 
obstacle(rx_1_19 + -1, ry_1_19 + 1)==False, 
obstacle(rx_1_19 + -2, ry_1_19 + 2)==False, 
)))
s.add(Or(rprim_1_19!=16,
And(rx_f_1_19==-2, ry_f_1_19==-2, rcost_1_19==4, 
obstacle(rx_1_19 + 0, ry_1_19 + 0)==False, 
obstacle(rx_1_19 + -1, ry_1_19 + -1)==False, 
obstacle(rx_1_19 + -2, ry_1_19 + -2)==False, 
)))
s.add(Or(rprim_1_19!=17,
And(rx_f_1_19==2, ry_f_1_19==-2, rcost_1_19==4, 
obstacle(rx_1_19 + 0, ry_1_19 + 0)==False, 
obstacle(rx_1_19 + 1, ry_1_19 + -1)==False, 
obstacle(rx_1_19 + 2, ry_1_19 + -2)==False, 
)))
s.add(Or(rprim_1_19!=18,
And(rx_f_1_19==3, ry_f_1_19==0, rcost_1_19==4, 
obstacle(rx_1_19 + 0, ry_1_19 + 0)==False, 
obstacle(rx_1_19 + 1, ry_1_19 + 0)==False, 
obstacle(rx_1_19 + 2, ry_1_19 + 0)==False, 
obstacle(rx_1_19 + 3, ry_1_19 + 0)==False, 
)))
s.add(Or(rprim_1_19!=19,
And(rx_f_1_19==0, ry_f_1_19==3, rcost_1_19==4, 
obstacle(rx_1_19 + 0, ry_1_19 + 0)==False, 
obstacle(rx_1_19 + 0, ry_1_19 + 1)==False, 
obstacle(rx_1_19 + 0, ry_1_19 + 2)==False, 
obstacle(rx_1_19 + 0, ry_1_19 + 3)==False, 
)))
s.add(Or(rprim_1_19!=20,
And(rx_f_1_19==-3, ry_f_1_19==0, rcost_1_19==4, 
obstacle(rx_1_19 + 0, ry_1_19 + 0)==False, 
obstacle(rx_1_19 + -1, ry_1_19 + 0)==False, 
obstacle(rx_1_19 + -2, ry_1_19 + 0)==False, 
obstacle(rx_1_19 + -3, ry_1_19 + 0)==False, 
)))
s.add(Or(rprim_1_19!=21,
And(rx_f_1_19==0, ry_f_1_19==-3, rcost_1_19==4, 
obstacle(rx_1_19 + 0, ry_1_19 + 0)==False, 
obstacle(rx_1_19 + 0, ry_1_19 + -1)==False, 
obstacle(rx_1_19 + 0, ry_1_19 + -2)==False, 
obstacle(rx_1_19 + 0, ry_1_19 + -3)==False, 
)))
s.add(Or(rprim_1_20!=1,
And(rx_f_1_20==0, ry_f_1_20==0, rcost_1_20==0, 
obstacle(rx_1_20 + 0, ry_1_20 + 0)==False, 
)))
s.add(Or(rprim_1_20!=2,
And(rx_f_1_20==1, ry_f_1_20==0, rcost_1_20==2, 
obstacle(rx_1_20 + 0, ry_1_20 + 0)==False, 
obstacle(rx_1_20 + 1, ry_1_20 + 0)==False, 
)))
s.add(Or(rprim_1_20!=3,
And(rx_f_1_20==0, ry_f_1_20==-1, rcost_1_20==2, 
obstacle(rx_1_20 + 0, ry_1_20 + 0)==False, 
obstacle(rx_1_20 + 0, ry_1_20 + -1)==False, 
)))
s.add(Or(rprim_1_20!=4,
And(rx_f_1_20==-1, ry_f_1_20==0, rcost_1_20==2, 
obstacle(rx_1_20 + 0, ry_1_20 + 0)==False, 
obstacle(rx_1_20 + -1, ry_1_20 + 0)==False, 
)))
s.add(Or(rprim_1_20!=5,
And(rx_f_1_20==0, ry_f_1_20==1, rcost_1_20==2, 
obstacle(rx_1_20 + 0, ry_1_20 + 0)==False, 
obstacle(rx_1_20 + 0, ry_1_20 + 1)==False, 
)))
s.add(Or(rprim_1_20!=6,
And(rx_f_1_20==1, ry_f_1_20==1, rcost_1_20==3, 
obstacle(rx_1_20 + 0, ry_1_20 + 0)==False, 
obstacle(rx_1_20 + 1, ry_1_20 + 1)==False, 
)))
s.add(Or(rprim_1_20!=7,
And(rx_f_1_20==-1, ry_f_1_20==1, rcost_1_20==3, 
obstacle(rx_1_20 + 0, ry_1_20 + 0)==False, 
obstacle(rx_1_20 + -1, ry_1_20 + 1)==False, 
)))
s.add(Or(rprim_1_20!=8,
And(rx_f_1_20==-1, ry_f_1_20==-1, rcost_1_20==3, 
obstacle(rx_1_20 + 0, ry_1_20 + 0)==False, 
obstacle(rx_1_20 + -1, ry_1_20 + -1)==False, 
)))
s.add(Or(rprim_1_20!=9,
And(rx_f_1_20==1, ry_f_1_20==-1, rcost_1_20==3, 
obstacle(rx_1_20 + 0, ry_1_20 + 0)==False, 
obstacle(rx_1_20 + 1, ry_1_20 + -1)==False, 
)))
s.add(Or(rprim_1_20!=10,
And(rx_f_1_20==2, ry_f_1_20==0, rcost_1_20==3, 
obstacle(rx_1_20 + 0, ry_1_20 + 0)==False, 
obstacle(rx_1_20 + 1, ry_1_20 + 0)==False, 
obstacle(rx_1_20 + 2, ry_1_20 + 0)==False, 
)))
s.add(Or(rprim_1_20!=11,
And(rx_f_1_20==0, ry_f_1_20==2, rcost_1_20==3, 
obstacle(rx_1_20 + 0, ry_1_20 + 0)==False, 
obstacle(rx_1_20 + 0, ry_1_20 + 1)==False, 
obstacle(rx_1_20 + 0, ry_1_20 + 2)==False, 
)))
s.add(Or(rprim_1_20!=12,
And(rx_f_1_20==-2, ry_f_1_20==0, rcost_1_20==3, 
obstacle(rx_1_20 + 0, ry_1_20 + 0)==False, 
obstacle(rx_1_20 + -1, ry_1_20 + 0)==False, 
obstacle(rx_1_20 + -2, ry_1_20 + 0)==False, 
)))
s.add(Or(rprim_1_20!=13,
And(rx_f_1_20==0, ry_f_1_20==-2, rcost_1_20==3, 
obstacle(rx_1_20 + 0, ry_1_20 + 0)==False, 
obstacle(rx_1_20 + 0, ry_1_20 + -1)==False, 
obstacle(rx_1_20 + 0, ry_1_20 + -2)==False, 
)))
s.add(Or(rprim_1_20!=14,
And(rx_f_1_20==2, ry_f_1_20==2, rcost_1_20==4, 
obstacle(rx_1_20 + 0, ry_1_20 + 0)==False, 
obstacle(rx_1_20 + 1, ry_1_20 + 1)==False, 
obstacle(rx_1_20 + 2, ry_1_20 + 2)==False, 
)))
s.add(Or(rprim_1_20!=15,
And(rx_f_1_20==-2, ry_f_1_20==2, rcost_1_20==4, 
obstacle(rx_1_20 + 0, ry_1_20 + 0)==False, 
obstacle(rx_1_20 + -1, ry_1_20 + 1)==False, 
obstacle(rx_1_20 + -2, ry_1_20 + 2)==False, 
)))
s.add(Or(rprim_1_20!=16,
And(rx_f_1_20==-2, ry_f_1_20==-2, rcost_1_20==4, 
obstacle(rx_1_20 + 0, ry_1_20 + 0)==False, 
obstacle(rx_1_20 + -1, ry_1_20 + -1)==False, 
obstacle(rx_1_20 + -2, ry_1_20 + -2)==False, 
)))
s.add(Or(rprim_1_20!=17,
And(rx_f_1_20==2, ry_f_1_20==-2, rcost_1_20==4, 
obstacle(rx_1_20 + 0, ry_1_20 + 0)==False, 
obstacle(rx_1_20 + 1, ry_1_20 + -1)==False, 
obstacle(rx_1_20 + 2, ry_1_20 + -2)==False, 
)))
s.add(Or(rprim_1_20!=18,
And(rx_f_1_20==3, ry_f_1_20==0, rcost_1_20==4, 
obstacle(rx_1_20 + 0, ry_1_20 + 0)==False, 
obstacle(rx_1_20 + 1, ry_1_20 + 0)==False, 
obstacle(rx_1_20 + 2, ry_1_20 + 0)==False, 
obstacle(rx_1_20 + 3, ry_1_20 + 0)==False, 
)))
s.add(Or(rprim_1_20!=19,
And(rx_f_1_20==0, ry_f_1_20==3, rcost_1_20==4, 
obstacle(rx_1_20 + 0, ry_1_20 + 0)==False, 
obstacle(rx_1_20 + 0, ry_1_20 + 1)==False, 
obstacle(rx_1_20 + 0, ry_1_20 + 2)==False, 
obstacle(rx_1_20 + 0, ry_1_20 + 3)==False, 
)))
s.add(Or(rprim_1_20!=20,
And(rx_f_1_20==-3, ry_f_1_20==0, rcost_1_20==4, 
obstacle(rx_1_20 + 0, ry_1_20 + 0)==False, 
obstacle(rx_1_20 + -1, ry_1_20 + 0)==False, 
obstacle(rx_1_20 + -2, ry_1_20 + 0)==False, 
obstacle(rx_1_20 + -3, ry_1_20 + 0)==False, 
)))
s.add(Or(rprim_1_20!=21,
And(rx_f_1_20==0, ry_f_1_20==-3, rcost_1_20==4, 
obstacle(rx_1_20 + 0, ry_1_20 + 0)==False, 
obstacle(rx_1_20 + 0, ry_1_20 + -1)==False, 
obstacle(rx_1_20 + 0, ry_1_20 + -2)==False, 
obstacle(rx_1_20 + 0, ry_1_20 + -3)==False, 
)))
s.add(Or(rprim_1_21!=1,
And(rx_f_1_21==0, ry_f_1_21==0, rcost_1_21==0, 
obstacle(rx_1_21 + 0, ry_1_21 + 0)==False, 
)))
s.add(Or(rprim_1_21!=2,
And(rx_f_1_21==1, ry_f_1_21==0, rcost_1_21==2, 
obstacle(rx_1_21 + 0, ry_1_21 + 0)==False, 
obstacle(rx_1_21 + 1, ry_1_21 + 0)==False, 
)))
s.add(Or(rprim_1_21!=3,
And(rx_f_1_21==0, ry_f_1_21==-1, rcost_1_21==2, 
obstacle(rx_1_21 + 0, ry_1_21 + 0)==False, 
obstacle(rx_1_21 + 0, ry_1_21 + -1)==False, 
)))
s.add(Or(rprim_1_21!=4,
And(rx_f_1_21==-1, ry_f_1_21==0, rcost_1_21==2, 
obstacle(rx_1_21 + 0, ry_1_21 + 0)==False, 
obstacle(rx_1_21 + -1, ry_1_21 + 0)==False, 
)))
s.add(Or(rprim_1_21!=5,
And(rx_f_1_21==0, ry_f_1_21==1, rcost_1_21==2, 
obstacle(rx_1_21 + 0, ry_1_21 + 0)==False, 
obstacle(rx_1_21 + 0, ry_1_21 + 1)==False, 
)))
s.add(Or(rprim_1_21!=6,
And(rx_f_1_21==1, ry_f_1_21==1, rcost_1_21==3, 
obstacle(rx_1_21 + 0, ry_1_21 + 0)==False, 
obstacle(rx_1_21 + 1, ry_1_21 + 1)==False, 
)))
s.add(Or(rprim_1_21!=7,
And(rx_f_1_21==-1, ry_f_1_21==1, rcost_1_21==3, 
obstacle(rx_1_21 + 0, ry_1_21 + 0)==False, 
obstacle(rx_1_21 + -1, ry_1_21 + 1)==False, 
)))
s.add(Or(rprim_1_21!=8,
And(rx_f_1_21==-1, ry_f_1_21==-1, rcost_1_21==3, 
obstacle(rx_1_21 + 0, ry_1_21 + 0)==False, 
obstacle(rx_1_21 + -1, ry_1_21 + -1)==False, 
)))
s.add(Or(rprim_1_21!=9,
And(rx_f_1_21==1, ry_f_1_21==-1, rcost_1_21==3, 
obstacle(rx_1_21 + 0, ry_1_21 + 0)==False, 
obstacle(rx_1_21 + 1, ry_1_21 + -1)==False, 
)))
s.add(Or(rprim_1_21!=10,
And(rx_f_1_21==2, ry_f_1_21==0, rcost_1_21==3, 
obstacle(rx_1_21 + 0, ry_1_21 + 0)==False, 
obstacle(rx_1_21 + 1, ry_1_21 + 0)==False, 
obstacle(rx_1_21 + 2, ry_1_21 + 0)==False, 
)))
s.add(Or(rprim_1_21!=11,
And(rx_f_1_21==0, ry_f_1_21==2, rcost_1_21==3, 
obstacle(rx_1_21 + 0, ry_1_21 + 0)==False, 
obstacle(rx_1_21 + 0, ry_1_21 + 1)==False, 
obstacle(rx_1_21 + 0, ry_1_21 + 2)==False, 
)))
s.add(Or(rprim_1_21!=12,
And(rx_f_1_21==-2, ry_f_1_21==0, rcost_1_21==3, 
obstacle(rx_1_21 + 0, ry_1_21 + 0)==False, 
obstacle(rx_1_21 + -1, ry_1_21 + 0)==False, 
obstacle(rx_1_21 + -2, ry_1_21 + 0)==False, 
)))
s.add(Or(rprim_1_21!=13,
And(rx_f_1_21==0, ry_f_1_21==-2, rcost_1_21==3, 
obstacle(rx_1_21 + 0, ry_1_21 + 0)==False, 
obstacle(rx_1_21 + 0, ry_1_21 + -1)==False, 
obstacle(rx_1_21 + 0, ry_1_21 + -2)==False, 
)))
s.add(Or(rprim_1_21!=14,
And(rx_f_1_21==2, ry_f_1_21==2, rcost_1_21==4, 
obstacle(rx_1_21 + 0, ry_1_21 + 0)==False, 
obstacle(rx_1_21 + 1, ry_1_21 + 1)==False, 
obstacle(rx_1_21 + 2, ry_1_21 + 2)==False, 
)))
s.add(Or(rprim_1_21!=15,
And(rx_f_1_21==-2, ry_f_1_21==2, rcost_1_21==4, 
obstacle(rx_1_21 + 0, ry_1_21 + 0)==False, 
obstacle(rx_1_21 + -1, ry_1_21 + 1)==False, 
obstacle(rx_1_21 + -2, ry_1_21 + 2)==False, 
)))
s.add(Or(rprim_1_21!=16,
And(rx_f_1_21==-2, ry_f_1_21==-2, rcost_1_21==4, 
obstacle(rx_1_21 + 0, ry_1_21 + 0)==False, 
obstacle(rx_1_21 + -1, ry_1_21 + -1)==False, 
obstacle(rx_1_21 + -2, ry_1_21 + -2)==False, 
)))
s.add(Or(rprim_1_21!=17,
And(rx_f_1_21==2, ry_f_1_21==-2, rcost_1_21==4, 
obstacle(rx_1_21 + 0, ry_1_21 + 0)==False, 
obstacle(rx_1_21 + 1, ry_1_21 + -1)==False, 
obstacle(rx_1_21 + 2, ry_1_21 + -2)==False, 
)))
s.add(Or(rprim_1_21!=18,
And(rx_f_1_21==3, ry_f_1_21==0, rcost_1_21==4, 
obstacle(rx_1_21 + 0, ry_1_21 + 0)==False, 
obstacle(rx_1_21 + 1, ry_1_21 + 0)==False, 
obstacle(rx_1_21 + 2, ry_1_21 + 0)==False, 
obstacle(rx_1_21 + 3, ry_1_21 + 0)==False, 
)))
s.add(Or(rprim_1_21!=19,
And(rx_f_1_21==0, ry_f_1_21==3, rcost_1_21==4, 
obstacle(rx_1_21 + 0, ry_1_21 + 0)==False, 
obstacle(rx_1_21 + 0, ry_1_21 + 1)==False, 
obstacle(rx_1_21 + 0, ry_1_21 + 2)==False, 
obstacle(rx_1_21 + 0, ry_1_21 + 3)==False, 
)))
s.add(Or(rprim_1_21!=20,
And(rx_f_1_21==-3, ry_f_1_21==0, rcost_1_21==4, 
obstacle(rx_1_21 + 0, ry_1_21 + 0)==False, 
obstacle(rx_1_21 + -1, ry_1_21 + 0)==False, 
obstacle(rx_1_21 + -2, ry_1_21 + 0)==False, 
obstacle(rx_1_21 + -3, ry_1_21 + 0)==False, 
)))
s.add(Or(rprim_1_21!=21,
And(rx_f_1_21==0, ry_f_1_21==-3, rcost_1_21==4, 
obstacle(rx_1_21 + 0, ry_1_21 + 0)==False, 
obstacle(rx_1_21 + 0, ry_1_21 + -1)==False, 
obstacle(rx_1_21 + 0, ry_1_21 + -2)==False, 
obstacle(rx_1_21 + 0, ry_1_21 + -3)==False, 
)))
s.add(Or(rprim_1_22!=1,
And(rx_f_1_22==0, ry_f_1_22==0, rcost_1_22==0, 
obstacle(rx_1_22 + 0, ry_1_22 + 0)==False, 
)))
s.add(Or(rprim_1_22!=2,
And(rx_f_1_22==1, ry_f_1_22==0, rcost_1_22==2, 
obstacle(rx_1_22 + 0, ry_1_22 + 0)==False, 
obstacle(rx_1_22 + 1, ry_1_22 + 0)==False, 
)))
s.add(Or(rprim_1_22!=3,
And(rx_f_1_22==0, ry_f_1_22==-1, rcost_1_22==2, 
obstacle(rx_1_22 + 0, ry_1_22 + 0)==False, 
obstacle(rx_1_22 + 0, ry_1_22 + -1)==False, 
)))
s.add(Or(rprim_1_22!=4,
And(rx_f_1_22==-1, ry_f_1_22==0, rcost_1_22==2, 
obstacle(rx_1_22 + 0, ry_1_22 + 0)==False, 
obstacle(rx_1_22 + -1, ry_1_22 + 0)==False, 
)))
s.add(Or(rprim_1_22!=5,
And(rx_f_1_22==0, ry_f_1_22==1, rcost_1_22==2, 
obstacle(rx_1_22 + 0, ry_1_22 + 0)==False, 
obstacle(rx_1_22 + 0, ry_1_22 + 1)==False, 
)))
s.add(Or(rprim_1_22!=6,
And(rx_f_1_22==1, ry_f_1_22==1, rcost_1_22==3, 
obstacle(rx_1_22 + 0, ry_1_22 + 0)==False, 
obstacle(rx_1_22 + 1, ry_1_22 + 1)==False, 
)))
s.add(Or(rprim_1_22!=7,
And(rx_f_1_22==-1, ry_f_1_22==1, rcost_1_22==3, 
obstacle(rx_1_22 + 0, ry_1_22 + 0)==False, 
obstacle(rx_1_22 + -1, ry_1_22 + 1)==False, 
)))
s.add(Or(rprim_1_22!=8,
And(rx_f_1_22==-1, ry_f_1_22==-1, rcost_1_22==3, 
obstacle(rx_1_22 + 0, ry_1_22 + 0)==False, 
obstacle(rx_1_22 + -1, ry_1_22 + -1)==False, 
)))
s.add(Or(rprim_1_22!=9,
And(rx_f_1_22==1, ry_f_1_22==-1, rcost_1_22==3, 
obstacle(rx_1_22 + 0, ry_1_22 + 0)==False, 
obstacle(rx_1_22 + 1, ry_1_22 + -1)==False, 
)))
s.add(Or(rprim_1_22!=10,
And(rx_f_1_22==2, ry_f_1_22==0, rcost_1_22==3, 
obstacle(rx_1_22 + 0, ry_1_22 + 0)==False, 
obstacle(rx_1_22 + 1, ry_1_22 + 0)==False, 
obstacle(rx_1_22 + 2, ry_1_22 + 0)==False, 
)))
s.add(Or(rprim_1_22!=11,
And(rx_f_1_22==0, ry_f_1_22==2, rcost_1_22==3, 
obstacle(rx_1_22 + 0, ry_1_22 + 0)==False, 
obstacle(rx_1_22 + 0, ry_1_22 + 1)==False, 
obstacle(rx_1_22 + 0, ry_1_22 + 2)==False, 
)))
s.add(Or(rprim_1_22!=12,
And(rx_f_1_22==-2, ry_f_1_22==0, rcost_1_22==3, 
obstacle(rx_1_22 + 0, ry_1_22 + 0)==False, 
obstacle(rx_1_22 + -1, ry_1_22 + 0)==False, 
obstacle(rx_1_22 + -2, ry_1_22 + 0)==False, 
)))
s.add(Or(rprim_1_22!=13,
And(rx_f_1_22==0, ry_f_1_22==-2, rcost_1_22==3, 
obstacle(rx_1_22 + 0, ry_1_22 + 0)==False, 
obstacle(rx_1_22 + 0, ry_1_22 + -1)==False, 
obstacle(rx_1_22 + 0, ry_1_22 + -2)==False, 
)))
s.add(Or(rprim_1_22!=14,
And(rx_f_1_22==2, ry_f_1_22==2, rcost_1_22==4, 
obstacle(rx_1_22 + 0, ry_1_22 + 0)==False, 
obstacle(rx_1_22 + 1, ry_1_22 + 1)==False, 
obstacle(rx_1_22 + 2, ry_1_22 + 2)==False, 
)))
s.add(Or(rprim_1_22!=15,
And(rx_f_1_22==-2, ry_f_1_22==2, rcost_1_22==4, 
obstacle(rx_1_22 + 0, ry_1_22 + 0)==False, 
obstacle(rx_1_22 + -1, ry_1_22 + 1)==False, 
obstacle(rx_1_22 + -2, ry_1_22 + 2)==False, 
)))
s.add(Or(rprim_1_22!=16,
And(rx_f_1_22==-2, ry_f_1_22==-2, rcost_1_22==4, 
obstacle(rx_1_22 + 0, ry_1_22 + 0)==False, 
obstacle(rx_1_22 + -1, ry_1_22 + -1)==False, 
obstacle(rx_1_22 + -2, ry_1_22 + -2)==False, 
)))
s.add(Or(rprim_1_22!=17,
And(rx_f_1_22==2, ry_f_1_22==-2, rcost_1_22==4, 
obstacle(rx_1_22 + 0, ry_1_22 + 0)==False, 
obstacle(rx_1_22 + 1, ry_1_22 + -1)==False, 
obstacle(rx_1_22 + 2, ry_1_22 + -2)==False, 
)))
s.add(Or(rprim_1_22!=18,
And(rx_f_1_22==3, ry_f_1_22==0, rcost_1_22==4, 
obstacle(rx_1_22 + 0, ry_1_22 + 0)==False, 
obstacle(rx_1_22 + 1, ry_1_22 + 0)==False, 
obstacle(rx_1_22 + 2, ry_1_22 + 0)==False, 
obstacle(rx_1_22 + 3, ry_1_22 + 0)==False, 
)))
s.add(Or(rprim_1_22!=19,
And(rx_f_1_22==0, ry_f_1_22==3, rcost_1_22==4, 
obstacle(rx_1_22 + 0, ry_1_22 + 0)==False, 
obstacle(rx_1_22 + 0, ry_1_22 + 1)==False, 
obstacle(rx_1_22 + 0, ry_1_22 + 2)==False, 
obstacle(rx_1_22 + 0, ry_1_22 + 3)==False, 
)))
s.add(Or(rprim_1_22!=20,
And(rx_f_1_22==-3, ry_f_1_22==0, rcost_1_22==4, 
obstacle(rx_1_22 + 0, ry_1_22 + 0)==False, 
obstacle(rx_1_22 + -1, ry_1_22 + 0)==False, 
obstacle(rx_1_22 + -2, ry_1_22 + 0)==False, 
obstacle(rx_1_22 + -3, ry_1_22 + 0)==False, 
)))
s.add(Or(rprim_1_22!=21,
And(rx_f_1_22==0, ry_f_1_22==-3, rcost_1_22==4, 
obstacle(rx_1_22 + 0, ry_1_22 + 0)==False, 
obstacle(rx_1_22 + 0, ry_1_22 + -1)==False, 
obstacle(rx_1_22 + 0, ry_1_22 + -2)==False, 
obstacle(rx_1_22 + 0, ry_1_22 + -3)==False, 
)))
s.add(Or(rprim_1_23!=1,
And(rx_f_1_23==0, ry_f_1_23==0, rcost_1_23==0, 
obstacle(rx_1_23 + 0, ry_1_23 + 0)==False, 
)))
s.add(Or(rprim_1_23!=2,
And(rx_f_1_23==1, ry_f_1_23==0, rcost_1_23==2, 
obstacle(rx_1_23 + 0, ry_1_23 + 0)==False, 
obstacle(rx_1_23 + 1, ry_1_23 + 0)==False, 
)))
s.add(Or(rprim_1_23!=3,
And(rx_f_1_23==0, ry_f_1_23==-1, rcost_1_23==2, 
obstacle(rx_1_23 + 0, ry_1_23 + 0)==False, 
obstacle(rx_1_23 + 0, ry_1_23 + -1)==False, 
)))
s.add(Or(rprim_1_23!=4,
And(rx_f_1_23==-1, ry_f_1_23==0, rcost_1_23==2, 
obstacle(rx_1_23 + 0, ry_1_23 + 0)==False, 
obstacle(rx_1_23 + -1, ry_1_23 + 0)==False, 
)))
s.add(Or(rprim_1_23!=5,
And(rx_f_1_23==0, ry_f_1_23==1, rcost_1_23==2, 
obstacle(rx_1_23 + 0, ry_1_23 + 0)==False, 
obstacle(rx_1_23 + 0, ry_1_23 + 1)==False, 
)))
s.add(Or(rprim_1_23!=6,
And(rx_f_1_23==1, ry_f_1_23==1, rcost_1_23==3, 
obstacle(rx_1_23 + 0, ry_1_23 + 0)==False, 
obstacle(rx_1_23 + 1, ry_1_23 + 1)==False, 
)))
s.add(Or(rprim_1_23!=7,
And(rx_f_1_23==-1, ry_f_1_23==1, rcost_1_23==3, 
obstacle(rx_1_23 + 0, ry_1_23 + 0)==False, 
obstacle(rx_1_23 + -1, ry_1_23 + 1)==False, 
)))
s.add(Or(rprim_1_23!=8,
And(rx_f_1_23==-1, ry_f_1_23==-1, rcost_1_23==3, 
obstacle(rx_1_23 + 0, ry_1_23 + 0)==False, 
obstacle(rx_1_23 + -1, ry_1_23 + -1)==False, 
)))
s.add(Or(rprim_1_23!=9,
And(rx_f_1_23==1, ry_f_1_23==-1, rcost_1_23==3, 
obstacle(rx_1_23 + 0, ry_1_23 + 0)==False, 
obstacle(rx_1_23 + 1, ry_1_23 + -1)==False, 
)))
s.add(Or(rprim_1_23!=10,
And(rx_f_1_23==2, ry_f_1_23==0, rcost_1_23==3, 
obstacle(rx_1_23 + 0, ry_1_23 + 0)==False, 
obstacle(rx_1_23 + 1, ry_1_23 + 0)==False, 
obstacle(rx_1_23 + 2, ry_1_23 + 0)==False, 
)))
s.add(Or(rprim_1_23!=11,
And(rx_f_1_23==0, ry_f_1_23==2, rcost_1_23==3, 
obstacle(rx_1_23 + 0, ry_1_23 + 0)==False, 
obstacle(rx_1_23 + 0, ry_1_23 + 1)==False, 
obstacle(rx_1_23 + 0, ry_1_23 + 2)==False, 
)))
s.add(Or(rprim_1_23!=12,
And(rx_f_1_23==-2, ry_f_1_23==0, rcost_1_23==3, 
obstacle(rx_1_23 + 0, ry_1_23 + 0)==False, 
obstacle(rx_1_23 + -1, ry_1_23 + 0)==False, 
obstacle(rx_1_23 + -2, ry_1_23 + 0)==False, 
)))
s.add(Or(rprim_1_23!=13,
And(rx_f_1_23==0, ry_f_1_23==-2, rcost_1_23==3, 
obstacle(rx_1_23 + 0, ry_1_23 + 0)==False, 
obstacle(rx_1_23 + 0, ry_1_23 + -1)==False, 
obstacle(rx_1_23 + 0, ry_1_23 + -2)==False, 
)))
s.add(Or(rprim_1_23!=14,
And(rx_f_1_23==2, ry_f_1_23==2, rcost_1_23==4, 
obstacle(rx_1_23 + 0, ry_1_23 + 0)==False, 
obstacle(rx_1_23 + 1, ry_1_23 + 1)==False, 
obstacle(rx_1_23 + 2, ry_1_23 + 2)==False, 
)))
s.add(Or(rprim_1_23!=15,
And(rx_f_1_23==-2, ry_f_1_23==2, rcost_1_23==4, 
obstacle(rx_1_23 + 0, ry_1_23 + 0)==False, 
obstacle(rx_1_23 + -1, ry_1_23 + 1)==False, 
obstacle(rx_1_23 + -2, ry_1_23 + 2)==False, 
)))
s.add(Or(rprim_1_23!=16,
And(rx_f_1_23==-2, ry_f_1_23==-2, rcost_1_23==4, 
obstacle(rx_1_23 + 0, ry_1_23 + 0)==False, 
obstacle(rx_1_23 + -1, ry_1_23 + -1)==False, 
obstacle(rx_1_23 + -2, ry_1_23 + -2)==False, 
)))
s.add(Or(rprim_1_23!=17,
And(rx_f_1_23==2, ry_f_1_23==-2, rcost_1_23==4, 
obstacle(rx_1_23 + 0, ry_1_23 + 0)==False, 
obstacle(rx_1_23 + 1, ry_1_23 + -1)==False, 
obstacle(rx_1_23 + 2, ry_1_23 + -2)==False, 
)))
s.add(Or(rprim_1_23!=18,
And(rx_f_1_23==3, ry_f_1_23==0, rcost_1_23==4, 
obstacle(rx_1_23 + 0, ry_1_23 + 0)==False, 
obstacle(rx_1_23 + 1, ry_1_23 + 0)==False, 
obstacle(rx_1_23 + 2, ry_1_23 + 0)==False, 
obstacle(rx_1_23 + 3, ry_1_23 + 0)==False, 
)))
s.add(Or(rprim_1_23!=19,
And(rx_f_1_23==0, ry_f_1_23==3, rcost_1_23==4, 
obstacle(rx_1_23 + 0, ry_1_23 + 0)==False, 
obstacle(rx_1_23 + 0, ry_1_23 + 1)==False, 
obstacle(rx_1_23 + 0, ry_1_23 + 2)==False, 
obstacle(rx_1_23 + 0, ry_1_23 + 3)==False, 
)))
s.add(Or(rprim_1_23!=20,
And(rx_f_1_23==-3, ry_f_1_23==0, rcost_1_23==4, 
obstacle(rx_1_23 + 0, ry_1_23 + 0)==False, 
obstacle(rx_1_23 + -1, ry_1_23 + 0)==False, 
obstacle(rx_1_23 + -2, ry_1_23 + 0)==False, 
obstacle(rx_1_23 + -3, ry_1_23 + 0)==False, 
)))
s.add(Or(rprim_1_23!=21,
And(rx_f_1_23==0, ry_f_1_23==-3, rcost_1_23==4, 
obstacle(rx_1_23 + 0, ry_1_23 + 0)==False, 
obstacle(rx_1_23 + 0, ry_1_23 + -1)==False, 
obstacle(rx_1_23 + 0, ry_1_23 + -2)==False, 
obstacle(rx_1_23 + 0, ry_1_23 + -3)==False, 
)))
s.add(Or(rprim_1_24!=1,
And(rx_f_1_24==0, ry_f_1_24==0, rcost_1_24==0, 
obstacle(rx_1_24 + 0, ry_1_24 + 0)==False, 
)))
s.add(Or(rprim_1_24!=2,
And(rx_f_1_24==1, ry_f_1_24==0, rcost_1_24==2, 
obstacle(rx_1_24 + 0, ry_1_24 + 0)==False, 
obstacle(rx_1_24 + 1, ry_1_24 + 0)==False, 
)))
s.add(Or(rprim_1_24!=3,
And(rx_f_1_24==0, ry_f_1_24==-1, rcost_1_24==2, 
obstacle(rx_1_24 + 0, ry_1_24 + 0)==False, 
obstacle(rx_1_24 + 0, ry_1_24 + -1)==False, 
)))
s.add(Or(rprim_1_24!=4,
And(rx_f_1_24==-1, ry_f_1_24==0, rcost_1_24==2, 
obstacle(rx_1_24 + 0, ry_1_24 + 0)==False, 
obstacle(rx_1_24 + -1, ry_1_24 + 0)==False, 
)))
s.add(Or(rprim_1_24!=5,
And(rx_f_1_24==0, ry_f_1_24==1, rcost_1_24==2, 
obstacle(rx_1_24 + 0, ry_1_24 + 0)==False, 
obstacle(rx_1_24 + 0, ry_1_24 + 1)==False, 
)))
s.add(Or(rprim_1_24!=6,
And(rx_f_1_24==1, ry_f_1_24==1, rcost_1_24==3, 
obstacle(rx_1_24 + 0, ry_1_24 + 0)==False, 
obstacle(rx_1_24 + 1, ry_1_24 + 1)==False, 
)))
s.add(Or(rprim_1_24!=7,
And(rx_f_1_24==-1, ry_f_1_24==1, rcost_1_24==3, 
obstacle(rx_1_24 + 0, ry_1_24 + 0)==False, 
obstacle(rx_1_24 + -1, ry_1_24 + 1)==False, 
)))
s.add(Or(rprim_1_24!=8,
And(rx_f_1_24==-1, ry_f_1_24==-1, rcost_1_24==3, 
obstacle(rx_1_24 + 0, ry_1_24 + 0)==False, 
obstacle(rx_1_24 + -1, ry_1_24 + -1)==False, 
)))
s.add(Or(rprim_1_24!=9,
And(rx_f_1_24==1, ry_f_1_24==-1, rcost_1_24==3, 
obstacle(rx_1_24 + 0, ry_1_24 + 0)==False, 
obstacle(rx_1_24 + 1, ry_1_24 + -1)==False, 
)))
s.add(Or(rprim_1_24!=10,
And(rx_f_1_24==2, ry_f_1_24==0, rcost_1_24==3, 
obstacle(rx_1_24 + 0, ry_1_24 + 0)==False, 
obstacle(rx_1_24 + 1, ry_1_24 + 0)==False, 
obstacle(rx_1_24 + 2, ry_1_24 + 0)==False, 
)))
s.add(Or(rprim_1_24!=11,
And(rx_f_1_24==0, ry_f_1_24==2, rcost_1_24==3, 
obstacle(rx_1_24 + 0, ry_1_24 + 0)==False, 
obstacle(rx_1_24 + 0, ry_1_24 + 1)==False, 
obstacle(rx_1_24 + 0, ry_1_24 + 2)==False, 
)))
s.add(Or(rprim_1_24!=12,
And(rx_f_1_24==-2, ry_f_1_24==0, rcost_1_24==3, 
obstacle(rx_1_24 + 0, ry_1_24 + 0)==False, 
obstacle(rx_1_24 + -1, ry_1_24 + 0)==False, 
obstacle(rx_1_24 + -2, ry_1_24 + 0)==False, 
)))
s.add(Or(rprim_1_24!=13,
And(rx_f_1_24==0, ry_f_1_24==-2, rcost_1_24==3, 
obstacle(rx_1_24 + 0, ry_1_24 + 0)==False, 
obstacle(rx_1_24 + 0, ry_1_24 + -1)==False, 
obstacle(rx_1_24 + 0, ry_1_24 + -2)==False, 
)))
s.add(Or(rprim_1_24!=14,
And(rx_f_1_24==2, ry_f_1_24==2, rcost_1_24==4, 
obstacle(rx_1_24 + 0, ry_1_24 + 0)==False, 
obstacle(rx_1_24 + 1, ry_1_24 + 1)==False, 
obstacle(rx_1_24 + 2, ry_1_24 + 2)==False, 
)))
s.add(Or(rprim_1_24!=15,
And(rx_f_1_24==-2, ry_f_1_24==2, rcost_1_24==4, 
obstacle(rx_1_24 + 0, ry_1_24 + 0)==False, 
obstacle(rx_1_24 + -1, ry_1_24 + 1)==False, 
obstacle(rx_1_24 + -2, ry_1_24 + 2)==False, 
)))
s.add(Or(rprim_1_24!=16,
And(rx_f_1_24==-2, ry_f_1_24==-2, rcost_1_24==4, 
obstacle(rx_1_24 + 0, ry_1_24 + 0)==False, 
obstacle(rx_1_24 + -1, ry_1_24 + -1)==False, 
obstacle(rx_1_24 + -2, ry_1_24 + -2)==False, 
)))
s.add(Or(rprim_1_24!=17,
And(rx_f_1_24==2, ry_f_1_24==-2, rcost_1_24==4, 
obstacle(rx_1_24 + 0, ry_1_24 + 0)==False, 
obstacle(rx_1_24 + 1, ry_1_24 + -1)==False, 
obstacle(rx_1_24 + 2, ry_1_24 + -2)==False, 
)))
s.add(Or(rprim_1_24!=18,
And(rx_f_1_24==3, ry_f_1_24==0, rcost_1_24==4, 
obstacle(rx_1_24 + 0, ry_1_24 + 0)==False, 
obstacle(rx_1_24 + 1, ry_1_24 + 0)==False, 
obstacle(rx_1_24 + 2, ry_1_24 + 0)==False, 
obstacle(rx_1_24 + 3, ry_1_24 + 0)==False, 
)))
s.add(Or(rprim_1_24!=19,
And(rx_f_1_24==0, ry_f_1_24==3, rcost_1_24==4, 
obstacle(rx_1_24 + 0, ry_1_24 + 0)==False, 
obstacle(rx_1_24 + 0, ry_1_24 + 1)==False, 
obstacle(rx_1_24 + 0, ry_1_24 + 2)==False, 
obstacle(rx_1_24 + 0, ry_1_24 + 3)==False, 
)))
s.add(Or(rprim_1_24!=20,
And(rx_f_1_24==-3, ry_f_1_24==0, rcost_1_24==4, 
obstacle(rx_1_24 + 0, ry_1_24 + 0)==False, 
obstacle(rx_1_24 + -1, ry_1_24 + 0)==False, 
obstacle(rx_1_24 + -2, ry_1_24 + 0)==False, 
obstacle(rx_1_24 + -3, ry_1_24 + 0)==False, 
)))
s.add(Or(rprim_1_24!=21,
And(rx_f_1_24==0, ry_f_1_24==-3, rcost_1_24==4, 
obstacle(rx_1_24 + 0, ry_1_24 + 0)==False, 
obstacle(rx_1_24 + 0, ry_1_24 + -1)==False, 
obstacle(rx_1_24 + 0, ry_1_24 + -2)==False, 
obstacle(rx_1_24 + 0, ry_1_24 + -3)==False, 
)))
s.add(Or(rprim_1_25!=1,
And(rx_f_1_25==0, ry_f_1_25==0, rcost_1_25==0, 
obstacle(rx_1_25 + 0, ry_1_25 + 0)==False, 
)))
s.add(Or(rprim_1_25!=2,
And(rx_f_1_25==1, ry_f_1_25==0, rcost_1_25==2, 
obstacle(rx_1_25 + 0, ry_1_25 + 0)==False, 
obstacle(rx_1_25 + 1, ry_1_25 + 0)==False, 
)))
s.add(Or(rprim_1_25!=3,
And(rx_f_1_25==0, ry_f_1_25==-1, rcost_1_25==2, 
obstacle(rx_1_25 + 0, ry_1_25 + 0)==False, 
obstacle(rx_1_25 + 0, ry_1_25 + -1)==False, 
)))
s.add(Or(rprim_1_25!=4,
And(rx_f_1_25==-1, ry_f_1_25==0, rcost_1_25==2, 
obstacle(rx_1_25 + 0, ry_1_25 + 0)==False, 
obstacle(rx_1_25 + -1, ry_1_25 + 0)==False, 
)))
s.add(Or(rprim_1_25!=5,
And(rx_f_1_25==0, ry_f_1_25==1, rcost_1_25==2, 
obstacle(rx_1_25 + 0, ry_1_25 + 0)==False, 
obstacle(rx_1_25 + 0, ry_1_25 + 1)==False, 
)))
s.add(Or(rprim_1_25!=6,
And(rx_f_1_25==1, ry_f_1_25==1, rcost_1_25==3, 
obstacle(rx_1_25 + 0, ry_1_25 + 0)==False, 
obstacle(rx_1_25 + 1, ry_1_25 + 1)==False, 
)))
s.add(Or(rprim_1_25!=7,
And(rx_f_1_25==-1, ry_f_1_25==1, rcost_1_25==3, 
obstacle(rx_1_25 + 0, ry_1_25 + 0)==False, 
obstacle(rx_1_25 + -1, ry_1_25 + 1)==False, 
)))
s.add(Or(rprim_1_25!=8,
And(rx_f_1_25==-1, ry_f_1_25==-1, rcost_1_25==3, 
obstacle(rx_1_25 + 0, ry_1_25 + 0)==False, 
obstacle(rx_1_25 + -1, ry_1_25 + -1)==False, 
)))
s.add(Or(rprim_1_25!=9,
And(rx_f_1_25==1, ry_f_1_25==-1, rcost_1_25==3, 
obstacle(rx_1_25 + 0, ry_1_25 + 0)==False, 
obstacle(rx_1_25 + 1, ry_1_25 + -1)==False, 
)))
s.add(Or(rprim_1_25!=10,
And(rx_f_1_25==2, ry_f_1_25==0, rcost_1_25==3, 
obstacle(rx_1_25 + 0, ry_1_25 + 0)==False, 
obstacle(rx_1_25 + 1, ry_1_25 + 0)==False, 
obstacle(rx_1_25 + 2, ry_1_25 + 0)==False, 
)))
s.add(Or(rprim_1_25!=11,
And(rx_f_1_25==0, ry_f_1_25==2, rcost_1_25==3, 
obstacle(rx_1_25 + 0, ry_1_25 + 0)==False, 
obstacle(rx_1_25 + 0, ry_1_25 + 1)==False, 
obstacle(rx_1_25 + 0, ry_1_25 + 2)==False, 
)))
s.add(Or(rprim_1_25!=12,
And(rx_f_1_25==-2, ry_f_1_25==0, rcost_1_25==3, 
obstacle(rx_1_25 + 0, ry_1_25 + 0)==False, 
obstacle(rx_1_25 + -1, ry_1_25 + 0)==False, 
obstacle(rx_1_25 + -2, ry_1_25 + 0)==False, 
)))
s.add(Or(rprim_1_25!=13,
And(rx_f_1_25==0, ry_f_1_25==-2, rcost_1_25==3, 
obstacle(rx_1_25 + 0, ry_1_25 + 0)==False, 
obstacle(rx_1_25 + 0, ry_1_25 + -1)==False, 
obstacle(rx_1_25 + 0, ry_1_25 + -2)==False, 
)))
s.add(Or(rprim_1_25!=14,
And(rx_f_1_25==2, ry_f_1_25==2, rcost_1_25==4, 
obstacle(rx_1_25 + 0, ry_1_25 + 0)==False, 
obstacle(rx_1_25 + 1, ry_1_25 + 1)==False, 
obstacle(rx_1_25 + 2, ry_1_25 + 2)==False, 
)))
s.add(Or(rprim_1_25!=15,
And(rx_f_1_25==-2, ry_f_1_25==2, rcost_1_25==4, 
obstacle(rx_1_25 + 0, ry_1_25 + 0)==False, 
obstacle(rx_1_25 + -1, ry_1_25 + 1)==False, 
obstacle(rx_1_25 + -2, ry_1_25 + 2)==False, 
)))
s.add(Or(rprim_1_25!=16,
And(rx_f_1_25==-2, ry_f_1_25==-2, rcost_1_25==4, 
obstacle(rx_1_25 + 0, ry_1_25 + 0)==False, 
obstacle(rx_1_25 + -1, ry_1_25 + -1)==False, 
obstacle(rx_1_25 + -2, ry_1_25 + -2)==False, 
)))
s.add(Or(rprim_1_25!=17,
And(rx_f_1_25==2, ry_f_1_25==-2, rcost_1_25==4, 
obstacle(rx_1_25 + 0, ry_1_25 + 0)==False, 
obstacle(rx_1_25 + 1, ry_1_25 + -1)==False, 
obstacle(rx_1_25 + 2, ry_1_25 + -2)==False, 
)))
s.add(Or(rprim_1_25!=18,
And(rx_f_1_25==3, ry_f_1_25==0, rcost_1_25==4, 
obstacle(rx_1_25 + 0, ry_1_25 + 0)==False, 
obstacle(rx_1_25 + 1, ry_1_25 + 0)==False, 
obstacle(rx_1_25 + 2, ry_1_25 + 0)==False, 
obstacle(rx_1_25 + 3, ry_1_25 + 0)==False, 
)))
s.add(Or(rprim_1_25!=19,
And(rx_f_1_25==0, ry_f_1_25==3, rcost_1_25==4, 
obstacle(rx_1_25 + 0, ry_1_25 + 0)==False, 
obstacle(rx_1_25 + 0, ry_1_25 + 1)==False, 
obstacle(rx_1_25 + 0, ry_1_25 + 2)==False, 
obstacle(rx_1_25 + 0, ry_1_25 + 3)==False, 
)))
s.add(Or(rprim_1_25!=20,
And(rx_f_1_25==-3, ry_f_1_25==0, rcost_1_25==4, 
obstacle(rx_1_25 + 0, ry_1_25 + 0)==False, 
obstacle(rx_1_25 + -1, ry_1_25 + 0)==False, 
obstacle(rx_1_25 + -2, ry_1_25 + 0)==False, 
obstacle(rx_1_25 + -3, ry_1_25 + 0)==False, 
)))
s.add(Or(rprim_1_25!=21,
And(rx_f_1_25==0, ry_f_1_25==-3, rcost_1_25==4, 
obstacle(rx_1_25 + 0, ry_1_25 + 0)==False, 
obstacle(rx_1_25 + 0, ry_1_25 + -1)==False, 
obstacle(rx_1_25 + 0, ry_1_25 + -2)==False, 
obstacle(rx_1_25 + 0, ry_1_25 + -3)==False, 
)))
s.add(Or(rprim_1_26!=1,
And(rx_f_1_26==0, ry_f_1_26==0, rcost_1_26==0, 
obstacle(rx_1_26 + 0, ry_1_26 + 0)==False, 
)))
s.add(Or(rprim_1_26!=2,
And(rx_f_1_26==1, ry_f_1_26==0, rcost_1_26==2, 
obstacle(rx_1_26 + 0, ry_1_26 + 0)==False, 
obstacle(rx_1_26 + 1, ry_1_26 + 0)==False, 
)))
s.add(Or(rprim_1_26!=3,
And(rx_f_1_26==0, ry_f_1_26==-1, rcost_1_26==2, 
obstacle(rx_1_26 + 0, ry_1_26 + 0)==False, 
obstacle(rx_1_26 + 0, ry_1_26 + -1)==False, 
)))
s.add(Or(rprim_1_26!=4,
And(rx_f_1_26==-1, ry_f_1_26==0, rcost_1_26==2, 
obstacle(rx_1_26 + 0, ry_1_26 + 0)==False, 
obstacle(rx_1_26 + -1, ry_1_26 + 0)==False, 
)))
s.add(Or(rprim_1_26!=5,
And(rx_f_1_26==0, ry_f_1_26==1, rcost_1_26==2, 
obstacle(rx_1_26 + 0, ry_1_26 + 0)==False, 
obstacle(rx_1_26 + 0, ry_1_26 + 1)==False, 
)))
s.add(Or(rprim_1_26!=6,
And(rx_f_1_26==1, ry_f_1_26==1, rcost_1_26==3, 
obstacle(rx_1_26 + 0, ry_1_26 + 0)==False, 
obstacle(rx_1_26 + 1, ry_1_26 + 1)==False, 
)))
s.add(Or(rprim_1_26!=7,
And(rx_f_1_26==-1, ry_f_1_26==1, rcost_1_26==3, 
obstacle(rx_1_26 + 0, ry_1_26 + 0)==False, 
obstacle(rx_1_26 + -1, ry_1_26 + 1)==False, 
)))
s.add(Or(rprim_1_26!=8,
And(rx_f_1_26==-1, ry_f_1_26==-1, rcost_1_26==3, 
obstacle(rx_1_26 + 0, ry_1_26 + 0)==False, 
obstacle(rx_1_26 + -1, ry_1_26 + -1)==False, 
)))
s.add(Or(rprim_1_26!=9,
And(rx_f_1_26==1, ry_f_1_26==-1, rcost_1_26==3, 
obstacle(rx_1_26 + 0, ry_1_26 + 0)==False, 
obstacle(rx_1_26 + 1, ry_1_26 + -1)==False, 
)))
s.add(Or(rprim_1_26!=10,
And(rx_f_1_26==2, ry_f_1_26==0, rcost_1_26==3, 
obstacle(rx_1_26 + 0, ry_1_26 + 0)==False, 
obstacle(rx_1_26 + 1, ry_1_26 + 0)==False, 
obstacle(rx_1_26 + 2, ry_1_26 + 0)==False, 
)))
s.add(Or(rprim_1_26!=11,
And(rx_f_1_26==0, ry_f_1_26==2, rcost_1_26==3, 
obstacle(rx_1_26 + 0, ry_1_26 + 0)==False, 
obstacle(rx_1_26 + 0, ry_1_26 + 1)==False, 
obstacle(rx_1_26 + 0, ry_1_26 + 2)==False, 
)))
s.add(Or(rprim_1_26!=12,
And(rx_f_1_26==-2, ry_f_1_26==0, rcost_1_26==3, 
obstacle(rx_1_26 + 0, ry_1_26 + 0)==False, 
obstacle(rx_1_26 + -1, ry_1_26 + 0)==False, 
obstacle(rx_1_26 + -2, ry_1_26 + 0)==False, 
)))
s.add(Or(rprim_1_26!=13,
And(rx_f_1_26==0, ry_f_1_26==-2, rcost_1_26==3, 
obstacle(rx_1_26 + 0, ry_1_26 + 0)==False, 
obstacle(rx_1_26 + 0, ry_1_26 + -1)==False, 
obstacle(rx_1_26 + 0, ry_1_26 + -2)==False, 
)))
s.add(Or(rprim_1_26!=14,
And(rx_f_1_26==2, ry_f_1_26==2, rcost_1_26==4, 
obstacle(rx_1_26 + 0, ry_1_26 + 0)==False, 
obstacle(rx_1_26 + 1, ry_1_26 + 1)==False, 
obstacle(rx_1_26 + 2, ry_1_26 + 2)==False, 
)))
s.add(Or(rprim_1_26!=15,
And(rx_f_1_26==-2, ry_f_1_26==2, rcost_1_26==4, 
obstacle(rx_1_26 + 0, ry_1_26 + 0)==False, 
obstacle(rx_1_26 + -1, ry_1_26 + 1)==False, 
obstacle(rx_1_26 + -2, ry_1_26 + 2)==False, 
)))
s.add(Or(rprim_1_26!=16,
And(rx_f_1_26==-2, ry_f_1_26==-2, rcost_1_26==4, 
obstacle(rx_1_26 + 0, ry_1_26 + 0)==False, 
obstacle(rx_1_26 + -1, ry_1_26 + -1)==False, 
obstacle(rx_1_26 + -2, ry_1_26 + -2)==False, 
)))
s.add(Or(rprim_1_26!=17,
And(rx_f_1_26==2, ry_f_1_26==-2, rcost_1_26==4, 
obstacle(rx_1_26 + 0, ry_1_26 + 0)==False, 
obstacle(rx_1_26 + 1, ry_1_26 + -1)==False, 
obstacle(rx_1_26 + 2, ry_1_26 + -2)==False, 
)))
s.add(Or(rprim_1_26!=18,
And(rx_f_1_26==3, ry_f_1_26==0, rcost_1_26==4, 
obstacle(rx_1_26 + 0, ry_1_26 + 0)==False, 
obstacle(rx_1_26 + 1, ry_1_26 + 0)==False, 
obstacle(rx_1_26 + 2, ry_1_26 + 0)==False, 
obstacle(rx_1_26 + 3, ry_1_26 + 0)==False, 
)))
s.add(Or(rprim_1_26!=19,
And(rx_f_1_26==0, ry_f_1_26==3, rcost_1_26==4, 
obstacle(rx_1_26 + 0, ry_1_26 + 0)==False, 
obstacle(rx_1_26 + 0, ry_1_26 + 1)==False, 
obstacle(rx_1_26 + 0, ry_1_26 + 2)==False, 
obstacle(rx_1_26 + 0, ry_1_26 + 3)==False, 
)))
s.add(Or(rprim_1_26!=20,
And(rx_f_1_26==-3, ry_f_1_26==0, rcost_1_26==4, 
obstacle(rx_1_26 + 0, ry_1_26 + 0)==False, 
obstacle(rx_1_26 + -1, ry_1_26 + 0)==False, 
obstacle(rx_1_26 + -2, ry_1_26 + 0)==False, 
obstacle(rx_1_26 + -3, ry_1_26 + 0)==False, 
)))
s.add(Or(rprim_1_26!=21,
And(rx_f_1_26==0, ry_f_1_26==-3, rcost_1_26==4, 
obstacle(rx_1_26 + 0, ry_1_26 + 0)==False, 
obstacle(rx_1_26 + 0, ry_1_26 + -1)==False, 
obstacle(rx_1_26 + 0, ry_1_26 + -2)==False, 
obstacle(rx_1_26 + 0, ry_1_26 + -3)==False, 
)))
s.add(Or(rprim_1_27!=1,
And(rx_f_1_27==0, ry_f_1_27==0, rcost_1_27==0, 
obstacle(rx_1_27 + 0, ry_1_27 + 0)==False, 
)))
s.add(Or(rprim_1_27!=2,
And(rx_f_1_27==1, ry_f_1_27==0, rcost_1_27==2, 
obstacle(rx_1_27 + 0, ry_1_27 + 0)==False, 
obstacle(rx_1_27 + 1, ry_1_27 + 0)==False, 
)))
s.add(Or(rprim_1_27!=3,
And(rx_f_1_27==0, ry_f_1_27==-1, rcost_1_27==2, 
obstacle(rx_1_27 + 0, ry_1_27 + 0)==False, 
obstacle(rx_1_27 + 0, ry_1_27 + -1)==False, 
)))
s.add(Or(rprim_1_27!=4,
And(rx_f_1_27==-1, ry_f_1_27==0, rcost_1_27==2, 
obstacle(rx_1_27 + 0, ry_1_27 + 0)==False, 
obstacle(rx_1_27 + -1, ry_1_27 + 0)==False, 
)))
s.add(Or(rprim_1_27!=5,
And(rx_f_1_27==0, ry_f_1_27==1, rcost_1_27==2, 
obstacle(rx_1_27 + 0, ry_1_27 + 0)==False, 
obstacle(rx_1_27 + 0, ry_1_27 + 1)==False, 
)))
s.add(Or(rprim_1_27!=6,
And(rx_f_1_27==1, ry_f_1_27==1, rcost_1_27==3, 
obstacle(rx_1_27 + 0, ry_1_27 + 0)==False, 
obstacle(rx_1_27 + 1, ry_1_27 + 1)==False, 
)))
s.add(Or(rprim_1_27!=7,
And(rx_f_1_27==-1, ry_f_1_27==1, rcost_1_27==3, 
obstacle(rx_1_27 + 0, ry_1_27 + 0)==False, 
obstacle(rx_1_27 + -1, ry_1_27 + 1)==False, 
)))
s.add(Or(rprim_1_27!=8,
And(rx_f_1_27==-1, ry_f_1_27==-1, rcost_1_27==3, 
obstacle(rx_1_27 + 0, ry_1_27 + 0)==False, 
obstacle(rx_1_27 + -1, ry_1_27 + -1)==False, 
)))
s.add(Or(rprim_1_27!=9,
And(rx_f_1_27==1, ry_f_1_27==-1, rcost_1_27==3, 
obstacle(rx_1_27 + 0, ry_1_27 + 0)==False, 
obstacle(rx_1_27 + 1, ry_1_27 + -1)==False, 
)))
s.add(Or(rprim_1_27!=10,
And(rx_f_1_27==2, ry_f_1_27==0, rcost_1_27==3, 
obstacle(rx_1_27 + 0, ry_1_27 + 0)==False, 
obstacle(rx_1_27 + 1, ry_1_27 + 0)==False, 
obstacle(rx_1_27 + 2, ry_1_27 + 0)==False, 
)))
s.add(Or(rprim_1_27!=11,
And(rx_f_1_27==0, ry_f_1_27==2, rcost_1_27==3, 
obstacle(rx_1_27 + 0, ry_1_27 + 0)==False, 
obstacle(rx_1_27 + 0, ry_1_27 + 1)==False, 
obstacle(rx_1_27 + 0, ry_1_27 + 2)==False, 
)))
s.add(Or(rprim_1_27!=12,
And(rx_f_1_27==-2, ry_f_1_27==0, rcost_1_27==3, 
obstacle(rx_1_27 + 0, ry_1_27 + 0)==False, 
obstacle(rx_1_27 + -1, ry_1_27 + 0)==False, 
obstacle(rx_1_27 + -2, ry_1_27 + 0)==False, 
)))
s.add(Or(rprim_1_27!=13,
And(rx_f_1_27==0, ry_f_1_27==-2, rcost_1_27==3, 
obstacle(rx_1_27 + 0, ry_1_27 + 0)==False, 
obstacle(rx_1_27 + 0, ry_1_27 + -1)==False, 
obstacle(rx_1_27 + 0, ry_1_27 + -2)==False, 
)))
s.add(Or(rprim_1_27!=14,
And(rx_f_1_27==2, ry_f_1_27==2, rcost_1_27==4, 
obstacle(rx_1_27 + 0, ry_1_27 + 0)==False, 
obstacle(rx_1_27 + 1, ry_1_27 + 1)==False, 
obstacle(rx_1_27 + 2, ry_1_27 + 2)==False, 
)))
s.add(Or(rprim_1_27!=15,
And(rx_f_1_27==-2, ry_f_1_27==2, rcost_1_27==4, 
obstacle(rx_1_27 + 0, ry_1_27 + 0)==False, 
obstacle(rx_1_27 + -1, ry_1_27 + 1)==False, 
obstacle(rx_1_27 + -2, ry_1_27 + 2)==False, 
)))
s.add(Or(rprim_1_27!=16,
And(rx_f_1_27==-2, ry_f_1_27==-2, rcost_1_27==4, 
obstacle(rx_1_27 + 0, ry_1_27 + 0)==False, 
obstacle(rx_1_27 + -1, ry_1_27 + -1)==False, 
obstacle(rx_1_27 + -2, ry_1_27 + -2)==False, 
)))
s.add(Or(rprim_1_27!=17,
And(rx_f_1_27==2, ry_f_1_27==-2, rcost_1_27==4, 
obstacle(rx_1_27 + 0, ry_1_27 + 0)==False, 
obstacle(rx_1_27 + 1, ry_1_27 + -1)==False, 
obstacle(rx_1_27 + 2, ry_1_27 + -2)==False, 
)))
s.add(Or(rprim_1_27!=18,
And(rx_f_1_27==3, ry_f_1_27==0, rcost_1_27==4, 
obstacle(rx_1_27 + 0, ry_1_27 + 0)==False, 
obstacle(rx_1_27 + 1, ry_1_27 + 0)==False, 
obstacle(rx_1_27 + 2, ry_1_27 + 0)==False, 
obstacle(rx_1_27 + 3, ry_1_27 + 0)==False, 
)))
s.add(Or(rprim_1_27!=19,
And(rx_f_1_27==0, ry_f_1_27==3, rcost_1_27==4, 
obstacle(rx_1_27 + 0, ry_1_27 + 0)==False, 
obstacle(rx_1_27 + 0, ry_1_27 + 1)==False, 
obstacle(rx_1_27 + 0, ry_1_27 + 2)==False, 
obstacle(rx_1_27 + 0, ry_1_27 + 3)==False, 
)))
s.add(Or(rprim_1_27!=20,
And(rx_f_1_27==-3, ry_f_1_27==0, rcost_1_27==4, 
obstacle(rx_1_27 + 0, ry_1_27 + 0)==False, 
obstacle(rx_1_27 + -1, ry_1_27 + 0)==False, 
obstacle(rx_1_27 + -2, ry_1_27 + 0)==False, 
obstacle(rx_1_27 + -3, ry_1_27 + 0)==False, 
)))
s.add(Or(rprim_1_27!=21,
And(rx_f_1_27==0, ry_f_1_27==-3, rcost_1_27==4, 
obstacle(rx_1_27 + 0, ry_1_27 + 0)==False, 
obstacle(rx_1_27 + 0, ry_1_27 + -1)==False, 
obstacle(rx_1_27 + 0, ry_1_27 + -2)==False, 
obstacle(rx_1_27 + 0, ry_1_27 + -3)==False, 
)))
s.add(Or(rprim_1_28!=1,
And(rx_f_1_28==0, ry_f_1_28==0, rcost_1_28==0, 
obstacle(rx_1_28 + 0, ry_1_28 + 0)==False, 
)))
s.add(Or(rprim_1_28!=2,
And(rx_f_1_28==1, ry_f_1_28==0, rcost_1_28==2, 
obstacle(rx_1_28 + 0, ry_1_28 + 0)==False, 
obstacle(rx_1_28 + 1, ry_1_28 + 0)==False, 
)))
s.add(Or(rprim_1_28!=3,
And(rx_f_1_28==0, ry_f_1_28==-1, rcost_1_28==2, 
obstacle(rx_1_28 + 0, ry_1_28 + 0)==False, 
obstacle(rx_1_28 + 0, ry_1_28 + -1)==False, 
)))
s.add(Or(rprim_1_28!=4,
And(rx_f_1_28==-1, ry_f_1_28==0, rcost_1_28==2, 
obstacle(rx_1_28 + 0, ry_1_28 + 0)==False, 
obstacle(rx_1_28 + -1, ry_1_28 + 0)==False, 
)))
s.add(Or(rprim_1_28!=5,
And(rx_f_1_28==0, ry_f_1_28==1, rcost_1_28==2, 
obstacle(rx_1_28 + 0, ry_1_28 + 0)==False, 
obstacle(rx_1_28 + 0, ry_1_28 + 1)==False, 
)))
s.add(Or(rprim_1_28!=6,
And(rx_f_1_28==1, ry_f_1_28==1, rcost_1_28==3, 
obstacle(rx_1_28 + 0, ry_1_28 + 0)==False, 
obstacle(rx_1_28 + 1, ry_1_28 + 1)==False, 
)))
s.add(Or(rprim_1_28!=7,
And(rx_f_1_28==-1, ry_f_1_28==1, rcost_1_28==3, 
obstacle(rx_1_28 + 0, ry_1_28 + 0)==False, 
obstacle(rx_1_28 + -1, ry_1_28 + 1)==False, 
)))
s.add(Or(rprim_1_28!=8,
And(rx_f_1_28==-1, ry_f_1_28==-1, rcost_1_28==3, 
obstacle(rx_1_28 + 0, ry_1_28 + 0)==False, 
obstacle(rx_1_28 + -1, ry_1_28 + -1)==False, 
)))
s.add(Or(rprim_1_28!=9,
And(rx_f_1_28==1, ry_f_1_28==-1, rcost_1_28==3, 
obstacle(rx_1_28 + 0, ry_1_28 + 0)==False, 
obstacle(rx_1_28 + 1, ry_1_28 + -1)==False, 
)))
s.add(Or(rprim_1_28!=10,
And(rx_f_1_28==2, ry_f_1_28==0, rcost_1_28==3, 
obstacle(rx_1_28 + 0, ry_1_28 + 0)==False, 
obstacle(rx_1_28 + 1, ry_1_28 + 0)==False, 
obstacle(rx_1_28 + 2, ry_1_28 + 0)==False, 
)))
s.add(Or(rprim_1_28!=11,
And(rx_f_1_28==0, ry_f_1_28==2, rcost_1_28==3, 
obstacle(rx_1_28 + 0, ry_1_28 + 0)==False, 
obstacle(rx_1_28 + 0, ry_1_28 + 1)==False, 
obstacle(rx_1_28 + 0, ry_1_28 + 2)==False, 
)))
s.add(Or(rprim_1_28!=12,
And(rx_f_1_28==-2, ry_f_1_28==0, rcost_1_28==3, 
obstacle(rx_1_28 + 0, ry_1_28 + 0)==False, 
obstacle(rx_1_28 + -1, ry_1_28 + 0)==False, 
obstacle(rx_1_28 + -2, ry_1_28 + 0)==False, 
)))
s.add(Or(rprim_1_28!=13,
And(rx_f_1_28==0, ry_f_1_28==-2, rcost_1_28==3, 
obstacle(rx_1_28 + 0, ry_1_28 + 0)==False, 
obstacle(rx_1_28 + 0, ry_1_28 + -1)==False, 
obstacle(rx_1_28 + 0, ry_1_28 + -2)==False, 
)))
s.add(Or(rprim_1_28!=14,
And(rx_f_1_28==2, ry_f_1_28==2, rcost_1_28==4, 
obstacle(rx_1_28 + 0, ry_1_28 + 0)==False, 
obstacle(rx_1_28 + 1, ry_1_28 + 1)==False, 
obstacle(rx_1_28 + 2, ry_1_28 + 2)==False, 
)))
s.add(Or(rprim_1_28!=15,
And(rx_f_1_28==-2, ry_f_1_28==2, rcost_1_28==4, 
obstacle(rx_1_28 + 0, ry_1_28 + 0)==False, 
obstacle(rx_1_28 + -1, ry_1_28 + 1)==False, 
obstacle(rx_1_28 + -2, ry_1_28 + 2)==False, 
)))
s.add(Or(rprim_1_28!=16,
And(rx_f_1_28==-2, ry_f_1_28==-2, rcost_1_28==4, 
obstacle(rx_1_28 + 0, ry_1_28 + 0)==False, 
obstacle(rx_1_28 + -1, ry_1_28 + -1)==False, 
obstacle(rx_1_28 + -2, ry_1_28 + -2)==False, 
)))
s.add(Or(rprim_1_28!=17,
And(rx_f_1_28==2, ry_f_1_28==-2, rcost_1_28==4, 
obstacle(rx_1_28 + 0, ry_1_28 + 0)==False, 
obstacle(rx_1_28 + 1, ry_1_28 + -1)==False, 
obstacle(rx_1_28 + 2, ry_1_28 + -2)==False, 
)))
s.add(Or(rprim_1_28!=18,
And(rx_f_1_28==3, ry_f_1_28==0, rcost_1_28==4, 
obstacle(rx_1_28 + 0, ry_1_28 + 0)==False, 
obstacle(rx_1_28 + 1, ry_1_28 + 0)==False, 
obstacle(rx_1_28 + 2, ry_1_28 + 0)==False, 
obstacle(rx_1_28 + 3, ry_1_28 + 0)==False, 
)))
s.add(Or(rprim_1_28!=19,
And(rx_f_1_28==0, ry_f_1_28==3, rcost_1_28==4, 
obstacle(rx_1_28 + 0, ry_1_28 + 0)==False, 
obstacle(rx_1_28 + 0, ry_1_28 + 1)==False, 
obstacle(rx_1_28 + 0, ry_1_28 + 2)==False, 
obstacle(rx_1_28 + 0, ry_1_28 + 3)==False, 
)))
s.add(Or(rprim_1_28!=20,
And(rx_f_1_28==-3, ry_f_1_28==0, rcost_1_28==4, 
obstacle(rx_1_28 + 0, ry_1_28 + 0)==False, 
obstacle(rx_1_28 + -1, ry_1_28 + 0)==False, 
obstacle(rx_1_28 + -2, ry_1_28 + 0)==False, 
obstacle(rx_1_28 + -3, ry_1_28 + 0)==False, 
)))
s.add(Or(rprim_1_28!=21,
And(rx_f_1_28==0, ry_f_1_28==-3, rcost_1_28==4, 
obstacle(rx_1_28 + 0, ry_1_28 + 0)==False, 
obstacle(rx_1_28 + 0, ry_1_28 + -1)==False, 
obstacle(rx_1_28 + 0, ry_1_28 + -2)==False, 
obstacle(rx_1_28 + 0, ry_1_28 + -3)==False, 
)))
s.add(Or(rprim_1_29!=1,
And(rx_f_1_29==0, ry_f_1_29==0, rcost_1_29==0, 
obstacle(rx_1_29 + 0, ry_1_29 + 0)==False, 
)))
s.add(Or(rprim_1_29!=2,
And(rx_f_1_29==1, ry_f_1_29==0, rcost_1_29==2, 
obstacle(rx_1_29 + 0, ry_1_29 + 0)==False, 
obstacle(rx_1_29 + 1, ry_1_29 + 0)==False, 
)))
s.add(Or(rprim_1_29!=3,
And(rx_f_1_29==0, ry_f_1_29==-1, rcost_1_29==2, 
obstacle(rx_1_29 + 0, ry_1_29 + 0)==False, 
obstacle(rx_1_29 + 0, ry_1_29 + -1)==False, 
)))
s.add(Or(rprim_1_29!=4,
And(rx_f_1_29==-1, ry_f_1_29==0, rcost_1_29==2, 
obstacle(rx_1_29 + 0, ry_1_29 + 0)==False, 
obstacle(rx_1_29 + -1, ry_1_29 + 0)==False, 
)))
s.add(Or(rprim_1_29!=5,
And(rx_f_1_29==0, ry_f_1_29==1, rcost_1_29==2, 
obstacle(rx_1_29 + 0, ry_1_29 + 0)==False, 
obstacle(rx_1_29 + 0, ry_1_29 + 1)==False, 
)))
s.add(Or(rprim_1_29!=6,
And(rx_f_1_29==1, ry_f_1_29==1, rcost_1_29==3, 
obstacle(rx_1_29 + 0, ry_1_29 + 0)==False, 
obstacle(rx_1_29 + 1, ry_1_29 + 1)==False, 
)))
s.add(Or(rprim_1_29!=7,
And(rx_f_1_29==-1, ry_f_1_29==1, rcost_1_29==3, 
obstacle(rx_1_29 + 0, ry_1_29 + 0)==False, 
obstacle(rx_1_29 + -1, ry_1_29 + 1)==False, 
)))
s.add(Or(rprim_1_29!=8,
And(rx_f_1_29==-1, ry_f_1_29==-1, rcost_1_29==3, 
obstacle(rx_1_29 + 0, ry_1_29 + 0)==False, 
obstacle(rx_1_29 + -1, ry_1_29 + -1)==False, 
)))
s.add(Or(rprim_1_29!=9,
And(rx_f_1_29==1, ry_f_1_29==-1, rcost_1_29==3, 
obstacle(rx_1_29 + 0, ry_1_29 + 0)==False, 
obstacle(rx_1_29 + 1, ry_1_29 + -1)==False, 
)))
s.add(Or(rprim_1_29!=10,
And(rx_f_1_29==2, ry_f_1_29==0, rcost_1_29==3, 
obstacle(rx_1_29 + 0, ry_1_29 + 0)==False, 
obstacle(rx_1_29 + 1, ry_1_29 + 0)==False, 
obstacle(rx_1_29 + 2, ry_1_29 + 0)==False, 
)))
s.add(Or(rprim_1_29!=11,
And(rx_f_1_29==0, ry_f_1_29==2, rcost_1_29==3, 
obstacle(rx_1_29 + 0, ry_1_29 + 0)==False, 
obstacle(rx_1_29 + 0, ry_1_29 + 1)==False, 
obstacle(rx_1_29 + 0, ry_1_29 + 2)==False, 
)))
s.add(Or(rprim_1_29!=12,
And(rx_f_1_29==-2, ry_f_1_29==0, rcost_1_29==3, 
obstacle(rx_1_29 + 0, ry_1_29 + 0)==False, 
obstacle(rx_1_29 + -1, ry_1_29 + 0)==False, 
obstacle(rx_1_29 + -2, ry_1_29 + 0)==False, 
)))
s.add(Or(rprim_1_29!=13,
And(rx_f_1_29==0, ry_f_1_29==-2, rcost_1_29==3, 
obstacle(rx_1_29 + 0, ry_1_29 + 0)==False, 
obstacle(rx_1_29 + 0, ry_1_29 + -1)==False, 
obstacle(rx_1_29 + 0, ry_1_29 + -2)==False, 
)))
s.add(Or(rprim_1_29!=14,
And(rx_f_1_29==2, ry_f_1_29==2, rcost_1_29==4, 
obstacle(rx_1_29 + 0, ry_1_29 + 0)==False, 
obstacle(rx_1_29 + 1, ry_1_29 + 1)==False, 
obstacle(rx_1_29 + 2, ry_1_29 + 2)==False, 
)))
s.add(Or(rprim_1_29!=15,
And(rx_f_1_29==-2, ry_f_1_29==2, rcost_1_29==4, 
obstacle(rx_1_29 + 0, ry_1_29 + 0)==False, 
obstacle(rx_1_29 + -1, ry_1_29 + 1)==False, 
obstacle(rx_1_29 + -2, ry_1_29 + 2)==False, 
)))
s.add(Or(rprim_1_29!=16,
And(rx_f_1_29==-2, ry_f_1_29==-2, rcost_1_29==4, 
obstacle(rx_1_29 + 0, ry_1_29 + 0)==False, 
obstacle(rx_1_29 + -1, ry_1_29 + -1)==False, 
obstacle(rx_1_29 + -2, ry_1_29 + -2)==False, 
)))
s.add(Or(rprim_1_29!=17,
And(rx_f_1_29==2, ry_f_1_29==-2, rcost_1_29==4, 
obstacle(rx_1_29 + 0, ry_1_29 + 0)==False, 
obstacle(rx_1_29 + 1, ry_1_29 + -1)==False, 
obstacle(rx_1_29 + 2, ry_1_29 + -2)==False, 
)))
s.add(Or(rprim_1_29!=18,
And(rx_f_1_29==3, ry_f_1_29==0, rcost_1_29==4, 
obstacle(rx_1_29 + 0, ry_1_29 + 0)==False, 
obstacle(rx_1_29 + 1, ry_1_29 + 0)==False, 
obstacle(rx_1_29 + 2, ry_1_29 + 0)==False, 
obstacle(rx_1_29 + 3, ry_1_29 + 0)==False, 
)))
s.add(Or(rprim_1_29!=19,
And(rx_f_1_29==0, ry_f_1_29==3, rcost_1_29==4, 
obstacle(rx_1_29 + 0, ry_1_29 + 0)==False, 
obstacle(rx_1_29 + 0, ry_1_29 + 1)==False, 
obstacle(rx_1_29 + 0, ry_1_29 + 2)==False, 
obstacle(rx_1_29 + 0, ry_1_29 + 3)==False, 
)))
s.add(Or(rprim_1_29!=20,
And(rx_f_1_29==-3, ry_f_1_29==0, rcost_1_29==4, 
obstacle(rx_1_29 + 0, ry_1_29 + 0)==False, 
obstacle(rx_1_29 + -1, ry_1_29 + 0)==False, 
obstacle(rx_1_29 + -2, ry_1_29 + 0)==False, 
obstacle(rx_1_29 + -3, ry_1_29 + 0)==False, 
)))
s.add(Or(rprim_1_29!=21,
And(rx_f_1_29==0, ry_f_1_29==-3, rcost_1_29==4, 
obstacle(rx_1_29 + 0, ry_1_29 + 0)==False, 
obstacle(rx_1_29 + 0, ry_1_29 + -1)==False, 
obstacle(rx_1_29 + 0, ry_1_29 + -2)==False, 
obstacle(rx_1_29 + 0, ry_1_29 + -3)==False, 
)))
s.add(Or(rprim_1_30!=1,
And(rx_f_1_30==0, ry_f_1_30==0, rcost_1_30==0, 
obstacle(rx_1_30 + 0, ry_1_30 + 0)==False, 
)))
s.add(Or(rprim_1_30!=2,
And(rx_f_1_30==1, ry_f_1_30==0, rcost_1_30==2, 
obstacle(rx_1_30 + 0, ry_1_30 + 0)==False, 
obstacle(rx_1_30 + 1, ry_1_30 + 0)==False, 
)))
s.add(Or(rprim_1_30!=3,
And(rx_f_1_30==0, ry_f_1_30==-1, rcost_1_30==2, 
obstacle(rx_1_30 + 0, ry_1_30 + 0)==False, 
obstacle(rx_1_30 + 0, ry_1_30 + -1)==False, 
)))
s.add(Or(rprim_1_30!=4,
And(rx_f_1_30==-1, ry_f_1_30==0, rcost_1_30==2, 
obstacle(rx_1_30 + 0, ry_1_30 + 0)==False, 
obstacle(rx_1_30 + -1, ry_1_30 + 0)==False, 
)))
s.add(Or(rprim_1_30!=5,
And(rx_f_1_30==0, ry_f_1_30==1, rcost_1_30==2, 
obstacle(rx_1_30 + 0, ry_1_30 + 0)==False, 
obstacle(rx_1_30 + 0, ry_1_30 + 1)==False, 
)))
s.add(Or(rprim_1_30!=6,
And(rx_f_1_30==1, ry_f_1_30==1, rcost_1_30==3, 
obstacle(rx_1_30 + 0, ry_1_30 + 0)==False, 
obstacle(rx_1_30 + 1, ry_1_30 + 1)==False, 
)))
s.add(Or(rprim_1_30!=7,
And(rx_f_1_30==-1, ry_f_1_30==1, rcost_1_30==3, 
obstacle(rx_1_30 + 0, ry_1_30 + 0)==False, 
obstacle(rx_1_30 + -1, ry_1_30 + 1)==False, 
)))
s.add(Or(rprim_1_30!=8,
And(rx_f_1_30==-1, ry_f_1_30==-1, rcost_1_30==3, 
obstacle(rx_1_30 + 0, ry_1_30 + 0)==False, 
obstacle(rx_1_30 + -1, ry_1_30 + -1)==False, 
)))
s.add(Or(rprim_1_30!=9,
And(rx_f_1_30==1, ry_f_1_30==-1, rcost_1_30==3, 
obstacle(rx_1_30 + 0, ry_1_30 + 0)==False, 
obstacle(rx_1_30 + 1, ry_1_30 + -1)==False, 
)))
s.add(Or(rprim_1_30!=10,
And(rx_f_1_30==2, ry_f_1_30==0, rcost_1_30==3, 
obstacle(rx_1_30 + 0, ry_1_30 + 0)==False, 
obstacle(rx_1_30 + 1, ry_1_30 + 0)==False, 
obstacle(rx_1_30 + 2, ry_1_30 + 0)==False, 
)))
s.add(Or(rprim_1_30!=11,
And(rx_f_1_30==0, ry_f_1_30==2, rcost_1_30==3, 
obstacle(rx_1_30 + 0, ry_1_30 + 0)==False, 
obstacle(rx_1_30 + 0, ry_1_30 + 1)==False, 
obstacle(rx_1_30 + 0, ry_1_30 + 2)==False, 
)))
s.add(Or(rprim_1_30!=12,
And(rx_f_1_30==-2, ry_f_1_30==0, rcost_1_30==3, 
obstacle(rx_1_30 + 0, ry_1_30 + 0)==False, 
obstacle(rx_1_30 + -1, ry_1_30 + 0)==False, 
obstacle(rx_1_30 + -2, ry_1_30 + 0)==False, 
)))
s.add(Or(rprim_1_30!=13,
And(rx_f_1_30==0, ry_f_1_30==-2, rcost_1_30==3, 
obstacle(rx_1_30 + 0, ry_1_30 + 0)==False, 
obstacle(rx_1_30 + 0, ry_1_30 + -1)==False, 
obstacle(rx_1_30 + 0, ry_1_30 + -2)==False, 
)))
s.add(Or(rprim_1_30!=14,
And(rx_f_1_30==2, ry_f_1_30==2, rcost_1_30==4, 
obstacle(rx_1_30 + 0, ry_1_30 + 0)==False, 
obstacle(rx_1_30 + 1, ry_1_30 + 1)==False, 
obstacle(rx_1_30 + 2, ry_1_30 + 2)==False, 
)))
s.add(Or(rprim_1_30!=15,
And(rx_f_1_30==-2, ry_f_1_30==2, rcost_1_30==4, 
obstacle(rx_1_30 + 0, ry_1_30 + 0)==False, 
obstacle(rx_1_30 + -1, ry_1_30 + 1)==False, 
obstacle(rx_1_30 + -2, ry_1_30 + 2)==False, 
)))
s.add(Or(rprim_1_30!=16,
And(rx_f_1_30==-2, ry_f_1_30==-2, rcost_1_30==4, 
obstacle(rx_1_30 + 0, ry_1_30 + 0)==False, 
obstacle(rx_1_30 + -1, ry_1_30 + -1)==False, 
obstacle(rx_1_30 + -2, ry_1_30 + -2)==False, 
)))
s.add(Or(rprim_1_30!=17,
And(rx_f_1_30==2, ry_f_1_30==-2, rcost_1_30==4, 
obstacle(rx_1_30 + 0, ry_1_30 + 0)==False, 
obstacle(rx_1_30 + 1, ry_1_30 + -1)==False, 
obstacle(rx_1_30 + 2, ry_1_30 + -2)==False, 
)))
s.add(Or(rprim_1_30!=18,
And(rx_f_1_30==3, ry_f_1_30==0, rcost_1_30==4, 
obstacle(rx_1_30 + 0, ry_1_30 + 0)==False, 
obstacle(rx_1_30 + 1, ry_1_30 + 0)==False, 
obstacle(rx_1_30 + 2, ry_1_30 + 0)==False, 
obstacle(rx_1_30 + 3, ry_1_30 + 0)==False, 
)))
s.add(Or(rprim_1_30!=19,
And(rx_f_1_30==0, ry_f_1_30==3, rcost_1_30==4, 
obstacle(rx_1_30 + 0, ry_1_30 + 0)==False, 
obstacle(rx_1_30 + 0, ry_1_30 + 1)==False, 
obstacle(rx_1_30 + 0, ry_1_30 + 2)==False, 
obstacle(rx_1_30 + 0, ry_1_30 + 3)==False, 
)))
s.add(Or(rprim_1_30!=20,
And(rx_f_1_30==-3, ry_f_1_30==0, rcost_1_30==4, 
obstacle(rx_1_30 + 0, ry_1_30 + 0)==False, 
obstacle(rx_1_30 + -1, ry_1_30 + 0)==False, 
obstacle(rx_1_30 + -2, ry_1_30 + 0)==False, 
obstacle(rx_1_30 + -3, ry_1_30 + 0)==False, 
)))
s.add(Or(rprim_1_30!=21,
And(rx_f_1_30==0, ry_f_1_30==-3, rcost_1_30==4, 
obstacle(rx_1_30 + 0, ry_1_30 + 0)==False, 
obstacle(rx_1_30 + 0, ry_1_30 + -1)==False, 
obstacle(rx_1_30 + 0, ry_1_30 + -2)==False, 
obstacle(rx_1_30 + 0, ry_1_30 + -3)==False, 
)))
s.add(Or(rprim_1_31!=1,
And(rx_f_1_31==0, ry_f_1_31==0, rcost_1_31==0, 
obstacle(rx_1_31 + 0, ry_1_31 + 0)==False, 
)))
s.add(Or(rprim_1_31!=2,
And(rx_f_1_31==1, ry_f_1_31==0, rcost_1_31==2, 
obstacle(rx_1_31 + 0, ry_1_31 + 0)==False, 
obstacle(rx_1_31 + 1, ry_1_31 + 0)==False, 
)))
s.add(Or(rprim_1_31!=3,
And(rx_f_1_31==0, ry_f_1_31==-1, rcost_1_31==2, 
obstacle(rx_1_31 + 0, ry_1_31 + 0)==False, 
obstacle(rx_1_31 + 0, ry_1_31 + -1)==False, 
)))
s.add(Or(rprim_1_31!=4,
And(rx_f_1_31==-1, ry_f_1_31==0, rcost_1_31==2, 
obstacle(rx_1_31 + 0, ry_1_31 + 0)==False, 
obstacle(rx_1_31 + -1, ry_1_31 + 0)==False, 
)))
s.add(Or(rprim_1_31!=5,
And(rx_f_1_31==0, ry_f_1_31==1, rcost_1_31==2, 
obstacle(rx_1_31 + 0, ry_1_31 + 0)==False, 
obstacle(rx_1_31 + 0, ry_1_31 + 1)==False, 
)))
s.add(Or(rprim_1_31!=6,
And(rx_f_1_31==1, ry_f_1_31==1, rcost_1_31==3, 
obstacle(rx_1_31 + 0, ry_1_31 + 0)==False, 
obstacle(rx_1_31 + 1, ry_1_31 + 1)==False, 
)))
s.add(Or(rprim_1_31!=7,
And(rx_f_1_31==-1, ry_f_1_31==1, rcost_1_31==3, 
obstacle(rx_1_31 + 0, ry_1_31 + 0)==False, 
obstacle(rx_1_31 + -1, ry_1_31 + 1)==False, 
)))
s.add(Or(rprim_1_31!=8,
And(rx_f_1_31==-1, ry_f_1_31==-1, rcost_1_31==3, 
obstacle(rx_1_31 + 0, ry_1_31 + 0)==False, 
obstacle(rx_1_31 + -1, ry_1_31 + -1)==False, 
)))
s.add(Or(rprim_1_31!=9,
And(rx_f_1_31==1, ry_f_1_31==-1, rcost_1_31==3, 
obstacle(rx_1_31 + 0, ry_1_31 + 0)==False, 
obstacle(rx_1_31 + 1, ry_1_31 + -1)==False, 
)))
s.add(Or(rprim_1_31!=10,
And(rx_f_1_31==2, ry_f_1_31==0, rcost_1_31==3, 
obstacle(rx_1_31 + 0, ry_1_31 + 0)==False, 
obstacle(rx_1_31 + 1, ry_1_31 + 0)==False, 
obstacle(rx_1_31 + 2, ry_1_31 + 0)==False, 
)))
s.add(Or(rprim_1_31!=11,
And(rx_f_1_31==0, ry_f_1_31==2, rcost_1_31==3, 
obstacle(rx_1_31 + 0, ry_1_31 + 0)==False, 
obstacle(rx_1_31 + 0, ry_1_31 + 1)==False, 
obstacle(rx_1_31 + 0, ry_1_31 + 2)==False, 
)))
s.add(Or(rprim_1_31!=12,
And(rx_f_1_31==-2, ry_f_1_31==0, rcost_1_31==3, 
obstacle(rx_1_31 + 0, ry_1_31 + 0)==False, 
obstacle(rx_1_31 + -1, ry_1_31 + 0)==False, 
obstacle(rx_1_31 + -2, ry_1_31 + 0)==False, 
)))
s.add(Or(rprim_1_31!=13,
And(rx_f_1_31==0, ry_f_1_31==-2, rcost_1_31==3, 
obstacle(rx_1_31 + 0, ry_1_31 + 0)==False, 
obstacle(rx_1_31 + 0, ry_1_31 + -1)==False, 
obstacle(rx_1_31 + 0, ry_1_31 + -2)==False, 
)))
s.add(Or(rprim_1_31!=14,
And(rx_f_1_31==2, ry_f_1_31==2, rcost_1_31==4, 
obstacle(rx_1_31 + 0, ry_1_31 + 0)==False, 
obstacle(rx_1_31 + 1, ry_1_31 + 1)==False, 
obstacle(rx_1_31 + 2, ry_1_31 + 2)==False, 
)))
s.add(Or(rprim_1_31!=15,
And(rx_f_1_31==-2, ry_f_1_31==2, rcost_1_31==4, 
obstacle(rx_1_31 + 0, ry_1_31 + 0)==False, 
obstacle(rx_1_31 + -1, ry_1_31 + 1)==False, 
obstacle(rx_1_31 + -2, ry_1_31 + 2)==False, 
)))
s.add(Or(rprim_1_31!=16,
And(rx_f_1_31==-2, ry_f_1_31==-2, rcost_1_31==4, 
obstacle(rx_1_31 + 0, ry_1_31 + 0)==False, 
obstacle(rx_1_31 + -1, ry_1_31 + -1)==False, 
obstacle(rx_1_31 + -2, ry_1_31 + -2)==False, 
)))
s.add(Or(rprim_1_31!=17,
And(rx_f_1_31==2, ry_f_1_31==-2, rcost_1_31==4, 
obstacle(rx_1_31 + 0, ry_1_31 + 0)==False, 
obstacle(rx_1_31 + 1, ry_1_31 + -1)==False, 
obstacle(rx_1_31 + 2, ry_1_31 + -2)==False, 
)))
s.add(Or(rprim_1_31!=18,
And(rx_f_1_31==3, ry_f_1_31==0, rcost_1_31==4, 
obstacle(rx_1_31 + 0, ry_1_31 + 0)==False, 
obstacle(rx_1_31 + 1, ry_1_31 + 0)==False, 
obstacle(rx_1_31 + 2, ry_1_31 + 0)==False, 
obstacle(rx_1_31 + 3, ry_1_31 + 0)==False, 
)))
s.add(Or(rprim_1_31!=19,
And(rx_f_1_31==0, ry_f_1_31==3, rcost_1_31==4, 
obstacle(rx_1_31 + 0, ry_1_31 + 0)==False, 
obstacle(rx_1_31 + 0, ry_1_31 + 1)==False, 
obstacle(rx_1_31 + 0, ry_1_31 + 2)==False, 
obstacle(rx_1_31 + 0, ry_1_31 + 3)==False, 
)))
s.add(Or(rprim_1_31!=20,
And(rx_f_1_31==-3, ry_f_1_31==0, rcost_1_31==4, 
obstacle(rx_1_31 + 0, ry_1_31 + 0)==False, 
obstacle(rx_1_31 + -1, ry_1_31 + 0)==False, 
obstacle(rx_1_31 + -2, ry_1_31 + 0)==False, 
obstacle(rx_1_31 + -3, ry_1_31 + 0)==False, 
)))
s.add(Or(rprim_1_31!=21,
And(rx_f_1_31==0, ry_f_1_31==-3, rcost_1_31==4, 
obstacle(rx_1_31 + 0, ry_1_31 + 0)==False, 
obstacle(rx_1_31 + 0, ry_1_31 + -1)==False, 
obstacle(rx_1_31 + 0, ry_1_31 + -2)==False, 
obstacle(rx_1_31 + 0, ry_1_31 + -3)==False, 
)))
s.add(Or(rprim_1_32!=1,
And(rx_f_1_32==0, ry_f_1_32==0, rcost_1_32==0, 
obstacle(rx_1_32 + 0, ry_1_32 + 0)==False, 
)))
s.add(Or(rprim_1_32!=2,
And(rx_f_1_32==1, ry_f_1_32==0, rcost_1_32==2, 
obstacle(rx_1_32 + 0, ry_1_32 + 0)==False, 
obstacle(rx_1_32 + 1, ry_1_32 + 0)==False, 
)))
s.add(Or(rprim_1_32!=3,
And(rx_f_1_32==0, ry_f_1_32==-1, rcost_1_32==2, 
obstacle(rx_1_32 + 0, ry_1_32 + 0)==False, 
obstacle(rx_1_32 + 0, ry_1_32 + -1)==False, 
)))
s.add(Or(rprim_1_32!=4,
And(rx_f_1_32==-1, ry_f_1_32==0, rcost_1_32==2, 
obstacle(rx_1_32 + 0, ry_1_32 + 0)==False, 
obstacle(rx_1_32 + -1, ry_1_32 + 0)==False, 
)))
s.add(Or(rprim_1_32!=5,
And(rx_f_1_32==0, ry_f_1_32==1, rcost_1_32==2, 
obstacle(rx_1_32 + 0, ry_1_32 + 0)==False, 
obstacle(rx_1_32 + 0, ry_1_32 + 1)==False, 
)))
s.add(Or(rprim_1_32!=6,
And(rx_f_1_32==1, ry_f_1_32==1, rcost_1_32==3, 
obstacle(rx_1_32 + 0, ry_1_32 + 0)==False, 
obstacle(rx_1_32 + 1, ry_1_32 + 1)==False, 
)))
s.add(Or(rprim_1_32!=7,
And(rx_f_1_32==-1, ry_f_1_32==1, rcost_1_32==3, 
obstacle(rx_1_32 + 0, ry_1_32 + 0)==False, 
obstacle(rx_1_32 + -1, ry_1_32 + 1)==False, 
)))
s.add(Or(rprim_1_32!=8,
And(rx_f_1_32==-1, ry_f_1_32==-1, rcost_1_32==3, 
obstacle(rx_1_32 + 0, ry_1_32 + 0)==False, 
obstacle(rx_1_32 + -1, ry_1_32 + -1)==False, 
)))
s.add(Or(rprim_1_32!=9,
And(rx_f_1_32==1, ry_f_1_32==-1, rcost_1_32==3, 
obstacle(rx_1_32 + 0, ry_1_32 + 0)==False, 
obstacle(rx_1_32 + 1, ry_1_32 + -1)==False, 
)))
s.add(Or(rprim_1_32!=10,
And(rx_f_1_32==2, ry_f_1_32==0, rcost_1_32==3, 
obstacle(rx_1_32 + 0, ry_1_32 + 0)==False, 
obstacle(rx_1_32 + 1, ry_1_32 + 0)==False, 
obstacle(rx_1_32 + 2, ry_1_32 + 0)==False, 
)))
s.add(Or(rprim_1_32!=11,
And(rx_f_1_32==0, ry_f_1_32==2, rcost_1_32==3, 
obstacle(rx_1_32 + 0, ry_1_32 + 0)==False, 
obstacle(rx_1_32 + 0, ry_1_32 + 1)==False, 
obstacle(rx_1_32 + 0, ry_1_32 + 2)==False, 
)))
s.add(Or(rprim_1_32!=12,
And(rx_f_1_32==-2, ry_f_1_32==0, rcost_1_32==3, 
obstacle(rx_1_32 + 0, ry_1_32 + 0)==False, 
obstacle(rx_1_32 + -1, ry_1_32 + 0)==False, 
obstacle(rx_1_32 + -2, ry_1_32 + 0)==False, 
)))
s.add(Or(rprim_1_32!=13,
And(rx_f_1_32==0, ry_f_1_32==-2, rcost_1_32==3, 
obstacle(rx_1_32 + 0, ry_1_32 + 0)==False, 
obstacle(rx_1_32 + 0, ry_1_32 + -1)==False, 
obstacle(rx_1_32 + 0, ry_1_32 + -2)==False, 
)))
s.add(Or(rprim_1_32!=14,
And(rx_f_1_32==2, ry_f_1_32==2, rcost_1_32==4, 
obstacle(rx_1_32 + 0, ry_1_32 + 0)==False, 
obstacle(rx_1_32 + 1, ry_1_32 + 1)==False, 
obstacle(rx_1_32 + 2, ry_1_32 + 2)==False, 
)))
s.add(Or(rprim_1_32!=15,
And(rx_f_1_32==-2, ry_f_1_32==2, rcost_1_32==4, 
obstacle(rx_1_32 + 0, ry_1_32 + 0)==False, 
obstacle(rx_1_32 + -1, ry_1_32 + 1)==False, 
obstacle(rx_1_32 + -2, ry_1_32 + 2)==False, 
)))
s.add(Or(rprim_1_32!=16,
And(rx_f_1_32==-2, ry_f_1_32==-2, rcost_1_32==4, 
obstacle(rx_1_32 + 0, ry_1_32 + 0)==False, 
obstacle(rx_1_32 + -1, ry_1_32 + -1)==False, 
obstacle(rx_1_32 + -2, ry_1_32 + -2)==False, 
)))
s.add(Or(rprim_1_32!=17,
And(rx_f_1_32==2, ry_f_1_32==-2, rcost_1_32==4, 
obstacle(rx_1_32 + 0, ry_1_32 + 0)==False, 
obstacle(rx_1_32 + 1, ry_1_32 + -1)==False, 
obstacle(rx_1_32 + 2, ry_1_32 + -2)==False, 
)))
s.add(Or(rprim_1_32!=18,
And(rx_f_1_32==3, ry_f_1_32==0, rcost_1_32==4, 
obstacle(rx_1_32 + 0, ry_1_32 + 0)==False, 
obstacle(rx_1_32 + 1, ry_1_32 + 0)==False, 
obstacle(rx_1_32 + 2, ry_1_32 + 0)==False, 
obstacle(rx_1_32 + 3, ry_1_32 + 0)==False, 
)))
s.add(Or(rprim_1_32!=19,
And(rx_f_1_32==0, ry_f_1_32==3, rcost_1_32==4, 
obstacle(rx_1_32 + 0, ry_1_32 + 0)==False, 
obstacle(rx_1_32 + 0, ry_1_32 + 1)==False, 
obstacle(rx_1_32 + 0, ry_1_32 + 2)==False, 
obstacle(rx_1_32 + 0, ry_1_32 + 3)==False, 
)))
s.add(Or(rprim_1_32!=20,
And(rx_f_1_32==-3, ry_f_1_32==0, rcost_1_32==4, 
obstacle(rx_1_32 + 0, ry_1_32 + 0)==False, 
obstacle(rx_1_32 + -1, ry_1_32 + 0)==False, 
obstacle(rx_1_32 + -2, ry_1_32 + 0)==False, 
obstacle(rx_1_32 + -3, ry_1_32 + 0)==False, 
)))
s.add(Or(rprim_1_32!=21,
And(rx_f_1_32==0, ry_f_1_32==-3, rcost_1_32==4, 
obstacle(rx_1_32 + 0, ry_1_32 + 0)==False, 
obstacle(rx_1_32 + 0, ry_1_32 + -1)==False, 
obstacle(rx_1_32 + 0, ry_1_32 + -2)==False, 
obstacle(rx_1_32 + 0, ry_1_32 + -3)==False, 
)))
s.add(Or(rprim_1_33!=1,
And(rx_f_1_33==0, ry_f_1_33==0, rcost_1_33==0, 
obstacle(rx_1_33 + 0, ry_1_33 + 0)==False, 
)))
s.add(Or(rprim_1_33!=2,
And(rx_f_1_33==1, ry_f_1_33==0, rcost_1_33==2, 
obstacle(rx_1_33 + 0, ry_1_33 + 0)==False, 
obstacle(rx_1_33 + 1, ry_1_33 + 0)==False, 
)))
s.add(Or(rprim_1_33!=3,
And(rx_f_1_33==0, ry_f_1_33==-1, rcost_1_33==2, 
obstacle(rx_1_33 + 0, ry_1_33 + 0)==False, 
obstacle(rx_1_33 + 0, ry_1_33 + -1)==False, 
)))
s.add(Or(rprim_1_33!=4,
And(rx_f_1_33==-1, ry_f_1_33==0, rcost_1_33==2, 
obstacle(rx_1_33 + 0, ry_1_33 + 0)==False, 
obstacle(rx_1_33 + -1, ry_1_33 + 0)==False, 
)))
s.add(Or(rprim_1_33!=5,
And(rx_f_1_33==0, ry_f_1_33==1, rcost_1_33==2, 
obstacle(rx_1_33 + 0, ry_1_33 + 0)==False, 
obstacle(rx_1_33 + 0, ry_1_33 + 1)==False, 
)))
s.add(Or(rprim_1_33!=6,
And(rx_f_1_33==1, ry_f_1_33==1, rcost_1_33==3, 
obstacle(rx_1_33 + 0, ry_1_33 + 0)==False, 
obstacle(rx_1_33 + 1, ry_1_33 + 1)==False, 
)))
s.add(Or(rprim_1_33!=7,
And(rx_f_1_33==-1, ry_f_1_33==1, rcost_1_33==3, 
obstacle(rx_1_33 + 0, ry_1_33 + 0)==False, 
obstacle(rx_1_33 + -1, ry_1_33 + 1)==False, 
)))
s.add(Or(rprim_1_33!=8,
And(rx_f_1_33==-1, ry_f_1_33==-1, rcost_1_33==3, 
obstacle(rx_1_33 + 0, ry_1_33 + 0)==False, 
obstacle(rx_1_33 + -1, ry_1_33 + -1)==False, 
)))
s.add(Or(rprim_1_33!=9,
And(rx_f_1_33==1, ry_f_1_33==-1, rcost_1_33==3, 
obstacle(rx_1_33 + 0, ry_1_33 + 0)==False, 
obstacle(rx_1_33 + 1, ry_1_33 + -1)==False, 
)))
s.add(Or(rprim_1_33!=10,
And(rx_f_1_33==2, ry_f_1_33==0, rcost_1_33==3, 
obstacle(rx_1_33 + 0, ry_1_33 + 0)==False, 
obstacle(rx_1_33 + 1, ry_1_33 + 0)==False, 
obstacle(rx_1_33 + 2, ry_1_33 + 0)==False, 
)))
s.add(Or(rprim_1_33!=11,
And(rx_f_1_33==0, ry_f_1_33==2, rcost_1_33==3, 
obstacle(rx_1_33 + 0, ry_1_33 + 0)==False, 
obstacle(rx_1_33 + 0, ry_1_33 + 1)==False, 
obstacle(rx_1_33 + 0, ry_1_33 + 2)==False, 
)))
s.add(Or(rprim_1_33!=12,
And(rx_f_1_33==-2, ry_f_1_33==0, rcost_1_33==3, 
obstacle(rx_1_33 + 0, ry_1_33 + 0)==False, 
obstacle(rx_1_33 + -1, ry_1_33 + 0)==False, 
obstacle(rx_1_33 + -2, ry_1_33 + 0)==False, 
)))
s.add(Or(rprim_1_33!=13,
And(rx_f_1_33==0, ry_f_1_33==-2, rcost_1_33==3, 
obstacle(rx_1_33 + 0, ry_1_33 + 0)==False, 
obstacle(rx_1_33 + 0, ry_1_33 + -1)==False, 
obstacle(rx_1_33 + 0, ry_1_33 + -2)==False, 
)))
s.add(Or(rprim_1_33!=14,
And(rx_f_1_33==2, ry_f_1_33==2, rcost_1_33==4, 
obstacle(rx_1_33 + 0, ry_1_33 + 0)==False, 
obstacle(rx_1_33 + 1, ry_1_33 + 1)==False, 
obstacle(rx_1_33 + 2, ry_1_33 + 2)==False, 
)))
s.add(Or(rprim_1_33!=15,
And(rx_f_1_33==-2, ry_f_1_33==2, rcost_1_33==4, 
obstacle(rx_1_33 + 0, ry_1_33 + 0)==False, 
obstacle(rx_1_33 + -1, ry_1_33 + 1)==False, 
obstacle(rx_1_33 + -2, ry_1_33 + 2)==False, 
)))
s.add(Or(rprim_1_33!=16,
And(rx_f_1_33==-2, ry_f_1_33==-2, rcost_1_33==4, 
obstacle(rx_1_33 + 0, ry_1_33 + 0)==False, 
obstacle(rx_1_33 + -1, ry_1_33 + -1)==False, 
obstacle(rx_1_33 + -2, ry_1_33 + -2)==False, 
)))
s.add(Or(rprim_1_33!=17,
And(rx_f_1_33==2, ry_f_1_33==-2, rcost_1_33==4, 
obstacle(rx_1_33 + 0, ry_1_33 + 0)==False, 
obstacle(rx_1_33 + 1, ry_1_33 + -1)==False, 
obstacle(rx_1_33 + 2, ry_1_33 + -2)==False, 
)))
s.add(Or(rprim_1_33!=18,
And(rx_f_1_33==3, ry_f_1_33==0, rcost_1_33==4, 
obstacle(rx_1_33 + 0, ry_1_33 + 0)==False, 
obstacle(rx_1_33 + 1, ry_1_33 + 0)==False, 
obstacle(rx_1_33 + 2, ry_1_33 + 0)==False, 
obstacle(rx_1_33 + 3, ry_1_33 + 0)==False, 
)))
s.add(Or(rprim_1_33!=19,
And(rx_f_1_33==0, ry_f_1_33==3, rcost_1_33==4, 
obstacle(rx_1_33 + 0, ry_1_33 + 0)==False, 
obstacle(rx_1_33 + 0, ry_1_33 + 1)==False, 
obstacle(rx_1_33 + 0, ry_1_33 + 2)==False, 
obstacle(rx_1_33 + 0, ry_1_33 + 3)==False, 
)))
s.add(Or(rprim_1_33!=20,
And(rx_f_1_33==-3, ry_f_1_33==0, rcost_1_33==4, 
obstacle(rx_1_33 + 0, ry_1_33 + 0)==False, 
obstacle(rx_1_33 + -1, ry_1_33 + 0)==False, 
obstacle(rx_1_33 + -2, ry_1_33 + 0)==False, 
obstacle(rx_1_33 + -3, ry_1_33 + 0)==False, 
)))
s.add(Or(rprim_1_33!=21,
And(rx_f_1_33==0, ry_f_1_33==-3, rcost_1_33==4, 
obstacle(rx_1_33 + 0, ry_1_33 + 0)==False, 
obstacle(rx_1_33 + 0, ry_1_33 + -1)==False, 
obstacle(rx_1_33 + 0, ry_1_33 + -2)==False, 
obstacle(rx_1_33 + 0, ry_1_33 + -3)==False, 
)))
s.add(Or(rprim_1_34!=1,
And(rx_f_1_34==0, ry_f_1_34==0, rcost_1_34==0, 
obstacle(rx_1_34 + 0, ry_1_34 + 0)==False, 
)))
s.add(Or(rprim_1_34!=2,
And(rx_f_1_34==1, ry_f_1_34==0, rcost_1_34==2, 
obstacle(rx_1_34 + 0, ry_1_34 + 0)==False, 
obstacle(rx_1_34 + 1, ry_1_34 + 0)==False, 
)))
s.add(Or(rprim_1_34!=3,
And(rx_f_1_34==0, ry_f_1_34==-1, rcost_1_34==2, 
obstacle(rx_1_34 + 0, ry_1_34 + 0)==False, 
obstacle(rx_1_34 + 0, ry_1_34 + -1)==False, 
)))
s.add(Or(rprim_1_34!=4,
And(rx_f_1_34==-1, ry_f_1_34==0, rcost_1_34==2, 
obstacle(rx_1_34 + 0, ry_1_34 + 0)==False, 
obstacle(rx_1_34 + -1, ry_1_34 + 0)==False, 
)))
s.add(Or(rprim_1_34!=5,
And(rx_f_1_34==0, ry_f_1_34==1, rcost_1_34==2, 
obstacle(rx_1_34 + 0, ry_1_34 + 0)==False, 
obstacle(rx_1_34 + 0, ry_1_34 + 1)==False, 
)))
s.add(Or(rprim_1_34!=6,
And(rx_f_1_34==1, ry_f_1_34==1, rcost_1_34==3, 
obstacle(rx_1_34 + 0, ry_1_34 + 0)==False, 
obstacle(rx_1_34 + 1, ry_1_34 + 1)==False, 
)))
s.add(Or(rprim_1_34!=7,
And(rx_f_1_34==-1, ry_f_1_34==1, rcost_1_34==3, 
obstacle(rx_1_34 + 0, ry_1_34 + 0)==False, 
obstacle(rx_1_34 + -1, ry_1_34 + 1)==False, 
)))
s.add(Or(rprim_1_34!=8,
And(rx_f_1_34==-1, ry_f_1_34==-1, rcost_1_34==3, 
obstacle(rx_1_34 + 0, ry_1_34 + 0)==False, 
obstacle(rx_1_34 + -1, ry_1_34 + -1)==False, 
)))
s.add(Or(rprim_1_34!=9,
And(rx_f_1_34==1, ry_f_1_34==-1, rcost_1_34==3, 
obstacle(rx_1_34 + 0, ry_1_34 + 0)==False, 
obstacle(rx_1_34 + 1, ry_1_34 + -1)==False, 
)))
s.add(Or(rprim_1_34!=10,
And(rx_f_1_34==2, ry_f_1_34==0, rcost_1_34==3, 
obstacle(rx_1_34 + 0, ry_1_34 + 0)==False, 
obstacle(rx_1_34 + 1, ry_1_34 + 0)==False, 
obstacle(rx_1_34 + 2, ry_1_34 + 0)==False, 
)))
s.add(Or(rprim_1_34!=11,
And(rx_f_1_34==0, ry_f_1_34==2, rcost_1_34==3, 
obstacle(rx_1_34 + 0, ry_1_34 + 0)==False, 
obstacle(rx_1_34 + 0, ry_1_34 + 1)==False, 
obstacle(rx_1_34 + 0, ry_1_34 + 2)==False, 
)))
s.add(Or(rprim_1_34!=12,
And(rx_f_1_34==-2, ry_f_1_34==0, rcost_1_34==3, 
obstacle(rx_1_34 + 0, ry_1_34 + 0)==False, 
obstacle(rx_1_34 + -1, ry_1_34 + 0)==False, 
obstacle(rx_1_34 + -2, ry_1_34 + 0)==False, 
)))
s.add(Or(rprim_1_34!=13,
And(rx_f_1_34==0, ry_f_1_34==-2, rcost_1_34==3, 
obstacle(rx_1_34 + 0, ry_1_34 + 0)==False, 
obstacle(rx_1_34 + 0, ry_1_34 + -1)==False, 
obstacle(rx_1_34 + 0, ry_1_34 + -2)==False, 
)))
s.add(Or(rprim_1_34!=14,
And(rx_f_1_34==2, ry_f_1_34==2, rcost_1_34==4, 
obstacle(rx_1_34 + 0, ry_1_34 + 0)==False, 
obstacle(rx_1_34 + 1, ry_1_34 + 1)==False, 
obstacle(rx_1_34 + 2, ry_1_34 + 2)==False, 
)))
s.add(Or(rprim_1_34!=15,
And(rx_f_1_34==-2, ry_f_1_34==2, rcost_1_34==4, 
obstacle(rx_1_34 + 0, ry_1_34 + 0)==False, 
obstacle(rx_1_34 + -1, ry_1_34 + 1)==False, 
obstacle(rx_1_34 + -2, ry_1_34 + 2)==False, 
)))
s.add(Or(rprim_1_34!=16,
And(rx_f_1_34==-2, ry_f_1_34==-2, rcost_1_34==4, 
obstacle(rx_1_34 + 0, ry_1_34 + 0)==False, 
obstacle(rx_1_34 + -1, ry_1_34 + -1)==False, 
obstacle(rx_1_34 + -2, ry_1_34 + -2)==False, 
)))
s.add(Or(rprim_1_34!=17,
And(rx_f_1_34==2, ry_f_1_34==-2, rcost_1_34==4, 
obstacle(rx_1_34 + 0, ry_1_34 + 0)==False, 
obstacle(rx_1_34 + 1, ry_1_34 + -1)==False, 
obstacle(rx_1_34 + 2, ry_1_34 + -2)==False, 
)))
s.add(Or(rprim_1_34!=18,
And(rx_f_1_34==3, ry_f_1_34==0, rcost_1_34==4, 
obstacle(rx_1_34 + 0, ry_1_34 + 0)==False, 
obstacle(rx_1_34 + 1, ry_1_34 + 0)==False, 
obstacle(rx_1_34 + 2, ry_1_34 + 0)==False, 
obstacle(rx_1_34 + 3, ry_1_34 + 0)==False, 
)))
s.add(Or(rprim_1_34!=19,
And(rx_f_1_34==0, ry_f_1_34==3, rcost_1_34==4, 
obstacle(rx_1_34 + 0, ry_1_34 + 0)==False, 
obstacle(rx_1_34 + 0, ry_1_34 + 1)==False, 
obstacle(rx_1_34 + 0, ry_1_34 + 2)==False, 
obstacle(rx_1_34 + 0, ry_1_34 + 3)==False, 
)))
s.add(Or(rprim_1_34!=20,
And(rx_f_1_34==-3, ry_f_1_34==0, rcost_1_34==4, 
obstacle(rx_1_34 + 0, ry_1_34 + 0)==False, 
obstacle(rx_1_34 + -1, ry_1_34 + 0)==False, 
obstacle(rx_1_34 + -2, ry_1_34 + 0)==False, 
obstacle(rx_1_34 + -3, ry_1_34 + 0)==False, 
)))
s.add(Or(rprim_1_34!=21,
And(rx_f_1_34==0, ry_f_1_34==-3, rcost_1_34==4, 
obstacle(rx_1_34 + 0, ry_1_34 + 0)==False, 
obstacle(rx_1_34 + 0, ry_1_34 + -1)==False, 
obstacle(rx_1_34 + 0, ry_1_34 + -2)==False, 
obstacle(rx_1_34 + 0, ry_1_34 + -3)==False, 
)))
s.add(Or(rprim_1_35!=1,
And(rx_f_1_35==0, ry_f_1_35==0, rcost_1_35==0, 
obstacle(rx_1_35 + 0, ry_1_35 + 0)==False, 
)))
s.add(Or(rprim_1_35!=2,
And(rx_f_1_35==1, ry_f_1_35==0, rcost_1_35==2, 
obstacle(rx_1_35 + 0, ry_1_35 + 0)==False, 
obstacle(rx_1_35 + 1, ry_1_35 + 0)==False, 
)))
s.add(Or(rprim_1_35!=3,
And(rx_f_1_35==0, ry_f_1_35==-1, rcost_1_35==2, 
obstacle(rx_1_35 + 0, ry_1_35 + 0)==False, 
obstacle(rx_1_35 + 0, ry_1_35 + -1)==False, 
)))
s.add(Or(rprim_1_35!=4,
And(rx_f_1_35==-1, ry_f_1_35==0, rcost_1_35==2, 
obstacle(rx_1_35 + 0, ry_1_35 + 0)==False, 
obstacle(rx_1_35 + -1, ry_1_35 + 0)==False, 
)))
s.add(Or(rprim_1_35!=5,
And(rx_f_1_35==0, ry_f_1_35==1, rcost_1_35==2, 
obstacle(rx_1_35 + 0, ry_1_35 + 0)==False, 
obstacle(rx_1_35 + 0, ry_1_35 + 1)==False, 
)))
s.add(Or(rprim_1_35!=6,
And(rx_f_1_35==1, ry_f_1_35==1, rcost_1_35==3, 
obstacle(rx_1_35 + 0, ry_1_35 + 0)==False, 
obstacle(rx_1_35 + 1, ry_1_35 + 1)==False, 
)))
s.add(Or(rprim_1_35!=7,
And(rx_f_1_35==-1, ry_f_1_35==1, rcost_1_35==3, 
obstacle(rx_1_35 + 0, ry_1_35 + 0)==False, 
obstacle(rx_1_35 + -1, ry_1_35 + 1)==False, 
)))
s.add(Or(rprim_1_35!=8,
And(rx_f_1_35==-1, ry_f_1_35==-1, rcost_1_35==3, 
obstacle(rx_1_35 + 0, ry_1_35 + 0)==False, 
obstacle(rx_1_35 + -1, ry_1_35 + -1)==False, 
)))
s.add(Or(rprim_1_35!=9,
And(rx_f_1_35==1, ry_f_1_35==-1, rcost_1_35==3, 
obstacle(rx_1_35 + 0, ry_1_35 + 0)==False, 
obstacle(rx_1_35 + 1, ry_1_35 + -1)==False, 
)))
s.add(Or(rprim_1_35!=10,
And(rx_f_1_35==2, ry_f_1_35==0, rcost_1_35==3, 
obstacle(rx_1_35 + 0, ry_1_35 + 0)==False, 
obstacle(rx_1_35 + 1, ry_1_35 + 0)==False, 
obstacle(rx_1_35 + 2, ry_1_35 + 0)==False, 
)))
s.add(Or(rprim_1_35!=11,
And(rx_f_1_35==0, ry_f_1_35==2, rcost_1_35==3, 
obstacle(rx_1_35 + 0, ry_1_35 + 0)==False, 
obstacle(rx_1_35 + 0, ry_1_35 + 1)==False, 
obstacle(rx_1_35 + 0, ry_1_35 + 2)==False, 
)))
s.add(Or(rprim_1_35!=12,
And(rx_f_1_35==-2, ry_f_1_35==0, rcost_1_35==3, 
obstacle(rx_1_35 + 0, ry_1_35 + 0)==False, 
obstacle(rx_1_35 + -1, ry_1_35 + 0)==False, 
obstacle(rx_1_35 + -2, ry_1_35 + 0)==False, 
)))
s.add(Or(rprim_1_35!=13,
And(rx_f_1_35==0, ry_f_1_35==-2, rcost_1_35==3, 
obstacle(rx_1_35 + 0, ry_1_35 + 0)==False, 
obstacle(rx_1_35 + 0, ry_1_35 + -1)==False, 
obstacle(rx_1_35 + 0, ry_1_35 + -2)==False, 
)))
s.add(Or(rprim_1_35!=14,
And(rx_f_1_35==2, ry_f_1_35==2, rcost_1_35==4, 
obstacle(rx_1_35 + 0, ry_1_35 + 0)==False, 
obstacle(rx_1_35 + 1, ry_1_35 + 1)==False, 
obstacle(rx_1_35 + 2, ry_1_35 + 2)==False, 
)))
s.add(Or(rprim_1_35!=15,
And(rx_f_1_35==-2, ry_f_1_35==2, rcost_1_35==4, 
obstacle(rx_1_35 + 0, ry_1_35 + 0)==False, 
obstacle(rx_1_35 + -1, ry_1_35 + 1)==False, 
obstacle(rx_1_35 + -2, ry_1_35 + 2)==False, 
)))
s.add(Or(rprim_1_35!=16,
And(rx_f_1_35==-2, ry_f_1_35==-2, rcost_1_35==4, 
obstacle(rx_1_35 + 0, ry_1_35 + 0)==False, 
obstacle(rx_1_35 + -1, ry_1_35 + -1)==False, 
obstacle(rx_1_35 + -2, ry_1_35 + -2)==False, 
)))
s.add(Or(rprim_1_35!=17,
And(rx_f_1_35==2, ry_f_1_35==-2, rcost_1_35==4, 
obstacle(rx_1_35 + 0, ry_1_35 + 0)==False, 
obstacle(rx_1_35 + 1, ry_1_35 + -1)==False, 
obstacle(rx_1_35 + 2, ry_1_35 + -2)==False, 
)))
s.add(Or(rprim_1_35!=18,
And(rx_f_1_35==3, ry_f_1_35==0, rcost_1_35==4, 
obstacle(rx_1_35 + 0, ry_1_35 + 0)==False, 
obstacle(rx_1_35 + 1, ry_1_35 + 0)==False, 
obstacle(rx_1_35 + 2, ry_1_35 + 0)==False, 
obstacle(rx_1_35 + 3, ry_1_35 + 0)==False, 
)))
s.add(Or(rprim_1_35!=19,
And(rx_f_1_35==0, ry_f_1_35==3, rcost_1_35==4, 
obstacle(rx_1_35 + 0, ry_1_35 + 0)==False, 
obstacle(rx_1_35 + 0, ry_1_35 + 1)==False, 
obstacle(rx_1_35 + 0, ry_1_35 + 2)==False, 
obstacle(rx_1_35 + 0, ry_1_35 + 3)==False, 
)))
s.add(Or(rprim_1_35!=20,
And(rx_f_1_35==-3, ry_f_1_35==0, rcost_1_35==4, 
obstacle(rx_1_35 + 0, ry_1_35 + 0)==False, 
obstacle(rx_1_35 + -1, ry_1_35 + 0)==False, 
obstacle(rx_1_35 + -2, ry_1_35 + 0)==False, 
obstacle(rx_1_35 + -3, ry_1_35 + 0)==False, 
)))
s.add(Or(rprim_1_35!=21,
And(rx_f_1_35==0, ry_f_1_35==-3, rcost_1_35==4, 
obstacle(rx_1_35 + 0, ry_1_35 + 0)==False, 
obstacle(rx_1_35 + 0, ry_1_35 + -1)==False, 
obstacle(rx_1_35 + 0, ry_1_35 + -2)==False, 
obstacle(rx_1_35 + 0, ry_1_35 + -3)==False, 
)))
s.add(Or(rprim_1_36!=1,
And(rx_f_1_36==0, ry_f_1_36==0, rcost_1_36==0, 
obstacle(rx_1_36 + 0, ry_1_36 + 0)==False, 
)))
s.add(Or(rprim_1_36!=2,
And(rx_f_1_36==1, ry_f_1_36==0, rcost_1_36==2, 
obstacle(rx_1_36 + 0, ry_1_36 + 0)==False, 
obstacle(rx_1_36 + 1, ry_1_36 + 0)==False, 
)))
s.add(Or(rprim_1_36!=3,
And(rx_f_1_36==0, ry_f_1_36==-1, rcost_1_36==2, 
obstacle(rx_1_36 + 0, ry_1_36 + 0)==False, 
obstacle(rx_1_36 + 0, ry_1_36 + -1)==False, 
)))
s.add(Or(rprim_1_36!=4,
And(rx_f_1_36==-1, ry_f_1_36==0, rcost_1_36==2, 
obstacle(rx_1_36 + 0, ry_1_36 + 0)==False, 
obstacle(rx_1_36 + -1, ry_1_36 + 0)==False, 
)))
s.add(Or(rprim_1_36!=5,
And(rx_f_1_36==0, ry_f_1_36==1, rcost_1_36==2, 
obstacle(rx_1_36 + 0, ry_1_36 + 0)==False, 
obstacle(rx_1_36 + 0, ry_1_36 + 1)==False, 
)))
s.add(Or(rprim_1_36!=6,
And(rx_f_1_36==1, ry_f_1_36==1, rcost_1_36==3, 
obstacle(rx_1_36 + 0, ry_1_36 + 0)==False, 
obstacle(rx_1_36 + 1, ry_1_36 + 1)==False, 
)))
s.add(Or(rprim_1_36!=7,
And(rx_f_1_36==-1, ry_f_1_36==1, rcost_1_36==3, 
obstacle(rx_1_36 + 0, ry_1_36 + 0)==False, 
obstacle(rx_1_36 + -1, ry_1_36 + 1)==False, 
)))
s.add(Or(rprim_1_36!=8,
And(rx_f_1_36==-1, ry_f_1_36==-1, rcost_1_36==3, 
obstacle(rx_1_36 + 0, ry_1_36 + 0)==False, 
obstacle(rx_1_36 + -1, ry_1_36 + -1)==False, 
)))
s.add(Or(rprim_1_36!=9,
And(rx_f_1_36==1, ry_f_1_36==-1, rcost_1_36==3, 
obstacle(rx_1_36 + 0, ry_1_36 + 0)==False, 
obstacle(rx_1_36 + 1, ry_1_36 + -1)==False, 
)))
s.add(Or(rprim_1_36!=10,
And(rx_f_1_36==2, ry_f_1_36==0, rcost_1_36==3, 
obstacle(rx_1_36 + 0, ry_1_36 + 0)==False, 
obstacle(rx_1_36 + 1, ry_1_36 + 0)==False, 
obstacle(rx_1_36 + 2, ry_1_36 + 0)==False, 
)))
s.add(Or(rprim_1_36!=11,
And(rx_f_1_36==0, ry_f_1_36==2, rcost_1_36==3, 
obstacle(rx_1_36 + 0, ry_1_36 + 0)==False, 
obstacle(rx_1_36 + 0, ry_1_36 + 1)==False, 
obstacle(rx_1_36 + 0, ry_1_36 + 2)==False, 
)))
s.add(Or(rprim_1_36!=12,
And(rx_f_1_36==-2, ry_f_1_36==0, rcost_1_36==3, 
obstacle(rx_1_36 + 0, ry_1_36 + 0)==False, 
obstacle(rx_1_36 + -1, ry_1_36 + 0)==False, 
obstacle(rx_1_36 + -2, ry_1_36 + 0)==False, 
)))
s.add(Or(rprim_1_36!=13,
And(rx_f_1_36==0, ry_f_1_36==-2, rcost_1_36==3, 
obstacle(rx_1_36 + 0, ry_1_36 + 0)==False, 
obstacle(rx_1_36 + 0, ry_1_36 + -1)==False, 
obstacle(rx_1_36 + 0, ry_1_36 + -2)==False, 
)))
s.add(Or(rprim_1_36!=14,
And(rx_f_1_36==2, ry_f_1_36==2, rcost_1_36==4, 
obstacle(rx_1_36 + 0, ry_1_36 + 0)==False, 
obstacle(rx_1_36 + 1, ry_1_36 + 1)==False, 
obstacle(rx_1_36 + 2, ry_1_36 + 2)==False, 
)))
s.add(Or(rprim_1_36!=15,
And(rx_f_1_36==-2, ry_f_1_36==2, rcost_1_36==4, 
obstacle(rx_1_36 + 0, ry_1_36 + 0)==False, 
obstacle(rx_1_36 + -1, ry_1_36 + 1)==False, 
obstacle(rx_1_36 + -2, ry_1_36 + 2)==False, 
)))
s.add(Or(rprim_1_36!=16,
And(rx_f_1_36==-2, ry_f_1_36==-2, rcost_1_36==4, 
obstacle(rx_1_36 + 0, ry_1_36 + 0)==False, 
obstacle(rx_1_36 + -1, ry_1_36 + -1)==False, 
obstacle(rx_1_36 + -2, ry_1_36 + -2)==False, 
)))
s.add(Or(rprim_1_36!=17,
And(rx_f_1_36==2, ry_f_1_36==-2, rcost_1_36==4, 
obstacle(rx_1_36 + 0, ry_1_36 + 0)==False, 
obstacle(rx_1_36 + 1, ry_1_36 + -1)==False, 
obstacle(rx_1_36 + 2, ry_1_36 + -2)==False, 
)))
s.add(Or(rprim_1_36!=18,
And(rx_f_1_36==3, ry_f_1_36==0, rcost_1_36==4, 
obstacle(rx_1_36 + 0, ry_1_36 + 0)==False, 
obstacle(rx_1_36 + 1, ry_1_36 + 0)==False, 
obstacle(rx_1_36 + 2, ry_1_36 + 0)==False, 
obstacle(rx_1_36 + 3, ry_1_36 + 0)==False, 
)))
s.add(Or(rprim_1_36!=19,
And(rx_f_1_36==0, ry_f_1_36==3, rcost_1_36==4, 
obstacle(rx_1_36 + 0, ry_1_36 + 0)==False, 
obstacle(rx_1_36 + 0, ry_1_36 + 1)==False, 
obstacle(rx_1_36 + 0, ry_1_36 + 2)==False, 
obstacle(rx_1_36 + 0, ry_1_36 + 3)==False, 
)))
s.add(Or(rprim_1_36!=20,
And(rx_f_1_36==-3, ry_f_1_36==0, rcost_1_36==4, 
obstacle(rx_1_36 + 0, ry_1_36 + 0)==False, 
obstacle(rx_1_36 + -1, ry_1_36 + 0)==False, 
obstacle(rx_1_36 + -2, ry_1_36 + 0)==False, 
obstacle(rx_1_36 + -3, ry_1_36 + 0)==False, 
)))
s.add(Or(rprim_1_36!=21,
And(rx_f_1_36==0, ry_f_1_36==-3, rcost_1_36==4, 
obstacle(rx_1_36 + 0, ry_1_36 + 0)==False, 
obstacle(rx_1_36 + 0, ry_1_36 + -1)==False, 
obstacle(rx_1_36 + 0, ry_1_36 + -2)==False, 
obstacle(rx_1_36 + 0, ry_1_36 + -3)==False, 
)))
s.add(Or(rprim_1_37!=1,
And(rx_f_1_37==0, ry_f_1_37==0, rcost_1_37==0, 
obstacle(rx_1_37 + 0, ry_1_37 + 0)==False, 
)))
s.add(Or(rprim_1_37!=2,
And(rx_f_1_37==1, ry_f_1_37==0, rcost_1_37==2, 
obstacle(rx_1_37 + 0, ry_1_37 + 0)==False, 
obstacle(rx_1_37 + 1, ry_1_37 + 0)==False, 
)))
s.add(Or(rprim_1_37!=3,
And(rx_f_1_37==0, ry_f_1_37==-1, rcost_1_37==2, 
obstacle(rx_1_37 + 0, ry_1_37 + 0)==False, 
obstacle(rx_1_37 + 0, ry_1_37 + -1)==False, 
)))
s.add(Or(rprim_1_37!=4,
And(rx_f_1_37==-1, ry_f_1_37==0, rcost_1_37==2, 
obstacle(rx_1_37 + 0, ry_1_37 + 0)==False, 
obstacle(rx_1_37 + -1, ry_1_37 + 0)==False, 
)))
s.add(Or(rprim_1_37!=5,
And(rx_f_1_37==0, ry_f_1_37==1, rcost_1_37==2, 
obstacle(rx_1_37 + 0, ry_1_37 + 0)==False, 
obstacle(rx_1_37 + 0, ry_1_37 + 1)==False, 
)))
s.add(Or(rprim_1_37!=6,
And(rx_f_1_37==1, ry_f_1_37==1, rcost_1_37==3, 
obstacle(rx_1_37 + 0, ry_1_37 + 0)==False, 
obstacle(rx_1_37 + 1, ry_1_37 + 1)==False, 
)))
s.add(Or(rprim_1_37!=7,
And(rx_f_1_37==-1, ry_f_1_37==1, rcost_1_37==3, 
obstacle(rx_1_37 + 0, ry_1_37 + 0)==False, 
obstacle(rx_1_37 + -1, ry_1_37 + 1)==False, 
)))
s.add(Or(rprim_1_37!=8,
And(rx_f_1_37==-1, ry_f_1_37==-1, rcost_1_37==3, 
obstacle(rx_1_37 + 0, ry_1_37 + 0)==False, 
obstacle(rx_1_37 + -1, ry_1_37 + -1)==False, 
)))
s.add(Or(rprim_1_37!=9,
And(rx_f_1_37==1, ry_f_1_37==-1, rcost_1_37==3, 
obstacle(rx_1_37 + 0, ry_1_37 + 0)==False, 
obstacle(rx_1_37 + 1, ry_1_37 + -1)==False, 
)))
s.add(Or(rprim_1_37!=10,
And(rx_f_1_37==2, ry_f_1_37==0, rcost_1_37==3, 
obstacle(rx_1_37 + 0, ry_1_37 + 0)==False, 
obstacle(rx_1_37 + 1, ry_1_37 + 0)==False, 
obstacle(rx_1_37 + 2, ry_1_37 + 0)==False, 
)))
s.add(Or(rprim_1_37!=11,
And(rx_f_1_37==0, ry_f_1_37==2, rcost_1_37==3, 
obstacle(rx_1_37 + 0, ry_1_37 + 0)==False, 
obstacle(rx_1_37 + 0, ry_1_37 + 1)==False, 
obstacle(rx_1_37 + 0, ry_1_37 + 2)==False, 
)))
s.add(Or(rprim_1_37!=12,
And(rx_f_1_37==-2, ry_f_1_37==0, rcost_1_37==3, 
obstacle(rx_1_37 + 0, ry_1_37 + 0)==False, 
obstacle(rx_1_37 + -1, ry_1_37 + 0)==False, 
obstacle(rx_1_37 + -2, ry_1_37 + 0)==False, 
)))
s.add(Or(rprim_1_37!=13,
And(rx_f_1_37==0, ry_f_1_37==-2, rcost_1_37==3, 
obstacle(rx_1_37 + 0, ry_1_37 + 0)==False, 
obstacle(rx_1_37 + 0, ry_1_37 + -1)==False, 
obstacle(rx_1_37 + 0, ry_1_37 + -2)==False, 
)))
s.add(Or(rprim_1_37!=14,
And(rx_f_1_37==2, ry_f_1_37==2, rcost_1_37==4, 
obstacle(rx_1_37 + 0, ry_1_37 + 0)==False, 
obstacle(rx_1_37 + 1, ry_1_37 + 1)==False, 
obstacle(rx_1_37 + 2, ry_1_37 + 2)==False, 
)))
s.add(Or(rprim_1_37!=15,
And(rx_f_1_37==-2, ry_f_1_37==2, rcost_1_37==4, 
obstacle(rx_1_37 + 0, ry_1_37 + 0)==False, 
obstacle(rx_1_37 + -1, ry_1_37 + 1)==False, 
obstacle(rx_1_37 + -2, ry_1_37 + 2)==False, 
)))
s.add(Or(rprim_1_37!=16,
And(rx_f_1_37==-2, ry_f_1_37==-2, rcost_1_37==4, 
obstacle(rx_1_37 + 0, ry_1_37 + 0)==False, 
obstacle(rx_1_37 + -1, ry_1_37 + -1)==False, 
obstacle(rx_1_37 + -2, ry_1_37 + -2)==False, 
)))
s.add(Or(rprim_1_37!=17,
And(rx_f_1_37==2, ry_f_1_37==-2, rcost_1_37==4, 
obstacle(rx_1_37 + 0, ry_1_37 + 0)==False, 
obstacle(rx_1_37 + 1, ry_1_37 + -1)==False, 
obstacle(rx_1_37 + 2, ry_1_37 + -2)==False, 
)))
s.add(Or(rprim_1_37!=18,
And(rx_f_1_37==3, ry_f_1_37==0, rcost_1_37==4, 
obstacle(rx_1_37 + 0, ry_1_37 + 0)==False, 
obstacle(rx_1_37 + 1, ry_1_37 + 0)==False, 
obstacle(rx_1_37 + 2, ry_1_37 + 0)==False, 
obstacle(rx_1_37 + 3, ry_1_37 + 0)==False, 
)))
s.add(Or(rprim_1_37!=19,
And(rx_f_1_37==0, ry_f_1_37==3, rcost_1_37==4, 
obstacle(rx_1_37 + 0, ry_1_37 + 0)==False, 
obstacle(rx_1_37 + 0, ry_1_37 + 1)==False, 
obstacle(rx_1_37 + 0, ry_1_37 + 2)==False, 
obstacle(rx_1_37 + 0, ry_1_37 + 3)==False, 
)))
s.add(Or(rprim_1_37!=20,
And(rx_f_1_37==-3, ry_f_1_37==0, rcost_1_37==4, 
obstacle(rx_1_37 + 0, ry_1_37 + 0)==False, 
obstacle(rx_1_37 + -1, ry_1_37 + 0)==False, 
obstacle(rx_1_37 + -2, ry_1_37 + 0)==False, 
obstacle(rx_1_37 + -3, ry_1_37 + 0)==False, 
)))
s.add(Or(rprim_1_37!=21,
And(rx_f_1_37==0, ry_f_1_37==-3, rcost_1_37==4, 
obstacle(rx_1_37 + 0, ry_1_37 + 0)==False, 
obstacle(rx_1_37 + 0, ry_1_37 + -1)==False, 
obstacle(rx_1_37 + 0, ry_1_37 + -2)==False, 
obstacle(rx_1_37 + 0, ry_1_37 + -3)==False, 
)))
s.add(Or(rprim_1_38!=1,
And(rx_f_1_38==0, ry_f_1_38==0, rcost_1_38==0, 
obstacle(rx_1_38 + 0, ry_1_38 + 0)==False, 
)))
s.add(Or(rprim_1_38!=2,
And(rx_f_1_38==1, ry_f_1_38==0, rcost_1_38==2, 
obstacle(rx_1_38 + 0, ry_1_38 + 0)==False, 
obstacle(rx_1_38 + 1, ry_1_38 + 0)==False, 
)))
s.add(Or(rprim_1_38!=3,
And(rx_f_1_38==0, ry_f_1_38==-1, rcost_1_38==2, 
obstacle(rx_1_38 + 0, ry_1_38 + 0)==False, 
obstacle(rx_1_38 + 0, ry_1_38 + -1)==False, 
)))
s.add(Or(rprim_1_38!=4,
And(rx_f_1_38==-1, ry_f_1_38==0, rcost_1_38==2, 
obstacle(rx_1_38 + 0, ry_1_38 + 0)==False, 
obstacle(rx_1_38 + -1, ry_1_38 + 0)==False, 
)))
s.add(Or(rprim_1_38!=5,
And(rx_f_1_38==0, ry_f_1_38==1, rcost_1_38==2, 
obstacle(rx_1_38 + 0, ry_1_38 + 0)==False, 
obstacle(rx_1_38 + 0, ry_1_38 + 1)==False, 
)))
s.add(Or(rprim_1_38!=6,
And(rx_f_1_38==1, ry_f_1_38==1, rcost_1_38==3, 
obstacle(rx_1_38 + 0, ry_1_38 + 0)==False, 
obstacle(rx_1_38 + 1, ry_1_38 + 1)==False, 
)))
s.add(Or(rprim_1_38!=7,
And(rx_f_1_38==-1, ry_f_1_38==1, rcost_1_38==3, 
obstacle(rx_1_38 + 0, ry_1_38 + 0)==False, 
obstacle(rx_1_38 + -1, ry_1_38 + 1)==False, 
)))
s.add(Or(rprim_1_38!=8,
And(rx_f_1_38==-1, ry_f_1_38==-1, rcost_1_38==3, 
obstacle(rx_1_38 + 0, ry_1_38 + 0)==False, 
obstacle(rx_1_38 + -1, ry_1_38 + -1)==False, 
)))
s.add(Or(rprim_1_38!=9,
And(rx_f_1_38==1, ry_f_1_38==-1, rcost_1_38==3, 
obstacle(rx_1_38 + 0, ry_1_38 + 0)==False, 
obstacle(rx_1_38 + 1, ry_1_38 + -1)==False, 
)))
s.add(Or(rprim_1_38!=10,
And(rx_f_1_38==2, ry_f_1_38==0, rcost_1_38==3, 
obstacle(rx_1_38 + 0, ry_1_38 + 0)==False, 
obstacle(rx_1_38 + 1, ry_1_38 + 0)==False, 
obstacle(rx_1_38 + 2, ry_1_38 + 0)==False, 
)))
s.add(Or(rprim_1_38!=11,
And(rx_f_1_38==0, ry_f_1_38==2, rcost_1_38==3, 
obstacle(rx_1_38 + 0, ry_1_38 + 0)==False, 
obstacle(rx_1_38 + 0, ry_1_38 + 1)==False, 
obstacle(rx_1_38 + 0, ry_1_38 + 2)==False, 
)))
s.add(Or(rprim_1_38!=12,
And(rx_f_1_38==-2, ry_f_1_38==0, rcost_1_38==3, 
obstacle(rx_1_38 + 0, ry_1_38 + 0)==False, 
obstacle(rx_1_38 + -1, ry_1_38 + 0)==False, 
obstacle(rx_1_38 + -2, ry_1_38 + 0)==False, 
)))
s.add(Or(rprim_1_38!=13,
And(rx_f_1_38==0, ry_f_1_38==-2, rcost_1_38==3, 
obstacle(rx_1_38 + 0, ry_1_38 + 0)==False, 
obstacle(rx_1_38 + 0, ry_1_38 + -1)==False, 
obstacle(rx_1_38 + 0, ry_1_38 + -2)==False, 
)))
s.add(Or(rprim_1_38!=14,
And(rx_f_1_38==2, ry_f_1_38==2, rcost_1_38==4, 
obstacle(rx_1_38 + 0, ry_1_38 + 0)==False, 
obstacle(rx_1_38 + 1, ry_1_38 + 1)==False, 
obstacle(rx_1_38 + 2, ry_1_38 + 2)==False, 
)))
s.add(Or(rprim_1_38!=15,
And(rx_f_1_38==-2, ry_f_1_38==2, rcost_1_38==4, 
obstacle(rx_1_38 + 0, ry_1_38 + 0)==False, 
obstacle(rx_1_38 + -1, ry_1_38 + 1)==False, 
obstacle(rx_1_38 + -2, ry_1_38 + 2)==False, 
)))
s.add(Or(rprim_1_38!=16,
And(rx_f_1_38==-2, ry_f_1_38==-2, rcost_1_38==4, 
obstacle(rx_1_38 + 0, ry_1_38 + 0)==False, 
obstacle(rx_1_38 + -1, ry_1_38 + -1)==False, 
obstacle(rx_1_38 + -2, ry_1_38 + -2)==False, 
)))
s.add(Or(rprim_1_38!=17,
And(rx_f_1_38==2, ry_f_1_38==-2, rcost_1_38==4, 
obstacle(rx_1_38 + 0, ry_1_38 + 0)==False, 
obstacle(rx_1_38 + 1, ry_1_38 + -1)==False, 
obstacle(rx_1_38 + 2, ry_1_38 + -2)==False, 
)))
s.add(Or(rprim_1_38!=18,
And(rx_f_1_38==3, ry_f_1_38==0, rcost_1_38==4, 
obstacle(rx_1_38 + 0, ry_1_38 + 0)==False, 
obstacle(rx_1_38 + 1, ry_1_38 + 0)==False, 
obstacle(rx_1_38 + 2, ry_1_38 + 0)==False, 
obstacle(rx_1_38 + 3, ry_1_38 + 0)==False, 
)))
s.add(Or(rprim_1_38!=19,
And(rx_f_1_38==0, ry_f_1_38==3, rcost_1_38==4, 
obstacle(rx_1_38 + 0, ry_1_38 + 0)==False, 
obstacle(rx_1_38 + 0, ry_1_38 + 1)==False, 
obstacle(rx_1_38 + 0, ry_1_38 + 2)==False, 
obstacle(rx_1_38 + 0, ry_1_38 + 3)==False, 
)))
s.add(Or(rprim_1_38!=20,
And(rx_f_1_38==-3, ry_f_1_38==0, rcost_1_38==4, 
obstacle(rx_1_38 + 0, ry_1_38 + 0)==False, 
obstacle(rx_1_38 + -1, ry_1_38 + 0)==False, 
obstacle(rx_1_38 + -2, ry_1_38 + 0)==False, 
obstacle(rx_1_38 + -3, ry_1_38 + 0)==False, 
)))
s.add(Or(rprim_1_38!=21,
And(rx_f_1_38==0, ry_f_1_38==-3, rcost_1_38==4, 
obstacle(rx_1_38 + 0, ry_1_38 + 0)==False, 
obstacle(rx_1_38 + 0, ry_1_38 + -1)==False, 
obstacle(rx_1_38 + 0, ry_1_38 + -2)==False, 
obstacle(rx_1_38 + 0, ry_1_38 + -3)==False, 
)))
s.add(Or(rprim_1_39!=1,
And(rx_f_1_39==0, ry_f_1_39==0, rcost_1_39==0, 
obstacle(rx_1_39 + 0, ry_1_39 + 0)==False, 
)))
s.add(Or(rprim_1_39!=2,
And(rx_f_1_39==1, ry_f_1_39==0, rcost_1_39==2, 
obstacle(rx_1_39 + 0, ry_1_39 + 0)==False, 
obstacle(rx_1_39 + 1, ry_1_39 + 0)==False, 
)))
s.add(Or(rprim_1_39!=3,
And(rx_f_1_39==0, ry_f_1_39==-1, rcost_1_39==2, 
obstacle(rx_1_39 + 0, ry_1_39 + 0)==False, 
obstacle(rx_1_39 + 0, ry_1_39 + -1)==False, 
)))
s.add(Or(rprim_1_39!=4,
And(rx_f_1_39==-1, ry_f_1_39==0, rcost_1_39==2, 
obstacle(rx_1_39 + 0, ry_1_39 + 0)==False, 
obstacle(rx_1_39 + -1, ry_1_39 + 0)==False, 
)))
s.add(Or(rprim_1_39!=5,
And(rx_f_1_39==0, ry_f_1_39==1, rcost_1_39==2, 
obstacle(rx_1_39 + 0, ry_1_39 + 0)==False, 
obstacle(rx_1_39 + 0, ry_1_39 + 1)==False, 
)))
s.add(Or(rprim_1_39!=6,
And(rx_f_1_39==1, ry_f_1_39==1, rcost_1_39==3, 
obstacle(rx_1_39 + 0, ry_1_39 + 0)==False, 
obstacle(rx_1_39 + 1, ry_1_39 + 1)==False, 
)))
s.add(Or(rprim_1_39!=7,
And(rx_f_1_39==-1, ry_f_1_39==1, rcost_1_39==3, 
obstacle(rx_1_39 + 0, ry_1_39 + 0)==False, 
obstacle(rx_1_39 + -1, ry_1_39 + 1)==False, 
)))
s.add(Or(rprim_1_39!=8,
And(rx_f_1_39==-1, ry_f_1_39==-1, rcost_1_39==3, 
obstacle(rx_1_39 + 0, ry_1_39 + 0)==False, 
obstacle(rx_1_39 + -1, ry_1_39 + -1)==False, 
)))
s.add(Or(rprim_1_39!=9,
And(rx_f_1_39==1, ry_f_1_39==-1, rcost_1_39==3, 
obstacle(rx_1_39 + 0, ry_1_39 + 0)==False, 
obstacle(rx_1_39 + 1, ry_1_39 + -1)==False, 
)))
s.add(Or(rprim_1_39!=10,
And(rx_f_1_39==2, ry_f_1_39==0, rcost_1_39==3, 
obstacle(rx_1_39 + 0, ry_1_39 + 0)==False, 
obstacle(rx_1_39 + 1, ry_1_39 + 0)==False, 
obstacle(rx_1_39 + 2, ry_1_39 + 0)==False, 
)))
s.add(Or(rprim_1_39!=11,
And(rx_f_1_39==0, ry_f_1_39==2, rcost_1_39==3, 
obstacle(rx_1_39 + 0, ry_1_39 + 0)==False, 
obstacle(rx_1_39 + 0, ry_1_39 + 1)==False, 
obstacle(rx_1_39 + 0, ry_1_39 + 2)==False, 
)))
s.add(Or(rprim_1_39!=12,
And(rx_f_1_39==-2, ry_f_1_39==0, rcost_1_39==3, 
obstacle(rx_1_39 + 0, ry_1_39 + 0)==False, 
obstacle(rx_1_39 + -1, ry_1_39 + 0)==False, 
obstacle(rx_1_39 + -2, ry_1_39 + 0)==False, 
)))
s.add(Or(rprim_1_39!=13,
And(rx_f_1_39==0, ry_f_1_39==-2, rcost_1_39==3, 
obstacle(rx_1_39 + 0, ry_1_39 + 0)==False, 
obstacle(rx_1_39 + 0, ry_1_39 + -1)==False, 
obstacle(rx_1_39 + 0, ry_1_39 + -2)==False, 
)))
s.add(Or(rprim_1_39!=14,
And(rx_f_1_39==2, ry_f_1_39==2, rcost_1_39==4, 
obstacle(rx_1_39 + 0, ry_1_39 + 0)==False, 
obstacle(rx_1_39 + 1, ry_1_39 + 1)==False, 
obstacle(rx_1_39 + 2, ry_1_39 + 2)==False, 
)))
s.add(Or(rprim_1_39!=15,
And(rx_f_1_39==-2, ry_f_1_39==2, rcost_1_39==4, 
obstacle(rx_1_39 + 0, ry_1_39 + 0)==False, 
obstacle(rx_1_39 + -1, ry_1_39 + 1)==False, 
obstacle(rx_1_39 + -2, ry_1_39 + 2)==False, 
)))
s.add(Or(rprim_1_39!=16,
And(rx_f_1_39==-2, ry_f_1_39==-2, rcost_1_39==4, 
obstacle(rx_1_39 + 0, ry_1_39 + 0)==False, 
obstacle(rx_1_39 + -1, ry_1_39 + -1)==False, 
obstacle(rx_1_39 + -2, ry_1_39 + -2)==False, 
)))
s.add(Or(rprim_1_39!=17,
And(rx_f_1_39==2, ry_f_1_39==-2, rcost_1_39==4, 
obstacle(rx_1_39 + 0, ry_1_39 + 0)==False, 
obstacle(rx_1_39 + 1, ry_1_39 + -1)==False, 
obstacle(rx_1_39 + 2, ry_1_39 + -2)==False, 
)))
s.add(Or(rprim_1_39!=18,
And(rx_f_1_39==3, ry_f_1_39==0, rcost_1_39==4, 
obstacle(rx_1_39 + 0, ry_1_39 + 0)==False, 
obstacle(rx_1_39 + 1, ry_1_39 + 0)==False, 
obstacle(rx_1_39 + 2, ry_1_39 + 0)==False, 
obstacle(rx_1_39 + 3, ry_1_39 + 0)==False, 
)))
s.add(Or(rprim_1_39!=19,
And(rx_f_1_39==0, ry_f_1_39==3, rcost_1_39==4, 
obstacle(rx_1_39 + 0, ry_1_39 + 0)==False, 
obstacle(rx_1_39 + 0, ry_1_39 + 1)==False, 
obstacle(rx_1_39 + 0, ry_1_39 + 2)==False, 
obstacle(rx_1_39 + 0, ry_1_39 + 3)==False, 
)))
s.add(Or(rprim_1_39!=20,
And(rx_f_1_39==-3, ry_f_1_39==0, rcost_1_39==4, 
obstacle(rx_1_39 + 0, ry_1_39 + 0)==False, 
obstacle(rx_1_39 + -1, ry_1_39 + 0)==False, 
obstacle(rx_1_39 + -2, ry_1_39 + 0)==False, 
obstacle(rx_1_39 + -3, ry_1_39 + 0)==False, 
)))
s.add(Or(rprim_1_39!=21,
And(rx_f_1_39==0, ry_f_1_39==-3, rcost_1_39==4, 
obstacle(rx_1_39 + 0, ry_1_39 + 0)==False, 
obstacle(rx_1_39 + 0, ry_1_39 + -1)==False, 
obstacle(rx_1_39 + 0, ry_1_39 + -2)==False, 
obstacle(rx_1_39 + 0, ry_1_39 + -3)==False, 
)))
s.add(Or(rprim_1_40!=1,
And(rx_f_1_40==0, ry_f_1_40==0, rcost_1_40==0, 
obstacle(rx_1_40 + 0, ry_1_40 + 0)==False, 
)))
s.add(Or(rprim_1_40!=2,
And(rx_f_1_40==1, ry_f_1_40==0, rcost_1_40==2, 
obstacle(rx_1_40 + 0, ry_1_40 + 0)==False, 
obstacle(rx_1_40 + 1, ry_1_40 + 0)==False, 
)))
s.add(Or(rprim_1_40!=3,
And(rx_f_1_40==0, ry_f_1_40==-1, rcost_1_40==2, 
obstacle(rx_1_40 + 0, ry_1_40 + 0)==False, 
obstacle(rx_1_40 + 0, ry_1_40 + -1)==False, 
)))
s.add(Or(rprim_1_40!=4,
And(rx_f_1_40==-1, ry_f_1_40==0, rcost_1_40==2, 
obstacle(rx_1_40 + 0, ry_1_40 + 0)==False, 
obstacle(rx_1_40 + -1, ry_1_40 + 0)==False, 
)))
s.add(Or(rprim_1_40!=5,
And(rx_f_1_40==0, ry_f_1_40==1, rcost_1_40==2, 
obstacle(rx_1_40 + 0, ry_1_40 + 0)==False, 
obstacle(rx_1_40 + 0, ry_1_40 + 1)==False, 
)))
s.add(Or(rprim_1_40!=6,
And(rx_f_1_40==1, ry_f_1_40==1, rcost_1_40==3, 
obstacle(rx_1_40 + 0, ry_1_40 + 0)==False, 
obstacle(rx_1_40 + 1, ry_1_40 + 1)==False, 
)))
s.add(Or(rprim_1_40!=7,
And(rx_f_1_40==-1, ry_f_1_40==1, rcost_1_40==3, 
obstacle(rx_1_40 + 0, ry_1_40 + 0)==False, 
obstacle(rx_1_40 + -1, ry_1_40 + 1)==False, 
)))
s.add(Or(rprim_1_40!=8,
And(rx_f_1_40==-1, ry_f_1_40==-1, rcost_1_40==3, 
obstacle(rx_1_40 + 0, ry_1_40 + 0)==False, 
obstacle(rx_1_40 + -1, ry_1_40 + -1)==False, 
)))
s.add(Or(rprim_1_40!=9,
And(rx_f_1_40==1, ry_f_1_40==-1, rcost_1_40==3, 
obstacle(rx_1_40 + 0, ry_1_40 + 0)==False, 
obstacle(rx_1_40 + 1, ry_1_40 + -1)==False, 
)))
s.add(Or(rprim_1_40!=10,
And(rx_f_1_40==2, ry_f_1_40==0, rcost_1_40==3, 
obstacle(rx_1_40 + 0, ry_1_40 + 0)==False, 
obstacle(rx_1_40 + 1, ry_1_40 + 0)==False, 
obstacle(rx_1_40 + 2, ry_1_40 + 0)==False, 
)))
s.add(Or(rprim_1_40!=11,
And(rx_f_1_40==0, ry_f_1_40==2, rcost_1_40==3, 
obstacle(rx_1_40 + 0, ry_1_40 + 0)==False, 
obstacle(rx_1_40 + 0, ry_1_40 + 1)==False, 
obstacle(rx_1_40 + 0, ry_1_40 + 2)==False, 
)))
s.add(Or(rprim_1_40!=12,
And(rx_f_1_40==-2, ry_f_1_40==0, rcost_1_40==3, 
obstacle(rx_1_40 + 0, ry_1_40 + 0)==False, 
obstacle(rx_1_40 + -1, ry_1_40 + 0)==False, 
obstacle(rx_1_40 + -2, ry_1_40 + 0)==False, 
)))
s.add(Or(rprim_1_40!=13,
And(rx_f_1_40==0, ry_f_1_40==-2, rcost_1_40==3, 
obstacle(rx_1_40 + 0, ry_1_40 + 0)==False, 
obstacle(rx_1_40 + 0, ry_1_40 + -1)==False, 
obstacle(rx_1_40 + 0, ry_1_40 + -2)==False, 
)))
s.add(Or(rprim_1_40!=14,
And(rx_f_1_40==2, ry_f_1_40==2, rcost_1_40==4, 
obstacle(rx_1_40 + 0, ry_1_40 + 0)==False, 
obstacle(rx_1_40 + 1, ry_1_40 + 1)==False, 
obstacle(rx_1_40 + 2, ry_1_40 + 2)==False, 
)))
s.add(Or(rprim_1_40!=15,
And(rx_f_1_40==-2, ry_f_1_40==2, rcost_1_40==4, 
obstacle(rx_1_40 + 0, ry_1_40 + 0)==False, 
obstacle(rx_1_40 + -1, ry_1_40 + 1)==False, 
obstacle(rx_1_40 + -2, ry_1_40 + 2)==False, 
)))
s.add(Or(rprim_1_40!=16,
And(rx_f_1_40==-2, ry_f_1_40==-2, rcost_1_40==4, 
obstacle(rx_1_40 + 0, ry_1_40 + 0)==False, 
obstacle(rx_1_40 + -1, ry_1_40 + -1)==False, 
obstacle(rx_1_40 + -2, ry_1_40 + -2)==False, 
)))
s.add(Or(rprim_1_40!=17,
And(rx_f_1_40==2, ry_f_1_40==-2, rcost_1_40==4, 
obstacle(rx_1_40 + 0, ry_1_40 + 0)==False, 
obstacle(rx_1_40 + 1, ry_1_40 + -1)==False, 
obstacle(rx_1_40 + 2, ry_1_40 + -2)==False, 
)))
s.add(Or(rprim_1_40!=18,
And(rx_f_1_40==3, ry_f_1_40==0, rcost_1_40==4, 
obstacle(rx_1_40 + 0, ry_1_40 + 0)==False, 
obstacle(rx_1_40 + 1, ry_1_40 + 0)==False, 
obstacle(rx_1_40 + 2, ry_1_40 + 0)==False, 
obstacle(rx_1_40 + 3, ry_1_40 + 0)==False, 
)))
s.add(Or(rprim_1_40!=19,
And(rx_f_1_40==0, ry_f_1_40==3, rcost_1_40==4, 
obstacle(rx_1_40 + 0, ry_1_40 + 0)==False, 
obstacle(rx_1_40 + 0, ry_1_40 + 1)==False, 
obstacle(rx_1_40 + 0, ry_1_40 + 2)==False, 
obstacle(rx_1_40 + 0, ry_1_40 + 3)==False, 
)))
s.add(Or(rprim_1_40!=20,
And(rx_f_1_40==-3, ry_f_1_40==0, rcost_1_40==4, 
obstacle(rx_1_40 + 0, ry_1_40 + 0)==False, 
obstacle(rx_1_40 + -1, ry_1_40 + 0)==False, 
obstacle(rx_1_40 + -2, ry_1_40 + 0)==False, 
obstacle(rx_1_40 + -3, ry_1_40 + 0)==False, 
)))
s.add(Or(rprim_1_40!=21,
And(rx_f_1_40==0, ry_f_1_40==-3, rcost_1_40==4, 
obstacle(rx_1_40 + 0, ry_1_40 + 0)==False, 
obstacle(rx_1_40 + 0, ry_1_40 + -1)==False, 
obstacle(rx_1_40 + 0, ry_1_40 + -2)==False, 
obstacle(rx_1_40 + 0, ry_1_40 + -3)==False, 
)))
s.add(Or(rprim_1_41!=1,
And(rx_f_1_41==0, ry_f_1_41==0, rcost_1_41==0, 
obstacle(rx_1_41 + 0, ry_1_41 + 0)==False, 
)))
s.add(Or(rprim_1_41!=2,
And(rx_f_1_41==1, ry_f_1_41==0, rcost_1_41==2, 
obstacle(rx_1_41 + 0, ry_1_41 + 0)==False, 
obstacle(rx_1_41 + 1, ry_1_41 + 0)==False, 
)))
s.add(Or(rprim_1_41!=3,
And(rx_f_1_41==0, ry_f_1_41==-1, rcost_1_41==2, 
obstacle(rx_1_41 + 0, ry_1_41 + 0)==False, 
obstacle(rx_1_41 + 0, ry_1_41 + -1)==False, 
)))
s.add(Or(rprim_1_41!=4,
And(rx_f_1_41==-1, ry_f_1_41==0, rcost_1_41==2, 
obstacle(rx_1_41 + 0, ry_1_41 + 0)==False, 
obstacle(rx_1_41 + -1, ry_1_41 + 0)==False, 
)))
s.add(Or(rprim_1_41!=5,
And(rx_f_1_41==0, ry_f_1_41==1, rcost_1_41==2, 
obstacle(rx_1_41 + 0, ry_1_41 + 0)==False, 
obstacle(rx_1_41 + 0, ry_1_41 + 1)==False, 
)))
s.add(Or(rprim_1_41!=6,
And(rx_f_1_41==1, ry_f_1_41==1, rcost_1_41==3, 
obstacle(rx_1_41 + 0, ry_1_41 + 0)==False, 
obstacle(rx_1_41 + 1, ry_1_41 + 1)==False, 
)))
s.add(Or(rprim_1_41!=7,
And(rx_f_1_41==-1, ry_f_1_41==1, rcost_1_41==3, 
obstacle(rx_1_41 + 0, ry_1_41 + 0)==False, 
obstacle(rx_1_41 + -1, ry_1_41 + 1)==False, 
)))
s.add(Or(rprim_1_41!=8,
And(rx_f_1_41==-1, ry_f_1_41==-1, rcost_1_41==3, 
obstacle(rx_1_41 + 0, ry_1_41 + 0)==False, 
obstacle(rx_1_41 + -1, ry_1_41 + -1)==False, 
)))
s.add(Or(rprim_1_41!=9,
And(rx_f_1_41==1, ry_f_1_41==-1, rcost_1_41==3, 
obstacle(rx_1_41 + 0, ry_1_41 + 0)==False, 
obstacle(rx_1_41 + 1, ry_1_41 + -1)==False, 
)))
s.add(Or(rprim_1_41!=10,
And(rx_f_1_41==2, ry_f_1_41==0, rcost_1_41==3, 
obstacle(rx_1_41 + 0, ry_1_41 + 0)==False, 
obstacle(rx_1_41 + 1, ry_1_41 + 0)==False, 
obstacle(rx_1_41 + 2, ry_1_41 + 0)==False, 
)))
s.add(Or(rprim_1_41!=11,
And(rx_f_1_41==0, ry_f_1_41==2, rcost_1_41==3, 
obstacle(rx_1_41 + 0, ry_1_41 + 0)==False, 
obstacle(rx_1_41 + 0, ry_1_41 + 1)==False, 
obstacle(rx_1_41 + 0, ry_1_41 + 2)==False, 
)))
s.add(Or(rprim_1_41!=12,
And(rx_f_1_41==-2, ry_f_1_41==0, rcost_1_41==3, 
obstacle(rx_1_41 + 0, ry_1_41 + 0)==False, 
obstacle(rx_1_41 + -1, ry_1_41 + 0)==False, 
obstacle(rx_1_41 + -2, ry_1_41 + 0)==False, 
)))
s.add(Or(rprim_1_41!=13,
And(rx_f_1_41==0, ry_f_1_41==-2, rcost_1_41==3, 
obstacle(rx_1_41 + 0, ry_1_41 + 0)==False, 
obstacle(rx_1_41 + 0, ry_1_41 + -1)==False, 
obstacle(rx_1_41 + 0, ry_1_41 + -2)==False, 
)))
s.add(Or(rprim_1_41!=14,
And(rx_f_1_41==2, ry_f_1_41==2, rcost_1_41==4, 
obstacle(rx_1_41 + 0, ry_1_41 + 0)==False, 
obstacle(rx_1_41 + 1, ry_1_41 + 1)==False, 
obstacle(rx_1_41 + 2, ry_1_41 + 2)==False, 
)))
s.add(Or(rprim_1_41!=15,
And(rx_f_1_41==-2, ry_f_1_41==2, rcost_1_41==4, 
obstacle(rx_1_41 + 0, ry_1_41 + 0)==False, 
obstacle(rx_1_41 + -1, ry_1_41 + 1)==False, 
obstacle(rx_1_41 + -2, ry_1_41 + 2)==False, 
)))
s.add(Or(rprim_1_41!=16,
And(rx_f_1_41==-2, ry_f_1_41==-2, rcost_1_41==4, 
obstacle(rx_1_41 + 0, ry_1_41 + 0)==False, 
obstacle(rx_1_41 + -1, ry_1_41 + -1)==False, 
obstacle(rx_1_41 + -2, ry_1_41 + -2)==False, 
)))
s.add(Or(rprim_1_41!=17,
And(rx_f_1_41==2, ry_f_1_41==-2, rcost_1_41==4, 
obstacle(rx_1_41 + 0, ry_1_41 + 0)==False, 
obstacle(rx_1_41 + 1, ry_1_41 + -1)==False, 
obstacle(rx_1_41 + 2, ry_1_41 + -2)==False, 
)))
s.add(Or(rprim_1_41!=18,
And(rx_f_1_41==3, ry_f_1_41==0, rcost_1_41==4, 
obstacle(rx_1_41 + 0, ry_1_41 + 0)==False, 
obstacle(rx_1_41 + 1, ry_1_41 + 0)==False, 
obstacle(rx_1_41 + 2, ry_1_41 + 0)==False, 
obstacle(rx_1_41 + 3, ry_1_41 + 0)==False, 
)))
s.add(Or(rprim_1_41!=19,
And(rx_f_1_41==0, ry_f_1_41==3, rcost_1_41==4, 
obstacle(rx_1_41 + 0, ry_1_41 + 0)==False, 
obstacle(rx_1_41 + 0, ry_1_41 + 1)==False, 
obstacle(rx_1_41 + 0, ry_1_41 + 2)==False, 
obstacle(rx_1_41 + 0, ry_1_41 + 3)==False, 
)))
s.add(Or(rprim_1_41!=20,
And(rx_f_1_41==-3, ry_f_1_41==0, rcost_1_41==4, 
obstacle(rx_1_41 + 0, ry_1_41 + 0)==False, 
obstacle(rx_1_41 + -1, ry_1_41 + 0)==False, 
obstacle(rx_1_41 + -2, ry_1_41 + 0)==False, 
obstacle(rx_1_41 + -3, ry_1_41 + 0)==False, 
)))
s.add(Or(rprim_1_41!=21,
And(rx_f_1_41==0, ry_f_1_41==-3, rcost_1_41==4, 
obstacle(rx_1_41 + 0, ry_1_41 + 0)==False, 
obstacle(rx_1_41 + 0, ry_1_41 + -1)==False, 
obstacle(rx_1_41 + 0, ry_1_41 + -2)==False, 
obstacle(rx_1_41 + 0, ry_1_41 + -3)==False, 
)))
s.add(Or(rprim_1_42!=1,
And(rx_f_1_42==0, ry_f_1_42==0, rcost_1_42==0, 
obstacle(rx_1_42 + 0, ry_1_42 + 0)==False, 
)))
s.add(Or(rprim_1_42!=2,
And(rx_f_1_42==1, ry_f_1_42==0, rcost_1_42==2, 
obstacle(rx_1_42 + 0, ry_1_42 + 0)==False, 
obstacle(rx_1_42 + 1, ry_1_42 + 0)==False, 
)))
s.add(Or(rprim_1_42!=3,
And(rx_f_1_42==0, ry_f_1_42==-1, rcost_1_42==2, 
obstacle(rx_1_42 + 0, ry_1_42 + 0)==False, 
obstacle(rx_1_42 + 0, ry_1_42 + -1)==False, 
)))
s.add(Or(rprim_1_42!=4,
And(rx_f_1_42==-1, ry_f_1_42==0, rcost_1_42==2, 
obstacle(rx_1_42 + 0, ry_1_42 + 0)==False, 
obstacle(rx_1_42 + -1, ry_1_42 + 0)==False, 
)))
s.add(Or(rprim_1_42!=5,
And(rx_f_1_42==0, ry_f_1_42==1, rcost_1_42==2, 
obstacle(rx_1_42 + 0, ry_1_42 + 0)==False, 
obstacle(rx_1_42 + 0, ry_1_42 + 1)==False, 
)))
s.add(Or(rprim_1_42!=6,
And(rx_f_1_42==1, ry_f_1_42==1, rcost_1_42==3, 
obstacle(rx_1_42 + 0, ry_1_42 + 0)==False, 
obstacle(rx_1_42 + 1, ry_1_42 + 1)==False, 
)))
s.add(Or(rprim_1_42!=7,
And(rx_f_1_42==-1, ry_f_1_42==1, rcost_1_42==3, 
obstacle(rx_1_42 + 0, ry_1_42 + 0)==False, 
obstacle(rx_1_42 + -1, ry_1_42 + 1)==False, 
)))
s.add(Or(rprim_1_42!=8,
And(rx_f_1_42==-1, ry_f_1_42==-1, rcost_1_42==3, 
obstacle(rx_1_42 + 0, ry_1_42 + 0)==False, 
obstacle(rx_1_42 + -1, ry_1_42 + -1)==False, 
)))
s.add(Or(rprim_1_42!=9,
And(rx_f_1_42==1, ry_f_1_42==-1, rcost_1_42==3, 
obstacle(rx_1_42 + 0, ry_1_42 + 0)==False, 
obstacle(rx_1_42 + 1, ry_1_42 + -1)==False, 
)))
s.add(Or(rprim_1_42!=10,
And(rx_f_1_42==2, ry_f_1_42==0, rcost_1_42==3, 
obstacle(rx_1_42 + 0, ry_1_42 + 0)==False, 
obstacle(rx_1_42 + 1, ry_1_42 + 0)==False, 
obstacle(rx_1_42 + 2, ry_1_42 + 0)==False, 
)))
s.add(Or(rprim_1_42!=11,
And(rx_f_1_42==0, ry_f_1_42==2, rcost_1_42==3, 
obstacle(rx_1_42 + 0, ry_1_42 + 0)==False, 
obstacle(rx_1_42 + 0, ry_1_42 + 1)==False, 
obstacle(rx_1_42 + 0, ry_1_42 + 2)==False, 
)))
s.add(Or(rprim_1_42!=12,
And(rx_f_1_42==-2, ry_f_1_42==0, rcost_1_42==3, 
obstacle(rx_1_42 + 0, ry_1_42 + 0)==False, 
obstacle(rx_1_42 + -1, ry_1_42 + 0)==False, 
obstacle(rx_1_42 + -2, ry_1_42 + 0)==False, 
)))
s.add(Or(rprim_1_42!=13,
And(rx_f_1_42==0, ry_f_1_42==-2, rcost_1_42==3, 
obstacle(rx_1_42 + 0, ry_1_42 + 0)==False, 
obstacle(rx_1_42 + 0, ry_1_42 + -1)==False, 
obstacle(rx_1_42 + 0, ry_1_42 + -2)==False, 
)))
s.add(Or(rprim_1_42!=14,
And(rx_f_1_42==2, ry_f_1_42==2, rcost_1_42==4, 
obstacle(rx_1_42 + 0, ry_1_42 + 0)==False, 
obstacle(rx_1_42 + 1, ry_1_42 + 1)==False, 
obstacle(rx_1_42 + 2, ry_1_42 + 2)==False, 
)))
s.add(Or(rprim_1_42!=15,
And(rx_f_1_42==-2, ry_f_1_42==2, rcost_1_42==4, 
obstacle(rx_1_42 + 0, ry_1_42 + 0)==False, 
obstacle(rx_1_42 + -1, ry_1_42 + 1)==False, 
obstacle(rx_1_42 + -2, ry_1_42 + 2)==False, 
)))
s.add(Or(rprim_1_42!=16,
And(rx_f_1_42==-2, ry_f_1_42==-2, rcost_1_42==4, 
obstacle(rx_1_42 + 0, ry_1_42 + 0)==False, 
obstacle(rx_1_42 + -1, ry_1_42 + -1)==False, 
obstacle(rx_1_42 + -2, ry_1_42 + -2)==False, 
)))
s.add(Or(rprim_1_42!=17,
And(rx_f_1_42==2, ry_f_1_42==-2, rcost_1_42==4, 
obstacle(rx_1_42 + 0, ry_1_42 + 0)==False, 
obstacle(rx_1_42 + 1, ry_1_42 + -1)==False, 
obstacle(rx_1_42 + 2, ry_1_42 + -2)==False, 
)))
s.add(Or(rprim_1_42!=18,
And(rx_f_1_42==3, ry_f_1_42==0, rcost_1_42==4, 
obstacle(rx_1_42 + 0, ry_1_42 + 0)==False, 
obstacle(rx_1_42 + 1, ry_1_42 + 0)==False, 
obstacle(rx_1_42 + 2, ry_1_42 + 0)==False, 
obstacle(rx_1_42 + 3, ry_1_42 + 0)==False, 
)))
s.add(Or(rprim_1_42!=19,
And(rx_f_1_42==0, ry_f_1_42==3, rcost_1_42==4, 
obstacle(rx_1_42 + 0, ry_1_42 + 0)==False, 
obstacle(rx_1_42 + 0, ry_1_42 + 1)==False, 
obstacle(rx_1_42 + 0, ry_1_42 + 2)==False, 
obstacle(rx_1_42 + 0, ry_1_42 + 3)==False, 
)))
s.add(Or(rprim_1_42!=20,
And(rx_f_1_42==-3, ry_f_1_42==0, rcost_1_42==4, 
obstacle(rx_1_42 + 0, ry_1_42 + 0)==False, 
obstacle(rx_1_42 + -1, ry_1_42 + 0)==False, 
obstacle(rx_1_42 + -2, ry_1_42 + 0)==False, 
obstacle(rx_1_42 + -3, ry_1_42 + 0)==False, 
)))
s.add(Or(rprim_1_42!=21,
And(rx_f_1_42==0, ry_f_1_42==-3, rcost_1_42==4, 
obstacle(rx_1_42 + 0, ry_1_42 + 0)==False, 
obstacle(rx_1_42 + 0, ry_1_42 + -1)==False, 
obstacle(rx_1_42 + 0, ry_1_42 + -2)==False, 
obstacle(rx_1_42 + 0, ry_1_42 + -3)==False, 
)))
s.add(Or(rprim_1_43!=1,
And(rx_f_1_43==0, ry_f_1_43==0, rcost_1_43==0, 
obstacle(rx_1_43 + 0, ry_1_43 + 0)==False, 
)))
s.add(Or(rprim_1_43!=2,
And(rx_f_1_43==1, ry_f_1_43==0, rcost_1_43==2, 
obstacle(rx_1_43 + 0, ry_1_43 + 0)==False, 
obstacle(rx_1_43 + 1, ry_1_43 + 0)==False, 
)))
s.add(Or(rprim_1_43!=3,
And(rx_f_1_43==0, ry_f_1_43==-1, rcost_1_43==2, 
obstacle(rx_1_43 + 0, ry_1_43 + 0)==False, 
obstacle(rx_1_43 + 0, ry_1_43 + -1)==False, 
)))
s.add(Or(rprim_1_43!=4,
And(rx_f_1_43==-1, ry_f_1_43==0, rcost_1_43==2, 
obstacle(rx_1_43 + 0, ry_1_43 + 0)==False, 
obstacle(rx_1_43 + -1, ry_1_43 + 0)==False, 
)))
s.add(Or(rprim_1_43!=5,
And(rx_f_1_43==0, ry_f_1_43==1, rcost_1_43==2, 
obstacle(rx_1_43 + 0, ry_1_43 + 0)==False, 
obstacle(rx_1_43 + 0, ry_1_43 + 1)==False, 
)))
s.add(Or(rprim_1_43!=6,
And(rx_f_1_43==1, ry_f_1_43==1, rcost_1_43==3, 
obstacle(rx_1_43 + 0, ry_1_43 + 0)==False, 
obstacle(rx_1_43 + 1, ry_1_43 + 1)==False, 
)))
s.add(Or(rprim_1_43!=7,
And(rx_f_1_43==-1, ry_f_1_43==1, rcost_1_43==3, 
obstacle(rx_1_43 + 0, ry_1_43 + 0)==False, 
obstacle(rx_1_43 + -1, ry_1_43 + 1)==False, 
)))
s.add(Or(rprim_1_43!=8,
And(rx_f_1_43==-1, ry_f_1_43==-1, rcost_1_43==3, 
obstacle(rx_1_43 + 0, ry_1_43 + 0)==False, 
obstacle(rx_1_43 + -1, ry_1_43 + -1)==False, 
)))
s.add(Or(rprim_1_43!=9,
And(rx_f_1_43==1, ry_f_1_43==-1, rcost_1_43==3, 
obstacle(rx_1_43 + 0, ry_1_43 + 0)==False, 
obstacle(rx_1_43 + 1, ry_1_43 + -1)==False, 
)))
s.add(Or(rprim_1_43!=10,
And(rx_f_1_43==2, ry_f_1_43==0, rcost_1_43==3, 
obstacle(rx_1_43 + 0, ry_1_43 + 0)==False, 
obstacle(rx_1_43 + 1, ry_1_43 + 0)==False, 
obstacle(rx_1_43 + 2, ry_1_43 + 0)==False, 
)))
s.add(Or(rprim_1_43!=11,
And(rx_f_1_43==0, ry_f_1_43==2, rcost_1_43==3, 
obstacle(rx_1_43 + 0, ry_1_43 + 0)==False, 
obstacle(rx_1_43 + 0, ry_1_43 + 1)==False, 
obstacle(rx_1_43 + 0, ry_1_43 + 2)==False, 
)))
s.add(Or(rprim_1_43!=12,
And(rx_f_1_43==-2, ry_f_1_43==0, rcost_1_43==3, 
obstacle(rx_1_43 + 0, ry_1_43 + 0)==False, 
obstacle(rx_1_43 + -1, ry_1_43 + 0)==False, 
obstacle(rx_1_43 + -2, ry_1_43 + 0)==False, 
)))
s.add(Or(rprim_1_43!=13,
And(rx_f_1_43==0, ry_f_1_43==-2, rcost_1_43==3, 
obstacle(rx_1_43 + 0, ry_1_43 + 0)==False, 
obstacle(rx_1_43 + 0, ry_1_43 + -1)==False, 
obstacle(rx_1_43 + 0, ry_1_43 + -2)==False, 
)))
s.add(Or(rprim_1_43!=14,
And(rx_f_1_43==2, ry_f_1_43==2, rcost_1_43==4, 
obstacle(rx_1_43 + 0, ry_1_43 + 0)==False, 
obstacle(rx_1_43 + 1, ry_1_43 + 1)==False, 
obstacle(rx_1_43 + 2, ry_1_43 + 2)==False, 
)))
s.add(Or(rprim_1_43!=15,
And(rx_f_1_43==-2, ry_f_1_43==2, rcost_1_43==4, 
obstacle(rx_1_43 + 0, ry_1_43 + 0)==False, 
obstacle(rx_1_43 + -1, ry_1_43 + 1)==False, 
obstacle(rx_1_43 + -2, ry_1_43 + 2)==False, 
)))
s.add(Or(rprim_1_43!=16,
And(rx_f_1_43==-2, ry_f_1_43==-2, rcost_1_43==4, 
obstacle(rx_1_43 + 0, ry_1_43 + 0)==False, 
obstacle(rx_1_43 + -1, ry_1_43 + -1)==False, 
obstacle(rx_1_43 + -2, ry_1_43 + -2)==False, 
)))
s.add(Or(rprim_1_43!=17,
And(rx_f_1_43==2, ry_f_1_43==-2, rcost_1_43==4, 
obstacle(rx_1_43 + 0, ry_1_43 + 0)==False, 
obstacle(rx_1_43 + 1, ry_1_43 + -1)==False, 
obstacle(rx_1_43 + 2, ry_1_43 + -2)==False, 
)))
s.add(Or(rprim_1_43!=18,
And(rx_f_1_43==3, ry_f_1_43==0, rcost_1_43==4, 
obstacle(rx_1_43 + 0, ry_1_43 + 0)==False, 
obstacle(rx_1_43 + 1, ry_1_43 + 0)==False, 
obstacle(rx_1_43 + 2, ry_1_43 + 0)==False, 
obstacle(rx_1_43 + 3, ry_1_43 + 0)==False, 
)))
s.add(Or(rprim_1_43!=19,
And(rx_f_1_43==0, ry_f_1_43==3, rcost_1_43==4, 
obstacle(rx_1_43 + 0, ry_1_43 + 0)==False, 
obstacle(rx_1_43 + 0, ry_1_43 + 1)==False, 
obstacle(rx_1_43 + 0, ry_1_43 + 2)==False, 
obstacle(rx_1_43 + 0, ry_1_43 + 3)==False, 
)))
s.add(Or(rprim_1_43!=20,
And(rx_f_1_43==-3, ry_f_1_43==0, rcost_1_43==4, 
obstacle(rx_1_43 + 0, ry_1_43 + 0)==False, 
obstacle(rx_1_43 + -1, ry_1_43 + 0)==False, 
obstacle(rx_1_43 + -2, ry_1_43 + 0)==False, 
obstacle(rx_1_43 + -3, ry_1_43 + 0)==False, 
)))
s.add(Or(rprim_1_43!=21,
And(rx_f_1_43==0, ry_f_1_43==-3, rcost_1_43==4, 
obstacle(rx_1_43 + 0, ry_1_43 + 0)==False, 
obstacle(rx_1_43 + 0, ry_1_43 + -1)==False, 
obstacle(rx_1_43 + 0, ry_1_43 + -2)==False, 
obstacle(rx_1_43 + 0, ry_1_43 + -3)==False, 
)))
s.add(Or(rprim_1_44!=1,
And(rx_f_1_44==0, ry_f_1_44==0, rcost_1_44==0, 
obstacle(rx_1_44 + 0, ry_1_44 + 0)==False, 
)))
s.add(Or(rprim_1_44!=2,
And(rx_f_1_44==1, ry_f_1_44==0, rcost_1_44==2, 
obstacle(rx_1_44 + 0, ry_1_44 + 0)==False, 
obstacle(rx_1_44 + 1, ry_1_44 + 0)==False, 
)))
s.add(Or(rprim_1_44!=3,
And(rx_f_1_44==0, ry_f_1_44==-1, rcost_1_44==2, 
obstacle(rx_1_44 + 0, ry_1_44 + 0)==False, 
obstacle(rx_1_44 + 0, ry_1_44 + -1)==False, 
)))
s.add(Or(rprim_1_44!=4,
And(rx_f_1_44==-1, ry_f_1_44==0, rcost_1_44==2, 
obstacle(rx_1_44 + 0, ry_1_44 + 0)==False, 
obstacle(rx_1_44 + -1, ry_1_44 + 0)==False, 
)))
s.add(Or(rprim_1_44!=5,
And(rx_f_1_44==0, ry_f_1_44==1, rcost_1_44==2, 
obstacle(rx_1_44 + 0, ry_1_44 + 0)==False, 
obstacle(rx_1_44 + 0, ry_1_44 + 1)==False, 
)))
s.add(Or(rprim_1_44!=6,
And(rx_f_1_44==1, ry_f_1_44==1, rcost_1_44==3, 
obstacle(rx_1_44 + 0, ry_1_44 + 0)==False, 
obstacle(rx_1_44 + 1, ry_1_44 + 1)==False, 
)))
s.add(Or(rprim_1_44!=7,
And(rx_f_1_44==-1, ry_f_1_44==1, rcost_1_44==3, 
obstacle(rx_1_44 + 0, ry_1_44 + 0)==False, 
obstacle(rx_1_44 + -1, ry_1_44 + 1)==False, 
)))
s.add(Or(rprim_1_44!=8,
And(rx_f_1_44==-1, ry_f_1_44==-1, rcost_1_44==3, 
obstacle(rx_1_44 + 0, ry_1_44 + 0)==False, 
obstacle(rx_1_44 + -1, ry_1_44 + -1)==False, 
)))
s.add(Or(rprim_1_44!=9,
And(rx_f_1_44==1, ry_f_1_44==-1, rcost_1_44==3, 
obstacle(rx_1_44 + 0, ry_1_44 + 0)==False, 
obstacle(rx_1_44 + 1, ry_1_44 + -1)==False, 
)))
s.add(Or(rprim_1_44!=10,
And(rx_f_1_44==2, ry_f_1_44==0, rcost_1_44==3, 
obstacle(rx_1_44 + 0, ry_1_44 + 0)==False, 
obstacle(rx_1_44 + 1, ry_1_44 + 0)==False, 
obstacle(rx_1_44 + 2, ry_1_44 + 0)==False, 
)))
s.add(Or(rprim_1_44!=11,
And(rx_f_1_44==0, ry_f_1_44==2, rcost_1_44==3, 
obstacle(rx_1_44 + 0, ry_1_44 + 0)==False, 
obstacle(rx_1_44 + 0, ry_1_44 + 1)==False, 
obstacle(rx_1_44 + 0, ry_1_44 + 2)==False, 
)))
s.add(Or(rprim_1_44!=12,
And(rx_f_1_44==-2, ry_f_1_44==0, rcost_1_44==3, 
obstacle(rx_1_44 + 0, ry_1_44 + 0)==False, 
obstacle(rx_1_44 + -1, ry_1_44 + 0)==False, 
obstacle(rx_1_44 + -2, ry_1_44 + 0)==False, 
)))
s.add(Or(rprim_1_44!=13,
And(rx_f_1_44==0, ry_f_1_44==-2, rcost_1_44==3, 
obstacle(rx_1_44 + 0, ry_1_44 + 0)==False, 
obstacle(rx_1_44 + 0, ry_1_44 + -1)==False, 
obstacle(rx_1_44 + 0, ry_1_44 + -2)==False, 
)))
s.add(Or(rprim_1_44!=14,
And(rx_f_1_44==2, ry_f_1_44==2, rcost_1_44==4, 
obstacle(rx_1_44 + 0, ry_1_44 + 0)==False, 
obstacle(rx_1_44 + 1, ry_1_44 + 1)==False, 
obstacle(rx_1_44 + 2, ry_1_44 + 2)==False, 
)))
s.add(Or(rprim_1_44!=15,
And(rx_f_1_44==-2, ry_f_1_44==2, rcost_1_44==4, 
obstacle(rx_1_44 + 0, ry_1_44 + 0)==False, 
obstacle(rx_1_44 + -1, ry_1_44 + 1)==False, 
obstacle(rx_1_44 + -2, ry_1_44 + 2)==False, 
)))
s.add(Or(rprim_1_44!=16,
And(rx_f_1_44==-2, ry_f_1_44==-2, rcost_1_44==4, 
obstacle(rx_1_44 + 0, ry_1_44 + 0)==False, 
obstacle(rx_1_44 + -1, ry_1_44 + -1)==False, 
obstacle(rx_1_44 + -2, ry_1_44 + -2)==False, 
)))
s.add(Or(rprim_1_44!=17,
And(rx_f_1_44==2, ry_f_1_44==-2, rcost_1_44==4, 
obstacle(rx_1_44 + 0, ry_1_44 + 0)==False, 
obstacle(rx_1_44 + 1, ry_1_44 + -1)==False, 
obstacle(rx_1_44 + 2, ry_1_44 + -2)==False, 
)))
s.add(Or(rprim_1_44!=18,
And(rx_f_1_44==3, ry_f_1_44==0, rcost_1_44==4, 
obstacle(rx_1_44 + 0, ry_1_44 + 0)==False, 
obstacle(rx_1_44 + 1, ry_1_44 + 0)==False, 
obstacle(rx_1_44 + 2, ry_1_44 + 0)==False, 
obstacle(rx_1_44 + 3, ry_1_44 + 0)==False, 
)))
s.add(Or(rprim_1_44!=19,
And(rx_f_1_44==0, ry_f_1_44==3, rcost_1_44==4, 
obstacle(rx_1_44 + 0, ry_1_44 + 0)==False, 
obstacle(rx_1_44 + 0, ry_1_44 + 1)==False, 
obstacle(rx_1_44 + 0, ry_1_44 + 2)==False, 
obstacle(rx_1_44 + 0, ry_1_44 + 3)==False, 
)))
s.add(Or(rprim_1_44!=20,
And(rx_f_1_44==-3, ry_f_1_44==0, rcost_1_44==4, 
obstacle(rx_1_44 + 0, ry_1_44 + 0)==False, 
obstacle(rx_1_44 + -1, ry_1_44 + 0)==False, 
obstacle(rx_1_44 + -2, ry_1_44 + 0)==False, 
obstacle(rx_1_44 + -3, ry_1_44 + 0)==False, 
)))
s.add(Or(rprim_1_44!=21,
And(rx_f_1_44==0, ry_f_1_44==-3, rcost_1_44==4, 
obstacle(rx_1_44 + 0, ry_1_44 + 0)==False, 
obstacle(rx_1_44 + 0, ry_1_44 + -1)==False, 
obstacle(rx_1_44 + 0, ry_1_44 + -2)==False, 
obstacle(rx_1_44 + 0, ry_1_44 + -3)==False, 
)))
s.add(Or(rprim_1_45!=1,
And(rx_f_1_45==0, ry_f_1_45==0, rcost_1_45==0, 
obstacle(rx_1_45 + 0, ry_1_45 + 0)==False, 
)))
s.add(Or(rprim_1_45!=2,
And(rx_f_1_45==1, ry_f_1_45==0, rcost_1_45==2, 
obstacle(rx_1_45 + 0, ry_1_45 + 0)==False, 
obstacle(rx_1_45 + 1, ry_1_45 + 0)==False, 
)))
s.add(Or(rprim_1_45!=3,
And(rx_f_1_45==0, ry_f_1_45==-1, rcost_1_45==2, 
obstacle(rx_1_45 + 0, ry_1_45 + 0)==False, 
obstacle(rx_1_45 + 0, ry_1_45 + -1)==False, 
)))
s.add(Or(rprim_1_45!=4,
And(rx_f_1_45==-1, ry_f_1_45==0, rcost_1_45==2, 
obstacle(rx_1_45 + 0, ry_1_45 + 0)==False, 
obstacle(rx_1_45 + -1, ry_1_45 + 0)==False, 
)))
s.add(Or(rprim_1_45!=5,
And(rx_f_1_45==0, ry_f_1_45==1, rcost_1_45==2, 
obstacle(rx_1_45 + 0, ry_1_45 + 0)==False, 
obstacle(rx_1_45 + 0, ry_1_45 + 1)==False, 
)))
s.add(Or(rprim_1_45!=6,
And(rx_f_1_45==1, ry_f_1_45==1, rcost_1_45==3, 
obstacle(rx_1_45 + 0, ry_1_45 + 0)==False, 
obstacle(rx_1_45 + 1, ry_1_45 + 1)==False, 
)))
s.add(Or(rprim_1_45!=7,
And(rx_f_1_45==-1, ry_f_1_45==1, rcost_1_45==3, 
obstacle(rx_1_45 + 0, ry_1_45 + 0)==False, 
obstacle(rx_1_45 + -1, ry_1_45 + 1)==False, 
)))
s.add(Or(rprim_1_45!=8,
And(rx_f_1_45==-1, ry_f_1_45==-1, rcost_1_45==3, 
obstacle(rx_1_45 + 0, ry_1_45 + 0)==False, 
obstacle(rx_1_45 + -1, ry_1_45 + -1)==False, 
)))
s.add(Or(rprim_1_45!=9,
And(rx_f_1_45==1, ry_f_1_45==-1, rcost_1_45==3, 
obstacle(rx_1_45 + 0, ry_1_45 + 0)==False, 
obstacle(rx_1_45 + 1, ry_1_45 + -1)==False, 
)))
s.add(Or(rprim_1_45!=10,
And(rx_f_1_45==2, ry_f_1_45==0, rcost_1_45==3, 
obstacle(rx_1_45 + 0, ry_1_45 + 0)==False, 
obstacle(rx_1_45 + 1, ry_1_45 + 0)==False, 
obstacle(rx_1_45 + 2, ry_1_45 + 0)==False, 
)))
s.add(Or(rprim_1_45!=11,
And(rx_f_1_45==0, ry_f_1_45==2, rcost_1_45==3, 
obstacle(rx_1_45 + 0, ry_1_45 + 0)==False, 
obstacle(rx_1_45 + 0, ry_1_45 + 1)==False, 
obstacle(rx_1_45 + 0, ry_1_45 + 2)==False, 
)))
s.add(Or(rprim_1_45!=12,
And(rx_f_1_45==-2, ry_f_1_45==0, rcost_1_45==3, 
obstacle(rx_1_45 + 0, ry_1_45 + 0)==False, 
obstacle(rx_1_45 + -1, ry_1_45 + 0)==False, 
obstacle(rx_1_45 + -2, ry_1_45 + 0)==False, 
)))
s.add(Or(rprim_1_45!=13,
And(rx_f_1_45==0, ry_f_1_45==-2, rcost_1_45==3, 
obstacle(rx_1_45 + 0, ry_1_45 + 0)==False, 
obstacle(rx_1_45 + 0, ry_1_45 + -1)==False, 
obstacle(rx_1_45 + 0, ry_1_45 + -2)==False, 
)))
s.add(Or(rprim_1_45!=14,
And(rx_f_1_45==2, ry_f_1_45==2, rcost_1_45==4, 
obstacle(rx_1_45 + 0, ry_1_45 + 0)==False, 
obstacle(rx_1_45 + 1, ry_1_45 + 1)==False, 
obstacle(rx_1_45 + 2, ry_1_45 + 2)==False, 
)))
s.add(Or(rprim_1_45!=15,
And(rx_f_1_45==-2, ry_f_1_45==2, rcost_1_45==4, 
obstacle(rx_1_45 + 0, ry_1_45 + 0)==False, 
obstacle(rx_1_45 + -1, ry_1_45 + 1)==False, 
obstacle(rx_1_45 + -2, ry_1_45 + 2)==False, 
)))
s.add(Or(rprim_1_45!=16,
And(rx_f_1_45==-2, ry_f_1_45==-2, rcost_1_45==4, 
obstacle(rx_1_45 + 0, ry_1_45 + 0)==False, 
obstacle(rx_1_45 + -1, ry_1_45 + -1)==False, 
obstacle(rx_1_45 + -2, ry_1_45 + -2)==False, 
)))
s.add(Or(rprim_1_45!=17,
And(rx_f_1_45==2, ry_f_1_45==-2, rcost_1_45==4, 
obstacle(rx_1_45 + 0, ry_1_45 + 0)==False, 
obstacle(rx_1_45 + 1, ry_1_45 + -1)==False, 
obstacle(rx_1_45 + 2, ry_1_45 + -2)==False, 
)))
s.add(Or(rprim_1_45!=18,
And(rx_f_1_45==3, ry_f_1_45==0, rcost_1_45==4, 
obstacle(rx_1_45 + 0, ry_1_45 + 0)==False, 
obstacle(rx_1_45 + 1, ry_1_45 + 0)==False, 
obstacle(rx_1_45 + 2, ry_1_45 + 0)==False, 
obstacle(rx_1_45 + 3, ry_1_45 + 0)==False, 
)))
s.add(Or(rprim_1_45!=19,
And(rx_f_1_45==0, ry_f_1_45==3, rcost_1_45==4, 
obstacle(rx_1_45 + 0, ry_1_45 + 0)==False, 
obstacle(rx_1_45 + 0, ry_1_45 + 1)==False, 
obstacle(rx_1_45 + 0, ry_1_45 + 2)==False, 
obstacle(rx_1_45 + 0, ry_1_45 + 3)==False, 
)))
s.add(Or(rprim_1_45!=20,
And(rx_f_1_45==-3, ry_f_1_45==0, rcost_1_45==4, 
obstacle(rx_1_45 + 0, ry_1_45 + 0)==False, 
obstacle(rx_1_45 + -1, ry_1_45 + 0)==False, 
obstacle(rx_1_45 + -2, ry_1_45 + 0)==False, 
obstacle(rx_1_45 + -3, ry_1_45 + 0)==False, 
)))
s.add(Or(rprim_1_45!=21,
And(rx_f_1_45==0, ry_f_1_45==-3, rcost_1_45==4, 
obstacle(rx_1_45 + 0, ry_1_45 + 0)==False, 
obstacle(rx_1_45 + 0, ry_1_45 + -1)==False, 
obstacle(rx_1_45 + 0, ry_1_45 + -2)==False, 
obstacle(rx_1_45 + 0, ry_1_45 + -3)==False, 
)))
s.add(Or(rprim_1_46!=1,
And(rx_f_1_46==0, ry_f_1_46==0, rcost_1_46==0, 
obstacle(rx_1_46 + 0, ry_1_46 + 0)==False, 
)))
s.add(Or(rprim_1_46!=2,
And(rx_f_1_46==1, ry_f_1_46==0, rcost_1_46==2, 
obstacle(rx_1_46 + 0, ry_1_46 + 0)==False, 
obstacle(rx_1_46 + 1, ry_1_46 + 0)==False, 
)))
s.add(Or(rprim_1_46!=3,
And(rx_f_1_46==0, ry_f_1_46==-1, rcost_1_46==2, 
obstacle(rx_1_46 + 0, ry_1_46 + 0)==False, 
obstacle(rx_1_46 + 0, ry_1_46 + -1)==False, 
)))
s.add(Or(rprim_1_46!=4,
And(rx_f_1_46==-1, ry_f_1_46==0, rcost_1_46==2, 
obstacle(rx_1_46 + 0, ry_1_46 + 0)==False, 
obstacle(rx_1_46 + -1, ry_1_46 + 0)==False, 
)))
s.add(Or(rprim_1_46!=5,
And(rx_f_1_46==0, ry_f_1_46==1, rcost_1_46==2, 
obstacle(rx_1_46 + 0, ry_1_46 + 0)==False, 
obstacle(rx_1_46 + 0, ry_1_46 + 1)==False, 
)))
s.add(Or(rprim_1_46!=6,
And(rx_f_1_46==1, ry_f_1_46==1, rcost_1_46==3, 
obstacle(rx_1_46 + 0, ry_1_46 + 0)==False, 
obstacle(rx_1_46 + 1, ry_1_46 + 1)==False, 
)))
s.add(Or(rprim_1_46!=7,
And(rx_f_1_46==-1, ry_f_1_46==1, rcost_1_46==3, 
obstacle(rx_1_46 + 0, ry_1_46 + 0)==False, 
obstacle(rx_1_46 + -1, ry_1_46 + 1)==False, 
)))
s.add(Or(rprim_1_46!=8,
And(rx_f_1_46==-1, ry_f_1_46==-1, rcost_1_46==3, 
obstacle(rx_1_46 + 0, ry_1_46 + 0)==False, 
obstacle(rx_1_46 + -1, ry_1_46 + -1)==False, 
)))
s.add(Or(rprim_1_46!=9,
And(rx_f_1_46==1, ry_f_1_46==-1, rcost_1_46==3, 
obstacle(rx_1_46 + 0, ry_1_46 + 0)==False, 
obstacle(rx_1_46 + 1, ry_1_46 + -1)==False, 
)))
s.add(Or(rprim_1_46!=10,
And(rx_f_1_46==2, ry_f_1_46==0, rcost_1_46==3, 
obstacle(rx_1_46 + 0, ry_1_46 + 0)==False, 
obstacle(rx_1_46 + 1, ry_1_46 + 0)==False, 
obstacle(rx_1_46 + 2, ry_1_46 + 0)==False, 
)))
s.add(Or(rprim_1_46!=11,
And(rx_f_1_46==0, ry_f_1_46==2, rcost_1_46==3, 
obstacle(rx_1_46 + 0, ry_1_46 + 0)==False, 
obstacle(rx_1_46 + 0, ry_1_46 + 1)==False, 
obstacle(rx_1_46 + 0, ry_1_46 + 2)==False, 
)))
s.add(Or(rprim_1_46!=12,
And(rx_f_1_46==-2, ry_f_1_46==0, rcost_1_46==3, 
obstacle(rx_1_46 + 0, ry_1_46 + 0)==False, 
obstacle(rx_1_46 + -1, ry_1_46 + 0)==False, 
obstacle(rx_1_46 + -2, ry_1_46 + 0)==False, 
)))
s.add(Or(rprim_1_46!=13,
And(rx_f_1_46==0, ry_f_1_46==-2, rcost_1_46==3, 
obstacle(rx_1_46 + 0, ry_1_46 + 0)==False, 
obstacle(rx_1_46 + 0, ry_1_46 + -1)==False, 
obstacle(rx_1_46 + 0, ry_1_46 + -2)==False, 
)))
s.add(Or(rprim_1_46!=14,
And(rx_f_1_46==2, ry_f_1_46==2, rcost_1_46==4, 
obstacle(rx_1_46 + 0, ry_1_46 + 0)==False, 
obstacle(rx_1_46 + 1, ry_1_46 + 1)==False, 
obstacle(rx_1_46 + 2, ry_1_46 + 2)==False, 
)))
s.add(Or(rprim_1_46!=15,
And(rx_f_1_46==-2, ry_f_1_46==2, rcost_1_46==4, 
obstacle(rx_1_46 + 0, ry_1_46 + 0)==False, 
obstacle(rx_1_46 + -1, ry_1_46 + 1)==False, 
obstacle(rx_1_46 + -2, ry_1_46 + 2)==False, 
)))
s.add(Or(rprim_1_46!=16,
And(rx_f_1_46==-2, ry_f_1_46==-2, rcost_1_46==4, 
obstacle(rx_1_46 + 0, ry_1_46 + 0)==False, 
obstacle(rx_1_46 + -1, ry_1_46 + -1)==False, 
obstacle(rx_1_46 + -2, ry_1_46 + -2)==False, 
)))
s.add(Or(rprim_1_46!=17,
And(rx_f_1_46==2, ry_f_1_46==-2, rcost_1_46==4, 
obstacle(rx_1_46 + 0, ry_1_46 + 0)==False, 
obstacle(rx_1_46 + 1, ry_1_46 + -1)==False, 
obstacle(rx_1_46 + 2, ry_1_46 + -2)==False, 
)))
s.add(Or(rprim_1_46!=18,
And(rx_f_1_46==3, ry_f_1_46==0, rcost_1_46==4, 
obstacle(rx_1_46 + 0, ry_1_46 + 0)==False, 
obstacle(rx_1_46 + 1, ry_1_46 + 0)==False, 
obstacle(rx_1_46 + 2, ry_1_46 + 0)==False, 
obstacle(rx_1_46 + 3, ry_1_46 + 0)==False, 
)))
s.add(Or(rprim_1_46!=19,
And(rx_f_1_46==0, ry_f_1_46==3, rcost_1_46==4, 
obstacle(rx_1_46 + 0, ry_1_46 + 0)==False, 
obstacle(rx_1_46 + 0, ry_1_46 + 1)==False, 
obstacle(rx_1_46 + 0, ry_1_46 + 2)==False, 
obstacle(rx_1_46 + 0, ry_1_46 + 3)==False, 
)))
s.add(Or(rprim_1_46!=20,
And(rx_f_1_46==-3, ry_f_1_46==0, rcost_1_46==4, 
obstacle(rx_1_46 + 0, ry_1_46 + 0)==False, 
obstacle(rx_1_46 + -1, ry_1_46 + 0)==False, 
obstacle(rx_1_46 + -2, ry_1_46 + 0)==False, 
obstacle(rx_1_46 + -3, ry_1_46 + 0)==False, 
)))
s.add(Or(rprim_1_46!=21,
And(rx_f_1_46==0, ry_f_1_46==-3, rcost_1_46==4, 
obstacle(rx_1_46 + 0, ry_1_46 + 0)==False, 
obstacle(rx_1_46 + 0, ry_1_46 + -1)==False, 
obstacle(rx_1_46 + 0, ry_1_46 + -2)==False, 
obstacle(rx_1_46 + 0, ry_1_46 + -3)==False, 
)))
s.add(Or(rprim_1_47!=1,
And(rx_f_1_47==0, ry_f_1_47==0, rcost_1_47==0, 
obstacle(rx_1_47 + 0, ry_1_47 + 0)==False, 
)))
s.add(Or(rprim_1_47!=2,
And(rx_f_1_47==1, ry_f_1_47==0, rcost_1_47==2, 
obstacle(rx_1_47 + 0, ry_1_47 + 0)==False, 
obstacle(rx_1_47 + 1, ry_1_47 + 0)==False, 
)))
s.add(Or(rprim_1_47!=3,
And(rx_f_1_47==0, ry_f_1_47==-1, rcost_1_47==2, 
obstacle(rx_1_47 + 0, ry_1_47 + 0)==False, 
obstacle(rx_1_47 + 0, ry_1_47 + -1)==False, 
)))
s.add(Or(rprim_1_47!=4,
And(rx_f_1_47==-1, ry_f_1_47==0, rcost_1_47==2, 
obstacle(rx_1_47 + 0, ry_1_47 + 0)==False, 
obstacle(rx_1_47 + -1, ry_1_47 + 0)==False, 
)))
s.add(Or(rprim_1_47!=5,
And(rx_f_1_47==0, ry_f_1_47==1, rcost_1_47==2, 
obstacle(rx_1_47 + 0, ry_1_47 + 0)==False, 
obstacle(rx_1_47 + 0, ry_1_47 + 1)==False, 
)))
s.add(Or(rprim_1_47!=6,
And(rx_f_1_47==1, ry_f_1_47==1, rcost_1_47==3, 
obstacle(rx_1_47 + 0, ry_1_47 + 0)==False, 
obstacle(rx_1_47 + 1, ry_1_47 + 1)==False, 
)))
s.add(Or(rprim_1_47!=7,
And(rx_f_1_47==-1, ry_f_1_47==1, rcost_1_47==3, 
obstacle(rx_1_47 + 0, ry_1_47 + 0)==False, 
obstacle(rx_1_47 + -1, ry_1_47 + 1)==False, 
)))
s.add(Or(rprim_1_47!=8,
And(rx_f_1_47==-1, ry_f_1_47==-1, rcost_1_47==3, 
obstacle(rx_1_47 + 0, ry_1_47 + 0)==False, 
obstacle(rx_1_47 + -1, ry_1_47 + -1)==False, 
)))
s.add(Or(rprim_1_47!=9,
And(rx_f_1_47==1, ry_f_1_47==-1, rcost_1_47==3, 
obstacle(rx_1_47 + 0, ry_1_47 + 0)==False, 
obstacle(rx_1_47 + 1, ry_1_47 + -1)==False, 
)))
s.add(Or(rprim_1_47!=10,
And(rx_f_1_47==2, ry_f_1_47==0, rcost_1_47==3, 
obstacle(rx_1_47 + 0, ry_1_47 + 0)==False, 
obstacle(rx_1_47 + 1, ry_1_47 + 0)==False, 
obstacle(rx_1_47 + 2, ry_1_47 + 0)==False, 
)))
s.add(Or(rprim_1_47!=11,
And(rx_f_1_47==0, ry_f_1_47==2, rcost_1_47==3, 
obstacle(rx_1_47 + 0, ry_1_47 + 0)==False, 
obstacle(rx_1_47 + 0, ry_1_47 + 1)==False, 
obstacle(rx_1_47 + 0, ry_1_47 + 2)==False, 
)))
s.add(Or(rprim_1_47!=12,
And(rx_f_1_47==-2, ry_f_1_47==0, rcost_1_47==3, 
obstacle(rx_1_47 + 0, ry_1_47 + 0)==False, 
obstacle(rx_1_47 + -1, ry_1_47 + 0)==False, 
obstacle(rx_1_47 + -2, ry_1_47 + 0)==False, 
)))
s.add(Or(rprim_1_47!=13,
And(rx_f_1_47==0, ry_f_1_47==-2, rcost_1_47==3, 
obstacle(rx_1_47 + 0, ry_1_47 + 0)==False, 
obstacle(rx_1_47 + 0, ry_1_47 + -1)==False, 
obstacle(rx_1_47 + 0, ry_1_47 + -2)==False, 
)))
s.add(Or(rprim_1_47!=14,
And(rx_f_1_47==2, ry_f_1_47==2, rcost_1_47==4, 
obstacle(rx_1_47 + 0, ry_1_47 + 0)==False, 
obstacle(rx_1_47 + 1, ry_1_47 + 1)==False, 
obstacle(rx_1_47 + 2, ry_1_47 + 2)==False, 
)))
s.add(Or(rprim_1_47!=15,
And(rx_f_1_47==-2, ry_f_1_47==2, rcost_1_47==4, 
obstacle(rx_1_47 + 0, ry_1_47 + 0)==False, 
obstacle(rx_1_47 + -1, ry_1_47 + 1)==False, 
obstacle(rx_1_47 + -2, ry_1_47 + 2)==False, 
)))
s.add(Or(rprim_1_47!=16,
And(rx_f_1_47==-2, ry_f_1_47==-2, rcost_1_47==4, 
obstacle(rx_1_47 + 0, ry_1_47 + 0)==False, 
obstacle(rx_1_47 + -1, ry_1_47 + -1)==False, 
obstacle(rx_1_47 + -2, ry_1_47 + -2)==False, 
)))
s.add(Or(rprim_1_47!=17,
And(rx_f_1_47==2, ry_f_1_47==-2, rcost_1_47==4, 
obstacle(rx_1_47 + 0, ry_1_47 + 0)==False, 
obstacle(rx_1_47 + 1, ry_1_47 + -1)==False, 
obstacle(rx_1_47 + 2, ry_1_47 + -2)==False, 
)))
s.add(Or(rprim_1_47!=18,
And(rx_f_1_47==3, ry_f_1_47==0, rcost_1_47==4, 
obstacle(rx_1_47 + 0, ry_1_47 + 0)==False, 
obstacle(rx_1_47 + 1, ry_1_47 + 0)==False, 
obstacle(rx_1_47 + 2, ry_1_47 + 0)==False, 
obstacle(rx_1_47 + 3, ry_1_47 + 0)==False, 
)))
s.add(Or(rprim_1_47!=19,
And(rx_f_1_47==0, ry_f_1_47==3, rcost_1_47==4, 
obstacle(rx_1_47 + 0, ry_1_47 + 0)==False, 
obstacle(rx_1_47 + 0, ry_1_47 + 1)==False, 
obstacle(rx_1_47 + 0, ry_1_47 + 2)==False, 
obstacle(rx_1_47 + 0, ry_1_47 + 3)==False, 
)))
s.add(Or(rprim_1_47!=20,
And(rx_f_1_47==-3, ry_f_1_47==0, rcost_1_47==4, 
obstacle(rx_1_47 + 0, ry_1_47 + 0)==False, 
obstacle(rx_1_47 + -1, ry_1_47 + 0)==False, 
obstacle(rx_1_47 + -2, ry_1_47 + 0)==False, 
obstacle(rx_1_47 + -3, ry_1_47 + 0)==False, 
)))
s.add(Or(rprim_1_47!=21,
And(rx_f_1_47==0, ry_f_1_47==-3, rcost_1_47==4, 
obstacle(rx_1_47 + 0, ry_1_47 + 0)==False, 
obstacle(rx_1_47 + 0, ry_1_47 + -1)==False, 
obstacle(rx_1_47 + 0, ry_1_47 + -2)==False, 
obstacle(rx_1_47 + 0, ry_1_47 + -3)==False, 
)))
s.add(Or(rprim_1_48!=1,
And(rx_f_1_48==0, ry_f_1_48==0, rcost_1_48==0, 
obstacle(rx_1_48 + 0, ry_1_48 + 0)==False, 
)))
s.add(Or(rprim_1_48!=2,
And(rx_f_1_48==1, ry_f_1_48==0, rcost_1_48==2, 
obstacle(rx_1_48 + 0, ry_1_48 + 0)==False, 
obstacle(rx_1_48 + 1, ry_1_48 + 0)==False, 
)))
s.add(Or(rprim_1_48!=3,
And(rx_f_1_48==0, ry_f_1_48==-1, rcost_1_48==2, 
obstacle(rx_1_48 + 0, ry_1_48 + 0)==False, 
obstacle(rx_1_48 + 0, ry_1_48 + -1)==False, 
)))
s.add(Or(rprim_1_48!=4,
And(rx_f_1_48==-1, ry_f_1_48==0, rcost_1_48==2, 
obstacle(rx_1_48 + 0, ry_1_48 + 0)==False, 
obstacle(rx_1_48 + -1, ry_1_48 + 0)==False, 
)))
s.add(Or(rprim_1_48!=5,
And(rx_f_1_48==0, ry_f_1_48==1, rcost_1_48==2, 
obstacle(rx_1_48 + 0, ry_1_48 + 0)==False, 
obstacle(rx_1_48 + 0, ry_1_48 + 1)==False, 
)))
s.add(Or(rprim_1_48!=6,
And(rx_f_1_48==1, ry_f_1_48==1, rcost_1_48==3, 
obstacle(rx_1_48 + 0, ry_1_48 + 0)==False, 
obstacle(rx_1_48 + 1, ry_1_48 + 1)==False, 
)))
s.add(Or(rprim_1_48!=7,
And(rx_f_1_48==-1, ry_f_1_48==1, rcost_1_48==3, 
obstacle(rx_1_48 + 0, ry_1_48 + 0)==False, 
obstacle(rx_1_48 + -1, ry_1_48 + 1)==False, 
)))
s.add(Or(rprim_1_48!=8,
And(rx_f_1_48==-1, ry_f_1_48==-1, rcost_1_48==3, 
obstacle(rx_1_48 + 0, ry_1_48 + 0)==False, 
obstacle(rx_1_48 + -1, ry_1_48 + -1)==False, 
)))
s.add(Or(rprim_1_48!=9,
And(rx_f_1_48==1, ry_f_1_48==-1, rcost_1_48==3, 
obstacle(rx_1_48 + 0, ry_1_48 + 0)==False, 
obstacle(rx_1_48 + 1, ry_1_48 + -1)==False, 
)))
s.add(Or(rprim_1_48!=10,
And(rx_f_1_48==2, ry_f_1_48==0, rcost_1_48==3, 
obstacle(rx_1_48 + 0, ry_1_48 + 0)==False, 
obstacle(rx_1_48 + 1, ry_1_48 + 0)==False, 
obstacle(rx_1_48 + 2, ry_1_48 + 0)==False, 
)))
s.add(Or(rprim_1_48!=11,
And(rx_f_1_48==0, ry_f_1_48==2, rcost_1_48==3, 
obstacle(rx_1_48 + 0, ry_1_48 + 0)==False, 
obstacle(rx_1_48 + 0, ry_1_48 + 1)==False, 
obstacle(rx_1_48 + 0, ry_1_48 + 2)==False, 
)))
s.add(Or(rprim_1_48!=12,
And(rx_f_1_48==-2, ry_f_1_48==0, rcost_1_48==3, 
obstacle(rx_1_48 + 0, ry_1_48 + 0)==False, 
obstacle(rx_1_48 + -1, ry_1_48 + 0)==False, 
obstacle(rx_1_48 + -2, ry_1_48 + 0)==False, 
)))
s.add(Or(rprim_1_48!=13,
And(rx_f_1_48==0, ry_f_1_48==-2, rcost_1_48==3, 
obstacle(rx_1_48 + 0, ry_1_48 + 0)==False, 
obstacle(rx_1_48 + 0, ry_1_48 + -1)==False, 
obstacle(rx_1_48 + 0, ry_1_48 + -2)==False, 
)))
s.add(Or(rprim_1_48!=14,
And(rx_f_1_48==2, ry_f_1_48==2, rcost_1_48==4, 
obstacle(rx_1_48 + 0, ry_1_48 + 0)==False, 
obstacle(rx_1_48 + 1, ry_1_48 + 1)==False, 
obstacle(rx_1_48 + 2, ry_1_48 + 2)==False, 
)))
s.add(Or(rprim_1_48!=15,
And(rx_f_1_48==-2, ry_f_1_48==2, rcost_1_48==4, 
obstacle(rx_1_48 + 0, ry_1_48 + 0)==False, 
obstacle(rx_1_48 + -1, ry_1_48 + 1)==False, 
obstacle(rx_1_48 + -2, ry_1_48 + 2)==False, 
)))
s.add(Or(rprim_1_48!=16,
And(rx_f_1_48==-2, ry_f_1_48==-2, rcost_1_48==4, 
obstacle(rx_1_48 + 0, ry_1_48 + 0)==False, 
obstacle(rx_1_48 + -1, ry_1_48 + -1)==False, 
obstacle(rx_1_48 + -2, ry_1_48 + -2)==False, 
)))
s.add(Or(rprim_1_48!=17,
And(rx_f_1_48==2, ry_f_1_48==-2, rcost_1_48==4, 
obstacle(rx_1_48 + 0, ry_1_48 + 0)==False, 
obstacle(rx_1_48 + 1, ry_1_48 + -1)==False, 
obstacle(rx_1_48 + 2, ry_1_48 + -2)==False, 
)))
s.add(Or(rprim_1_48!=18,
And(rx_f_1_48==3, ry_f_1_48==0, rcost_1_48==4, 
obstacle(rx_1_48 + 0, ry_1_48 + 0)==False, 
obstacle(rx_1_48 + 1, ry_1_48 + 0)==False, 
obstacle(rx_1_48 + 2, ry_1_48 + 0)==False, 
obstacle(rx_1_48 + 3, ry_1_48 + 0)==False, 
)))
s.add(Or(rprim_1_48!=19,
And(rx_f_1_48==0, ry_f_1_48==3, rcost_1_48==4, 
obstacle(rx_1_48 + 0, ry_1_48 + 0)==False, 
obstacle(rx_1_48 + 0, ry_1_48 + 1)==False, 
obstacle(rx_1_48 + 0, ry_1_48 + 2)==False, 
obstacle(rx_1_48 + 0, ry_1_48 + 3)==False, 
)))
s.add(Or(rprim_1_48!=20,
And(rx_f_1_48==-3, ry_f_1_48==0, rcost_1_48==4, 
obstacle(rx_1_48 + 0, ry_1_48 + 0)==False, 
obstacle(rx_1_48 + -1, ry_1_48 + 0)==False, 
obstacle(rx_1_48 + -2, ry_1_48 + 0)==False, 
obstacle(rx_1_48 + -3, ry_1_48 + 0)==False, 
)))
s.add(Or(rprim_1_48!=21,
And(rx_f_1_48==0, ry_f_1_48==-3, rcost_1_48==4, 
obstacle(rx_1_48 + 0, ry_1_48 + 0)==False, 
obstacle(rx_1_48 + 0, ry_1_48 + -1)==False, 
obstacle(rx_1_48 + 0, ry_1_48 + -2)==False, 
obstacle(rx_1_48 + 0, ry_1_48 + -3)==False, 
)))

# transition : change rx and ry of rechargers
s.add(rx_1_2==rx_1_1 + rx_f_1_1, ry_1_2==ry_1_1 + ry_f_1_1)
s.add(rx_1_3==rx_1_2 + rx_f_1_2, ry_1_3==ry_1_2 + ry_f_1_2)
s.add(rx_1_4==rx_1_3 + rx_f_1_3, ry_1_4==ry_1_3 + ry_f_1_3)
s.add(rx_1_5==rx_1_4 + rx_f_1_4, ry_1_5==ry_1_4 + ry_f_1_4)
s.add(rx_1_6==rx_1_5 + rx_f_1_5, ry_1_6==ry_1_5 + ry_f_1_5)
s.add(rx_1_7==rx_1_6 + rx_f_1_6, ry_1_7==ry_1_6 + ry_f_1_6)
s.add(rx_1_8==rx_1_7 + rx_f_1_7, ry_1_8==ry_1_7 + ry_f_1_7)
s.add(rx_1_9==rx_1_8 + rx_f_1_8, ry_1_9==ry_1_8 + ry_f_1_8)
s.add(rx_1_10==rx_1_9 + rx_f_1_9, ry_1_10==ry_1_9 + ry_f_1_9)
s.add(rx_1_11==rx_1_10 + rx_f_1_10, ry_1_11==ry_1_10 + ry_f_1_10)
s.add(rx_1_12==rx_1_11 + rx_f_1_11, ry_1_12==ry_1_11 + ry_f_1_11)
s.add(rx_1_13==rx_1_12 + rx_f_1_12, ry_1_13==ry_1_12 + ry_f_1_12)
s.add(rx_1_14==rx_1_13 + rx_f_1_13, ry_1_14==ry_1_13 + ry_f_1_13)
s.add(rx_1_15==rx_1_14 + rx_f_1_14, ry_1_15==ry_1_14 + ry_f_1_14)
s.add(rx_1_16==rx_1_15 + rx_f_1_15, ry_1_16==ry_1_15 + ry_f_1_15)
s.add(rx_1_17==rx_1_16 + rx_f_1_16, ry_1_17==ry_1_16 + ry_f_1_16)
s.add(rx_1_18==rx_1_17 + rx_f_1_17, ry_1_18==ry_1_17 + ry_f_1_17)
s.add(rx_1_19==rx_1_18 + rx_f_1_18, ry_1_19==ry_1_18 + ry_f_1_18)
s.add(rx_1_20==rx_1_19 + rx_f_1_19, ry_1_20==ry_1_19 + ry_f_1_19)
s.add(rx_1_21==rx_1_20 + rx_f_1_20, ry_1_21==ry_1_20 + ry_f_1_20)
s.add(rx_1_22==rx_1_21 + rx_f_1_21, ry_1_22==ry_1_21 + ry_f_1_21)
s.add(rx_1_23==rx_1_22 + rx_f_1_22, ry_1_23==ry_1_22 + ry_f_1_22)
s.add(rx_1_24==rx_1_23 + rx_f_1_23, ry_1_24==ry_1_23 + ry_f_1_23)
s.add(rx_1_25==rx_1_24 + rx_f_1_24, ry_1_25==ry_1_24 + ry_f_1_24)
s.add(rx_1_26==rx_1_25 + rx_f_1_25, ry_1_26==ry_1_25 + ry_f_1_25)
s.add(rx_1_27==rx_1_26 + rx_f_1_26, ry_1_27==ry_1_26 + ry_f_1_26)
s.add(rx_1_28==rx_1_27 + rx_f_1_27, ry_1_28==ry_1_27 + ry_f_1_27)
s.add(rx_1_29==rx_1_28 + rx_f_1_28, ry_1_29==ry_1_28 + ry_f_1_28)
s.add(rx_1_30==rx_1_29 + rx_f_1_29, ry_1_30==ry_1_29 + ry_f_1_29)
s.add(rx_1_31==rx_1_30 + rx_f_1_30, ry_1_31==ry_1_30 + ry_f_1_30)
s.add(rx_1_32==rx_1_31 + rx_f_1_31, ry_1_32==ry_1_31 + ry_f_1_31)
s.add(rx_1_33==rx_1_32 + rx_f_1_32, ry_1_33==ry_1_32 + ry_f_1_32)
s.add(rx_1_34==rx_1_33 + rx_f_1_33, ry_1_34==ry_1_33 + ry_f_1_33)
s.add(rx_1_35==rx_1_34 + rx_f_1_34, ry_1_35==ry_1_34 + ry_f_1_34)
s.add(rx_1_36==rx_1_35 + rx_f_1_35, ry_1_36==ry_1_35 + ry_f_1_35)
s.add(rx_1_37==rx_1_36 + rx_f_1_36, ry_1_37==ry_1_36 + ry_f_1_36)
s.add(rx_1_38==rx_1_37 + rx_f_1_37, ry_1_38==ry_1_37 + ry_f_1_37)
s.add(rx_1_39==rx_1_38 + rx_f_1_38, ry_1_39==ry_1_38 + ry_f_1_38)
s.add(rx_1_40==rx_1_39 + rx_f_1_39, ry_1_40==ry_1_39 + ry_f_1_39)
s.add(rx_1_41==rx_1_40 + rx_f_1_40, ry_1_41==ry_1_40 + ry_f_1_40)
s.add(rx_1_42==rx_1_41 + rx_f_1_41, ry_1_42==ry_1_41 + ry_f_1_41)
s.add(rx_1_43==rx_1_42 + rx_f_1_42, ry_1_43==ry_1_42 + ry_f_1_42)
s.add(rx_1_44==rx_1_43 + rx_f_1_43, ry_1_44==ry_1_43 + ry_f_1_43)
s.add(rx_1_45==rx_1_44 + rx_f_1_44, ry_1_45==ry_1_44 + ry_f_1_44)
s.add(rx_1_46==rx_1_45 + rx_f_1_45, ry_1_46==ry_1_45 + ry_f_1_45)
s.add(rx_1_47==rx_1_46 + rx_f_1_46, ry_1_47==ry_1_46 + ry_f_1_46)
s.add(rx_1_48==rx_1_47 + rx_f_1_47, ry_1_48==ry_1_47 + ry_f_1_47)
s.add(rx_1_49==rx_1_48 + rx_f_1_48, ry_1_49==ry_1_48 + ry_f_1_48)

s.add(
Implies(wprim_1_1==0, And(waitcount_1_1==1, rechcount_1_1==0)), 
Implies(wprim_1_1==2, And(waitcount_1_1==1, rechcount_1_1==1)), 
Implies(wprim_1_1==1, And(waitcount_1_1==0, rechcount_1_1==0)))
s.add(
Implies(wprim_1_2==0, And(waitcount_1_2==1, rechcount_1_2==0)), 
Implies(wprim_1_2==2, And(waitcount_1_2==1, rechcount_1_2==1)), 
Implies(wprim_1_2==1, And(waitcount_1_2==0, rechcount_1_2==0)))
s.add(
Implies(wprim_1_3==0, And(waitcount_1_3==1, rechcount_1_3==0)), 
Implies(wprim_1_3==2, And(waitcount_1_3==1, rechcount_1_3==1)), 
Implies(wprim_1_3==1, And(waitcount_1_3==0, rechcount_1_3==0)))
s.add(
Implies(wprim_1_4==0, And(waitcount_1_4==1, rechcount_1_4==0)), 
Implies(wprim_1_4==2, And(waitcount_1_4==1, rechcount_1_4==1)), 
Implies(wprim_1_4==1, And(waitcount_1_4==0, rechcount_1_4==0)))
s.add(
Implies(wprim_1_5==0, And(waitcount_1_5==1, rechcount_1_5==0)), 
Implies(wprim_1_5==2, And(waitcount_1_5==1, rechcount_1_5==1)), 
Implies(wprim_1_5==1, And(waitcount_1_5==0, rechcount_1_5==0)))
s.add(
Implies(wprim_1_6==0, And(waitcount_1_6==1, rechcount_1_6==0)), 
Implies(wprim_1_6==2, And(waitcount_1_6==1, rechcount_1_6==1)), 
Implies(wprim_1_6==1, And(waitcount_1_6==0, rechcount_1_6==0)))
s.add(
Implies(wprim_1_7==0, And(waitcount_1_7==1, rechcount_1_7==0)), 
Implies(wprim_1_7==2, And(waitcount_1_7==1, rechcount_1_7==1)), 
Implies(wprim_1_7==1, And(waitcount_1_7==0, rechcount_1_7==0)))
s.add(
Implies(wprim_1_8==0, And(waitcount_1_8==1, rechcount_1_8==0)), 
Implies(wprim_1_8==2, And(waitcount_1_8==1, rechcount_1_8==1)), 
Implies(wprim_1_8==1, And(waitcount_1_8==0, rechcount_1_8==0)))
s.add(
Implies(wprim_1_9==0, And(waitcount_1_9==1, rechcount_1_9==0)), 
Implies(wprim_1_9==2, And(waitcount_1_9==1, rechcount_1_9==1)), 
Implies(wprim_1_9==1, And(waitcount_1_9==0, rechcount_1_9==0)))
s.add(
Implies(wprim_1_10==0, And(waitcount_1_10==1, rechcount_1_10==0)), 
Implies(wprim_1_10==2, And(waitcount_1_10==1, rechcount_1_10==1)), 
Implies(wprim_1_10==1, And(waitcount_1_10==0, rechcount_1_10==0)))
s.add(
Implies(wprim_1_11==0, And(waitcount_1_11==1, rechcount_1_11==0)), 
Implies(wprim_1_11==2, And(waitcount_1_11==1, rechcount_1_11==1)), 
Implies(wprim_1_11==1, And(waitcount_1_11==0, rechcount_1_11==0)))
s.add(
Implies(wprim_1_12==0, And(waitcount_1_12==1, rechcount_1_12==0)), 
Implies(wprim_1_12==2, And(waitcount_1_12==1, rechcount_1_12==1)), 
Implies(wprim_1_12==1, And(waitcount_1_12==0, rechcount_1_12==0)))
s.add(
Implies(wprim_1_13==0, And(waitcount_1_13==1, rechcount_1_13==0)), 
Implies(wprim_1_13==2, And(waitcount_1_13==1, rechcount_1_13==1)), 
Implies(wprim_1_13==1, And(waitcount_1_13==0, rechcount_1_13==0)))
s.add(
Implies(wprim_1_14==0, And(waitcount_1_14==1, rechcount_1_14==0)), 
Implies(wprim_1_14==2, And(waitcount_1_14==1, rechcount_1_14==1)), 
Implies(wprim_1_14==1, And(waitcount_1_14==0, rechcount_1_14==0)))
s.add(
Implies(wprim_1_15==0, And(waitcount_1_15==1, rechcount_1_15==0)), 
Implies(wprim_1_15==2, And(waitcount_1_15==1, rechcount_1_15==1)), 
Implies(wprim_1_15==1, And(waitcount_1_15==0, rechcount_1_15==0)))
s.add(
Implies(wprim_1_16==0, And(waitcount_1_16==1, rechcount_1_16==0)), 
Implies(wprim_1_16==2, And(waitcount_1_16==1, rechcount_1_16==1)), 
Implies(wprim_1_16==1, And(waitcount_1_16==0, rechcount_1_16==0)))
s.add(
Implies(wprim_1_17==0, And(waitcount_1_17==1, rechcount_1_17==0)), 
Implies(wprim_1_17==2, And(waitcount_1_17==1, rechcount_1_17==1)), 
Implies(wprim_1_17==1, And(waitcount_1_17==0, rechcount_1_17==0)))
s.add(
Implies(wprim_1_18==0, And(waitcount_1_18==1, rechcount_1_18==0)), 
Implies(wprim_1_18==2, And(waitcount_1_18==1, rechcount_1_18==1)), 
Implies(wprim_1_18==1, And(waitcount_1_18==0, rechcount_1_18==0)))
s.add(
Implies(wprim_1_19==0, And(waitcount_1_19==1, rechcount_1_19==0)), 
Implies(wprim_1_19==2, And(waitcount_1_19==1, rechcount_1_19==1)), 
Implies(wprim_1_19==1, And(waitcount_1_19==0, rechcount_1_19==0)))
s.add(
Implies(wprim_1_20==0, And(waitcount_1_20==1, rechcount_1_20==0)), 
Implies(wprim_1_20==2, And(waitcount_1_20==1, rechcount_1_20==1)), 
Implies(wprim_1_20==1, And(waitcount_1_20==0, rechcount_1_20==0)))
s.add(
Implies(wprim_1_21==0, And(waitcount_1_21==1, rechcount_1_21==0)), 
Implies(wprim_1_21==2, And(waitcount_1_21==1, rechcount_1_21==1)), 
Implies(wprim_1_21==1, And(waitcount_1_21==0, rechcount_1_21==0)))
s.add(
Implies(wprim_1_22==0, And(waitcount_1_22==1, rechcount_1_22==0)), 
Implies(wprim_1_22==2, And(waitcount_1_22==1, rechcount_1_22==1)), 
Implies(wprim_1_22==1, And(waitcount_1_22==0, rechcount_1_22==0)))
s.add(
Implies(wprim_1_23==0, And(waitcount_1_23==1, rechcount_1_23==0)), 
Implies(wprim_1_23==2, And(waitcount_1_23==1, rechcount_1_23==1)), 
Implies(wprim_1_23==1, And(waitcount_1_23==0, rechcount_1_23==0)))
s.add(
Implies(wprim_1_24==0, And(waitcount_1_24==1, rechcount_1_24==0)), 
Implies(wprim_1_24==2, And(waitcount_1_24==1, rechcount_1_24==1)), 
Implies(wprim_1_24==1, And(waitcount_1_24==0, rechcount_1_24==0)))
s.add(
Implies(wprim_1_25==0, And(waitcount_1_25==1, rechcount_1_25==0)), 
Implies(wprim_1_25==2, And(waitcount_1_25==1, rechcount_1_25==1)), 
Implies(wprim_1_25==1, And(waitcount_1_25==0, rechcount_1_25==0)))
s.add(
Implies(wprim_1_26==0, And(waitcount_1_26==1, rechcount_1_26==0)), 
Implies(wprim_1_26==2, And(waitcount_1_26==1, rechcount_1_26==1)), 
Implies(wprim_1_26==1, And(waitcount_1_26==0, rechcount_1_26==0)))
s.add(
Implies(wprim_1_27==0, And(waitcount_1_27==1, rechcount_1_27==0)), 
Implies(wprim_1_27==2, And(waitcount_1_27==1, rechcount_1_27==1)), 
Implies(wprim_1_27==1, And(waitcount_1_27==0, rechcount_1_27==0)))
s.add(
Implies(wprim_1_28==0, And(waitcount_1_28==1, rechcount_1_28==0)), 
Implies(wprim_1_28==2, And(waitcount_1_28==1, rechcount_1_28==1)), 
Implies(wprim_1_28==1, And(waitcount_1_28==0, rechcount_1_28==0)))
s.add(
Implies(wprim_1_29==0, And(waitcount_1_29==1, rechcount_1_29==0)), 
Implies(wprim_1_29==2, And(waitcount_1_29==1, rechcount_1_29==1)), 
Implies(wprim_1_29==1, And(waitcount_1_29==0, rechcount_1_29==0)))
s.add(
Implies(wprim_1_30==0, And(waitcount_1_30==1, rechcount_1_30==0)), 
Implies(wprim_1_30==2, And(waitcount_1_30==1, rechcount_1_30==1)), 
Implies(wprim_1_30==1, And(waitcount_1_30==0, rechcount_1_30==0)))
s.add(
Implies(wprim_1_31==0, And(waitcount_1_31==1, rechcount_1_31==0)), 
Implies(wprim_1_31==2, And(waitcount_1_31==1, rechcount_1_31==1)), 
Implies(wprim_1_31==1, And(waitcount_1_31==0, rechcount_1_31==0)))
s.add(
Implies(wprim_1_32==0, And(waitcount_1_32==1, rechcount_1_32==0)), 
Implies(wprim_1_32==2, And(waitcount_1_32==1, rechcount_1_32==1)), 
Implies(wprim_1_32==1, And(waitcount_1_32==0, rechcount_1_32==0)))
s.add(
Implies(wprim_1_33==0, And(waitcount_1_33==1, rechcount_1_33==0)), 
Implies(wprim_1_33==2, And(waitcount_1_33==1, rechcount_1_33==1)), 
Implies(wprim_1_33==1, And(waitcount_1_33==0, rechcount_1_33==0)))
s.add(
Implies(wprim_1_34==0, And(waitcount_1_34==1, rechcount_1_34==0)), 
Implies(wprim_1_34==2, And(waitcount_1_34==1, rechcount_1_34==1)), 
Implies(wprim_1_34==1, And(waitcount_1_34==0, rechcount_1_34==0)))
s.add(
Implies(wprim_1_35==0, And(waitcount_1_35==1, rechcount_1_35==0)), 
Implies(wprim_1_35==2, And(waitcount_1_35==1, rechcount_1_35==1)), 
Implies(wprim_1_35==1, And(waitcount_1_35==0, rechcount_1_35==0)))
s.add(
Implies(wprim_1_36==0, And(waitcount_1_36==1, rechcount_1_36==0)), 
Implies(wprim_1_36==2, And(waitcount_1_36==1, rechcount_1_36==1)), 
Implies(wprim_1_36==1, And(waitcount_1_36==0, rechcount_1_36==0)))
s.add(
Implies(wprim_1_37==0, And(waitcount_1_37==1, rechcount_1_37==0)), 
Implies(wprim_1_37==2, And(waitcount_1_37==1, rechcount_1_37==1)), 
Implies(wprim_1_37==1, And(waitcount_1_37==0, rechcount_1_37==0)))
s.add(
Implies(wprim_1_38==0, And(waitcount_1_38==1, rechcount_1_38==0)), 
Implies(wprim_1_38==2, And(waitcount_1_38==1, rechcount_1_38==1)), 
Implies(wprim_1_38==1, And(waitcount_1_38==0, rechcount_1_38==0)))
s.add(
Implies(wprim_1_39==0, And(waitcount_1_39==1, rechcount_1_39==0)), 
Implies(wprim_1_39==2, And(waitcount_1_39==1, rechcount_1_39==1)), 
Implies(wprim_1_39==1, And(waitcount_1_39==0, rechcount_1_39==0)))
s.add(
Implies(wprim_1_40==0, And(waitcount_1_40==1, rechcount_1_40==0)), 
Implies(wprim_1_40==2, And(waitcount_1_40==1, rechcount_1_40==1)), 
Implies(wprim_1_40==1, And(waitcount_1_40==0, rechcount_1_40==0)))
s.add(
Implies(wprim_1_41==0, And(waitcount_1_41==1, rechcount_1_41==0)), 
Implies(wprim_1_41==2, And(waitcount_1_41==1, rechcount_1_41==1)), 
Implies(wprim_1_41==1, And(waitcount_1_41==0, rechcount_1_41==0)))
s.add(
Implies(wprim_1_42==0, And(waitcount_1_42==1, rechcount_1_42==0)), 
Implies(wprim_1_42==2, And(waitcount_1_42==1, rechcount_1_42==1)), 
Implies(wprim_1_42==1, And(waitcount_1_42==0, rechcount_1_42==0)))
s.add(
Implies(wprim_1_43==0, And(waitcount_1_43==1, rechcount_1_43==0)), 
Implies(wprim_1_43==2, And(waitcount_1_43==1, rechcount_1_43==1)), 
Implies(wprim_1_43==1, And(waitcount_1_43==0, rechcount_1_43==0)))
s.add(
Implies(wprim_1_44==0, And(waitcount_1_44==1, rechcount_1_44==0)), 
Implies(wprim_1_44==2, And(waitcount_1_44==1, rechcount_1_44==1)), 
Implies(wprim_1_44==1, And(waitcount_1_44==0, rechcount_1_44==0)))
s.add(
Implies(wprim_1_45==0, And(waitcount_1_45==1, rechcount_1_45==0)), 
Implies(wprim_1_45==2, And(waitcount_1_45==1, rechcount_1_45==1)), 
Implies(wprim_1_45==1, And(waitcount_1_45==0, rechcount_1_45==0)))
s.add(
Implies(wprim_1_46==0, And(waitcount_1_46==1, rechcount_1_46==0)), 
Implies(wprim_1_46==2, And(waitcount_1_46==1, rechcount_1_46==1)), 
Implies(wprim_1_46==1, And(waitcount_1_46==0, rechcount_1_46==0)))
s.add(
Implies(wprim_1_47==0, And(waitcount_1_47==1, rechcount_1_47==0)), 
Implies(wprim_1_47==2, And(waitcount_1_47==1, rechcount_1_47==1)), 
Implies(wprim_1_47==1, And(waitcount_1_47==0, rechcount_1_47==0)))
s.add(
Implies(wprim_1_48==0, And(waitcount_1_48==1, rechcount_1_48==0)), 
Implies(wprim_1_48==2, And(waitcount_1_48==1, rechcount_1_48==1)), 
Implies(wprim_1_48==1, And(waitcount_1_48==0, rechcount_1_48==0)))

s.add(
Implies(wprim_2_1==0, And(waitcount_2_1==1, rechcount_2_1==0)), 
Implies(wprim_2_1==2, And(waitcount_2_1==1, rechcount_2_1==1)), 
Implies(wprim_2_1==1, And(waitcount_2_1==0, rechcount_2_1==0)))
s.add(
Implies(wprim_2_2==0, And(waitcount_2_2==1, rechcount_2_2==0)), 
Implies(wprim_2_2==2, And(waitcount_2_2==1, rechcount_2_2==1)), 
Implies(wprim_2_2==1, And(waitcount_2_2==0, rechcount_2_2==0)))
s.add(
Implies(wprim_2_3==0, And(waitcount_2_3==1, rechcount_2_3==0)), 
Implies(wprim_2_3==2, And(waitcount_2_3==1, rechcount_2_3==1)), 
Implies(wprim_2_3==1, And(waitcount_2_3==0, rechcount_2_3==0)))
s.add(
Implies(wprim_2_4==0, And(waitcount_2_4==1, rechcount_2_4==0)), 
Implies(wprim_2_4==2, And(waitcount_2_4==1, rechcount_2_4==1)), 
Implies(wprim_2_4==1, And(waitcount_2_4==0, rechcount_2_4==0)))
s.add(
Implies(wprim_2_5==0, And(waitcount_2_5==1, rechcount_2_5==0)), 
Implies(wprim_2_5==2, And(waitcount_2_5==1, rechcount_2_5==1)), 
Implies(wprim_2_5==1, And(waitcount_2_5==0, rechcount_2_5==0)))
s.add(
Implies(wprim_2_6==0, And(waitcount_2_6==1, rechcount_2_6==0)), 
Implies(wprim_2_6==2, And(waitcount_2_6==1, rechcount_2_6==1)), 
Implies(wprim_2_6==1, And(waitcount_2_6==0, rechcount_2_6==0)))
s.add(
Implies(wprim_2_7==0, And(waitcount_2_7==1, rechcount_2_7==0)), 
Implies(wprim_2_7==2, And(waitcount_2_7==1, rechcount_2_7==1)), 
Implies(wprim_2_7==1, And(waitcount_2_7==0, rechcount_2_7==0)))
s.add(
Implies(wprim_2_8==0, And(waitcount_2_8==1, rechcount_2_8==0)), 
Implies(wprim_2_8==2, And(waitcount_2_8==1, rechcount_2_8==1)), 
Implies(wprim_2_8==1, And(waitcount_2_8==0, rechcount_2_8==0)))
s.add(
Implies(wprim_2_9==0, And(waitcount_2_9==1, rechcount_2_9==0)), 
Implies(wprim_2_9==2, And(waitcount_2_9==1, rechcount_2_9==1)), 
Implies(wprim_2_9==1, And(waitcount_2_9==0, rechcount_2_9==0)))
s.add(
Implies(wprim_2_10==0, And(waitcount_2_10==1, rechcount_2_10==0)), 
Implies(wprim_2_10==2, And(waitcount_2_10==1, rechcount_2_10==1)), 
Implies(wprim_2_10==1, And(waitcount_2_10==0, rechcount_2_10==0)))
s.add(
Implies(wprim_2_11==0, And(waitcount_2_11==1, rechcount_2_11==0)), 
Implies(wprim_2_11==2, And(waitcount_2_11==1, rechcount_2_11==1)), 
Implies(wprim_2_11==1, And(waitcount_2_11==0, rechcount_2_11==0)))
s.add(
Implies(wprim_2_12==0, And(waitcount_2_12==1, rechcount_2_12==0)), 
Implies(wprim_2_12==2, And(waitcount_2_12==1, rechcount_2_12==1)), 
Implies(wprim_2_12==1, And(waitcount_2_12==0, rechcount_2_12==0)))
s.add(
Implies(wprim_2_13==0, And(waitcount_2_13==1, rechcount_2_13==0)), 
Implies(wprim_2_13==2, And(waitcount_2_13==1, rechcount_2_13==1)), 
Implies(wprim_2_13==1, And(waitcount_2_13==0, rechcount_2_13==0)))
s.add(
Implies(wprim_2_14==0, And(waitcount_2_14==1, rechcount_2_14==0)), 
Implies(wprim_2_14==2, And(waitcount_2_14==1, rechcount_2_14==1)), 
Implies(wprim_2_14==1, And(waitcount_2_14==0, rechcount_2_14==0)))
s.add(
Implies(wprim_2_15==0, And(waitcount_2_15==1, rechcount_2_15==0)), 
Implies(wprim_2_15==2, And(waitcount_2_15==1, rechcount_2_15==1)), 
Implies(wprim_2_15==1, And(waitcount_2_15==0, rechcount_2_15==0)))
s.add(
Implies(wprim_2_16==0, And(waitcount_2_16==1, rechcount_2_16==0)), 
Implies(wprim_2_16==2, And(waitcount_2_16==1, rechcount_2_16==1)), 
Implies(wprim_2_16==1, And(waitcount_2_16==0, rechcount_2_16==0)))
s.add(
Implies(wprim_2_17==0, And(waitcount_2_17==1, rechcount_2_17==0)), 
Implies(wprim_2_17==2, And(waitcount_2_17==1, rechcount_2_17==1)), 
Implies(wprim_2_17==1, And(waitcount_2_17==0, rechcount_2_17==0)))
s.add(
Implies(wprim_2_18==0, And(waitcount_2_18==1, rechcount_2_18==0)), 
Implies(wprim_2_18==2, And(waitcount_2_18==1, rechcount_2_18==1)), 
Implies(wprim_2_18==1, And(waitcount_2_18==0, rechcount_2_18==0)))
s.add(
Implies(wprim_2_19==0, And(waitcount_2_19==1, rechcount_2_19==0)), 
Implies(wprim_2_19==2, And(waitcount_2_19==1, rechcount_2_19==1)), 
Implies(wprim_2_19==1, And(waitcount_2_19==0, rechcount_2_19==0)))
s.add(
Implies(wprim_2_20==0, And(waitcount_2_20==1, rechcount_2_20==0)), 
Implies(wprim_2_20==2, And(waitcount_2_20==1, rechcount_2_20==1)), 
Implies(wprim_2_20==1, And(waitcount_2_20==0, rechcount_2_20==0)))
s.add(
Implies(wprim_2_21==0, And(waitcount_2_21==1, rechcount_2_21==0)), 
Implies(wprim_2_21==2, And(waitcount_2_21==1, rechcount_2_21==1)), 
Implies(wprim_2_21==1, And(waitcount_2_21==0, rechcount_2_21==0)))
s.add(
Implies(wprim_2_22==0, And(waitcount_2_22==1, rechcount_2_22==0)), 
Implies(wprim_2_22==2, And(waitcount_2_22==1, rechcount_2_22==1)), 
Implies(wprim_2_22==1, And(waitcount_2_22==0, rechcount_2_22==0)))
s.add(
Implies(wprim_2_23==0, And(waitcount_2_23==1, rechcount_2_23==0)), 
Implies(wprim_2_23==2, And(waitcount_2_23==1, rechcount_2_23==1)), 
Implies(wprim_2_23==1, And(waitcount_2_23==0, rechcount_2_23==0)))
s.add(
Implies(wprim_2_24==0, And(waitcount_2_24==1, rechcount_2_24==0)), 
Implies(wprim_2_24==2, And(waitcount_2_24==1, rechcount_2_24==1)), 
Implies(wprim_2_24==1, And(waitcount_2_24==0, rechcount_2_24==0)))
s.add(
Implies(wprim_2_25==0, And(waitcount_2_25==1, rechcount_2_25==0)), 
Implies(wprim_2_25==2, And(waitcount_2_25==1, rechcount_2_25==1)), 
Implies(wprim_2_25==1, And(waitcount_2_25==0, rechcount_2_25==0)))
s.add(
Implies(wprim_2_26==0, And(waitcount_2_26==1, rechcount_2_26==0)), 
Implies(wprim_2_26==2, And(waitcount_2_26==1, rechcount_2_26==1)), 
Implies(wprim_2_26==1, And(waitcount_2_26==0, rechcount_2_26==0)))
s.add(
Implies(wprim_2_27==0, And(waitcount_2_27==1, rechcount_2_27==0)), 
Implies(wprim_2_27==2, And(waitcount_2_27==1, rechcount_2_27==1)), 
Implies(wprim_2_27==1, And(waitcount_2_27==0, rechcount_2_27==0)))
s.add(
Implies(wprim_2_28==0, And(waitcount_2_28==1, rechcount_2_28==0)), 
Implies(wprim_2_28==2, And(waitcount_2_28==1, rechcount_2_28==1)), 
Implies(wprim_2_28==1, And(waitcount_2_28==0, rechcount_2_28==0)))
s.add(
Implies(wprim_2_29==0, And(waitcount_2_29==1, rechcount_2_29==0)), 
Implies(wprim_2_29==2, And(waitcount_2_29==1, rechcount_2_29==1)), 
Implies(wprim_2_29==1, And(waitcount_2_29==0, rechcount_2_29==0)))
s.add(
Implies(wprim_2_30==0, And(waitcount_2_30==1, rechcount_2_30==0)), 
Implies(wprim_2_30==2, And(waitcount_2_30==1, rechcount_2_30==1)), 
Implies(wprim_2_30==1, And(waitcount_2_30==0, rechcount_2_30==0)))
s.add(
Implies(wprim_2_31==0, And(waitcount_2_31==1, rechcount_2_31==0)), 
Implies(wprim_2_31==2, And(waitcount_2_31==1, rechcount_2_31==1)), 
Implies(wprim_2_31==1, And(waitcount_2_31==0, rechcount_2_31==0)))
s.add(
Implies(wprim_2_32==0, And(waitcount_2_32==1, rechcount_2_32==0)), 
Implies(wprim_2_32==2, And(waitcount_2_32==1, rechcount_2_32==1)), 
Implies(wprim_2_32==1, And(waitcount_2_32==0, rechcount_2_32==0)))
s.add(
Implies(wprim_2_33==0, And(waitcount_2_33==1, rechcount_2_33==0)), 
Implies(wprim_2_33==2, And(waitcount_2_33==1, rechcount_2_33==1)), 
Implies(wprim_2_33==1, And(waitcount_2_33==0, rechcount_2_33==0)))
s.add(
Implies(wprim_2_34==0, And(waitcount_2_34==1, rechcount_2_34==0)), 
Implies(wprim_2_34==2, And(waitcount_2_34==1, rechcount_2_34==1)), 
Implies(wprim_2_34==1, And(waitcount_2_34==0, rechcount_2_34==0)))
s.add(
Implies(wprim_2_35==0, And(waitcount_2_35==1, rechcount_2_35==0)), 
Implies(wprim_2_35==2, And(waitcount_2_35==1, rechcount_2_35==1)), 
Implies(wprim_2_35==1, And(waitcount_2_35==0, rechcount_2_35==0)))
s.add(
Implies(wprim_2_36==0, And(waitcount_2_36==1, rechcount_2_36==0)), 
Implies(wprim_2_36==2, And(waitcount_2_36==1, rechcount_2_36==1)), 
Implies(wprim_2_36==1, And(waitcount_2_36==0, rechcount_2_36==0)))
s.add(
Implies(wprim_2_37==0, And(waitcount_2_37==1, rechcount_2_37==0)), 
Implies(wprim_2_37==2, And(waitcount_2_37==1, rechcount_2_37==1)), 
Implies(wprim_2_37==1, And(waitcount_2_37==0, rechcount_2_37==0)))
s.add(
Implies(wprim_2_38==0, And(waitcount_2_38==1, rechcount_2_38==0)), 
Implies(wprim_2_38==2, And(waitcount_2_38==1, rechcount_2_38==1)), 
Implies(wprim_2_38==1, And(waitcount_2_38==0, rechcount_2_38==0)))
s.add(
Implies(wprim_2_39==0, And(waitcount_2_39==1, rechcount_2_39==0)), 
Implies(wprim_2_39==2, And(waitcount_2_39==1, rechcount_2_39==1)), 
Implies(wprim_2_39==1, And(waitcount_2_39==0, rechcount_2_39==0)))
s.add(
Implies(wprim_2_40==0, And(waitcount_2_40==1, rechcount_2_40==0)), 
Implies(wprim_2_40==2, And(waitcount_2_40==1, rechcount_2_40==1)), 
Implies(wprim_2_40==1, And(waitcount_2_40==0, rechcount_2_40==0)))
s.add(
Implies(wprim_2_41==0, And(waitcount_2_41==1, rechcount_2_41==0)), 
Implies(wprim_2_41==2, And(waitcount_2_41==1, rechcount_2_41==1)), 
Implies(wprim_2_41==1, And(waitcount_2_41==0, rechcount_2_41==0)))
s.add(
Implies(wprim_2_42==0, And(waitcount_2_42==1, rechcount_2_42==0)), 
Implies(wprim_2_42==2, And(waitcount_2_42==1, rechcount_2_42==1)), 
Implies(wprim_2_42==1, And(waitcount_2_42==0, rechcount_2_42==0)))
s.add(
Implies(wprim_2_43==0, And(waitcount_2_43==1, rechcount_2_43==0)), 
Implies(wprim_2_43==2, And(waitcount_2_43==1, rechcount_2_43==1)), 
Implies(wprim_2_43==1, And(waitcount_2_43==0, rechcount_2_43==0)))
s.add(
Implies(wprim_2_44==0, And(waitcount_2_44==1, rechcount_2_44==0)), 
Implies(wprim_2_44==2, And(waitcount_2_44==1, rechcount_2_44==1)), 
Implies(wprim_2_44==1, And(waitcount_2_44==0, rechcount_2_44==0)))
s.add(
Implies(wprim_2_45==0, And(waitcount_2_45==1, rechcount_2_45==0)), 
Implies(wprim_2_45==2, And(waitcount_2_45==1, rechcount_2_45==1)), 
Implies(wprim_2_45==1, And(waitcount_2_45==0, rechcount_2_45==0)))
s.add(
Implies(wprim_2_46==0, And(waitcount_2_46==1, rechcount_2_46==0)), 
Implies(wprim_2_46==2, And(waitcount_2_46==1, rechcount_2_46==1)), 
Implies(wprim_2_46==1, And(waitcount_2_46==0, rechcount_2_46==0)))
s.add(
Implies(wprim_2_47==0, And(waitcount_2_47==1, rechcount_2_47==0)), 
Implies(wprim_2_47==2, And(waitcount_2_47==1, rechcount_2_47==1)), 
Implies(wprim_2_47==1, And(waitcount_2_47==0, rechcount_2_47==0)))
s.add(
Implies(wprim_2_48==0, And(waitcount_2_48==1, rechcount_2_48==0)), 
Implies(wprim_2_48==2, And(waitcount_2_48==1, rechcount_2_48==1)), 
Implies(wprim_2_48==1, And(waitcount_2_48==0, rechcount_2_48==0)))

s.add(
Implies(wprim_3_1==0, And(waitcount_3_1==1, rechcount_3_1==0)), 
Implies(wprim_3_1==2, And(waitcount_3_1==1, rechcount_3_1==1)), 
Implies(wprim_3_1==1, And(waitcount_3_1==0, rechcount_3_1==0)))
s.add(
Implies(wprim_3_2==0, And(waitcount_3_2==1, rechcount_3_2==0)), 
Implies(wprim_3_2==2, And(waitcount_3_2==1, rechcount_3_2==1)), 
Implies(wprim_3_2==1, And(waitcount_3_2==0, rechcount_3_2==0)))
s.add(
Implies(wprim_3_3==0, And(waitcount_3_3==1, rechcount_3_3==0)), 
Implies(wprim_3_3==2, And(waitcount_3_3==1, rechcount_3_3==1)), 
Implies(wprim_3_3==1, And(waitcount_3_3==0, rechcount_3_3==0)))
s.add(
Implies(wprim_3_4==0, And(waitcount_3_4==1, rechcount_3_4==0)), 
Implies(wprim_3_4==2, And(waitcount_3_4==1, rechcount_3_4==1)), 
Implies(wprim_3_4==1, And(waitcount_3_4==0, rechcount_3_4==0)))
s.add(
Implies(wprim_3_5==0, And(waitcount_3_5==1, rechcount_3_5==0)), 
Implies(wprim_3_5==2, And(waitcount_3_5==1, rechcount_3_5==1)), 
Implies(wprim_3_5==1, And(waitcount_3_5==0, rechcount_3_5==0)))
s.add(
Implies(wprim_3_6==0, And(waitcount_3_6==1, rechcount_3_6==0)), 
Implies(wprim_3_6==2, And(waitcount_3_6==1, rechcount_3_6==1)), 
Implies(wprim_3_6==1, And(waitcount_3_6==0, rechcount_3_6==0)))
s.add(
Implies(wprim_3_7==0, And(waitcount_3_7==1, rechcount_3_7==0)), 
Implies(wprim_3_7==2, And(waitcount_3_7==1, rechcount_3_7==1)), 
Implies(wprim_3_7==1, And(waitcount_3_7==0, rechcount_3_7==0)))
s.add(
Implies(wprim_3_8==0, And(waitcount_3_8==1, rechcount_3_8==0)), 
Implies(wprim_3_8==2, And(waitcount_3_8==1, rechcount_3_8==1)), 
Implies(wprim_3_8==1, And(waitcount_3_8==0, rechcount_3_8==0)))
s.add(
Implies(wprim_3_9==0, And(waitcount_3_9==1, rechcount_3_9==0)), 
Implies(wprim_3_9==2, And(waitcount_3_9==1, rechcount_3_9==1)), 
Implies(wprim_3_9==1, And(waitcount_3_9==0, rechcount_3_9==0)))
s.add(
Implies(wprim_3_10==0, And(waitcount_3_10==1, rechcount_3_10==0)), 
Implies(wprim_3_10==2, And(waitcount_3_10==1, rechcount_3_10==1)), 
Implies(wprim_3_10==1, And(waitcount_3_10==0, rechcount_3_10==0)))
s.add(
Implies(wprim_3_11==0, And(waitcount_3_11==1, rechcount_3_11==0)), 
Implies(wprim_3_11==2, And(waitcount_3_11==1, rechcount_3_11==1)), 
Implies(wprim_3_11==1, And(waitcount_3_11==0, rechcount_3_11==0)))
s.add(
Implies(wprim_3_12==0, And(waitcount_3_12==1, rechcount_3_12==0)), 
Implies(wprim_3_12==2, And(waitcount_3_12==1, rechcount_3_12==1)), 
Implies(wprim_3_12==1, And(waitcount_3_12==0, rechcount_3_12==0)))
s.add(
Implies(wprim_3_13==0, And(waitcount_3_13==1, rechcount_3_13==0)), 
Implies(wprim_3_13==2, And(waitcount_3_13==1, rechcount_3_13==1)), 
Implies(wprim_3_13==1, And(waitcount_3_13==0, rechcount_3_13==0)))
s.add(
Implies(wprim_3_14==0, And(waitcount_3_14==1, rechcount_3_14==0)), 
Implies(wprim_3_14==2, And(waitcount_3_14==1, rechcount_3_14==1)), 
Implies(wprim_3_14==1, And(waitcount_3_14==0, rechcount_3_14==0)))
s.add(
Implies(wprim_3_15==0, And(waitcount_3_15==1, rechcount_3_15==0)), 
Implies(wprim_3_15==2, And(waitcount_3_15==1, rechcount_3_15==1)), 
Implies(wprim_3_15==1, And(waitcount_3_15==0, rechcount_3_15==0)))
s.add(
Implies(wprim_3_16==0, And(waitcount_3_16==1, rechcount_3_16==0)), 
Implies(wprim_3_16==2, And(waitcount_3_16==1, rechcount_3_16==1)), 
Implies(wprim_3_16==1, And(waitcount_3_16==0, rechcount_3_16==0)))
s.add(
Implies(wprim_3_17==0, And(waitcount_3_17==1, rechcount_3_17==0)), 
Implies(wprim_3_17==2, And(waitcount_3_17==1, rechcount_3_17==1)), 
Implies(wprim_3_17==1, And(waitcount_3_17==0, rechcount_3_17==0)))
s.add(
Implies(wprim_3_18==0, And(waitcount_3_18==1, rechcount_3_18==0)), 
Implies(wprim_3_18==2, And(waitcount_3_18==1, rechcount_3_18==1)), 
Implies(wprim_3_18==1, And(waitcount_3_18==0, rechcount_3_18==0)))
s.add(
Implies(wprim_3_19==0, And(waitcount_3_19==1, rechcount_3_19==0)), 
Implies(wprim_3_19==2, And(waitcount_3_19==1, rechcount_3_19==1)), 
Implies(wprim_3_19==1, And(waitcount_3_19==0, rechcount_3_19==0)))
s.add(
Implies(wprim_3_20==0, And(waitcount_3_20==1, rechcount_3_20==0)), 
Implies(wprim_3_20==2, And(waitcount_3_20==1, rechcount_3_20==1)), 
Implies(wprim_3_20==1, And(waitcount_3_20==0, rechcount_3_20==0)))
s.add(
Implies(wprim_3_21==0, And(waitcount_3_21==1, rechcount_3_21==0)), 
Implies(wprim_3_21==2, And(waitcount_3_21==1, rechcount_3_21==1)), 
Implies(wprim_3_21==1, And(waitcount_3_21==0, rechcount_3_21==0)))
s.add(
Implies(wprim_3_22==0, And(waitcount_3_22==1, rechcount_3_22==0)), 
Implies(wprim_3_22==2, And(waitcount_3_22==1, rechcount_3_22==1)), 
Implies(wprim_3_22==1, And(waitcount_3_22==0, rechcount_3_22==0)))
s.add(
Implies(wprim_3_23==0, And(waitcount_3_23==1, rechcount_3_23==0)), 
Implies(wprim_3_23==2, And(waitcount_3_23==1, rechcount_3_23==1)), 
Implies(wprim_3_23==1, And(waitcount_3_23==0, rechcount_3_23==0)))
s.add(
Implies(wprim_3_24==0, And(waitcount_3_24==1, rechcount_3_24==0)), 
Implies(wprim_3_24==2, And(waitcount_3_24==1, rechcount_3_24==1)), 
Implies(wprim_3_24==1, And(waitcount_3_24==0, rechcount_3_24==0)))
s.add(
Implies(wprim_3_25==0, And(waitcount_3_25==1, rechcount_3_25==0)), 
Implies(wprim_3_25==2, And(waitcount_3_25==1, rechcount_3_25==1)), 
Implies(wprim_3_25==1, And(waitcount_3_25==0, rechcount_3_25==0)))
s.add(
Implies(wprim_3_26==0, And(waitcount_3_26==1, rechcount_3_26==0)), 
Implies(wprim_3_26==2, And(waitcount_3_26==1, rechcount_3_26==1)), 
Implies(wprim_3_26==1, And(waitcount_3_26==0, rechcount_3_26==0)))
s.add(
Implies(wprim_3_27==0, And(waitcount_3_27==1, rechcount_3_27==0)), 
Implies(wprim_3_27==2, And(waitcount_3_27==1, rechcount_3_27==1)), 
Implies(wprim_3_27==1, And(waitcount_3_27==0, rechcount_3_27==0)))
s.add(
Implies(wprim_3_28==0, And(waitcount_3_28==1, rechcount_3_28==0)), 
Implies(wprim_3_28==2, And(waitcount_3_28==1, rechcount_3_28==1)), 
Implies(wprim_3_28==1, And(waitcount_3_28==0, rechcount_3_28==0)))
s.add(
Implies(wprim_3_29==0, And(waitcount_3_29==1, rechcount_3_29==0)), 
Implies(wprim_3_29==2, And(waitcount_3_29==1, rechcount_3_29==1)), 
Implies(wprim_3_29==1, And(waitcount_3_29==0, rechcount_3_29==0)))
s.add(
Implies(wprim_3_30==0, And(waitcount_3_30==1, rechcount_3_30==0)), 
Implies(wprim_3_30==2, And(waitcount_3_30==1, rechcount_3_30==1)), 
Implies(wprim_3_30==1, And(waitcount_3_30==0, rechcount_3_30==0)))
s.add(
Implies(wprim_3_31==0, And(waitcount_3_31==1, rechcount_3_31==0)), 
Implies(wprim_3_31==2, And(waitcount_3_31==1, rechcount_3_31==1)), 
Implies(wprim_3_31==1, And(waitcount_3_31==0, rechcount_3_31==0)))
s.add(
Implies(wprim_3_32==0, And(waitcount_3_32==1, rechcount_3_32==0)), 
Implies(wprim_3_32==2, And(waitcount_3_32==1, rechcount_3_32==1)), 
Implies(wprim_3_32==1, And(waitcount_3_32==0, rechcount_3_32==0)))
s.add(
Implies(wprim_3_33==0, And(waitcount_3_33==1, rechcount_3_33==0)), 
Implies(wprim_3_33==2, And(waitcount_3_33==1, rechcount_3_33==1)), 
Implies(wprim_3_33==1, And(waitcount_3_33==0, rechcount_3_33==0)))
s.add(
Implies(wprim_3_34==0, And(waitcount_3_34==1, rechcount_3_34==0)), 
Implies(wprim_3_34==2, And(waitcount_3_34==1, rechcount_3_34==1)), 
Implies(wprim_3_34==1, And(waitcount_3_34==0, rechcount_3_34==0)))
s.add(
Implies(wprim_3_35==0, And(waitcount_3_35==1, rechcount_3_35==0)), 
Implies(wprim_3_35==2, And(waitcount_3_35==1, rechcount_3_35==1)), 
Implies(wprim_3_35==1, And(waitcount_3_35==0, rechcount_3_35==0)))
s.add(
Implies(wprim_3_36==0, And(waitcount_3_36==1, rechcount_3_36==0)), 
Implies(wprim_3_36==2, And(waitcount_3_36==1, rechcount_3_36==1)), 
Implies(wprim_3_36==1, And(waitcount_3_36==0, rechcount_3_36==0)))
s.add(
Implies(wprim_3_37==0, And(waitcount_3_37==1, rechcount_3_37==0)), 
Implies(wprim_3_37==2, And(waitcount_3_37==1, rechcount_3_37==1)), 
Implies(wprim_3_37==1, And(waitcount_3_37==0, rechcount_3_37==0)))
s.add(
Implies(wprim_3_38==0, And(waitcount_3_38==1, rechcount_3_38==0)), 
Implies(wprim_3_38==2, And(waitcount_3_38==1, rechcount_3_38==1)), 
Implies(wprim_3_38==1, And(waitcount_3_38==0, rechcount_3_38==0)))
s.add(
Implies(wprim_3_39==0, And(waitcount_3_39==1, rechcount_3_39==0)), 
Implies(wprim_3_39==2, And(waitcount_3_39==1, rechcount_3_39==1)), 
Implies(wprim_3_39==1, And(waitcount_3_39==0, rechcount_3_39==0)))
s.add(
Implies(wprim_3_40==0, And(waitcount_3_40==1, rechcount_3_40==0)), 
Implies(wprim_3_40==2, And(waitcount_3_40==1, rechcount_3_40==1)), 
Implies(wprim_3_40==1, And(waitcount_3_40==0, rechcount_3_40==0)))
s.add(
Implies(wprim_3_41==0, And(waitcount_3_41==1, rechcount_3_41==0)), 
Implies(wprim_3_41==2, And(waitcount_3_41==1, rechcount_3_41==1)), 
Implies(wprim_3_41==1, And(waitcount_3_41==0, rechcount_3_41==0)))
s.add(
Implies(wprim_3_42==0, And(waitcount_3_42==1, rechcount_3_42==0)), 
Implies(wprim_3_42==2, And(waitcount_3_42==1, rechcount_3_42==1)), 
Implies(wprim_3_42==1, And(waitcount_3_42==0, rechcount_3_42==0)))
s.add(
Implies(wprim_3_43==0, And(waitcount_3_43==1, rechcount_3_43==0)), 
Implies(wprim_3_43==2, And(waitcount_3_43==1, rechcount_3_43==1)), 
Implies(wprim_3_43==1, And(waitcount_3_43==0, rechcount_3_43==0)))
s.add(
Implies(wprim_3_44==0, And(waitcount_3_44==1, rechcount_3_44==0)), 
Implies(wprim_3_44==2, And(waitcount_3_44==1, rechcount_3_44==1)), 
Implies(wprim_3_44==1, And(waitcount_3_44==0, rechcount_3_44==0)))
s.add(
Implies(wprim_3_45==0, And(waitcount_3_45==1, rechcount_3_45==0)), 
Implies(wprim_3_45==2, And(waitcount_3_45==1, rechcount_3_45==1)), 
Implies(wprim_3_45==1, And(waitcount_3_45==0, rechcount_3_45==0)))
s.add(
Implies(wprim_3_46==0, And(waitcount_3_46==1, rechcount_3_46==0)), 
Implies(wprim_3_46==2, And(waitcount_3_46==1, rechcount_3_46==1)), 
Implies(wprim_3_46==1, And(waitcount_3_46==0, rechcount_3_46==0)))
s.add(
Implies(wprim_3_47==0, And(waitcount_3_47==1, rechcount_3_47==0)), 
Implies(wprim_3_47==2, And(waitcount_3_47==1, rechcount_3_47==1)), 
Implies(wprim_3_47==1, And(waitcount_3_47==0, rechcount_3_47==0)))
s.add(
Implies(wprim_3_48==0, And(waitcount_3_48==1, rechcount_3_48==0)), 
Implies(wprim_3_48==2, And(waitcount_3_48==1, rechcount_3_48==1)), 
Implies(wprim_3_48==1, And(waitcount_3_48==0, rechcount_3_48==0)))

s.add(
Implies(wprim_4_1==0, And(waitcount_4_1==1, rechcount_4_1==0)), 
Implies(wprim_4_1==2, And(waitcount_4_1==1, rechcount_4_1==1)), 
Implies(wprim_4_1==1, And(waitcount_4_1==0, rechcount_4_1==0)))
s.add(
Implies(wprim_4_2==0, And(waitcount_4_2==1, rechcount_4_2==0)), 
Implies(wprim_4_2==2, And(waitcount_4_2==1, rechcount_4_2==1)), 
Implies(wprim_4_2==1, And(waitcount_4_2==0, rechcount_4_2==0)))
s.add(
Implies(wprim_4_3==0, And(waitcount_4_3==1, rechcount_4_3==0)), 
Implies(wprim_4_3==2, And(waitcount_4_3==1, rechcount_4_3==1)), 
Implies(wprim_4_3==1, And(waitcount_4_3==0, rechcount_4_3==0)))
s.add(
Implies(wprim_4_4==0, And(waitcount_4_4==1, rechcount_4_4==0)), 
Implies(wprim_4_4==2, And(waitcount_4_4==1, rechcount_4_4==1)), 
Implies(wprim_4_4==1, And(waitcount_4_4==0, rechcount_4_4==0)))
s.add(
Implies(wprim_4_5==0, And(waitcount_4_5==1, rechcount_4_5==0)), 
Implies(wprim_4_5==2, And(waitcount_4_5==1, rechcount_4_5==1)), 
Implies(wprim_4_5==1, And(waitcount_4_5==0, rechcount_4_5==0)))
s.add(
Implies(wprim_4_6==0, And(waitcount_4_6==1, rechcount_4_6==0)), 
Implies(wprim_4_6==2, And(waitcount_4_6==1, rechcount_4_6==1)), 
Implies(wprim_4_6==1, And(waitcount_4_6==0, rechcount_4_6==0)))
s.add(
Implies(wprim_4_7==0, And(waitcount_4_7==1, rechcount_4_7==0)), 
Implies(wprim_4_7==2, And(waitcount_4_7==1, rechcount_4_7==1)), 
Implies(wprim_4_7==1, And(waitcount_4_7==0, rechcount_4_7==0)))
s.add(
Implies(wprim_4_8==0, And(waitcount_4_8==1, rechcount_4_8==0)), 
Implies(wprim_4_8==2, And(waitcount_4_8==1, rechcount_4_8==1)), 
Implies(wprim_4_8==1, And(waitcount_4_8==0, rechcount_4_8==0)))
s.add(
Implies(wprim_4_9==0, And(waitcount_4_9==1, rechcount_4_9==0)), 
Implies(wprim_4_9==2, And(waitcount_4_9==1, rechcount_4_9==1)), 
Implies(wprim_4_9==1, And(waitcount_4_9==0, rechcount_4_9==0)))
s.add(
Implies(wprim_4_10==0, And(waitcount_4_10==1, rechcount_4_10==0)), 
Implies(wprim_4_10==2, And(waitcount_4_10==1, rechcount_4_10==1)), 
Implies(wprim_4_10==1, And(waitcount_4_10==0, rechcount_4_10==0)))
s.add(
Implies(wprim_4_11==0, And(waitcount_4_11==1, rechcount_4_11==0)), 
Implies(wprim_4_11==2, And(waitcount_4_11==1, rechcount_4_11==1)), 
Implies(wprim_4_11==1, And(waitcount_4_11==0, rechcount_4_11==0)))
s.add(
Implies(wprim_4_12==0, And(waitcount_4_12==1, rechcount_4_12==0)), 
Implies(wprim_4_12==2, And(waitcount_4_12==1, rechcount_4_12==1)), 
Implies(wprim_4_12==1, And(waitcount_4_12==0, rechcount_4_12==0)))
s.add(
Implies(wprim_4_13==0, And(waitcount_4_13==1, rechcount_4_13==0)), 
Implies(wprim_4_13==2, And(waitcount_4_13==1, rechcount_4_13==1)), 
Implies(wprim_4_13==1, And(waitcount_4_13==0, rechcount_4_13==0)))
s.add(
Implies(wprim_4_14==0, And(waitcount_4_14==1, rechcount_4_14==0)), 
Implies(wprim_4_14==2, And(waitcount_4_14==1, rechcount_4_14==1)), 
Implies(wprim_4_14==1, And(waitcount_4_14==0, rechcount_4_14==0)))
s.add(
Implies(wprim_4_15==0, And(waitcount_4_15==1, rechcount_4_15==0)), 
Implies(wprim_4_15==2, And(waitcount_4_15==1, rechcount_4_15==1)), 
Implies(wprim_4_15==1, And(waitcount_4_15==0, rechcount_4_15==0)))
s.add(
Implies(wprim_4_16==0, And(waitcount_4_16==1, rechcount_4_16==0)), 
Implies(wprim_4_16==2, And(waitcount_4_16==1, rechcount_4_16==1)), 
Implies(wprim_4_16==1, And(waitcount_4_16==0, rechcount_4_16==0)))
s.add(
Implies(wprim_4_17==0, And(waitcount_4_17==1, rechcount_4_17==0)), 
Implies(wprim_4_17==2, And(waitcount_4_17==1, rechcount_4_17==1)), 
Implies(wprim_4_17==1, And(waitcount_4_17==0, rechcount_4_17==0)))
s.add(
Implies(wprim_4_18==0, And(waitcount_4_18==1, rechcount_4_18==0)), 
Implies(wprim_4_18==2, And(waitcount_4_18==1, rechcount_4_18==1)), 
Implies(wprim_4_18==1, And(waitcount_4_18==0, rechcount_4_18==0)))
s.add(
Implies(wprim_4_19==0, And(waitcount_4_19==1, rechcount_4_19==0)), 
Implies(wprim_4_19==2, And(waitcount_4_19==1, rechcount_4_19==1)), 
Implies(wprim_4_19==1, And(waitcount_4_19==0, rechcount_4_19==0)))
s.add(
Implies(wprim_4_20==0, And(waitcount_4_20==1, rechcount_4_20==0)), 
Implies(wprim_4_20==2, And(waitcount_4_20==1, rechcount_4_20==1)), 
Implies(wprim_4_20==1, And(waitcount_4_20==0, rechcount_4_20==0)))
s.add(
Implies(wprim_4_21==0, And(waitcount_4_21==1, rechcount_4_21==0)), 
Implies(wprim_4_21==2, And(waitcount_4_21==1, rechcount_4_21==1)), 
Implies(wprim_4_21==1, And(waitcount_4_21==0, rechcount_4_21==0)))
s.add(
Implies(wprim_4_22==0, And(waitcount_4_22==1, rechcount_4_22==0)), 
Implies(wprim_4_22==2, And(waitcount_4_22==1, rechcount_4_22==1)), 
Implies(wprim_4_22==1, And(waitcount_4_22==0, rechcount_4_22==0)))
s.add(
Implies(wprim_4_23==0, And(waitcount_4_23==1, rechcount_4_23==0)), 
Implies(wprim_4_23==2, And(waitcount_4_23==1, rechcount_4_23==1)), 
Implies(wprim_4_23==1, And(waitcount_4_23==0, rechcount_4_23==0)))
s.add(
Implies(wprim_4_24==0, And(waitcount_4_24==1, rechcount_4_24==0)), 
Implies(wprim_4_24==2, And(waitcount_4_24==1, rechcount_4_24==1)), 
Implies(wprim_4_24==1, And(waitcount_4_24==0, rechcount_4_24==0)))
s.add(
Implies(wprim_4_25==0, And(waitcount_4_25==1, rechcount_4_25==0)), 
Implies(wprim_4_25==2, And(waitcount_4_25==1, rechcount_4_25==1)), 
Implies(wprim_4_25==1, And(waitcount_4_25==0, rechcount_4_25==0)))
s.add(
Implies(wprim_4_26==0, And(waitcount_4_26==1, rechcount_4_26==0)), 
Implies(wprim_4_26==2, And(waitcount_4_26==1, rechcount_4_26==1)), 
Implies(wprim_4_26==1, And(waitcount_4_26==0, rechcount_4_26==0)))
s.add(
Implies(wprim_4_27==0, And(waitcount_4_27==1, rechcount_4_27==0)), 
Implies(wprim_4_27==2, And(waitcount_4_27==1, rechcount_4_27==1)), 
Implies(wprim_4_27==1, And(waitcount_4_27==0, rechcount_4_27==0)))
s.add(
Implies(wprim_4_28==0, And(waitcount_4_28==1, rechcount_4_28==0)), 
Implies(wprim_4_28==2, And(waitcount_4_28==1, rechcount_4_28==1)), 
Implies(wprim_4_28==1, And(waitcount_4_28==0, rechcount_4_28==0)))
s.add(
Implies(wprim_4_29==0, And(waitcount_4_29==1, rechcount_4_29==0)), 
Implies(wprim_4_29==2, And(waitcount_4_29==1, rechcount_4_29==1)), 
Implies(wprim_4_29==1, And(waitcount_4_29==0, rechcount_4_29==0)))
s.add(
Implies(wprim_4_30==0, And(waitcount_4_30==1, rechcount_4_30==0)), 
Implies(wprim_4_30==2, And(waitcount_4_30==1, rechcount_4_30==1)), 
Implies(wprim_4_30==1, And(waitcount_4_30==0, rechcount_4_30==0)))
s.add(
Implies(wprim_4_31==0, And(waitcount_4_31==1, rechcount_4_31==0)), 
Implies(wprim_4_31==2, And(waitcount_4_31==1, rechcount_4_31==1)), 
Implies(wprim_4_31==1, And(waitcount_4_31==0, rechcount_4_31==0)))
s.add(
Implies(wprim_4_32==0, And(waitcount_4_32==1, rechcount_4_32==0)), 
Implies(wprim_4_32==2, And(waitcount_4_32==1, rechcount_4_32==1)), 
Implies(wprim_4_32==1, And(waitcount_4_32==0, rechcount_4_32==0)))
s.add(
Implies(wprim_4_33==0, And(waitcount_4_33==1, rechcount_4_33==0)), 
Implies(wprim_4_33==2, And(waitcount_4_33==1, rechcount_4_33==1)), 
Implies(wprim_4_33==1, And(waitcount_4_33==0, rechcount_4_33==0)))
s.add(
Implies(wprim_4_34==0, And(waitcount_4_34==1, rechcount_4_34==0)), 
Implies(wprim_4_34==2, And(waitcount_4_34==1, rechcount_4_34==1)), 
Implies(wprim_4_34==1, And(waitcount_4_34==0, rechcount_4_34==0)))
s.add(
Implies(wprim_4_35==0, And(waitcount_4_35==1, rechcount_4_35==0)), 
Implies(wprim_4_35==2, And(waitcount_4_35==1, rechcount_4_35==1)), 
Implies(wprim_4_35==1, And(waitcount_4_35==0, rechcount_4_35==0)))
s.add(
Implies(wprim_4_36==0, And(waitcount_4_36==1, rechcount_4_36==0)), 
Implies(wprim_4_36==2, And(waitcount_4_36==1, rechcount_4_36==1)), 
Implies(wprim_4_36==1, And(waitcount_4_36==0, rechcount_4_36==0)))
s.add(
Implies(wprim_4_37==0, And(waitcount_4_37==1, rechcount_4_37==0)), 
Implies(wprim_4_37==2, And(waitcount_4_37==1, rechcount_4_37==1)), 
Implies(wprim_4_37==1, And(waitcount_4_37==0, rechcount_4_37==0)))
s.add(
Implies(wprim_4_38==0, And(waitcount_4_38==1, rechcount_4_38==0)), 
Implies(wprim_4_38==2, And(waitcount_4_38==1, rechcount_4_38==1)), 
Implies(wprim_4_38==1, And(waitcount_4_38==0, rechcount_4_38==0)))
s.add(
Implies(wprim_4_39==0, And(waitcount_4_39==1, rechcount_4_39==0)), 
Implies(wprim_4_39==2, And(waitcount_4_39==1, rechcount_4_39==1)), 
Implies(wprim_4_39==1, And(waitcount_4_39==0, rechcount_4_39==0)))
s.add(
Implies(wprim_4_40==0, And(waitcount_4_40==1, rechcount_4_40==0)), 
Implies(wprim_4_40==2, And(waitcount_4_40==1, rechcount_4_40==1)), 
Implies(wprim_4_40==1, And(waitcount_4_40==0, rechcount_4_40==0)))
s.add(
Implies(wprim_4_41==0, And(waitcount_4_41==1, rechcount_4_41==0)), 
Implies(wprim_4_41==2, And(waitcount_4_41==1, rechcount_4_41==1)), 
Implies(wprim_4_41==1, And(waitcount_4_41==0, rechcount_4_41==0)))
s.add(
Implies(wprim_4_42==0, And(waitcount_4_42==1, rechcount_4_42==0)), 
Implies(wprim_4_42==2, And(waitcount_4_42==1, rechcount_4_42==1)), 
Implies(wprim_4_42==1, And(waitcount_4_42==0, rechcount_4_42==0)))
s.add(
Implies(wprim_4_43==0, And(waitcount_4_43==1, rechcount_4_43==0)), 
Implies(wprim_4_43==2, And(waitcount_4_43==1, rechcount_4_43==1)), 
Implies(wprim_4_43==1, And(waitcount_4_43==0, rechcount_4_43==0)))
s.add(
Implies(wprim_4_44==0, And(waitcount_4_44==1, rechcount_4_44==0)), 
Implies(wprim_4_44==2, And(waitcount_4_44==1, rechcount_4_44==1)), 
Implies(wprim_4_44==1, And(waitcount_4_44==0, rechcount_4_44==0)))
s.add(
Implies(wprim_4_45==0, And(waitcount_4_45==1, rechcount_4_45==0)), 
Implies(wprim_4_45==2, And(waitcount_4_45==1, rechcount_4_45==1)), 
Implies(wprim_4_45==1, And(waitcount_4_45==0, rechcount_4_45==0)))
s.add(
Implies(wprim_4_46==0, And(waitcount_4_46==1, rechcount_4_46==0)), 
Implies(wprim_4_46==2, And(waitcount_4_46==1, rechcount_4_46==1)), 
Implies(wprim_4_46==1, And(waitcount_4_46==0, rechcount_4_46==0)))
s.add(
Implies(wprim_4_47==0, And(waitcount_4_47==1, rechcount_4_47==0)), 
Implies(wprim_4_47==2, And(waitcount_4_47==1, rechcount_4_47==1)), 
Implies(wprim_4_47==1, And(waitcount_4_47==0, rechcount_4_47==0)))
s.add(
Implies(wprim_4_48==0, And(waitcount_4_48==1, rechcount_4_48==0)), 
Implies(wprim_4_48==2, And(waitcount_4_48==1, rechcount_4_48==1)), 
Implies(wprim_4_48==1, And(waitcount_4_48==0, rechcount_4_48==0)))


# summation of all waits
s.add(total_wait==
waitcount_1_1 +
waitcount_1_2 +
waitcount_1_3 +
waitcount_1_4 +
waitcount_1_5 +
waitcount_1_6 +
waitcount_1_7 +
waitcount_1_8 +
waitcount_1_9 +
waitcount_1_10 +
waitcount_1_11 +
waitcount_1_12 +
waitcount_1_13 +
waitcount_1_14 +
waitcount_1_15 +
waitcount_1_16 +
waitcount_1_17 +
waitcount_1_18 +
waitcount_1_19 +
waitcount_1_20 +
waitcount_1_21 +
waitcount_1_22 +
waitcount_1_23 +
waitcount_1_24 +
waitcount_1_25 +
waitcount_1_26 +
waitcount_1_27 +
waitcount_1_28 +
waitcount_1_29 +
waitcount_1_30 +
waitcount_1_31 +
waitcount_1_32 +
waitcount_1_33 +
waitcount_1_34 +
waitcount_1_35 +
waitcount_1_36 +
waitcount_1_37 +
waitcount_1_38 +
waitcount_1_39 +
waitcount_1_40 +
waitcount_1_41 +
waitcount_1_42 +
waitcount_1_43 +
waitcount_1_44 +
waitcount_1_45 +
waitcount_1_46 +
waitcount_1_47 +
waitcount_1_48 +
waitcount_2_1 +
waitcount_2_2 +
waitcount_2_3 +
waitcount_2_4 +
waitcount_2_5 +
waitcount_2_6 +
waitcount_2_7 +
waitcount_2_8 +
waitcount_2_9 +
waitcount_2_10 +
waitcount_2_11 +
waitcount_2_12 +
waitcount_2_13 +
waitcount_2_14 +
waitcount_2_15 +
waitcount_2_16 +
waitcount_2_17 +
waitcount_2_18 +
waitcount_2_19 +
waitcount_2_20 +
waitcount_2_21 +
waitcount_2_22 +
waitcount_2_23 +
waitcount_2_24 +
waitcount_2_25 +
waitcount_2_26 +
waitcount_2_27 +
waitcount_2_28 +
waitcount_2_29 +
waitcount_2_30 +
waitcount_2_31 +
waitcount_2_32 +
waitcount_2_33 +
waitcount_2_34 +
waitcount_2_35 +
waitcount_2_36 +
waitcount_2_37 +
waitcount_2_38 +
waitcount_2_39 +
waitcount_2_40 +
waitcount_2_41 +
waitcount_2_42 +
waitcount_2_43 +
waitcount_2_44 +
waitcount_2_45 +
waitcount_2_46 +
waitcount_2_47 +
waitcount_2_48 +
waitcount_3_1 +
waitcount_3_2 +
waitcount_3_3 +
waitcount_3_4 +
waitcount_3_5 +
waitcount_3_6 +
waitcount_3_7 +
waitcount_3_8 +
waitcount_3_9 +
waitcount_3_10 +
waitcount_3_11 +
waitcount_3_12 +
waitcount_3_13 +
waitcount_3_14 +
waitcount_3_15 +
waitcount_3_16 +
waitcount_3_17 +
waitcount_3_18 +
waitcount_3_19 +
waitcount_3_20 +
waitcount_3_21 +
waitcount_3_22 +
waitcount_3_23 +
waitcount_3_24 +
waitcount_3_25 +
waitcount_3_26 +
waitcount_3_27 +
waitcount_3_28 +
waitcount_3_29 +
waitcount_3_30 +
waitcount_3_31 +
waitcount_3_32 +
waitcount_3_33 +
waitcount_3_34 +
waitcount_3_35 +
waitcount_3_36 +
waitcount_3_37 +
waitcount_3_38 +
waitcount_3_39 +
waitcount_3_40 +
waitcount_3_41 +
waitcount_3_42 +
waitcount_3_43 +
waitcount_3_44 +
waitcount_3_45 +
waitcount_3_46 +
waitcount_3_47 +
waitcount_3_48 +
waitcount_4_1 +
waitcount_4_2 +
waitcount_4_3 +
waitcount_4_4 +
waitcount_4_5 +
waitcount_4_6 +
waitcount_4_7 +
waitcount_4_8 +
waitcount_4_9 +
waitcount_4_10 +
waitcount_4_11 +
waitcount_4_12 +
waitcount_4_13 +
waitcount_4_14 +
waitcount_4_15 +
waitcount_4_16 +
waitcount_4_17 +
waitcount_4_18 +
waitcount_4_19 +
waitcount_4_20 +
waitcount_4_21 +
waitcount_4_22 +
waitcount_4_23 +
waitcount_4_24 +
waitcount_4_25 +
waitcount_4_26 +
waitcount_4_27 +
waitcount_4_28 +
waitcount_4_29 +
waitcount_4_30 +
waitcount_4_31 +
waitcount_4_32 +
waitcount_4_33 +
waitcount_4_34 +
waitcount_4_35 +
waitcount_4_36 +
waitcount_4_37 +
waitcount_4_38 +
waitcount_4_39 +
waitcount_4_40 +
waitcount_4_41 +
waitcount_4_42 +
waitcount_4_43 +
waitcount_4_44 +
waitcount_4_45 +
waitcount_4_46 +
waitcount_4_47 +
waitcount_4_48
)


# summation of all recharge events
s.add(total_rech==
rechcount_1_1 +
rechcount_1_2 +
rechcount_1_3 +
rechcount_1_4 +
rechcount_1_5 +
rechcount_1_6 +
rechcount_1_7 +
rechcount_1_8 +
rechcount_1_9 +
rechcount_1_10 +
rechcount_1_11 +
rechcount_1_12 +
rechcount_1_13 +
rechcount_1_14 +
rechcount_1_15 +
rechcount_1_16 +
rechcount_1_17 +
rechcount_1_18 +
rechcount_1_19 +
rechcount_1_20 +
rechcount_1_21 +
rechcount_1_22 +
rechcount_1_23 +
rechcount_1_24 +
rechcount_1_25 +
rechcount_1_26 +
rechcount_1_27 +
rechcount_1_28 +
rechcount_1_29 +
rechcount_1_30 +
rechcount_1_31 +
rechcount_1_32 +
rechcount_1_33 +
rechcount_1_34 +
rechcount_1_35 +
rechcount_1_36 +
rechcount_1_37 +
rechcount_1_38 +
rechcount_1_39 +
rechcount_1_40 +
rechcount_1_41 +
rechcount_1_42 +
rechcount_1_43 +
rechcount_1_44 +
rechcount_1_45 +
rechcount_1_46 +
rechcount_1_47 +
rechcount_1_48 +
rechcount_2_1 +
rechcount_2_2 +
rechcount_2_3 +
rechcount_2_4 +
rechcount_2_5 +
rechcount_2_6 +
rechcount_2_7 +
rechcount_2_8 +
rechcount_2_9 +
rechcount_2_10 +
rechcount_2_11 +
rechcount_2_12 +
rechcount_2_13 +
rechcount_2_14 +
rechcount_2_15 +
rechcount_2_16 +
rechcount_2_17 +
rechcount_2_18 +
rechcount_2_19 +
rechcount_2_20 +
rechcount_2_21 +
rechcount_2_22 +
rechcount_2_23 +
rechcount_2_24 +
rechcount_2_25 +
rechcount_2_26 +
rechcount_2_27 +
rechcount_2_28 +
rechcount_2_29 +
rechcount_2_30 +
rechcount_2_31 +
rechcount_2_32 +
rechcount_2_33 +
rechcount_2_34 +
rechcount_2_35 +
rechcount_2_36 +
rechcount_2_37 +
rechcount_2_38 +
rechcount_2_39 +
rechcount_2_40 +
rechcount_2_41 +
rechcount_2_42 +
rechcount_2_43 +
rechcount_2_44 +
rechcount_2_45 +
rechcount_2_46 +
rechcount_2_47 +
rechcount_2_48 +
rechcount_3_1 +
rechcount_3_2 +
rechcount_3_3 +
rechcount_3_4 +
rechcount_3_5 +
rechcount_3_6 +
rechcount_3_7 +
rechcount_3_8 +
rechcount_3_9 +
rechcount_3_10 +
rechcount_3_11 +
rechcount_3_12 +
rechcount_3_13 +
rechcount_3_14 +
rechcount_3_15 +
rechcount_3_16 +
rechcount_3_17 +
rechcount_3_18 +
rechcount_3_19 +
rechcount_3_20 +
rechcount_3_21 +
rechcount_3_22 +
rechcount_3_23 +
rechcount_3_24 +
rechcount_3_25 +
rechcount_3_26 +
rechcount_3_27 +
rechcount_3_28 +
rechcount_3_29 +
rechcount_3_30 +
rechcount_3_31 +
rechcount_3_32 +
rechcount_3_33 +
rechcount_3_34 +
rechcount_3_35 +
rechcount_3_36 +
rechcount_3_37 +
rechcount_3_38 +
rechcount_3_39 +
rechcount_3_40 +
rechcount_3_41 +
rechcount_3_42 +
rechcount_3_43 +
rechcount_3_44 +
rechcount_3_45 +
rechcount_3_46 +
rechcount_3_47 +
rechcount_3_48 +
rechcount_4_1 +
rechcount_4_2 +
rechcount_4_3 +
rechcount_4_4 +
rechcount_4_5 +
rechcount_4_6 +
rechcount_4_7 +
rechcount_4_8 +
rechcount_4_9 +
rechcount_4_10 +
rechcount_4_11 +
rechcount_4_12 +
rechcount_4_13 +
rechcount_4_14 +
rechcount_4_15 +
rechcount_4_16 +
rechcount_4_17 +
rechcount_4_18 +
rechcount_4_19 +
rechcount_4_20 +
rechcount_4_21 +
rechcount_4_22 +
rechcount_4_23 +
rechcount_4_24 +
rechcount_4_25 +
rechcount_4_26 +
rechcount_4_27 +
rechcount_4_28 +
rechcount_4_29 +
rechcount_4_30 +
rechcount_4_31 +
rechcount_4_32 +
rechcount_4_33 +
rechcount_4_34 +
rechcount_4_35 +
rechcount_4_36 +
rechcount_4_37 +
rechcount_4_38 +
rechcount_4_39 +
rechcount_4_40 +
rechcount_4_41 +
rechcount_4_42 +
rechcount_4_43 +
rechcount_4_44 +
rechcount_4_45 +
rechcount_4_46 +
rechcount_4_47 +
rechcount_4_48
)

# checking for SAT for a given value of total_wait

# driver code -- terminate
s.set('timeout', 7200000)
print '\n================='
print 'check static part ---> %s\n' % s.check()

m = s.model()
r = get_model(total_wait, total_rech)
l = 1
print '-----------------'

x = binarySearch_solving (l, r)

#x = linearSearch_solving (l, r)

print '\nmin(total_wait) = %s' % x
if x==-1: print '--undefined--'
print '\n================='
