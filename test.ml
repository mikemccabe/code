let add p q =
    {num = p.num * q.denom + q.num * p.denom;
       denom = p.denom * q.denom};;
(* val add : rational -> rational -> rational = <fun> *)
let addtup (p, q) =
  { num = p.num * q.denom + q.num * p.denom;
  denom = p.denom * q.denom};;
(* val addtup : rational * rational -> rational = <fun> *)
