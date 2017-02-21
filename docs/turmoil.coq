(* system definition *)

Inductive state : Type :=
  | awesome
  | okay
  | bad.

Definition fortune (s : state) : state :=
  match s with
    | awesome => awesome
    | okay => awesome
    | bad => okay
  end.

Check fortune.
Compute (fortune bad).

Definition turmoil (s : state) : state := 
  match s with
    | awesome => okay
    | okay => bad
    | bad => bad
  end.

Check turmoil.

(* proofs! *)

Theorem fortune_rocks :  forall s, fortune (fortune (fortune s)) = awesome.

Proof. 

intros s. destruct s.
simpl. reflexivity.
simpl. reflexivity.
simpl. reflexivity.

Qed.

Check fortune_rocks.
Print fortune_rocks.

Theorem karma : forall s, fortune (turmoil s) = s.

Proof.
intros s. destruct s.
simpl. reflexivity.
simpl. reflexivity.
simpl. reflexivity.

Qed.


