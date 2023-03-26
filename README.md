# Hungarian Algorithm

Der ungarische Algorithmus, auch bekannt als Munkres-Algorithmus oder Kuhn-Munkres-Algorithmus, ist ein effizienter Algorithmus zur Lösung des Zuordnungsproblems in der Optimierungstheorie.

Das Problem besteht darin, eine optimale Zuordnung von N Elementen in N anderen Elementen zu finden, wobei jeder Element in genau einem anderen Element zugewiesen werden muss und die Gesamtkosten minimiert werden sollen. Es gibt viele Anwendungen in der Praxis, wie z.B. die Zuordnung von Aufgaben an Mitarbeiter oder die Zuordnung von Ressourcen zu Projekten.

Der ungarische Algorithmus löst dieses Problem in polynomieller Zeit, was bedeutet, dass er auch für große Probleme effizient genug ist. Er basiert auf der Idee der schrittweisen Verbesserung einer bestehenden Zuordnung, indem eine optimale Lösung aus einer Teilmenge des Problems gefunden wird.

Der Algorithmus besteht aus den folgenden Schritten:

Subtrahieren Sie das Minimum jedes Zeilen- und Spalten-Elementes von jedem Element, um das Problem in eine reduzierte Matrix zu überführen.
Markieren Sie alle null Elemente in der reduzierten Matrix.
Wenn es eine Zeile mit genau einem markierten Null-Element gibt, ordnen Sie das Element zu und entfernen Sie alle Markierungen in der gleichen Spalte und Zeile.
Wenn es keine solche Zeile gibt, wählen Sie eine unmarkierte Null und führen Sie die folgenden Schritte aus:
Markieren Sie das Element
Wenn es eine Zeile gibt, die markiert ist, die dieses Element enthält, gehen Sie zur Spalte dieser Zeile und wiederholen Sie den Prozess.
Wenn es keine solche Zeile gibt, starten Sie einen alternativen Pfad von einem markierten Element aus und gehen Sie abwechselnd zu einem markierten Element und zu einem unmarkierten Element, bis ein markiertes Element gefunden wird.
Entfernen Sie alle Markierungen auf diesem alternativen Pfad und markieren Sie das ursprüngliche Element, von dem aus der Pfad begonnen hat.
Wiederholen Sie die Schritte 3 und 4, bis alle Elemente zugewiesen sind.
Am Ende des Algorithmus wird die optimale Zuordnung mit den minimalen Gesamtkosten gefunden. Der Algorithmus hat eine Laufzeit von $O(n^3)$, was für die meisten praktischen Anwendungen ausreichend schnell ist.
