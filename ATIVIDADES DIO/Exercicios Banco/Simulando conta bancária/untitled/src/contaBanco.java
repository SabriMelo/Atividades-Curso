import java.util.Scanner;

public class contaBanco {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.println("Digite o número da conta: ");
        var numeroConta = scan.nextInt();
        scan.nextLine();
        System.out.println("Digite o número da agência: ");
        var agenciaConta = scan.nextLine();
        System.out.println("Digite o nome do cliente: ");
        var nomeCliente = scan.nextLine();
        System.out.println("Digite o saldo da conta: ");
        var saldoConta = scan.nextDouble();

        System.out.printf("Olá %s, obrigado por criar uma conta em nosso banco, sua agência é %s, conta %d e seu saldo %.2f já está disponivel para sague.", nomeCliente, agenciaConta, numeroConta, saldoConta);


    }
}